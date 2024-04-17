"""ShaftRadialHole"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.shafts import _21
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_RADIAL_HOLE = python_net_import("SMT.MastaAPI.Shafts", "ShaftRadialHole")

if TYPE_CHECKING:
    from mastapy.shafts import _42


__docformat__ = "restructuredtext en"
__all__ = ("ShaftRadialHole",)


Self = TypeVar("Self", bound="ShaftRadialHole")


class ShaftRadialHole(_21.ShaftFeature):
    """ShaftRadialHole

    This is a mastapy class.
    """

    TYPE = _SHAFT_RADIAL_HOLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftRadialHole")

    class _Cast_ShaftRadialHole:
        """Special nested class for casting ShaftRadialHole to subclasses."""

        def __init__(
            self: "ShaftRadialHole._Cast_ShaftRadialHole", parent: "ShaftRadialHole"
        ):
            self._parent = parent

        @property
        def shaft_feature(
            self: "ShaftRadialHole._Cast_ShaftRadialHole",
        ) -> "_21.ShaftFeature":
            return self._parent._cast(_21.ShaftFeature)

        @property
        def shaft_radial_hole(
            self: "ShaftRadialHole._Cast_ShaftRadialHole",
        ) -> "ShaftRadialHole":
            return self._parent

        def __getattr__(self: "ShaftRadialHole._Cast_ShaftRadialHole", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftRadialHole.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "float"):
        self.wrapped.Angle = float(value) if value is not None else 0.0

    @property
    def diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "float"):
        self.wrapped.Diameter = float(value) if value is not None else 0.0

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

    def add_new_radial_hole(self: Self):
        """Method does not return."""
        self.wrapped.AddNewRadialHole()

    @property
    def cast_to(self: Self) -> "ShaftRadialHole._Cast_ShaftRadialHole":
        return self._Cast_ShaftRadialHole(self)
