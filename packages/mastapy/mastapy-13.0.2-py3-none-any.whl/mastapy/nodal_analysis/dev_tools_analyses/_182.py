"""EigenvalueOptions"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.nodal_analysis import _78
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EIGENVALUE_OPTIONS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "EigenvalueOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("EigenvalueOptions",)


Self = TypeVar("Self", bound="EigenvalueOptions")


class EigenvalueOptions(_0.APIBase):
    """EigenvalueOptions

    This is a mastapy class.
    """

    TYPE = _EIGENVALUE_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EigenvalueOptions")

    class _Cast_EigenvalueOptions:
        """Special nested class for casting EigenvalueOptions to subclasses."""

        def __init__(
            self: "EigenvalueOptions._Cast_EigenvalueOptions",
            parent: "EigenvalueOptions",
        ):
            self._parent = parent

        @property
        def eigenvalue_options(
            self: "EigenvalueOptions._Cast_EigenvalueOptions",
        ) -> "EigenvalueOptions":
            return self._parent

        def __getattr__(self: "EigenvalueOptions._Cast_EigenvalueOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EigenvalueOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_mode_frequency(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MaximumModeFrequency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @maximum_mode_frequency.setter
    @enforce_parameter_types
    def maximum_mode_frequency(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MaximumModeFrequency = value

    @property
    def minimum_mode_frequency(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumModeFrequency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_mode_frequency.setter
    @enforce_parameter_types
    def minimum_mode_frequency(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumModeFrequency = value

    @property
    def mode_frequency_shift(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModeFrequencyShift

        if temp is None:
            return 0.0

        return temp

    @mode_frequency_shift.setter
    @enforce_parameter_types
    def mode_frequency_shift(self: Self, value: "float"):
        self.wrapped.ModeFrequencyShift = float(value) if value is not None else 0.0

    @property
    def mode_input_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ModeInputType":
        """EnumWithSelectedValue[mastapy.nodal_analysis.ModeInputType]"""
        temp = self.wrapped.ModeInputMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ModeInputType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @mode_input_method.setter
    @enforce_parameter_types
    def mode_input_method(self: Self, value: "_78.ModeInputType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ModeInputType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ModeInputMethod = value

    @property
    def number_of_modes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfModes

        if temp is None:
            return 0

        return temp

    @number_of_modes.setter
    @enforce_parameter_types
    def number_of_modes(self: Self, value: "int"):
        self.wrapped.NumberOfModes = int(value) if value is not None else 0

    @property
    def overall_amls_cutoff_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OverallAMLSCutoffFactor

        if temp is None:
            return 0.0

        return temp

    @overall_amls_cutoff_factor.setter
    @enforce_parameter_types
    def overall_amls_cutoff_factor(self: Self, value: "float"):
        self.wrapped.OverallAMLSCutoffFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def reduced_amls_cutoff_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReducedAMLSCutoffFactor

        if temp is None:
            return 0.0

        return temp

    @reduced_amls_cutoff_factor.setter
    @enforce_parameter_types
    def reduced_amls_cutoff_factor(self: Self, value: "float"):
        self.wrapped.ReducedAMLSCutoffFactor = (
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
    def cast_to(self: Self) -> "EigenvalueOptions._Cast_EigenvalueOptions":
        return self._Cast_EigenvalueOptions(self)
