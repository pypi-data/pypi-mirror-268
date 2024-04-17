"""DynamicForcesOperatingPoint"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCES_OPERATING_POINT = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "DynamicForcesOperatingPoint"
)


__docformat__ = "restructuredtext en"
__all__ = ("DynamicForcesOperatingPoint",)


Self = TypeVar("Self", bound="DynamicForcesOperatingPoint")


class DynamicForcesOperatingPoint(_0.APIBase):
    """DynamicForcesOperatingPoint

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCES_OPERATING_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicForcesOperatingPoint")

    class _Cast_DynamicForcesOperatingPoint:
        """Special nested class for casting DynamicForcesOperatingPoint to subclasses."""

        def __init__(
            self: "DynamicForcesOperatingPoint._Cast_DynamicForcesOperatingPoint",
            parent: "DynamicForcesOperatingPoint",
        ):
            self._parent = parent

        @property
        def dynamic_forces_operating_point(
            self: "DynamicForcesOperatingPoint._Cast_DynamicForcesOperatingPoint",
        ) -> "DynamicForcesOperatingPoint":
            return self._parent

        def __getattr__(
            self: "DynamicForcesOperatingPoint._Cast_DynamicForcesOperatingPoint",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicForcesOperatingPoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CurrentAngle

        if temp is None:
            return 0.0

        return temp

    @current_angle.setter
    @enforce_parameter_types
    def current_angle(self: Self, value: "float"):
        self.wrapped.CurrentAngle = float(value) if value is not None else 0.0

    @property
    def peak_line_current(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PeakLineCurrent

        if temp is None:
            return 0.0

        return temp

    @peak_line_current.setter
    @enforce_parameter_types
    def peak_line_current(self: Self, value: "float"):
        self.wrapped.PeakLineCurrent = float(value) if value is not None else 0.0

    @property
    def rms_line_current(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RMSLineCurrent

        if temp is None:
            return 0.0

        return temp

    @rms_line_current.setter
    @enforce_parameter_types
    def rms_line_current(self: Self, value: "float"):
        self.wrapped.RMSLineCurrent = float(value) if value is not None else 0.0

    @property
    def speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @speed.setter
    @enforce_parameter_types
    def speed(self: Self, value: "float"):
        self.wrapped.Speed = float(value) if value is not None else 0.0

    @property
    def torque(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @torque.setter
    @enforce_parameter_types
    def torque(self: Self, value: "float"):
        self.wrapped.Torque = float(value) if value is not None else 0.0

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
    ) -> "DynamicForcesOperatingPoint._Cast_DynamicForcesOperatingPoint":
        return self._Cast_DynamicForcesOperatingPoint(self)
