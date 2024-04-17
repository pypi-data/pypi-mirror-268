"""MBDRunUpAnalysisOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MBD_RUN_UP_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "MBDRunUpAnalysisOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5456,
        _5491,
        _5496,
    )


__docformat__ = "restructuredtext en"
__all__ = ("MBDRunUpAnalysisOptions",)


Self = TypeVar("Self", bound="MBDRunUpAnalysisOptions")


class MBDRunUpAnalysisOptions(
    _7544.AbstractAnalysisOptions["_6814.TimeSeriesLoadCase"]
):
    """MBDRunUpAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _MBD_RUN_UP_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MBDRunUpAnalysisOptions")

    class _Cast_MBDRunUpAnalysisOptions:
        """Special nested class for casting MBDRunUpAnalysisOptions to subclasses."""

        def __init__(
            self: "MBDRunUpAnalysisOptions._Cast_MBDRunUpAnalysisOptions",
            parent: "MBDRunUpAnalysisOptions",
        ):
            self._parent = parent

        @property
        def abstract_analysis_options(
            self: "MBDRunUpAnalysisOptions._Cast_MBDRunUpAnalysisOptions",
        ) -> "_7544.AbstractAnalysisOptions":
            return self._parent._cast(_7544.AbstractAnalysisOptions)

        @property
        def mbd_run_up_analysis_options(
            self: "MBDRunUpAnalysisOptions._Cast_MBDRunUpAnalysisOptions",
        ) -> "MBDRunUpAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "MBDRunUpAnalysisOptions._Cast_MBDRunUpAnalysisOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MBDRunUpAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def input_velocity_processing_type(
        self: Self,
    ) -> "_5456.InputVelocityForRunUpProcessingType":
        """mastapy.system_model.analyses_and_results.mbd_analyses.InputVelocityForRunUpProcessingType"""
        temp = self.wrapped.InputVelocityProcessingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InputVelocityForRunUpProcessingType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5456",
            "InputVelocityForRunUpProcessingType",
        )(value)

    @input_velocity_processing_type.setter
    @enforce_parameter_types
    def input_velocity_processing_type(
        self: Self, value: "_5456.InputVelocityForRunUpProcessingType"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.InputVelocityForRunUpProcessingType",
        )
        self.wrapped.InputVelocityProcessingType = value

    @property
    def polynomial_order(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PolynomialOrder

        if temp is None:
            return 0

        return temp

    @polynomial_order.setter
    @enforce_parameter_types
    def polynomial_order(self: Self, value: "int"):
        self.wrapped.PolynomialOrder = int(value) if value is not None else 0

    @property
    def power_load_for_run_up_torque(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.PowerLoadForRunUpTorque

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @power_load_for_run_up_torque.setter
    @enforce_parameter_types
    def power_load_for_run_up_torque(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.PowerLoadForRunUpTorque = value

    @property
    def reference_power_load_for_run_up_speed(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.ReferencePowerLoadForRunUpSpeed

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @reference_power_load_for_run_up_speed.setter
    @enforce_parameter_types
    def reference_power_load_for_run_up_speed(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.ReferencePowerLoadForRunUpSpeed = value

    @property
    def run_down_after(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.RunDownAfter

        if temp is None:
            return False

        return temp

    @run_down_after.setter
    @enforce_parameter_types
    def run_down_after(self: Self, value: "bool"):
        self.wrapped.RunDownAfter = bool(value) if value is not None else False

    @property
    def run_up_driving_mode(self: Self) -> "_5491.RunUpDrivingMode":
        """mastapy.system_model.analyses_and_results.mbd_analyses.RunUpDrivingMode"""
        temp = self.wrapped.RunUpDrivingMode

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.RunUpDrivingMode",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5491",
            "RunUpDrivingMode",
        )(value)

    @run_up_driving_mode.setter
    @enforce_parameter_types
    def run_up_driving_mode(self: Self, value: "_5491.RunUpDrivingMode"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.RunUpDrivingMode",
        )
        self.wrapped.RunUpDrivingMode = value

    @property
    def run_up_end_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RunUpEndSpeed

        if temp is None:
            return 0.0

        return temp

    @run_up_end_speed.setter
    @enforce_parameter_types
    def run_up_end_speed(self: Self, value: "float"):
        self.wrapped.RunUpEndSpeed = float(value) if value is not None else 0.0

    @property
    def run_up_start_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RunUpStartSpeed

        if temp is None:
            return 0.0

        return temp

    @run_up_start_speed.setter
    @enforce_parameter_types
    def run_up_start_speed(self: Self, value: "float"):
        self.wrapped.RunUpStartSpeed = float(value) if value is not None else 0.0

    @property
    def shape_of_initial_acceleration_period(
        self: Self,
    ) -> "_5496.ShapeOfInitialAccelerationPeriodForRunUp":
        """mastapy.system_model.analyses_and_results.mbd_analyses.ShapeOfInitialAccelerationPeriodForRunUp"""
        temp = self.wrapped.ShapeOfInitialAccelerationPeriod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.ShapeOfInitialAccelerationPeriodForRunUp",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5496",
            "ShapeOfInitialAccelerationPeriodForRunUp",
        )(value)

    @shape_of_initial_acceleration_period.setter
    @enforce_parameter_types
    def shape_of_initial_acceleration_period(
        self: Self, value: "_5496.ShapeOfInitialAccelerationPeriodForRunUp"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.ShapeOfInitialAccelerationPeriodForRunUp",
        )
        self.wrapped.ShapeOfInitialAccelerationPeriod = value

    @property
    def time_to_change_direction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TimeToChangeDirection

        if temp is None:
            return 0.0

        return temp

    @time_to_change_direction.setter
    @enforce_parameter_types
    def time_to_change_direction(self: Self, value: "float"):
        self.wrapped.TimeToChangeDirection = float(value) if value is not None else 0.0

    @property
    def time_to_keep_linear_speed_before_reaching_minimum_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TimeToKeepLinearSpeedBeforeReachingMinimumSpeed

        if temp is None:
            return 0.0

        return temp

    @time_to_keep_linear_speed_before_reaching_minimum_speed.setter
    @enforce_parameter_types
    def time_to_keep_linear_speed_before_reaching_minimum_speed(
        self: Self, value: "float"
    ):
        self.wrapped.TimeToKeepLinearSpeedBeforeReachingMinimumSpeed = (
            float(value) if value is not None else 0.0
        )

    @property
    def time_to_reach_minimum_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TimeToReachMinimumSpeed

        if temp is None:
            return 0.0

        return temp

    @time_to_reach_minimum_speed.setter
    @enforce_parameter_types
    def time_to_reach_minimum_speed(self: Self, value: "float"):
        self.wrapped.TimeToReachMinimumSpeed = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "MBDRunUpAnalysisOptions._Cast_MBDRunUpAnalysisOptions":
        return self._Cast_MBDRunUpAnalysisOptions(self)
