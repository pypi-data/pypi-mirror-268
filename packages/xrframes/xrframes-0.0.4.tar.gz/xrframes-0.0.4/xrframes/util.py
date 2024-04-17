from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cartopy.crs import Projection
    from IPython.display import Image, Video


def cleanup() -> None:
    """Clean up frame files from the temporary directory and the CWD."""
    import tempfile

    for loc in [Path.cwd(), Path(tempfile.gettempdir())]:
        for f in loc.glob("*_frame*.png"):
            f.unlink()


def display(path: str | Path, **kwargs) -> Image | Video:
    """Display an animation in a Jupyter notebook.

    Parameters
    ---------
    path
        Path to the ``.mp4`` or ``.gif`` file.
    kwargs
        Passed to :func:`IPython.display.Video` or :func:`IPython.display.Image`.
    """
    from IPython.display import Image, Video

    p = Path(path)

    if p.suffix in {".mp4", ".MP4"}:
        return Video(p.as_posix(), **kwargs)
    elif p.suffix in {".gif", ".GIF"}:
        return Image(p.as_posix(), **kwargs)
    else:
        raise ValueError(f"unexpected file extension: {p.suffix!r}")


def get_globe_proj(*, smooth: bool = True, n: int = 361, **kwargs) -> Projection:
    # https://github.com/jbusecke/xmovie/blob/e19f47a6d17e682a00ab7d040497d65db5fe52a2/xmovie/presets.py#L72
    import cartopy.crs as ccrs

    proj = ccrs.NearsidePerspective(**kwargs)

    if smooth:
        import numpy as np
        import shapely.geometry as sgeom

        wgs84_semi_major_axis = 6378137.0

        a = proj.globe.semimajor_axis or wgs84_semi_major_axis
        h = proj.proj4_params["h"]
        false_easting = proj.proj4_params["x_0"]
        false_northing = proj.proj4_params["y_0"]
        max_x = a * np.sqrt(h / (2 * a + h))

        coords = ccrs._ellipse_boundary(max_x, max_x, false_easting, false_northing, n=n)
        proj._boundary = sgeom.LinearRing(coords.T)

    return proj
