"""LoadCaseGroupHistograms"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _2479
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_CASE_GROUP_HISTOGRAMS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "LoadCaseGroupHistograms",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874


__docformat__ = "restructuredtext en"
__all__ = ("LoadCaseGroupHistograms",)


Self = TypeVar("Self", bound="LoadCaseGroupHistograms")


class LoadCaseGroupHistograms(_0.APIBase):
    """LoadCaseGroupHistograms

    This is a mastapy class.
    """

    TYPE = _LOAD_CASE_GROUP_HISTOGRAMS

    class RevolutionsOrDuration(Enum):
        """RevolutionsOrDuration is a nested enum."""

        @classmethod
        def type_(cls):
            return _LOAD_CASE_GROUP_HISTOGRAMS.RevolutionsOrDuration

        REVOLUTIONS = 0
        DURATION = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    RevolutionsOrDuration.__setattr__ = __enum_setattr
    RevolutionsOrDuration.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadCaseGroupHistograms")

    class _Cast_LoadCaseGroupHistograms:
        """Special nested class for casting LoadCaseGroupHistograms to subclasses."""

        def __init__(
            self: "LoadCaseGroupHistograms._Cast_LoadCaseGroupHistograms",
            parent: "LoadCaseGroupHistograms",
        ):
            self._parent = parent

        @property
        def load_case_group_histograms(
            self: "LoadCaseGroupHistograms._Cast_LoadCaseGroupHistograms",
        ) -> "LoadCaseGroupHistograms":
            return self._parent

        def __getattr__(
            self: "LoadCaseGroupHistograms._Cast_LoadCaseGroupHistograms", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadCaseGroupHistograms.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def boost_pressure_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoostPressureChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_bins(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfBins

        if temp is None:
            return 0

        return temp

    @number_of_bins.setter
    @enforce_parameter_types
    def number_of_bins(self: Self, value: "int"):
        self.wrapped.NumberOfBins = int(value) if value is not None else 0

    @property
    def power_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_load(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_PowerLoad":
        """ListWithSelectedItem[mastapy.system_model.part_model.PowerLoad]"""
        temp = self.wrapped.PowerLoad

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_PowerLoad",
        )(temp)

    @power_load.setter
    @enforce_parameter_types
    def power_load(self: Self, value: "_2479.PowerLoad"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.PowerLoad = value

    @property
    def speed_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def torque_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def y_axis_variable(self: Self) -> "LoadCaseGroupHistograms.RevolutionsOrDuration":
        """mastapy.system_model.analyses_and_results.load_case_groups.LoadCaseGroupHistograms.RevolutionsOrDuration"""
        temp = self.wrapped.YAxisVariable

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.LoadCaseGroupHistograms+RevolutionsOrDuration",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.load_case_groups.LoadCaseGroupHistograms.LoadCaseGroupHistograms",
            "RevolutionsOrDuration",
        )(value)

    @y_axis_variable.setter
    @enforce_parameter_types
    def y_axis_variable(
        self: Self, value: "LoadCaseGroupHistograms.RevolutionsOrDuration"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.LoadCaseGroupHistograms+RevolutionsOrDuration",
        )
        self.wrapped.YAxisVariable = value

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

    def run_power_flow(self: Self):
        """Method does not return."""
        self.wrapped.RunPowerFlow()

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
    def cast_to(self: Self) -> "LoadCaseGroupHistograms._Cast_LoadCaseGroupHistograms":
        return self._Cast_LoadCaseGroupHistograms(self)
