"""PlanetManufactureError"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_MANUFACTURE_ERROR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PlanetManufactureError"
)


__docformat__ = "restructuredtext en"
__all__ = ("PlanetManufactureError",)


Self = TypeVar("Self", bound="PlanetManufactureError")


class PlanetManufactureError(_0.APIBase):
    """PlanetManufactureError

    This is a mastapy class.
    """

    TYPE = _PLANET_MANUFACTURE_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetManufactureError")

    class _Cast_PlanetManufactureError:
        """Special nested class for casting PlanetManufactureError to subclasses."""

        def __init__(
            self: "PlanetManufactureError._Cast_PlanetManufactureError",
            parent: "PlanetManufactureError",
        ):
            self._parent = parent

        @property
        def planet_manufacture_error(
            self: "PlanetManufactureError._Cast_PlanetManufactureError",
        ) -> "PlanetManufactureError":
            return self._parent

        def __getattr__(
            self: "PlanetManufactureError._Cast_PlanetManufactureError", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetManufactureError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_error_in_pin_coordinate_system(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngleOfErrorInPinCoordinateSystem

        if temp is None:
            return 0.0

        return temp

    @angle_of_error_in_pin_coordinate_system.setter
    @enforce_parameter_types
    def angle_of_error_in_pin_coordinate_system(self: Self, value: "float"):
        self.wrapped.AngleOfErrorInPinCoordinateSystem = (
            float(value) if value is not None else 0.0
        )

    @property
    def angular_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngularError

        if temp is None:
            return 0.0

        return temp

    @angular_error.setter
    @enforce_parameter_types
    def angular_error(self: Self, value: "float"):
        self.wrapped.AngularError = float(value) if value is not None else 0.0

    @property
    def hole_radial_displacement(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HoleRadialDisplacement

        if temp is None:
            return 0.0

        return temp

    @hole_radial_displacement.setter
    @enforce_parameter_types
    def hole_radial_displacement(self: Self, value: "float"):
        self.wrapped.HoleRadialDisplacement = float(value) if value is not None else 0.0

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def radial_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialError

        if temp is None:
            return 0.0

        return temp

    @radial_error.setter
    @enforce_parameter_types
    def radial_error(self: Self, value: "float"):
        self.wrapped.RadialError = float(value) if value is not None else 0.0

    @property
    def radial_error_carrier(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialErrorCarrier

        if temp is None:
            return 0.0

        return temp

    @radial_error_carrier.setter
    @enforce_parameter_types
    def radial_error_carrier(self: Self, value: "float"):
        self.wrapped.RadialErrorCarrier = float(value) if value is not None else 0.0

    @property
    def radial_tilt_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialTiltError

        if temp is None:
            return 0.0

        return temp

    @radial_tilt_error.setter
    @enforce_parameter_types
    def radial_tilt_error(self: Self, value: "float"):
        self.wrapped.RadialTiltError = float(value) if value is not None else 0.0

    @property
    def tangential_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TangentialError

        if temp is None:
            return 0.0

        return temp

    @tangential_error.setter
    @enforce_parameter_types
    def tangential_error(self: Self, value: "float"):
        self.wrapped.TangentialError = float(value) if value is not None else 0.0

    @property
    def tangential_tilt_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TangentialTiltError

        if temp is None:
            return 0.0

        return temp

    @tangential_tilt_error.setter
    @enforce_parameter_types
    def tangential_tilt_error(self: Self, value: "float"):
        self.wrapped.TangentialTiltError = float(value) if value is not None else 0.0

    @property
    def x_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.XError

        if temp is None:
            return 0.0

        return temp

    @x_error.setter
    @enforce_parameter_types
    def x_error(self: Self, value: "float"):
        self.wrapped.XError = float(value) if value is not None else 0.0

    @property
    def x_tilt_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.XTiltError

        if temp is None:
            return 0.0

        return temp

    @x_tilt_error.setter
    @enforce_parameter_types
    def x_tilt_error(self: Self, value: "float"):
        self.wrapped.XTiltError = float(value) if value is not None else 0.0

    @property
    def y_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.YError

        if temp is None:
            return 0.0

        return temp

    @y_error.setter
    @enforce_parameter_types
    def y_error(self: Self, value: "float"):
        self.wrapped.YError = float(value) if value is not None else 0.0

    @property
    def y_tilt_error(self: Self) -> "float":
        """float"""
        temp = self.wrapped.YTiltError

        if temp is None:
            return 0.0

        return temp

    @y_tilt_error.setter
    @enforce_parameter_types
    def y_tilt_error(self: Self, value: "float"):
        self.wrapped.YTiltError = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "PlanetManufactureError._Cast_PlanetManufactureError":
        return self._Cast_PlanetManufactureError(self)
