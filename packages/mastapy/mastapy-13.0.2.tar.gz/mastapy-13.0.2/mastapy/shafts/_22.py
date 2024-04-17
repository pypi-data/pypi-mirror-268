"""ShaftGroove"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.shafts import _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_GROOVE = python_net_import("SMT.MastaAPI.Shafts", "ShaftGroove")

if TYPE_CHECKING:
    from mastapy.shafts import _42


__docformat__ = "restructuredtext en"
__all__ = ("ShaftGroove",)


Self = TypeVar("Self", bound="ShaftGroove")


class ShaftGroove(_21.ShaftFeature):
    """ShaftGroove

    This is a mastapy class.
    """

    TYPE = _SHAFT_GROOVE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftGroove")

    class _Cast_ShaftGroove:
        """Special nested class for casting ShaftGroove to subclasses."""

        def __init__(self: "ShaftGroove._Cast_ShaftGroove", parent: "ShaftGroove"):
            self._parent = parent

        @property
        def shaft_feature(self: "ShaftGroove._Cast_ShaftGroove") -> "_21.ShaftFeature":
            return self._parent._cast(_21.ShaftFeature)

        @property
        def shaft_groove(self: "ShaftGroove._Cast_ShaftGroove") -> "ShaftGroove":
            return self._parent

        def __getattr__(self: "ShaftGroove._Cast_ShaftGroove", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftGroove.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Depth

        if temp is None:
            return 0.0

        return temp

    @depth.setter
    @enforce_parameter_types
    def depth(self: Self, value: "float"):
        self.wrapped.Depth = float(value) if value is not None else 0.0

    @property
    def fillet_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FilletRadius

        if temp is None:
            return 0.0

        return temp

    @fillet_radius.setter
    @enforce_parameter_types
    def fillet_radius(self: Self, value: "float"):
        self.wrapped.FilletRadius = float(value) if value is not None else 0.0

    @property
    def surface_roughness(self: Self) -> "_42.ShaftSurfaceRoughness":
        """mastapy.shafts.ShaftSurfaceRoughness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def add_new_groove(self: Self):
        """Method does not return."""
        self.wrapped.AddNewGroove()

    @property
    def cast_to(self: Self) -> "ShaftGroove._Cast_ShaftGroove":
        return self._Cast_ShaftGroove(self)
