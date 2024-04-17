"""
Similar to ``xmovie``, make animations from xarray objects.
"""

__version__ = "0.0.4"

from .core import Frames
from .util import cleanup, display

__all__ = (
    "Frames",
    "cleanup",
    "display",
)
