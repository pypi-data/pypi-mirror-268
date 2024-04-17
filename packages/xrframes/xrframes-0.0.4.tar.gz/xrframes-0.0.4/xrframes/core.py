"""
Similar to ``xmovie``, make animations from xarray objects.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Hashable, Iterable
    from typing import Any, Callable

    from IPython.display import Image, Video
    from matplotlib.figure import Figure
    from typing_extensions import Self
    from xarray import DataArray, Dataset


class Frames:

    def __init__(
        self,
        obj: DataArray | Dataset | None,
        func: Callable[[DataArray | Dataset], Figure | None] | None,
        *,
        dim: Hashable | None,
        id_: str = "xrframes_<rand>",
    ) -> None:
        """
        Parameters
        ----------
        obj
            Data to be plotted.
        func
            Function that takes a DataArray or Dataset and produces a matplotlib Figure
            and returns it (returning optional if not using Dask to write frames).
        dim
            Dimension along which frames are selected, before passing the data to `func`.
        id_
            Unique identifier for the movie frame file names
            (``<id>_frame<zero-padded frame num>.png``).
            The default ID is ``xrframes_<rand>``,
            where ``<rand>`` gets replaced by the first part of a UUID4 during
            class initialization.
        """
        self.obj = obj
        self.func = func
        self.dim = dim

        if "<rand>" in id_:
            import uuid

            rand = str(uuid.uuid4()).split("-")[0]
            id_ = id_.replace("<rand>", rand)
        self.id_ = id_

        self.paths: list[Path] | None = None

        self._anim_paths: list[Path] = []

    @classmethod
    def from_existing(cls, paths: str | Iterable[str | Path]) -> Frames:
        """Create a :class:`Frames` instance from existing frame files.

        This way you can call :meth:`to_mp4` and :meth:`to_gif`
        without calling :meth:`write` first, e.g. in a new session.

        If `paths` is a string, glob expansion is applied.
        """
        import re

        if isinstance(paths, str):
            from glob import glob

            paths_ = [Path(p) for p in sorted(glob(paths))]
        else:
            # Assume iterable of paths
            paths_ = [Path(p) for p in paths]

        if not paths_:
            raise ValueError("no frame files found")

        parts = paths_[0].stem.split("_")
        if not len(parts) >= 2 and parts[-1].startswith("frame"):
            raise ValueError("unexpected file name format")
        id_ = "_".join(parts[:-1])

        frames = cls(None, None, dim=None, id_=id_)
        frames.paths = paths_

        # Check path consistency (for patterns)
        re0 = re.compile(frames._to_re_pattern())
        for p in paths_:
            if not re0.fullmatch(p.as_posix()):
                raise ValueError(
                    f"file path {p.as_posix()!r} does not match "
                    f"the first file's detected pattern `{re0.pattern}`"
                )

        return frames

    def _first_path_num(self) -> tuple[Path, str]:
        if self.paths is None:
            raise RuntimeError("call `write` first")

        import re

        p0 = self.paths[0]

        patt = r"frame([0-9]+)"
        m = re.search(patt, p0.stem)
        if m is None:
            raise ValueError(f"file name {p0.name!r} does not match `{patt}`")
        num = m.group(1)

        return p0, num

    def _to_pct_pattern(self) -> str:
        p0, num = self._first_path_num()
        nd = len(num)

        return p0.with_name(p0.name.replace(num, f"%{nd}d")).as_posix()

    def _to_star_pattern(self) -> str:
        p0, num = self._first_path_num()

        return p0.with_name(p0.name.replace(num, "*")).as_posix()

    def _to_re_pattern(self) -> str:
        import re
        from io import StringIO

        p0, num = self._first_path_num()
        nd = len(num)

        s = StringIO()
        if p0.parent != Path("."):
            s.write(re.escape(p0.parent.as_posix()) + "/")
        s.write(re.escape(p0.name).replace(num, rf"[0-9]{{{nd}}}"))

        return s.getvalue()

    def preview(self, frame: int = 0, **kwargs) -> Self:
        """Preview a frame.

        This calls the plotting function for the selected frame
        and thus can be used before :meth:`write` has been called.

        Note that ``plt.show()`` is not applied.

        Parameters
        ----------
        frame
            Frame number to preview (plot).
        """
        if self.obj is None or self.func is None or self.dim is None:
            raise RuntimeError("`obj`, `func`, and `dim` must be set")

        if not 0 <= frame < self.obj.sizes[self.dim]:
            raise ValueError(f"frame number must be in [0, {self.obj.sizes[self.dim]})")
        self.func(self.obj.isel({self.dim: frame}), **kwargs)

        return self

    def write(
        self,
        path=None,
        *,
        parallel: bool | str = False,
        dpi: int = 200,
        transparent: bool = False,
        #
        parallel_kws: dict[str, Any] | None = None,
        plot_kws: dict[str, Any] | None = None,
        savefig_kws: dict[str, Any] | None = None,
    ) -> Self:
        """Write PNG frames.

        After writing, :attr:`paths` is set to the list of created PNGs.

        Parameters
        ----------
        path
            Directory to write the frames to.
            Default: temporary directory (``tempfile.gettempdir()``).
        parallel
            Save frames in parallel.

            - ``False``: sequential (default)
            - ``True`` or ``'Dask'``: parallel with Dask
            - ``'joblib'``: parallel with joblib
        dpi
            Used when saving the figures.
        """
        if self.obj is None or self.func is None or self.dim is None:
            raise RuntimeError("`obj`, `func`, and `dim` must be set")

        import matplotlib as mpl
        import matplotlib.pyplot as plt
        from rich.progress import MofNCompleteColumn, Progress, SpinnerColumn, TimeElapsedColumn

        if path is None:
            from tempfile import gettempdir

            path = Path(gettempdir())
        else:
            path = Path(path)

        if parallel_kws is None:
            parallel_kws = {}
        if plot_kws is None:
            plot_kws = {}
        if savefig_kws is None:
            savefig_kws = {}

        nd = len(str(self.obj.sizes[self.dim]))
        tpl = f"{self.id_}_frame{{frame:0{nd}d}}.png"

        savefig_kws_default = dict(
            dpi=dpi,
            bbox_inches="tight",
            pad_inches=0.05,
            transparent=transparent,
        )
        savefig_kws = {**savefig_kws_default, **savefig_kws}

        def write_frame(i: int) -> Path:
            assert self.func is not None and self.obj is not None
            with plt.ioff():
                fig = self.func(self.obj.isel({self.dim: i}), **plot_kws)
            if not isinstance(fig, plt.Figure):
                fig = plt.gcf()
            p = path / tpl.format(frame=i)
            fig.savefig(p, **savefig_kws)
            plt.close(fig)
            return p

        def write_frame_chunk(obj: DataArray | DataArray) -> DataArray:
            assert self.func is not None
            fig = self.func(obj.squeeze(), **plot_kws)
            if not isinstance(fig, plt.Figure):
                raise ValueError(
                    "for Dask, the supplied plotting function must return a matplotlib Figure"
                )
            p = obj["path"].item()
            fig.savefig(p, **savefig_kws)
            plt.close(fig)
            return obj["path"]

        if parallel is True or isinstance(parallel, str) and parallel.lower() == "dask":
            import xarray as xr

            from ._rich_dask import RichProgressDaskCallback

            current_backend = mpl.get_backend()
            mpl.use("agg")

            kws = dict()
            kws.update(parallel_kws)

            with RichProgressDaskCallback():
                chunked = self.obj.assign_coords(
                    {
                        "frame": (self.dim, range(self.obj.sizes[self.dim])),
                        "path": (
                            self.dim,
                            [path / tpl.format(frame=i) for i in range(self.obj.sizes[self.dim])],
                        ),
                    }
                ).chunk({self.dim: 1})
                ret = chunked.map_blocks(
                    write_frame_chunk,
                    template=xr.ones_like(chunked[self.dim]).chunk({self.dim: 1}),
                ).compute(**kws)
                frame_paths = ret.data.tolist()

            mpl.use(current_backend)
        elif isinstance(parallel, str) and parallel.lower() == "joblib":
            from joblib import delayed

            from ._rich_joblib import RichProgressJoblibParallel

            kws = dict(n_jobs=-2)
            kws.update(parallel_kws)

            frame_paths = RichProgressJoblibParallel(**kws)(
                delayed(write_frame)(i) for i in range(self.obj.sizes[self.dim])
            )
        elif parallel is False:
            with Progress(
                SpinnerColumn(finished_text="✔"),
                r" [progress.description]{task.description}",
                MofNCompleteColumn(),
                TimeElapsedColumn(),
            ) as progress:
                frame_paths = []
                for i in progress.track(
                    range(self.obj.sizes[self.dim]), description="Writing frame"
                ):
                    frame_paths.append(write_frame(i))
        else:
            raise ValueError(f"invalid value for `parallel`: {parallel!r}")

        self.paths = frame_paths

        return self

    # TODO: display (frame images viewer, with ipywidgets?)

    def to_mp4(
        self,
        out: str | Path = "./movie.mp4",
        *,
        fps: int = 10,
        crf: int = 17,
        exe: str | Path = "ffmpeg",
    ) -> None:
        """Make an MP4 movie from the PNG frames with FFmpeg.

        Parameters
        ----------
        fps
            Frame rate (per second).
        crf
            Constant rate factor (0--51, lower is better quality, 23 is FFmpeg's default).
            https://trac.ffmpeg.org/wiki/Encode/H.264#a1.ChooseaCRFvalue
        exe
            Path to ``ffmpeg``.
        """
        import subprocess

        from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn

        if self.paths is None:
            raise RuntimeError("call `write` first")

        frame_pattern = self._to_pct_pattern()

        out = Path(out).expanduser()

        exe = Path(exe)

        # fmt: off
        cmd = [
            exe.as_posix(),
            "-y",
            "-r", str(fps),
            "-i", frame_pattern,
            "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-preset", "veryslow",
            "-crf", str(crf),
            out.as_posix(),
        ]
        # fmt: on

        try:
            with Progress(
                SpinnerColumn(finished_text="✔"),
                r" [progress.description]{task.description}",
                TimeElapsedColumn(),
            ) as progress:
                task = progress.add_task("Making MP4", total=1)
                subprocess.run(
                    cmd,
                    check=True,
                    capture_output=True,
                )
                progress.advance(task, 1)
                progress.refresh()
        except subprocess.CalledProcessError as e:
            print(e.stderr.decode())
            raise

        self._anim_paths.append(out)

        return None

    def to_gif(
        self,
        out: str | Path = "./movie.gif",
        *,
        fps: int = 10,
        scale: str = "100%",
        magick: bool | None = None,
        exe: str | Path = "convert",
    ) -> None:
        """Make a GIF from the PNG frames with ImageMagick.

        Parameters
        ----------
        fps
            Frame rate (per second).
        scale
            Scaling applied when generating the output.
            For example
            ``'480x380'`` (maximum width and height in pixels, preserves original aspect ratio)
            or ``'50%'``.
        magick
            Use ``magick`` base command (new CLI for ImageMagick 7),
            i.e. ``magick convert`` instead of just ``convert``.
            Default: ``True`` if ``magick`` is detected.
            Ignored if a custom `exe` is provived.
        exe
            Path to ``convert`` or ``magick``.
            If detected to be a path to ``magick``, ``convert`` is added after it in the command.
            If detected to be just ``convert`` (command), the `magick` setting will be considered,
            but ignored if `exe` is a *path* to ``convert``.
            Note that ``./convert`` (path in CWD), e.g., is treated as ``convert`` (command).
        """
        import subprocess

        from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn

        out = Path(out).expanduser()

        if magick is None:
            try:
                subprocess.run(["magick", "-version"], check=True, capture_output=True)
            except FileNotFoundError:
                magick = False
            else:
                magick = True

        exe = Path(exe)

        if self.paths is None:
            raise RuntimeError("call `write` first")

        files = [f.as_posix() for f in self.paths]

        # fmt: off
        cmd = [
            exe.as_posix(),
            "-scale", scale,
            # "-unsharp", "0x6+0.5+0",
            "-dispose", "previous",
            "-delay", str(round(100 / fps)),
            "-loop", "0",
            "-layers", "optimizeframe",
            *files,
            out.as_posix(),
        ]
        # fmt: on

        if magick and cmd[0] == "convert":
            cmd.insert(0, "magick")
        elif exe.name.startswith("magick"):
            cmd.insert(1, "convert")

        try:
            with Progress(
                SpinnerColumn(finished_text="✔"),
                r" [progress.description]{task.description}",
                TimeElapsedColumn(),
            ) as progress:
                task = progress.add_task("Making GIF", total=1)
                subprocess.run(
                    cmd,
                    check=True,
                    capture_output=True,
                )
                progress.advance(task, 1)
                progress.refresh()
        except subprocess.CalledProcessError as e:
            print(e.stderr.decode())
            raise

        self._anim_paths.append(out)

        return None

    def display(self, path: str | Path | None = None, **kwargs) -> Image | Video:
        """Display the animation in a Jupyter notebook.

        Parameters
        ----------
        path
            By default, the last animation file created by :meth:`to_mp4` or :meth:`to_gif`,
            but you can instead pass specify a specific file.
        kwargs
            Passed to :func:`IPython.display.Video` or :func:`IPython.display.Image`.
        """
        from .util import display

        if path is None:
            try:
                p = self._anim_paths[-1]
            except IndexError:
                raise RuntimeError("call `to_mp4` or `to_gif` first")
        else:
            p = Path(path)

        return display(p, **kwargs)

    def cleanup(self) -> Self:
        """Clean up (delete) the frame files associated with this instance.

        :attr:`paths` is reset to ``None``.
        """
        if self.paths is not None:
            for f in self.paths:
                f.unlink(missing_ok=True)
        self.paths = None

        return self
