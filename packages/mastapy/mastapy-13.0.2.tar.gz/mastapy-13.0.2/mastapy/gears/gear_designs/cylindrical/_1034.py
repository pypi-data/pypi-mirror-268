"""CylindricalGearSetMacroGeometryOptimiser"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears import _335
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MACRO_GEOMETRY_OPTIMISER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalGearSetMacroGeometryOptimiser",
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetMacroGeometryOptimiser",)


Self = TypeVar("Self", bound="CylindricalGearSetMacroGeometryOptimiser")


class CylindricalGearSetMacroGeometryOptimiser(_335.GearSetOptimiser):
    """CylindricalGearSetMacroGeometryOptimiser

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MACRO_GEOMETRY_OPTIMISER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetMacroGeometryOptimiser"
    )

    class _Cast_CylindricalGearSetMacroGeometryOptimiser:
        """Special nested class for casting CylindricalGearSetMacroGeometryOptimiser to subclasses."""

        def __init__(
            self: "CylindricalGearSetMacroGeometryOptimiser._Cast_CylindricalGearSetMacroGeometryOptimiser",
            parent: "CylindricalGearSetMacroGeometryOptimiser",
        ):
            self._parent = parent

        @property
        def gear_set_optimiser(
            self: "CylindricalGearSetMacroGeometryOptimiser._Cast_CylindricalGearSetMacroGeometryOptimiser",
        ) -> "_335.GearSetOptimiser":
            return self._parent._cast(_335.GearSetOptimiser)

        @property
        def cylindrical_gear_set_macro_geometry_optimiser(
            self: "CylindricalGearSetMacroGeometryOptimiser._Cast_CylindricalGearSetMacroGeometryOptimiser",
        ) -> "CylindricalGearSetMacroGeometryOptimiser":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetMacroGeometryOptimiser._Cast_CylindricalGearSetMacroGeometryOptimiser",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "CylindricalGearSetMacroGeometryOptimiser.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def modify_basic_rack(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ModifyBasicRack

        if temp is None:
            return False

        return temp

    @modify_basic_rack.setter
    @enforce_parameter_types
    def modify_basic_rack(self: Self, value: "bool"):
        self.wrapped.ModifyBasicRack = bool(value) if value is not None else False

    @property
    def modify_planet_carrier_diameter(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ModifyPlanetCarrierDiameter

        if temp is None:
            return False

        return temp

    @modify_planet_carrier_diameter.setter
    @enforce_parameter_types
    def modify_planet_carrier_diameter(self: Self, value: "bool"):
        self.wrapped.ModifyPlanetCarrierDiameter = (
            bool(value) if value is not None else False
        )

    @property
    def planet_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PlanetDiameter

        if temp is None:
            return 0.0

        return temp

    @planet_diameter.setter
    @enforce_parameter_types
    def planet_diameter(self: Self, value: "float"):
        self.wrapped.PlanetDiameter = float(value) if value is not None else 0.0

    @property
    def use_compressed_duty_cycle(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseCompressedDutyCycle

        if temp is None:
            return False

        return temp

    @use_compressed_duty_cycle.setter
    @enforce_parameter_types
    def use_compressed_duty_cycle(self: Self, value: "bool"):
        self.wrapped.UseCompressedDutyCycle = (
            bool(value) if value is not None else False
        )

    @property
    def helix_angle_input_is_active(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HelixAngleInputIsActive

        if temp is None:
            return False

        return temp

    @helix_angle_input_is_active.setter
    @enforce_parameter_types
    def helix_angle_input_is_active(self: Self, value: "bool"):
        self.wrapped.HelixAngleInputIsActive = (
            bool(value) if value is not None else False
        )

    @property
    def pressure_angle_input_is_active(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.PressureAngleInputIsActive

        if temp is None:
            return False

        return temp

    @pressure_angle_input_is_active.setter
    @enforce_parameter_types
    def pressure_angle_input_is_active(self: Self, value: "bool"):
        self.wrapped.PressureAngleInputIsActive = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetMacroGeometryOptimiser._Cast_CylindricalGearSetMacroGeometryOptimiser":
        return self._Cast_CylindricalGearSetMacroGeometryOptimiser(self)
