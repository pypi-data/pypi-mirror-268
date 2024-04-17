"""ResultLocationSelectionGroups"""

from __future__ import annotations

from typing import TypeVar, Any, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5859
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RESULT_LOCATION_SELECTION_GROUPS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results",
    "ResultLocationSelectionGroups",
)


__docformat__ = "restructuredtext en"
__all__ = ("ResultLocationSelectionGroups",)


Self = TypeVar("Self", bound="ResultLocationSelectionGroups")


class ResultLocationSelectionGroups(_0.APIBase):
    """ResultLocationSelectionGroups

    This is a mastapy class.
    """

    TYPE = _RESULT_LOCATION_SELECTION_GROUPS

    class DisplayLocationSelectionOption(Enum):
        """DisplayLocationSelectionOption is a nested enum."""

        @classmethod
        def type_(cls):
            return _RESULT_LOCATION_SELECTION_GROUPS.DisplayLocationSelectionOption

        CURRENT_ITEM = 0
        GROUPS = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    DisplayLocationSelectionOption.__setattr__ = __enum_setattr
    DisplayLocationSelectionOption.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ResultLocationSelectionGroups")

    class _Cast_ResultLocationSelectionGroups:
        """Special nested class for casting ResultLocationSelectionGroups to subclasses."""

        def __init__(
            self: "ResultLocationSelectionGroups._Cast_ResultLocationSelectionGroups",
            parent: "ResultLocationSelectionGroups",
        ):
            self._parent = parent

        @property
        def result_location_selection_groups(
            self: "ResultLocationSelectionGroups._Cast_ResultLocationSelectionGroups",
        ) -> "ResultLocationSelectionGroups":
            return self._parent

        def __getattr__(
            self: "ResultLocationSelectionGroups._Cast_ResultLocationSelectionGroups",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ResultLocationSelectionGroups.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def display_location_selection(
        self: Self,
    ) -> "ResultLocationSelectionGroups.DisplayLocationSelectionOption":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultLocationSelectionGroups.DisplayLocationSelectionOption"""
        temp = self.wrapped.DisplayLocationSelection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ResultLocationSelectionGroups+DisplayLocationSelectionOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultLocationSelectionGroups.ResultLocationSelectionGroups",
            "DisplayLocationSelectionOption",
        )(value)

    @display_location_selection.setter
    @enforce_parameter_types
    def display_location_selection(
        self: Self,
        value: "ResultLocationSelectionGroups.DisplayLocationSelectionOption",
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Results.ResultLocationSelectionGroups+DisplayLocationSelectionOption",
        )
        self.wrapped.DisplayLocationSelection = value

    @property
    def select_result_location_group(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ResultLocationSelectionGroup":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultLocationSelectionGroup]"""
        temp = self.wrapped.SelectResultLocationGroup

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ResultLocationSelectionGroup",
        )(temp)

    @select_result_location_group.setter
    @enforce_parameter_types
    def select_result_location_group(
        self: Self, value: "_5859.ResultLocationSelectionGroup"
    ):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ResultLocationSelectionGroup.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ResultLocationSelectionGroup.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SelectResultLocationGroup = value

    @property
    def selected_result_location_group(
        self: Self,
    ) -> "_5859.ResultLocationSelectionGroup":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultLocationSelectionGroup

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedResultLocationGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def result_location_groups(
        self: Self,
    ) -> "List[_5859.ResultLocationSelectionGroup]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.results.ResultLocationSelectionGroup]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultLocationGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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

    def add_new_group(self: Self):
        """Method does not return."""
        self.wrapped.AddNewGroup()

    def remove_groups(self: Self):
        """Method does not return."""
        self.wrapped.RemoveGroups()

    def view_groups(self: Self):
        """Method does not return."""
        self.wrapped.ViewGroups()

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
    ) -> "ResultLocationSelectionGroups._Cast_ResultLocationSelectionGroups":
        return self._Cast_ResultLocationSelectionGroups(self)
