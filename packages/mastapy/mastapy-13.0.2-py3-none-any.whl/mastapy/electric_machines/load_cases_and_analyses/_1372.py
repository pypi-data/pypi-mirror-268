"""LoadCaseTypeSelector"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.electric_machines.load_cases_and_analyses import _1371
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_CASE_TYPE_SELECTOR = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "LoadCaseTypeSelector"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadCaseTypeSelector",)


Self = TypeVar("Self", bound="LoadCaseTypeSelector")


class LoadCaseTypeSelector(_0.APIBase):
    """LoadCaseTypeSelector

    This is a mastapy class.
    """

    TYPE = _LOAD_CASE_TYPE_SELECTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadCaseTypeSelector")

    class _Cast_LoadCaseTypeSelector:
        """Special nested class for casting LoadCaseTypeSelector to subclasses."""

        def __init__(
            self: "LoadCaseTypeSelector._Cast_LoadCaseTypeSelector",
            parent: "LoadCaseTypeSelector",
        ):
            self._parent = parent

        @property
        def load_case_type_selector(
            self: "LoadCaseTypeSelector._Cast_LoadCaseTypeSelector",
        ) -> "LoadCaseTypeSelector":
            return self._parent

        def __getattr__(
            self: "LoadCaseTypeSelector._Cast_LoadCaseTypeSelector", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadCaseTypeSelector.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_case_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LoadCaseType":
        """EnumWithSelectedValue[mastapy.electric_machines.load_cases_and_analyses.LoadCaseType]"""
        temp = self.wrapped.LoadCaseType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LoadCaseType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @load_case_type.setter
    @enforce_parameter_types
    def load_case_type(self: Self, value: "_1371.LoadCaseType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LoadCaseType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LoadCaseType = value

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
    def cast_to(self: Self) -> "LoadCaseTypeSelector._Cast_LoadCaseTypeSelector":
        return self._Cast_LoadCaseTypeSelector(self)
