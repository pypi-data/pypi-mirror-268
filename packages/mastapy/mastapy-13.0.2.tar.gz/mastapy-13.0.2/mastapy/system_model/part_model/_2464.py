"""GuideModelUsage"""

from __future__ import annotations

from typing import TypeVar, Any
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_MODEL_USAGE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "GuideModelUsage"
)


__docformat__ = "restructuredtext en"
__all__ = ("GuideModelUsage",)


Self = TypeVar("Self", bound="GuideModelUsage")


class GuideModelUsage(_0.APIBase):
    """GuideModelUsage

    This is a mastapy class.
    """

    TYPE = _GUIDE_MODEL_USAGE

    class AlignmentOptions(Enum):
        """AlignmentOptions is a nested enum."""

        @classmethod
        def type_(cls):
            return _GUIDE_MODEL_USAGE.AlignmentOptions

        LEFT_EDGE_TO_LEFT_OFFSET_OF_SHAFT = 0
        LEFT_EDGE_TO_ZERO_OFFSET_OF_SHAFT = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    AlignmentOptions.__setattr__ = __enum_setattr
    AlignmentOptions.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GuideModelUsage")

    class _Cast_GuideModelUsage:
        """Special nested class for casting GuideModelUsage to subclasses."""

        def __init__(
            self: "GuideModelUsage._Cast_GuideModelUsage", parent: "GuideModelUsage"
        ):
            self._parent = parent

        @property
        def guide_model_usage(
            self: "GuideModelUsage._Cast_GuideModelUsage",
        ) -> "GuideModelUsage":
            return self._parent

        def __getattr__(self: "GuideModelUsage._Cast_GuideModelUsage", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GuideModelUsage.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alignment_method(self: Self) -> "GuideModelUsage.AlignmentOptions":
        """mastapy.system_model.part_model.GuideModelUsage.AlignmentOptions"""
        temp = self.wrapped.AlignmentMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.GuideModelUsage+AlignmentOptions"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.GuideModelUsage.GuideModelUsage",
            "AlignmentOptions",
        )(value)

    @alignment_method.setter
    @enforce_parameter_types
    def alignment_method(self: Self, value: "GuideModelUsage.AlignmentOptions"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.GuideModelUsage+AlignmentOptions"
        )
        self.wrapped.AlignmentMethod = value

    @property
    def clip_drawing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ClipDrawing

        if temp is None:
            return False

        return temp

    @clip_drawing.setter
    @enforce_parameter_types
    def clip_drawing(self: Self, value: "bool"):
        self.wrapped.ClipDrawing = bool(value) if value is not None else False

    @property
    def clipping_bottom(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClippingBottom

        if temp is None:
            return 0.0

        return temp

    @clipping_bottom.setter
    @enforce_parameter_types
    def clipping_bottom(self: Self, value: "float"):
        self.wrapped.ClippingBottom = float(value) if value is not None else 0.0

    @property
    def clipping_left(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClippingLeft

        if temp is None:
            return 0.0

        return temp

    @clipping_left.setter
    @enforce_parameter_types
    def clipping_left(self: Self, value: "float"):
        self.wrapped.ClippingLeft = float(value) if value is not None else 0.0

    @property
    def clipping_right(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClippingRight

        if temp is None:
            return 0.0

        return temp

    @clipping_right.setter
    @enforce_parameter_types
    def clipping_right(self: Self, value: "float"):
        self.wrapped.ClippingRight = float(value) if value is not None else 0.0

    @property
    def clipping_top(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClippingTop

        if temp is None:
            return 0.0

        return temp

    @clipping_top.setter
    @enforce_parameter_types
    def clipping_top(self: Self, value: "float"):
        self.wrapped.ClippingTop = float(value) if value is not None else 0.0

    @property
    def force_monochrome(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ForceMonochrome

        if temp is None:
            return False

        return temp

    @force_monochrome.setter
    @enforce_parameter_types
    def force_monochrome(self: Self, value: "bool"):
        self.wrapped.ForceMonochrome = bool(value) if value is not None else False

    @property
    def layout(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.Layout

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @layout.setter
    @enforce_parameter_types
    def layout(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.Layout = value

    @property
    def origin_horizontal(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OriginHorizontal

        if temp is None:
            return 0.0

        return temp

    @origin_horizontal.setter
    @enforce_parameter_types
    def origin_horizontal(self: Self, value: "float"):
        self.wrapped.OriginHorizontal = float(value) if value is not None else 0.0

    @property
    def origin_vertical(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OriginVertical

        if temp is None:
            return 0.0

        return temp

    @origin_vertical.setter
    @enforce_parameter_types
    def origin_vertical(self: Self, value: "float"):
        self.wrapped.OriginVertical = float(value) if value is not None else 0.0

    @property
    def rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Rotation

        if temp is None:
            return 0.0

        return temp

    @rotation.setter
    @enforce_parameter_types
    def rotation(self: Self, value: "float"):
        self.wrapped.Rotation = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "GuideModelUsage._Cast_GuideModelUsage":
        return self._Cast_GuideModelUsage(self)
