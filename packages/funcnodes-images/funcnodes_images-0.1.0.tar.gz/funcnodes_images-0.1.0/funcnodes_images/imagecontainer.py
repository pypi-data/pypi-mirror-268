from abc import ABC, abstractmethod
from typing import Type
import numpy as np
from typing import Any, TYPE_CHECKING, Generic, TypeVar, Callable, Dict
import io
from PIL import Image
import os
from .utils import calc_new_size


if TYPE_CHECKING:
    from ._numpy import NumpyImageFormat
    from ._pillow import PillowImageFormat


T = TypeVar("T")


IMAGE_FORMATS: Dict[str, Type["ImageFormat"]] = {}


class ImageFormat(ABC, Generic[T]):  # noqa: F821
    _to_converters: Dict[
        "ImageFormat", Dict["ImageFormat", Callable[["ImageFormat"], "ImageFormat"]]
    ] = {}

    def __init__(self, data: T):
        self._data: T = data

    @property
    def data(self) -> T:
        return self.get_data_copy()

    @abstractmethod
    def get_data_copy(self) -> T:
        pass

    def to(self, cls: Type["ImageFormat"] | str) -> "ImageFormat":
        if isinstance(cls, str):
            cls = IMAGE_FORMATS[cls]
        if self.__class__ == cls:
            return self
        if cls in ImageFormat._to_converters[self.__class__]:
            return self._to_converters[self.__class__][cls](self)

    @classmethod
    def add_to_converter(
        self_cls,
        other_cls: Type["ImageFormat"],
        converter: Callable[["ImageFormat"], "ImageFormat"],
    ):
        if self_cls not in ImageFormat._to_converters:
            ImageFormat._to_converters[self_cls] = {}
        ImageFormat._to_converters[self_cls][other_cls] = converter

    def get_to_converter(
        self, cls: Type["ImageFormat"]
    ) -> Callable[["ImageFormat"], "ImageFormat"]:
        if self.__class__ == cls:
            return lambda x: x
        if self.__class__ not in ImageFormat._to_converters:
            ImageFormat._to_converters[self.__class__] = {}
        return ImageFormat._to_converters[self.__class__].get(cls)

    def __getattribute__(self, name: str) -> Any:
        try:
            return super().__getattribute__(name)
        except AttributeError as e:
            if name.startswith("to_"):
                _to = name[3:]

                if _to in IMAGE_FORMATS:
                    other = IMAGE_FORMATS[_to]
                    conv = self.get_to_converter(other)
                    if conv:
                        return lambda: conv(self)
            raise

    @classmethod
    def from_array(cls, data: np.ndarray):
        from ._numpy import NumpyImageFormat

        return NumpyImageFormat(data).to(cls)

    def to_array(self) -> np.ndarray:
        return self.to_np.data

    @classmethod
    def from_file(cls, path: str):
        from ._pillow import PillowImageFormat

        img = Image.open(path)
        return PillowImageFormat(img).to(cls)

    @classmethod
    def from_bytes(cls, data: bytes):
        from ._pillow import PillowImageFormat

        img = Image.open(io.BytesIO(data))
        return PillowImageFormat(img).to(cls)

    def to_jpeg(self, quality=75) -> bytes:
        img: Image = self.to_img().data
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format="JPEG", quality=int(quality))
        return img_byte_array.getvalue()

    def to_thumbnail(self, size: tuple) -> "ImageFormat[T]":
        img: Image = self.to_img().data
        img.thumbnail(size)
        return self.__class__.from_array(np.array(img))

    def resize(
        self,
        w: int = None,
        h: int = None,
    ) -> "ImageFormat[T]":
        img: Image = self.to_img().data
        new_x, new_y = calc_new_size(img.width, img.height, w, h)
        img = img.resize((new_x, new_y))
        return self.__class__.from_array(np.array(img))

    def crop(self, x1, y1, x2, y2) -> "ImageFormat[T]":
        img: Image = self.to_img().data
        img = img.crop((x1, y1, x2, y2))
        return self.__class__.from_array(np.array(img))

    def scale(self, factor: float) -> "ImageFormat[T]":
        if factor <= 0:
            raise ValueError("factor must be greater than 0")

        img: Image = self.to_img().data
        img = img.resize((int(img.width * factor), int(img.height * factor)))
        return self.__class__.from_array(np.array(img))


def register_imageformat(
    imageformat: Type[ImageFormat], key: str, overwrite=False, _raise=True
):
    if not issubclass(imageformat, ImageFormat):
        raise ValueError("format must be a subclass of ImageFormat")
    if key in IMAGE_FORMATS:
        if IMAGE_FORMATS[key] == imageformat:
            return
        if not overwrite:
            if _raise:
                raise ValueError(
                    f"key '{key} 'already exists in image_formats as {IMAGE_FORMATS[key]}"
                )
            else:
                return
    IMAGE_FORMATS[key] = imageformat


def get_format(key: str) -> Type[ImageFormat]:
    return IMAGE_FORMATS[key]
