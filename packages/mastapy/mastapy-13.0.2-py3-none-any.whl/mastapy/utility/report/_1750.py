"""AxisSettings"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIS_SETTINGS = python_net_import("SMT.MastaAPI.Utility.Report", "AxisSettings")


__docformat__ = "restructuredtext en"
__all__ = ("AxisSettings",)


Self = TypeVar("Self", bound="AxisSettings")


class AxisSettings(_0.APIBase):
    """AxisSettings

    This is a mastapy class.
    """

    TYPE = _AXIS_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AxisSettings")

    class _Cast_AxisSettings:
        """Special nested class for casting AxisSettings to subclasses."""

        def __init__(self: "AxisSettings._Cast_AxisSettings", parent: "AxisSettings"):
            self._parent = parent

        @property
        def axis_settings(self: "AxisSettings._Cast_AxisSettings") -> "AxisSettings":
            return self._parent

        def __getattr__(self: "AxisSettings._Cast_AxisSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AxisSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def end_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EndValue

        if temp is None:
            return 0.0

        return temp

    @end_value.setter
    @enforce_parameter_types
    def end_value(self: Self, value: "float"):
        self.wrapped.EndValue = float(value) if value is not None else 0.0

    @property
    def hide_grid_lines(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HideGridLines

        if temp is None:
            return False

        return temp

    @hide_grid_lines.setter
    @enforce_parameter_types
    def hide_grid_lines(self: Self, value: "bool"):
        self.wrapped.HideGridLines = bool(value) if value is not None else False

    @property
    def show_title(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowTitle

        if temp is None:
            return False

        return temp

    @show_title.setter
    @enforce_parameter_types
    def show_title(self: Self, value: "bool"):
        self.wrapped.ShowTitle = bool(value) if value is not None else False

    @property
    def specify_range(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyRange

        if temp is None:
            return False

        return temp

    @specify_range.setter
    @enforce_parameter_types
    def specify_range(self: Self, value: "bool"):
        self.wrapped.SpecifyRange = bool(value) if value is not None else False

    @property
    def start_value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartValue

        if temp is None:
            return 0.0

        return temp

    @start_value.setter
    @enforce_parameter_types
    def start_value(self: Self, value: "float"):
        self.wrapped.StartValue = float(value) if value is not None else 0.0

    @property
    def title(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Title

        if temp is None:
            return ""

        return temp

    @property
    def unit(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Unit

        if temp is None:
            return ""

        return temp

    @property
    def custom_labels(self: Self) -> "List[str]":
        """List[str]"""
        temp = self.wrapped.CustomLabels

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @custom_labels.setter
    @enforce_parameter_types
    def custom_labels(self: Self, value: "List[str]"):
        value = conversion.mp_to_pn_objects_in_list(value)
        self.wrapped.CustomLabels = value

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
    def cast_to(self: Self) -> "AxisSettings._Cast_AxisSettings":
        return self._Cast_AxisSettings(self)
