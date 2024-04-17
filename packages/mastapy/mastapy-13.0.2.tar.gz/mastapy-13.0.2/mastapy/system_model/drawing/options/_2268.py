"""AdvancedTimeSteppingAnalysisForModulationModeViewOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model.gears import _2539
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_MODE_VIEW_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing.Options",
    "AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7019,
        _7020,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AdvancedTimeSteppingAnalysisForModulationModeViewOptions",)


Self = TypeVar("Self", bound="AdvancedTimeSteppingAnalysisForModulationModeViewOptions")


class AdvancedTimeSteppingAnalysisForModulationModeViewOptions(_0.APIBase):
    """AdvancedTimeSteppingAnalysisForModulationModeViewOptions

    This is a mastapy class.
    """

    TYPE = _ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_MODE_VIEW_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
    )

    class _Cast_AdvancedTimeSteppingAnalysisForModulationModeViewOptions:
        """Special nested class for casting AdvancedTimeSteppingAnalysisForModulationModeViewOptions to subclasses."""

        def __init__(
            self: "AdvancedTimeSteppingAnalysisForModulationModeViewOptions._Cast_AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
            parent: "AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
        ):
            self._parent = parent

        @property
        def advanced_time_stepping_analysis_for_modulation_mode_view_options(
            self: "AdvancedTimeSteppingAnalysisForModulationModeViewOptions._Cast_AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
        ) -> "AdvancedTimeSteppingAnalysisForModulationModeViewOptions":
            return self._parent

        def __getattr__(
            self: "AdvancedTimeSteppingAnalysisForModulationModeViewOptions._Cast_AdvancedTimeSteppingAnalysisForModulationModeViewOptions",
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
        self: Self,
        instance_to_wrap: "AdvancedTimeSteppingAnalysisForModulationModeViewOptions.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitations_type(self: Self) -> "_7019.AtsamExcitationsOrOthers":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AtsamExcitationsOrOthers"""
        temp = self.wrapped.ExcitationsType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.AtsamExcitationsOrOthers",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation._7019",
            "AtsamExcitationsOrOthers",
        )(value)

    @excitations_type.setter
    @enforce_parameter_types
    def excitations_type(self: Self, value: "_7019.AtsamExcitationsOrOthers"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.AtsamExcitationsOrOthers",
        )
        self.wrapped.ExcitationsType = value

    @property
    def gear_set(self: Self) -> "list_with_selected_item.ListWithSelectedItem_GearSet":
        """ListWithSelectedItem[mastapy.system_model.part_model.gears.GearSet]"""
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_GearSet",
        )(temp)

    @gear_set.setter
    @enforce_parameter_types
    def gear_set(self: Self, value: "_2539.GearSet"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_GearSet.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_GearSet.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.GearSet = value

    @property
    def large_time_step(self: Self) -> "int":
        """int"""
        temp = self.wrapped.LargeTimeStep

        if temp is None:
            return 0

        return temp

    @large_time_step.setter
    @enforce_parameter_types
    def large_time_step(self: Self, value: "int"):
        self.wrapped.LargeTimeStep = int(value) if value is not None else 0

    @property
    def mode_view_options(self: Self) -> "_7020.AtsamNaturalFrequencyViewOption":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AtsamNaturalFrequencyViewOption"""
        temp = self.wrapped.ModeViewOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.AtsamNaturalFrequencyViewOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation._7020",
            "AtsamNaturalFrequencyViewOption",
        )(value)

    @mode_view_options.setter
    @enforce_parameter_types
    def mode_view_options(self: Self, value: "_7020.AtsamNaturalFrequencyViewOption"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.AtsamNaturalFrequencyViewOption",
        )
        self.wrapped.ModeViewOptions = value

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "AdvancedTimeSteppingAnalysisForModulationModeViewOptions._Cast_AdvancedTimeSteppingAnalysisForModulationModeViewOptions":
        return self._Cast_AdvancedTimeSteppingAnalysisForModulationModeViewOptions(self)
