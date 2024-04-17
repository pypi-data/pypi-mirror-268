"""ParetoOptimisationVariableBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_VARIABLE_BASE = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "ParetoOptimisationVariableBase"
)

if TYPE_CHECKING:
    from mastapy.utility import _1595
    from mastapy.math_utility import _1496
    from mastapy.math_utility.optimisation import _1565, _1564, _1554, _1555, _1560
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4392


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationVariableBase",)


Self = TypeVar("Self", bound="ParetoOptimisationVariableBase")


class ParetoOptimisationVariableBase(_0.APIBase):
    """ParetoOptimisationVariableBase

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_VARIABLE_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParetoOptimisationVariableBase")

    class _Cast_ParetoOptimisationVariableBase:
        """Special nested class for casting ParetoOptimisationVariableBase to subclasses."""

        def __init__(
            self: "ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase",
            parent: "ParetoOptimisationVariableBase",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_input(
            self: "ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase",
        ) -> "_1554.ParetoOptimisationInput":
            from mastapy.math_utility.optimisation import _1554

            return self._parent._cast(_1554.ParetoOptimisationInput)

        @property
        def pareto_optimisation_output(
            self: "ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase",
        ) -> "_1555.ParetoOptimisationOutput":
            from mastapy.math_utility.optimisation import _1555

            return self._parent._cast(_1555.ParetoOptimisationOutput)

        @property
        def pareto_optimisation_variable(
            self: "ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase",
        ) -> "_1560.ParetoOptimisationVariable":
            from mastapy.math_utility.optimisation import _1560

            return self._parent._cast(_1560.ParetoOptimisationVariable)

        @property
        def parametric_study_doe_result_variable(
            self: "ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase",
        ) -> "_4392.ParametricStudyDOEResultVariable":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4392,
            )

            return self._parent._cast(_4392.ParametricStudyDOEResultVariable)

        @property
        def pareto_optimisation_variable_base(
            self: "ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase",
        ) -> "ParetoOptimisationVariableBase":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParetoOptimisationVariableBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def percent(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Percent

        if temp is None:
            return 0.0

        return temp

    @percent.setter
    @enforce_parameter_types
    def percent(self: Self, value: "float"):
        self.wrapped.Percent = float(value) if value is not None else 0.0

    @property
    def integer_range(self: Self) -> "_1595.IntegerRange":
        """mastapy.utility.IntegerRange"""
        temp = self.wrapped.IntegerRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @integer_range.setter
    @enforce_parameter_types
    def integer_range(self: Self, value: "_1595.IntegerRange"):
        self.wrapped.IntegerRange = value.wrapped

    @property
    def property_(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Property

        if temp is None:
            return ""

        return temp

    @property
    def range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range"""
        temp = self.wrapped.Range

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @range.setter
    @enforce_parameter_types
    def range(self: Self, value: "_1496.Range"):
        self.wrapped.Range = value.wrapped

    @property
    def specification_type(self: Self) -> "_1565.TargetingPropertyTo":
        """mastapy.math_utility.optimisation.TargetingPropertyTo"""
        temp = self.wrapped.SpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.Optimisation.TargetingPropertyTo"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility.optimisation._1565", "TargetingPropertyTo"
        )(value)

    @specification_type.setter
    @enforce_parameter_types
    def specification_type(self: Self, value: "_1565.TargetingPropertyTo"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.Optimisation.TargetingPropertyTo"
        )
        self.wrapped.SpecificationType = value

    @property
    def specify_input_range_as(self: Self) -> "_1564.SpecifyOptimisationInputAs":
        """mastapy.math_utility.optimisation.SpecifyOptimisationInputAs"""
        temp = self.wrapped.SpecifyInputRangeAs

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.Optimisation.SpecifyOptimisationInputAs"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility.optimisation._1564", "SpecifyOptimisationInputAs"
        )(value)

    @specify_input_range_as.setter
    @enforce_parameter_types
    def specify_input_range_as(self: Self, value: "_1564.SpecifyOptimisationInputAs"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.Optimisation.SpecifyOptimisationInputAs"
        )
        self.wrapped.SpecifyInputRangeAs = value

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
    def value(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @value.setter
    @enforce_parameter_types
    def value(self: Self, value: "float"):
        self.wrapped.Value = float(value) if value is not None else 0.0

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

    def delete(self: Self):
        """Method does not return."""
        self.wrapped.Delete()

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
    ) -> "ParetoOptimisationVariableBase._Cast_ParetoOptimisationVariableBase":
        return self._Cast_ParetoOptimisationVariableBase(self)
