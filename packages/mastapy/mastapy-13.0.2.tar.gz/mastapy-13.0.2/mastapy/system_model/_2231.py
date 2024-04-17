"""TransmissionTemperatureSet"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TRANSMISSION_TEMPERATURE_SET = python_net_import(
    "SMT.MastaAPI.SystemModel", "TransmissionTemperatureSet"
)


__docformat__ = "restructuredtext en"
__all__ = ("TransmissionTemperatureSet",)


Self = TypeVar("Self", bound="TransmissionTemperatureSet")


class TransmissionTemperatureSet(_0.APIBase):
    """TransmissionTemperatureSet

    This is a mastapy class.
    """

    TYPE = _TRANSMISSION_TEMPERATURE_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TransmissionTemperatureSet")

    class _Cast_TransmissionTemperatureSet:
        """Special nested class for casting TransmissionTemperatureSet to subclasses."""

        def __init__(
            self: "TransmissionTemperatureSet._Cast_TransmissionTemperatureSet",
            parent: "TransmissionTemperatureSet",
        ):
            self._parent = parent

        @property
        def transmission_temperature_set(
            self: "TransmissionTemperatureSet._Cast_TransmissionTemperatureSet",
        ) -> "TransmissionTemperatureSet":
            return self._parent

        def __getattr__(
            self: "TransmissionTemperatureSet._Cast_TransmissionTemperatureSet",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TransmissionTemperatureSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def air_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AirTemperature

        if temp is None:
            return 0.0

        return temp

    @air_temperature.setter
    @enforce_parameter_types
    def air_temperature(self: Self, value: "float"):
        self.wrapped.AirTemperature = float(value) if value is not None else 0.0

    @property
    def housing(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Housing

        if temp is None:
            return 0.0

        return temp

    @housing.setter
    @enforce_parameter_types
    def housing(self: Self, value: "float"):
        self.wrapped.Housing = float(value) if value is not None else 0.0

    @property
    def oil_sump_and_inlet_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilSumpAndInletTemperature

        if temp is None:
            return 0.0

        return temp

    @oil_sump_and_inlet_temperature.setter
    @enforce_parameter_types
    def oil_sump_and_inlet_temperature(self: Self, value: "float"):
        self.wrapped.OilSumpAndInletTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def rolling_bearing_element(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollingBearingElement

        if temp is None:
            return 0.0

        return temp

    @rolling_bearing_element.setter
    @enforce_parameter_types
    def rolling_bearing_element(self: Self, value: "float"):
        self.wrapped.RollingBearingElement = float(value) if value is not None else 0.0

    @property
    def rolling_bearing_inner_race(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollingBearingInnerRace

        if temp is None:
            return 0.0

        return temp

    @rolling_bearing_inner_race.setter
    @enforce_parameter_types
    def rolling_bearing_inner_race(self: Self, value: "float"):
        self.wrapped.RollingBearingInnerRace = (
            float(value) if value is not None else 0.0
        )

    @property
    def rolling_bearing_outer_race(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RollingBearingOuterRace

        if temp is None:
            return 0.0

        return temp

    @rolling_bearing_outer_race.setter
    @enforce_parameter_types
    def rolling_bearing_outer_race(self: Self, value: "float"):
        self.wrapped.RollingBearingOuterRace = (
            float(value) if value is not None else 0.0
        )

    @property
    def shaft(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Shaft

        if temp is None:
            return 0.0

        return temp

    @shaft.setter
    @enforce_parameter_types
    def shaft(self: Self, value: "float"):
        self.wrapped.Shaft = float(value) if value is not None else 0.0

    @property
    def temperature_when_assembled(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TemperatureWhenAssembled

        if temp is None:
            return 0.0

        return temp

    @temperature_when_assembled.setter
    @enforce_parameter_types
    def temperature_when_assembled(self: Self, value: "float"):
        self.wrapped.TemperatureWhenAssembled = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "TransmissionTemperatureSet._Cast_TransmissionTemperatureSet":
        return self._Cast_TransmissionTemperatureSet(self)
