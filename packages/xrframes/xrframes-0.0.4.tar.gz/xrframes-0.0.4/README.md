# xrframes

[![Version on PyPI](https://img.shields.io/pypi/v/xrframes.svg)](https://pypi.org/project/xrframes/)
[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)

Similar to (and inspired by) [jbusecke/xmovie](https://github.com/jbusecke/xmovie),
make animations from [xarray](https://xarray.dev/) objects
by applying a [matplotlib](https://matplotlib.org/)-based plotting function along a dimension.

## Install

```sh
pip install xrframes
```

Install and use Dask[^a] or joblib[^b] to parallelize the frame creation step.

`.to_gif()` uses ImageMagick (`magick` or `convert` required on PATH);
`.to_mp4()` uses FFmpeg (`ffmpeg` required on PATH).
Both are available via conda-forge[^c], as well as other package managers.

## Example

Basic example, using just the xarray object's plot method:

```python
import xarray as xr
from xrframes import Frames

# Note: `pooch` required
ta = xr.tutorial.open_dataset("air_temperature").air.isel(time=slice(0, 10))

frames = Frames(ta, lambda da: da.plot(size=2.5, aspect=1.7), dim="time")
frames.write(dpi=120)  # serial
frames.to_gif("./ta_basic.gif", fps=5)
```

A bit fancier example with the same data, using Cartopy:

```python
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
from xrframes import Frames

# Note: `pooch` required
ta = xr.tutorial.open_dataset("air_temperature").air.isel(time=slice(0, 10))

proj = ccrs.Mercator()
tran = ccrs.PlateCarree()

def plot(da, **kwargs):
    fig, ax = plt.subplots(figsize=(6, 3), layout="constrained", subplot_kw=dict(projection=proj))

    ax.coastlines()
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.STATES)
    ax.gridlines(draw_labels=True)

    da.plot.contourf(**kwargs, levels=np.arange(230, 305, 5), extend="both", ax=ax, transform=tran)

    ax.set_title("")
    ax.set_title(pd.Timestamp(da.time.item()).strftime(r"%Y-%m-%d %H:%M"), loc="left", size=10)

    return fig

frames = Frames(ta, plot, dim="time")
frames.write()  # serial
frames.to_mp4("./ta_cartopy.mp4", fps=5)
```

[^a]: `dask` on PyPI, `dask-core` on conda-forge, more info [here](https://docs.dask.org/en/stable/install.html)
[^b]: `joblib` on PyPI and on conda-forge
[^c]: `conda install -c conda-forge imagemagick ffmpeg`
