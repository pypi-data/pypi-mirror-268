"""ParetoOptimisationStrategyChartInformation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, List
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISATION_STRATEGY_CHART_INFORMATION = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation",
    "ParetoOptimisationStrategyChartInformation",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1557


__docformat__ = "restructuredtext en"
__all__ = ("ParetoOptimisationStrategyChartInformation",)


Self = TypeVar("Self", bound="ParetoOptimisationStrategyChartInformation")


class ParetoOptimisationStrategyChartInformation(_0.APIBase):
    """ParetoOptimisationStrategyChartInformation

    This is a mastapy class.
    """

    TYPE = _PARETO_OPTIMISATION_STRATEGY_CHART_INFORMATION

    class ScatterOrBarChart(Enum):
        """ScatterOrBarChart is a nested enum."""

        @classmethod
        def type_(cls):
            return _PARETO_OPTIMISATION_STRATEGY_CHART_INFORMATION.ScatterOrBarChart

        SCATTER_CHART = 0
        BAR_AND_LINE_CHART = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    ScatterOrBarChart.__setattr__ = __enum_setattr
    ScatterOrBarChart.__delattr__ = __enum_delattr
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ParetoOptimisationStrategyChartInformation"
    )

    class _Cast_ParetoOptimisationStrategyChartInformation:
        """Special nested class for casting ParetoOptimisationStrategyChartInformation to subclasses."""

        def __init__(
            self: "ParetoOptimisationStrategyChartInformation._Cast_ParetoOptimisationStrategyChartInformation",
            parent: "ParetoOptimisationStrategyChartInformation",
        ):
            self._parent = parent

        @property
        def pareto_optimisation_strategy_chart_information(
            self: "ParetoOptimisationStrategyChartInformation._Cast_ParetoOptimisationStrategyChartInformation",
        ) -> "ParetoOptimisationStrategyChartInformation":
            return self._parent

        def __getattr__(
            self: "ParetoOptimisationStrategyChartInformation._Cast_ParetoOptimisationStrategyChartInformation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ParetoOptimisationStrategyChartInformation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chart_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ChartName

        if temp is None:
            return ""

        return temp

    @chart_name.setter
    @enforce_parameter_types
    def chart_name(self: Self, value: "str"):
        self.wrapped.ChartName = str(value) if value is not None else ""

    @property
    def select_chart_type(
        self: Self,
    ) -> "ParetoOptimisationStrategyChartInformation.ScatterOrBarChart":
        """mastapy.math_utility.optimisation.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart"""
        temp = self.wrapped.SelectChartType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.MathUtility.Optimisation.ParetoOptimisationStrategyChartInformation+ScatterOrBarChart",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility.optimisation.ParetoOptimisationStrategyChartInformation.ParetoOptimisationStrategyChartInformation",
            "ScatterOrBarChart",
        )(value)

    @select_chart_type.setter
    @enforce_parameter_types
    def select_chart_type(
        self: Self,
        value: "ParetoOptimisationStrategyChartInformation.ScatterOrBarChart",
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.MathUtility.Optimisation.ParetoOptimisationStrategyChartInformation+ScatterOrBarChart",
        )
        self.wrapped.SelectChartType = value

    @property
    def bars(self: Self) -> "List[_1557.ParetoOptimisationStrategyBars]":
        """List[mastapy.math_utility.optimisation.ParetoOptimisationStrategyBars]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Bars

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

    def add_bar(self: Self):
        """Method does not return."""
        self.wrapped.AddBar()

    def remove_chart(self: Self):
        """Method does not return."""
        self.wrapped.RemoveChart()

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
    ) -> "ParetoOptimisationStrategyChartInformation._Cast_ParetoOptimisationStrategyChartInformation":
        return self._Cast_ParetoOptimisationStrategyChartInformation(self)
