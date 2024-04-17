"""GuideImage"""

from __future__ import annotations

from typing import TypeVar

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_IMAGE = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "GuideImage")


__docformat__ = "restructuredtext en"
__all__ = ("GuideImage",)


Self = TypeVar("Self", bound="GuideImage")


class GuideImage(_0.APIBase):
    """GuideImage

    This is a mastapy class.
    """

    TYPE = _GUIDE_IMAGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideImage")

    class _Cast_GuideImage:
        """Special nested class for casting GuideImage to subclasses."""

        def __init__(self: "GuideImage._Cast_GuideImage", parent: "GuideImage"):
            self._parent = parent

        @property
        def guide_image(self: "GuideImage._Cast_GuideImage") -> "GuideImage":
            return self._parent

        def __getattr__(self: "GuideImage._Cast_GuideImage", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideImage.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_from_left_to_origin(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceFromLeftToOrigin

        if temp is None:
            return 0.0

        return temp

    @distance_from_left_to_origin.setter
    @enforce_parameter_types
    def distance_from_left_to_origin(self: Self, value: "float"):
        self.wrapped.DistanceFromLeftToOrigin = (
            float(value) if value is not None else 0.0
        )

    @property
    def distance_from_top_to_centre(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DistanceFromTopToCentre

        if temp is None:
            return 0.0

        return temp

    @distance_from_top_to_centre.setter
    @enforce_parameter_types
    def distance_from_top_to_centre(self: Self, value: "float"):
        self.wrapped.DistanceFromTopToCentre = (
            float(value) if value is not None else 0.0
        )

    @property
    def image(self: Self) -> "Image":
        """Image"""
        temp = self.wrapped.Image

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @image.setter
    @enforce_parameter_types
    def image(self: Self, value: "Image"):
        value = conversion.mp_to_pn_smt_bitmap(value)
        self.wrapped.Image = value

    @property
    def image_height(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImageHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def image_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ImageWidth

        if temp is None:
            return 0.0

        return temp

    @image_width.setter
    @enforce_parameter_types
    def image_width(self: Self, value: "float"):
        self.wrapped.ImageWidth = float(value) if value is not None else 0.0

    @property
    def transparency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Transparency

        if temp is None:
            return 0.0

        return temp

    @transparency.setter
    @enforce_parameter_types
    def transparency(self: Self, value: "float"):
        self.wrapped.Transparency = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "GuideImage._Cast_GuideImage":
        return self._Cast_GuideImage(self)
