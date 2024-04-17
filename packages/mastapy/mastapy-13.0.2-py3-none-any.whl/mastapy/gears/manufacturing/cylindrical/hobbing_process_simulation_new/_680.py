"""HobResharpeningError"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOB_RESHARPENING_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobResharpeningError",
)


__docformat__ = "restructuredtext en"
__all__ = ("HobResharpeningError",)


Self = TypeVar("Self", bound="HobResharpeningError")


class HobResharpeningError(_0.APIBase):
    """HobResharpeningError

    This is a mastapy class.
    """

    TYPE = _HOB_RESHARPENING_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobResharpeningError")

    class _Cast_HobResharpeningError:
        """Special nested class for casting HobResharpeningError to subclasses."""

        def __init__(
            self: "HobResharpeningError._Cast_HobResharpeningError",
            parent: "HobResharpeningError",
        ):
            self._parent = parent

        @property
        def hob_resharpening_error(
            self: "HobResharpeningError._Cast_HobResharpeningError",
        ) -> "HobResharpeningError":
            return self._parent

        def __getattr__(
            self: "HobResharpeningError._Cast_HobResharpeningError", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobResharpeningError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gash_lead_error_reading(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GashLeadErrorReading

        if temp is None:
            return 0.0

        return temp

    @gash_lead_error_reading.setter
    @enforce_parameter_types
    def gash_lead_error_reading(self: Self, value: "float"):
        self.wrapped.GashLeadErrorReading = float(value) if value is not None else 0.0

    @property
    def gash_lead_measurement_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GashLeadMeasurementLength

        if temp is None:
            return 0.0

        return temp

    @gash_lead_measurement_length.setter
    @enforce_parameter_types
    def gash_lead_measurement_length(self: Self, value: "float"):
        self.wrapped.GashLeadMeasurementLength = (
            float(value) if value is not None else 0.0
        )

    @property
    def radial_alignment_error_reading(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialAlignmentErrorReading

        if temp is None:
            return 0.0

        return temp

    @radial_alignment_error_reading.setter
    @enforce_parameter_types
    def radial_alignment_error_reading(self: Self, value: "float"):
        self.wrapped.RadialAlignmentErrorReading = (
            float(value) if value is not None else 0.0
        )

    @property
    def radial_alignment_measurement_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialAlignmentMeasurementLength

        if temp is None:
            return 0.0

        return temp

    @radial_alignment_measurement_length.setter
    @enforce_parameter_types
    def radial_alignment_measurement_length(self: Self, value: "float"):
        self.wrapped.RadialAlignmentMeasurementLength = (
            float(value) if value is not None else 0.0
        )

    @property
    def total_gash_indexing_variation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TotalGashIndexingVariation

        if temp is None:
            return 0.0

        return temp

    @total_gash_indexing_variation.setter
    @enforce_parameter_types
    def total_gash_indexing_variation(self: Self, value: "float"):
        self.wrapped.TotalGashIndexingVariation = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_sin_curve_for_gash_index_variation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSinCurveForGashIndexVariation

        if temp is None:
            return False

        return temp

    @use_sin_curve_for_gash_index_variation.setter
    @enforce_parameter_types
    def use_sin_curve_for_gash_index_variation(self: Self, value: "bool"):
        self.wrapped.UseSinCurveForGashIndexVariation = (
            bool(value) if value is not None else False
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
    def cast_to(self: Self) -> "HobResharpeningError._Cast_HobResharpeningError":
        return self._Cast_HobResharpeningError(self)
