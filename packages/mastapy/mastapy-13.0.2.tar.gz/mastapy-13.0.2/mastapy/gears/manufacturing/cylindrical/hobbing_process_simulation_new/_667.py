"""CutterHeadSlideError"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUTTER_HEAD_SLIDE_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "CutterHeadSlideError",
)


__docformat__ = "restructuredtext en"
__all__ = ("CutterHeadSlideError",)


Self = TypeVar("Self", bound="CutterHeadSlideError")


class CutterHeadSlideError(_0.APIBase):
    """CutterHeadSlideError

    This is a mastapy class.
    """

    TYPE = _CUTTER_HEAD_SLIDE_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CutterHeadSlideError")

    class _Cast_CutterHeadSlideError:
        """Special nested class for casting CutterHeadSlideError to subclasses."""

        def __init__(
            self: "CutterHeadSlideError._Cast_CutterHeadSlideError",
            parent: "CutterHeadSlideError",
        ):
            self._parent = parent

        @property
        def cutter_head_slide_error(
            self: "CutterHeadSlideError._Cast_CutterHeadSlideError",
        ) -> "CutterHeadSlideError":
            return self._parent

        def __getattr__(
            self: "CutterHeadSlideError._Cast_CutterHeadSlideError", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CutterHeadSlideError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_plane_measurement_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.XPlaneMeasurementLength

        if temp is None:
            return 0.0

        return temp

    @x_plane_measurement_length.setter
    @enforce_parameter_types
    def x_plane_measurement_length(self: Self, value: "float"):
        self.wrapped.XPlaneMeasurementLength = (
            float(value) if value is not None else 0.0
        )

    @property
    def x_plane_measurement_reading(self: Self) -> "float":
        """float"""
        temp = self.wrapped.XPlaneMeasurementReading

        if temp is None:
            return 0.0

        return temp

    @x_plane_measurement_reading.setter
    @enforce_parameter_types
    def x_plane_measurement_reading(self: Self, value: "float"):
        self.wrapped.XPlaneMeasurementReading = (
            float(value) if value is not None else 0.0
        )

    @property
    def y_plane_measurement_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.YPlaneMeasurementLength

        if temp is None:
            return 0.0

        return temp

    @y_plane_measurement_length.setter
    @enforce_parameter_types
    def y_plane_measurement_length(self: Self, value: "float"):
        self.wrapped.YPlaneMeasurementLength = (
            float(value) if value is not None else 0.0
        )

    @property
    def y_plane_measurement_reading(self: Self) -> "float":
        """float"""
        temp = self.wrapped.YPlaneMeasurementReading

        if temp is None:
            return 0.0

        return temp

    @y_plane_measurement_reading.setter
    @enforce_parameter_types
    def y_plane_measurement_reading(self: Self, value: "float"):
        self.wrapped.YPlaneMeasurementReading = (
            float(value) if value is not None else 0.0
        )

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
    def cast_to(self: Self) -> "CutterHeadSlideError._Cast_CutterHeadSlideError":
        return self._Cast_CutterHeadSlideError(self)
