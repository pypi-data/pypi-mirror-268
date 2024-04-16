import funcnodes as fn
from funcnodes_images import ImageFormat
from PIL import Image
import io
from ._pillow import PillowImageFormat


class ShowImage(fn.Node):
    node_id = "image.show"
    node_name = "Show Image"

    default_render_options = {"data": {"src": "img"}}

    img = fn.NodeInput(
        id="img",
        type=ImageFormat,
    )

    async def func(self, image):
        pass


class ResizeImage(fn.Node):
    node_id = "image.resize"
    node_name = "Resize Image"

    img = fn.NodeInput(
        id="img",
        type=ImageFormat,
    )

    width = fn.NodeInput(
        id="width",
        type=int,
        required=False,
    )

    height = fn.NodeInput(
        id="height",
        type=int,
        required=False,
    )

    resized_img = fn.NodeOutput(
        id="resized_img",
        type=ImageFormat,
    )

    async def func(self, img: ImageFormat, width=None, height=None):
        out = img.resize(w=width, h=height)
        self.get_output("resized_img").value = out

        return out


class FromBytes(fn.Node):
    node_id = "image.from_bytes"
    node_name = "From Bytes"

    data = fn.NodeInput(
        id="data",
        type=bytes,
    )

    img = fn.NodeOutput(
        id="img",
        type=ImageFormat,
    )

    async def func(self, data: bytes):
        buff = io.BytesIO(data)
        img = Image.open(buff)
        self.get_output("img").value = PillowImageFormat(img)
        buff.close()
        return img


class ScaleImage(fn.Node):
    node_id = "image.scale"
    node_name = "Scale Image"

    img = fn.NodeInput(
        id="img",
        type=ImageFormat,
    )

    scale = fn.NodeInput(
        id="scale",
        type=float,
    )

    scaled_img = fn.NodeOutput(
        id="scaled_img",
        type=ImageFormat,
    )

    async def func(self, img: ImageFormat, scale: float):
        out = img.scale(scale)
        self.get_output("scaled_img").value = out

        return out


class CropImage(fn.Node):
    node_id = "image.crop"
    node_name = "Crop Image"

    img = fn.NodeInput(
        id="img",
        type=ImageFormat,
    )

    x1 = fn.NodeInput(id="x1", type=int, name="left")

    y1 = fn.NodeInput(
        id="y1",
        type=int,
        name="top",
    )

    x2 = fn.NodeInput(
        id="x2",
        type=int,
        name="right",
    )

    y2 = fn.NodeInput(
        id="y2",
        type=int,
        name="bottom",
    )

    cropped_img = fn.NodeOutput(
        id="cropped_img",
        type=ImageFormat,
    )

    async def func(self, img: ImageFormat, x1: int, y1: int, x2: int, y2: int):
        out = img.crop(x1, y1, x2, y2)
        self.get_output("cropped_img").value = out

        return out


NODE_SHELF = fn.Shelf(
    name="Images",
    nodes=[
        ShowImage,
        ResizeImage,
        FromBytes,
        ScaleImage,
        CropImage,
    ],
)
