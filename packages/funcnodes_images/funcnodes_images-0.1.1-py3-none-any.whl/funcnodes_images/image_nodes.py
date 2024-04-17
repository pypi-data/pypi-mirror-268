import funcnodes as fn
from funcnodes_images import ImageFormat
from PIL import Image
from typing import Optional
import io
from ._pillow import PillowImageFormat, NumpyImageFormat
from .utils import calc_crop_values


class ShowImage(fn.Node):
    node_id = "image.show"
    node_name = "Show Image"

    default_render_options = {"data": {"src": "img", "type": "image"}}

    img = fn.NodeInput(
        id="img",
        type=ImageFormat,
    )

    async def func(self, img):
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

    x1 = fn.NodeInput(
        id="x1",
        type=int,
        name="left",
        default=0,
        required=False,
    )

    y1 = fn.NodeInput(
        id="y1",
        type=int,
        name="top",
        default=0,
        required=False,
    )

    x2 = fn.NodeInput(
        id="x2",
        type=int,
        name="right",
        required=False,
    )

    y2 = fn.NodeInput(
        id="y2",
        type=int,
        name="bottom",
        required=False,
    )

    cropped_img = fn.NodeOutput(
        id="cropped_img",
        type=ImageFormat,
    )

    async def func(
        self,
        img: ImageFormat,
        x1: Optional[int] = None,
        y1: Optional[int] = None,
        x2: Optional[int] = None,
        y2: Optional[int] = None,
    ):
        x1, y1, x2, y2 = calc_crop_values(img.width(), img.height(), x1, y1, x2, y2)
        out = img.crop(x1, y1, x2, y2)

        self.get_input("x1").set_value(x1, does_trigger=False)
        self.get_input("y1").set_value(y1, does_trigger=False)
        self.get_input("x2").set_value(x2, does_trigger=False)
        self.get_input("y2").set_value(y2, does_trigger=False)
        self.get_output("cropped_img").value = out

        return out


class ToArray(fn.Node):
    node_id = "image.to_array"
    node_name = "To Array"

    img = fn.NodeInput(
        id="img",
        type=ImageFormat,
    )

    array = fn.NodeOutput(
        id="array",
        type="numpy.ndarray",
    )

    async def func(self, img: ImageFormat):
        out = img.to_array()
        self.get_output("array").value = out

        return out


class Dimensions(fn.Node):
    node_id = "image.dimensions"
    node_name = "Dimensions"

    img = fn.NodeInput(
        id="img",
        type=ImageFormat,
    )

    width = fn.NodeOutput(
        id="width",
        type=int,
    )

    height = fn.NodeOutput(
        id="height",
        type=int,
    )

    async def func(self, img: ImageFormat):
        self.get_output("width").value = img.width()
        self.get_output("height").value = img.height()
        return img.width(), img.height()


class FromArray(fn.Node):
    node_id = "image.from_array"
    node_name = "From Array"

    data = fn.NodeInput(
        id="data",
        type="numpy.ndarray",
    )

    img = fn.NodeOutput(
        id="img",
        type=ImageFormat,
    )

    async def func(self, data):
        img = NumpyImageFormat(data)
        self.get_output("img").value = img
        return img


NODE_SHELF = fn.Shelf(
    name="Images",
    nodes=[
        ShowImage,
        ResizeImage,
        FromBytes,
        ScaleImage,
        CropImage,
        ToArray,
        Dimensions,
    ],
    subshelves=[],
    description="Basic Image processing nodes",
)
