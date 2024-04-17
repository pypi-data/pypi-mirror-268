"""ISOScuffingResultsRow"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.rating.cylindrical import _487
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO_SCUFFING_RESULTS_ROW = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "ISOScuffingResultsRow"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISOScuffingResultsRow",)


Self = TypeVar("Self", bound="ISOScuffingResultsRow")


class ISOScuffingResultsRow(_487.ScuffingResultsRow):
    """ISOScuffingResultsRow

    This is a mastapy class.
    """

    TYPE = _ISO_SCUFFING_RESULTS_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISOScuffingResultsRow")

    class _Cast_ISOScuffingResultsRow:
        """Special nested class for casting ISOScuffingResultsRow to subclasses."""

        def __init__(
            self: "ISOScuffingResultsRow._Cast_ISOScuffingResultsRow",
            parent: "ISOScuffingResultsRow",
        ):
            self._parent = parent

        @property
        def scuffing_results_row(
            self: "ISOScuffingResultsRow._Cast_ISOScuffingResultsRow",
        ) -> "_487.ScuffingResultsRow":
            return self._parent._cast(_487.ScuffingResultsRow)

        @property
        def iso_scuffing_results_row(
            self: "ISOScuffingResultsRow._Cast_ISOScuffingResultsRow",
        ) -> "ISOScuffingResultsRow":
            return self._parent

        def __getattr__(
            self: "ISOScuffingResultsRow._Cast_ISOScuffingResultsRow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISOScuffingResultsRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def approach_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ApproachFactor

        if temp is None:
            return 0.0

        return temp

    @approach_factor.setter
    @enforce_parameter_types
    def approach_factor(self: Self, value: "float"):
        self.wrapped.ApproachFactor = float(value) if value is not None else 0.0

    @property
    def contact_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactTemperature

        if temp is None:
            return 0.0

        return temp

    @contact_temperature.setter
    @enforce_parameter_types
    def contact_temperature(self: Self, value: "float"):
        self.wrapped.ContactTemperature = float(value) if value is not None else 0.0

    @property
    def flash_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FlashTemperature

        if temp is None:
            return 0.0

        return temp

    @flash_temperature.setter
    @enforce_parameter_types
    def flash_temperature(self: Self, value: "float"):
        self.wrapped.FlashTemperature = float(value) if value is not None else 0.0

    @property
    def geometry_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GeometryFactor

        if temp is None:
            return 0.0

        return temp

    @geometry_factor.setter
    @enforce_parameter_types
    def geometry_factor(self: Self, value: "float"):
        self.wrapped.GeometryFactor = float(value) if value is not None else 0.0

    @property
    def pinion_rolling_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionRollingVelocity

        if temp is None:
            return 0.0

        return temp

    @pinion_rolling_velocity.setter
    @enforce_parameter_types
    def pinion_rolling_velocity(self: Self, value: "float"):
        self.wrapped.PinionRollingVelocity = float(value) if value is not None else 0.0

    @property
    def sliding_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @sliding_velocity.setter
    @enforce_parameter_types
    def sliding_velocity(self: Self, value: "float"):
        self.wrapped.SlidingVelocity = float(value) if value is not None else 0.0

    @property
    def thermo_elastic_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ThermoElasticFactor

        if temp is None:
            return 0.0

        return temp

    @thermo_elastic_factor.setter
    @enforce_parameter_types
    def thermo_elastic_factor(self: Self, value: "float"):
        self.wrapped.ThermoElasticFactor = float(value) if value is not None else 0.0

    @property
    def wheel_rolling_velocity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelRollingVelocity

        if temp is None:
            return 0.0

        return temp

    @wheel_rolling_velocity.setter
    @enforce_parameter_types
    def wheel_rolling_velocity(self: Self, value: "float"):
        self.wrapped.WheelRollingVelocity = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ISOScuffingResultsRow._Cast_ISOScuffingResultsRow":
        return self._Cast_ISOScuffingResultsRow(self)
