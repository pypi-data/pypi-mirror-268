from .imagecontainer import register_imageformat, get_format, ImageFormat
from ._numpy import NumpyImageFormat
from ._pillow import PillowImageFormat
import funcnodes as fn
from exposedfunctionality.function_parser.types import add_type
from . import image_nodes as nodes


add_type(ImageFormat, "ImageFormat")

FUNCNODES_RENDER_OPTIONS: fn.RenderOptions = {
    "typemap": {
        ImageFormat: "image",
    },
}


def imageFormatEncoder(obj: ImageFormat, preview=False):
    if isinstance(obj, ImageFormat):
        if preview:
            return obj.to_thumbnail((200, 200)).to_jpeg(), True
        return obj.to_jpeg(), True
    return obj, False


fn.JSONEncoder.add_encoder(imageFormatEncoder)

__all__ = [
    "register_imageformat",
    "NumpyImageFormat",
    "get_format",
    "PillowImageFormat",
    "ImageFormat",
    "nodes",
]


__version__ = "0.1.0"

NODE_SHELF = nodes.NODE_SHELF
