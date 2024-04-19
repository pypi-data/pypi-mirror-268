"""
This module provides access to Blender's image manipulation API.

It provides access to image buffers outside of Blender's
bpy.types.Image data-block context.

imbuf.types.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import imbuf.types

from . import types

GenericType = typing.TypeVar("GenericType")

def load(filepath: typing.Union[str, bytes]) -> imbuf.types.ImBuf:
    """Load an image from a file.

    :param filepath: the filepath of the image.
    :type filepath: typing.Union[str, bytes]
    :return: the newly loaded image.
    :rtype: imbuf.types.ImBuf
    """

    ...

def new(size) -> imbuf.types.ImBuf:
    """Load a new image.

    :param size: The size of the image in pixels.
    :return: the newly loaded image.
    :rtype: imbuf.types.ImBuf
    """

    ...

def write(image: imbuf.types.ImBuf, filepath: typing.Union[str, bytes] = None):
    """Write an image.

    :param image: the image to write.
    :type image: imbuf.types.ImBuf
    :param filepath: Optional filepath of the image (fallback to the images file path).
    :type filepath: typing.Union[str, bytes]
    """

    ...
