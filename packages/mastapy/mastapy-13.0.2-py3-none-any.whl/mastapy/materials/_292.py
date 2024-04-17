"""VehicleDynamicsProperties"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VEHICLE_DYNAMICS_PROPERTIES = python_net_import(
    "SMT.MastaAPI.Materials", "VehicleDynamicsProperties"
)


__docformat__ = "restructuredtext en"
__all__ = ("VehicleDynamicsProperties",)


Self = TypeVar("Self", bound="VehicleDynamicsProperties")


class VehicleDynamicsProperties(_0.APIBase):
    """VehicleDynamicsProperties

    This is a mastapy class.
    """

    TYPE = _VEHICLE_DYNAMICS_PROPERTIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VehicleDynamicsProperties")

    class _Cast_VehicleDynamicsProperties:
        """Special nested class for casting VehicleDynamicsProperties to subclasses."""

        def __init__(
            self: "VehicleDynamicsProperties._Cast_VehicleDynamicsProperties",
            parent: "VehicleDynamicsProperties",
        ):
            self._parent = parent

        @property
        def vehicle_dynamics_properties(
            self: "VehicleDynamicsProperties._Cast_VehicleDynamicsProperties",
        ) -> "VehicleDynamicsProperties":
            return self._parent

        def __getattr__(
            self: "VehicleDynamicsProperties._Cast_VehicleDynamicsProperties", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VehicleDynamicsProperties.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def aerodynamic_drag_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AerodynamicDragCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def air_density(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AirDensity

        if temp is None:
            return 0.0

        return temp

    @air_density.setter
    @enforce_parameter_types
    def air_density(self: Self, value: "float"):
        self.wrapped.AirDensity = float(value) if value is not None else 0.0

    @property
    def drag_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DragCoefficient

        if temp is None:
            return 0.0

        return temp

    @drag_coefficient.setter
    @enforce_parameter_types
    def drag_coefficient(self: Self, value: "float"):
        self.wrapped.DragCoefficient = float(value) if value is not None else 0.0

    @property
    def number_of_wheels(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfWheels

        if temp is None:
            return 0

        return temp

    @number_of_wheels.setter
    @enforce_parameter_types
    def number_of_wheels(self: Self, value: "int"):
        self.wrapped.NumberOfWheels = int(value) if value is not None else 0

    @property
    def rolling_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollingRadius

        if temp is None:
            return 0.0

        return temp

    @rolling_radius.setter
    @enforce_parameter_types
    def rolling_radius(self: Self, value: "float"):
        self.wrapped.RollingRadius = float(value) if value is not None else 0.0

    @property
    def rolling_resistance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingResistance

        if temp is None:
            return 0.0

        return temp

    @property
    def rolling_resistance_coefficient(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollingResistanceCoefficient

        if temp is None:
            return 0.0

        return temp

    @rolling_resistance_coefficient.setter
    @enforce_parameter_types
    def rolling_resistance_coefficient(self: Self, value: "float"):
        self.wrapped.RollingResistanceCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def vehicle_effective_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VehicleEffectiveInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def vehicle_effective_mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VehicleEffectiveMass

        if temp is None:
            return 0.0

        return temp

    @property
    def vehicle_frontal_area(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VehicleFrontalArea

        if temp is None:
            return 0.0

        return temp

    @vehicle_frontal_area.setter
    @enforce_parameter_types
    def vehicle_frontal_area(self: Self, value: "float"):
        self.wrapped.VehicleFrontalArea = float(value) if value is not None else 0.0

    @property
    def vehicle_mass(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VehicleMass

        if temp is None:
            return 0.0

        return temp

    @vehicle_mass.setter
    @enforce_parameter_types
    def vehicle_mass(self: Self, value: "float"):
        self.wrapped.VehicleMass = float(value) if value is not None else 0.0

    @property
    def wheel_inertia(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelInertia

        if temp is None:
            return 0.0

        return temp

    @wheel_inertia.setter
    @enforce_parameter_types
    def wheel_inertia(self: Self, value: "float"):
        self.wrapped.WheelInertia = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "VehicleDynamicsProperties._Cast_VehicleDynamicsProperties":
        return self._Cast_VehicleDynamicsProperties(self)
