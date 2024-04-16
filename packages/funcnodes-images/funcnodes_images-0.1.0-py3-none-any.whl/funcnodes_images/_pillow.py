from PIL import Image
from typing import TYPE_CHECKING, Generic
import numpy as np
from .imagecontainer import ImageFormat, register_imageformat
from ._numpy import NumpyImageFormat


class PillowImageFormat(ImageFormat[Image.Image]):
    def __init__(self, img: Image.Image) -> None:
        if not isinstance(img, Image.Image):
            raise TypeError("img must be a PIL Image")
        super().__init__(img)

    def to_array(self) -> np.ndarray:
        return np.array(self._data)

    def get_data_copy(self) -> Image.Image:
        return self._data.copy()


def pillow_to_numpy(img: PillowImageFormat) -> NumpyImageFormat:
    return NumpyImageFormat(np.array(img.data))


PillowImageFormat.add_to_converter(NumpyImageFormat, pillow_to_numpy)


def numpy_to_pil(img: NumpyImageFormat) -> PillowImageFormat:
    return PillowImageFormat(Image.fromarray(img.to_rgb_uint8()))


NumpyImageFormat.add_to_converter(PillowImageFormat, numpy_to_pil)


register_imageformat(PillowImageFormat, "img")
