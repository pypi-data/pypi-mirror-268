"""HairpinConductor"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.electric_machines import _1319
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HAIRPIN_CONDUCTOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "HairpinConductor"
)


__docformat__ = "restructuredtext en"
__all__ = ("HairpinConductor",)


Self = TypeVar("Self", bound="HairpinConductor")


class HairpinConductor(_1319.WindingConductor):
    """HairpinConductor

    This is a mastapy class.
    """

    TYPE = _HAIRPIN_CONDUCTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HairpinConductor")

    class _Cast_HairpinConductor:
        """Special nested class for casting HairpinConductor to subclasses."""

        def __init__(
            self: "HairpinConductor._Cast_HairpinConductor", parent: "HairpinConductor"
        ):
            self._parent = parent

        @property
        def winding_conductor(
            self: "HairpinConductor._Cast_HairpinConductor",
        ) -> "_1319.WindingConductor":
            return self._parent._cast(_1319.WindingConductor)

        @property
        def hairpin_conductor(
            self: "HairpinConductor._Cast_HairpinConductor",
        ) -> "HairpinConductor":
            return self._parent

        def __getattr__(self: "HairpinConductor._Cast_HairpinConductor", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HairpinConductor.TYPE"):
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
    def angle_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngleOffset

        if temp is None:
            return 0.0

        return temp

    @angle_offset.setter
    @enforce_parameter_types
    def angle_offset(self: Self, value: "float"):
        self.wrapped.AngleOffset = float(value) if value is not None else 0.0

    @property
    def corner_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CornerRadius

        if temp is None:
            return 0.0

        return temp

    @corner_radius.setter
    @enforce_parameter_types
    def corner_radius(self: Self, value: "float"):
        self.wrapped.CornerRadius = float(value) if value is not None else 0.0

    @property
    def radial_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialOffset

        if temp is None:
            return 0.0

        return temp

    @radial_offset.setter
    @enforce_parameter_types
    def radial_offset(self: Self, value: "float"):
        self.wrapped.RadialOffset = float(value) if value is not None else 0.0

    @property
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def winding_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindingArea

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_material_height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WindingMaterialHeight

        if temp is None:
            return 0.0

        return temp

    @winding_material_height.setter
    @enforce_parameter_types
    def winding_material_height(self: Self, value: "float"):
        self.wrapped.WindingMaterialHeight = float(value) if value is not None else 0.0

    @property
    def winding_material_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WindingMaterialWidth

        if temp is None:
            return 0.0

        return temp

    @winding_material_width.setter
    @enforce_parameter_types
    def winding_material_width(self: Self, value: "float"):
        self.wrapped.WindingMaterialWidth = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "HairpinConductor._Cast_HairpinConductor":
        return self._Cast_HairpinConductor(self)
