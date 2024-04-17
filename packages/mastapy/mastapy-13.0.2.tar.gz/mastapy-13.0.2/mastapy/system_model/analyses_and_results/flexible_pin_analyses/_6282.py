"""FlexiblePinAnalysisOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.load_case_groups import _5672
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.FlexiblePinAnalyses",
    "FlexiblePinAnalysisOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAnalysisOptions",)


Self = TypeVar("Self", bound="FlexiblePinAnalysisOptions")


class FlexiblePinAnalysisOptions(_0.APIBase):
    """FlexiblePinAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlexiblePinAnalysisOptions")

    class _Cast_FlexiblePinAnalysisOptions:
        """Special nested class for casting FlexiblePinAnalysisOptions to subclasses."""

        def __init__(
            self: "FlexiblePinAnalysisOptions._Cast_FlexiblePinAnalysisOptions",
            parent: "FlexiblePinAnalysisOptions",
        ):
            self._parent = parent

        @property
        def flexible_pin_analysis_options(
            self: "FlexiblePinAnalysisOptions._Cast_FlexiblePinAnalysisOptions",
        ) -> "FlexiblePinAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAnalysisOptions._Cast_FlexiblePinAnalysisOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlexiblePinAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extreme_load_case(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = self.wrapped.ExtremeLoadCase

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @extreme_load_case.setter
    @enforce_parameter_types
    def extreme_load_case(self: Self, value: "_6813.StaticLoadCase"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ExtremeLoadCase = value

    @property
    def extreme_load_case_for_stop_start(self: Self) -> "_6813.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase"""
        temp = self.wrapped.ExtremeLoadCaseForStopStart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @extreme_load_case_for_stop_start.setter
    @enforce_parameter_types
    def extreme_load_case_for_stop_start(self: Self, value: "_6813.StaticLoadCase"):
        self.wrapped.ExtremeLoadCaseForStopStart = value.wrapped

    @property
    def include_flexible_bearing_races(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeFlexibleBearingRaces

        if temp is None:
            return False

        return temp

    @include_flexible_bearing_races.setter
    @enforce_parameter_types
    def include_flexible_bearing_races(self: Self, value: "bool"):
        self.wrapped.IncludeFlexibleBearingRaces = (
            bool(value) if value is not None else False
        )

    @property
    def ldd(self: Self) -> "list_with_selected_item.ListWithSelectedItem_DutyCycle":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle]"""
        temp = self.wrapped.LDD

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_DutyCycle",
        )(temp)

    @ldd.setter
    @enforce_parameter_types
    def ldd(self: Self, value: "_5672.DutyCycle"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_DutyCycle.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_DutyCycle.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.LDD = value

    @property
    def nominal_load_case(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = self.wrapped.NominalLoadCase

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @nominal_load_case.setter
    @enforce_parameter_types
    def nominal_load_case(self: Self, value: "_6813.StaticLoadCase"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.NominalLoadCase = value

    @property
    def nominal_load_case_for_stop_start(self: Self) -> "_6813.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase"""
        temp = self.wrapped.NominalLoadCaseForStopStart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @nominal_load_case_for_stop_start.setter
    @enforce_parameter_types
    def nominal_load_case_for_stop_start(self: Self, value: "_6813.StaticLoadCase"):
        self.wrapped.NominalLoadCaseForStopStart = value.wrapped

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAnalysisOptions._Cast_FlexiblePinAnalysisOptions":
        return self._Cast_FlexiblePinAnalysisOptions(self)
