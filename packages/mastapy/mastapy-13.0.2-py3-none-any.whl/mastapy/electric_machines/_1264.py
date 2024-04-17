"""CoreLossCoefficients"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CORE_LOSS_COEFFICIENTS = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CoreLossCoefficients"
)


__docformat__ = "restructuredtext en"
__all__ = ("CoreLossCoefficients",)


Self = TypeVar("Self", bound="CoreLossCoefficients")


class CoreLossCoefficients(_0.APIBase):
    """CoreLossCoefficients

    This is a mastapy class.
    """

    TYPE = _CORE_LOSS_COEFFICIENTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoreLossCoefficients")

    class _Cast_CoreLossCoefficients:
        """Special nested class for casting CoreLossCoefficients to subclasses."""

        def __init__(
            self: "CoreLossCoefficients._Cast_CoreLossCoefficients",
            parent: "CoreLossCoefficients",
        ):
            self._parent = parent

        @property
        def core_loss_coefficients(
            self: "CoreLossCoefficients._Cast_CoreLossCoefficients",
        ) -> "CoreLossCoefficients":
            return self._parent

        def __getattr__(
            self: "CoreLossCoefficients._Cast_CoreLossCoefficients", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoreLossCoefficients.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def c_coefficient_eddy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CCoefficientEddy

        if temp is None:
            return 0.0

        return temp

    @c_coefficient_eddy.setter
    @enforce_parameter_types
    def c_coefficient_eddy(self: Self, value: "float"):
        self.wrapped.CCoefficientEddy = float(value) if value is not None else 0.0

    @property
    def c_coefficient_excess(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CCoefficientExcess

        if temp is None:
            return 0.0

        return temp

    @c_coefficient_excess.setter
    @enforce_parameter_types
    def c_coefficient_excess(self: Self, value: "float"):
        self.wrapped.CCoefficientExcess = float(value) if value is not None else 0.0

    @property
    def c_coefficient_hysteresis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CCoefficientHysteresis

        if temp is None:
            return 0.0

        return temp

    @c_coefficient_hysteresis.setter
    @enforce_parameter_types
    def c_coefficient_hysteresis(self: Self, value: "float"):
        self.wrapped.CCoefficientHysteresis = float(value) if value is not None else 0.0

    @property
    def field_exponent_eddy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FieldExponentEddy

        if temp is None:
            return 0.0

        return temp

    @field_exponent_eddy.setter
    @enforce_parameter_types
    def field_exponent_eddy(self: Self, value: "float"):
        self.wrapped.FieldExponentEddy = float(value) if value is not None else 0.0

    @property
    def field_exponent_excess(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FieldExponentExcess

        if temp is None:
            return 0.0

        return temp

    @field_exponent_excess.setter
    @enforce_parameter_types
    def field_exponent_excess(self: Self, value: "float"):
        self.wrapped.FieldExponentExcess = float(value) if value is not None else 0.0

    @property
    def field_exponent_hysteresis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FieldExponentHysteresis

        if temp is None:
            return 0.0

        return temp

    @field_exponent_hysteresis.setter
    @enforce_parameter_types
    def field_exponent_hysteresis(self: Self, value: "float"):
        self.wrapped.FieldExponentHysteresis = (
            float(value) if value is not None else 0.0
        )

    @property
    def frequency_exponent_eddy(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FrequencyExponentEddy

        if temp is None:
            return 0.0

        return temp

    @frequency_exponent_eddy.setter
    @enforce_parameter_types
    def frequency_exponent_eddy(self: Self, value: "float"):
        self.wrapped.FrequencyExponentEddy = float(value) if value is not None else 0.0

    @property
    def frequency_exponent_excess(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FrequencyExponentExcess

        if temp is None:
            return 0.0

        return temp

    @frequency_exponent_excess.setter
    @enforce_parameter_types
    def frequency_exponent_excess(self: Self, value: "float"):
        self.wrapped.FrequencyExponentExcess = (
            float(value) if value is not None else 0.0
        )

    @property
    def frequency_exponent_hysteresis(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FrequencyExponentHysteresis

        if temp is None:
            return 0.0

        return temp

    @frequency_exponent_hysteresis.setter
    @enforce_parameter_types
    def frequency_exponent_hysteresis(self: Self, value: "float"):
        self.wrapped.FrequencyExponentHysteresis = (
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
    def cast_to(self: Self) -> "CoreLossCoefficients._Cast_CoreLossCoefficients":
        return self._Cast_CoreLossCoefficients(self)
