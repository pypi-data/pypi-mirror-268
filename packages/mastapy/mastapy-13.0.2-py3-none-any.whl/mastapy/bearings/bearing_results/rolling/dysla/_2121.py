"""DynamicBearingAnalysisOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_BEARING_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.Dysla",
    "DynamicBearingAnalysisOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("DynamicBearingAnalysisOptions",)


Self = TypeVar("Self", bound="DynamicBearingAnalysisOptions")


class DynamicBearingAnalysisOptions(_0.APIBase):
    """DynamicBearingAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_BEARING_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicBearingAnalysisOptions")

    class _Cast_DynamicBearingAnalysisOptions:
        """Special nested class for casting DynamicBearingAnalysisOptions to subclasses."""

        def __init__(
            self: "DynamicBearingAnalysisOptions._Cast_DynamicBearingAnalysisOptions",
            parent: "DynamicBearingAnalysisOptions",
        ):
            self._parent = parent

        @property
        def dynamic_bearing_analysis_options(
            self: "DynamicBearingAnalysisOptions._Cast_DynamicBearingAnalysisOptions",
        ) -> "DynamicBearingAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "DynamicBearingAnalysisOptions._Cast_DynamicBearingAnalysisOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicBearingAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_displacement_damping_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ElementDisplacementDampingFactor

        if temp is None:
            return 0.0

        return temp

    @element_displacement_damping_factor.setter
    @enforce_parameter_types
    def element_displacement_damping_factor(self: Self, value: "float"):
        self.wrapped.ElementDisplacementDampingFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def end_revolution(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndRevolution

        if temp is None:
            return 0.0

        return temp

    @end_revolution.setter
    @enforce_parameter_types
    def end_revolution(self: Self, value: "float"):
        self.wrapped.EndRevolution = float(value) if value is not None else 0.0

    @property
    def end_time(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndTime

        if temp is None:
            return 0.0

        return temp

    @end_time.setter
    @enforce_parameter_types
    def end_time(self: Self, value: "float"):
        self.wrapped.EndTime = float(value) if value is not None else 0.0

    @property
    def include_cage(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeCage

        if temp is None:
            return False

        return temp

    @include_cage.setter
    @enforce_parameter_types
    def include_cage(self: Self, value: "bool"):
        self.wrapped.IncludeCage = bool(value) if value is not None else False

    @property
    def include_torsional_vibration_on_inner(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeTorsionalVibrationOnInner

        if temp is None:
            return False

        return temp

    @include_torsional_vibration_on_inner.setter
    @enforce_parameter_types
    def include_torsional_vibration_on_inner(self: Self, value: "bool"):
        self.wrapped.IncludeTorsionalVibrationOnInner = (
            bool(value) if value is not None else False
        )

    @property
    def include_torsional_vibration_on_outer(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeTorsionalVibrationOnOuter

        if temp is None:
            return False

        return temp

    @include_torsional_vibration_on_outer.setter
    @enforce_parameter_types
    def include_torsional_vibration_on_outer(self: Self, value: "bool"):
        self.wrapped.IncludeTorsionalVibrationOnOuter = (
            bool(value) if value is not None else False
        )

    @property
    def log_all_points_during_cage_impacts(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LogAllPointsDuringCageImpacts

        if temp is None:
            return False

        return temp

    @log_all_points_during_cage_impacts.setter
    @enforce_parameter_types
    def log_all_points_during_cage_impacts(self: Self, value: "bool"):
        self.wrapped.LogAllPointsDuringCageImpacts = (
            bool(value) if value is not None else False
        )

    @property
    def log_all_points(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LogAllPoints

        if temp is None:
            return False

        return temp

    @log_all_points.setter
    @enforce_parameter_types
    def log_all_points(self: Self, value: "bool"):
        self.wrapped.LogAllPoints = bool(value) if value is not None else False

    @property
    def logging_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LoggingFrequency

        if temp is None:
            return 0.0

        return temp

    @logging_frequency.setter
    @enforce_parameter_types
    def logging_frequency(self: Self, value: "float"):
        self.wrapped.LoggingFrequency = float(value) if value is not None else 0.0

    @property
    def maximum_number_of_time_steps(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfTimeSteps

        if temp is None:
            return 0

        return temp

    @maximum_number_of_time_steps.setter
    @enforce_parameter_types
    def maximum_number_of_time_steps(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfTimeSteps = int(value) if value is not None else 0

    @property
    def order_of_inner_torsional_vibrations(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OrderOfInnerTorsionalVibrations

        if temp is None:
            return 0.0

        return temp

    @order_of_inner_torsional_vibrations.setter
    @enforce_parameter_types
    def order_of_inner_torsional_vibrations(self: Self, value: "float"):
        self.wrapped.OrderOfInnerTorsionalVibrations = (
            float(value) if value is not None else 0.0
        )

    @property
    def order_of_outer_torsional_vibrations(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OrderOfOuterTorsionalVibrations

        if temp is None:
            return 0.0

        return temp

    @order_of_outer_torsional_vibrations.setter
    @enforce_parameter_types
    def order_of_outer_torsional_vibrations(self: Self, value: "float"):
        self.wrapped.OrderOfOuterTorsionalVibrations = (
            float(value) if value is not None else 0.0
        )

    @property
    def percentage_amplitude_inner_torsional_vibration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageAmplitudeInnerTorsionalVibration

        if temp is None:
            return 0.0

        return temp

    @percentage_amplitude_inner_torsional_vibration.setter
    @enforce_parameter_types
    def percentage_amplitude_inner_torsional_vibration(self: Self, value: "float"):
        self.wrapped.PercentageAmplitudeInnerTorsionalVibration = (
            float(value) if value is not None else 0.0
        )

    @property
    def percentage_amplitude_outer_torsional_vibration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PercentageAmplitudeOuterTorsionalVibration

        if temp is None:
            return 0.0

        return temp

    @percentage_amplitude_outer_torsional_vibration.setter
    @enforce_parameter_types
    def percentage_amplitude_outer_torsional_vibration(self: Self, value: "float"):
        self.wrapped.PercentageAmplitudeOuterTorsionalVibration = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_number_of_element_revolutions(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseNumberOfElementRevolutions

        if temp is None:
            return False

        return temp

    @use_number_of_element_revolutions.setter
    @enforce_parameter_types
    def use_number_of_element_revolutions(self: Self, value: "bool"):
        self.wrapped.UseNumberOfElementRevolutions = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicBearingAnalysisOptions._Cast_DynamicBearingAnalysisOptions":
        return self._Cast_DynamicBearingAnalysisOptions(self)
