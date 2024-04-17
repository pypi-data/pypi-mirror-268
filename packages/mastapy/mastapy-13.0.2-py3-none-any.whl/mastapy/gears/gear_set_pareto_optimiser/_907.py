"""ChartInfoBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CHART_INFO_BASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "ChartInfoBase"
)

if TYPE_CHECKING:
    from mastapy.utility.reporting_property_framework import _1796
    from mastapy.math_utility.optimisation import _1558
    from mastapy.gears.gear_set_pareto_optimiser import _909, _905, _917, _921, _936
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("ChartInfoBase",)


Self = TypeVar("Self", bound="ChartInfoBase")
TAnalysis = TypeVar("TAnalysis", bound="_1223.AbstractGearSetAnalysis")
TCandidate = TypeVar("TCandidate")


class ChartInfoBase(_0.APIBase, Generic[TAnalysis, TCandidate]):
    """ChartInfoBase

    This is a mastapy class.

    Generic Types:
        TAnalysis
        TCandidate
    """

    TYPE = _CHART_INFO_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ChartInfoBase")

    class _Cast_ChartInfoBase:
        """Special nested class for casting ChartInfoBase to subclasses."""

        def __init__(
            self: "ChartInfoBase._Cast_ChartInfoBase", parent: "ChartInfoBase"
        ):
            self._parent = parent

        @property
        def micro_geometry_design_space_search_chart_information(
            self: "ChartInfoBase._Cast_ChartInfoBase",
        ) -> "_921.MicroGeometryDesignSpaceSearchChartInformation":
            from mastapy.gears.gear_set_pareto_optimiser import _921

            return self._parent._cast(
                _921.MicroGeometryDesignSpaceSearchChartInformation
            )

        @property
        def pareto_optimiser_chart_information(
            self: "ChartInfoBase._Cast_ChartInfoBase",
        ) -> "_936.ParetoOptimiserChartInformation":
            from mastapy.gears.gear_set_pareto_optimiser import _936

            return self._parent._cast(_936.ParetoOptimiserChartInformation)

        @property
        def chart_info_base(
            self: "ChartInfoBase._Cast_ChartInfoBase",
        ) -> "ChartInfoBase":
            return self._parent

        def __getattr__(self: "ChartInfoBase._Cast_ChartInfoBase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ChartInfoBase.TYPE"):
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
    def chart_type(self: Self) -> "_1796.CustomChartType":
        """mastapy.utility.reporting_property_framework.CustomChartType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChartType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.ReportingPropertyFramework.CustomChartType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.reporting_property_framework._1796", "CustomChartType"
        )(value)

    @property
    def result_chart_bar_and_line(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultChartBarAndLine

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def result_chart_scatter(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultChartScatter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def select_chart_type(
        self: Self,
    ) -> "_1558.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart":
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
            "mastapy.math_utility.optimisation.ParetoOptimisationStrategyChartInformation._1558",
            "ParetoOptimisationStrategyChartInformation",
        )(value)

    @select_chart_type.setter
    @enforce_parameter_types
    def select_chart_type(
        self: Self,
        value: "_1558.ParetoOptimisationStrategyChartInformation.ScatterOrBarChart",
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.MathUtility.Optimisation.ParetoOptimisationStrategyChartInformation+ScatterOrBarChart",
        )
        self.wrapped.SelectChartType = value

    @property
    def selected_candidate_design(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedCandidateDesign

        if temp is None:
            return 0

        return temp

    @property
    def optimiser(self: Self) -> "_909.DesignSpaceSearchBase[TAnalysis, TCandidate]":
        """mastapy.gears.gear_set_pareto_optimiser.DesignSpaceSearchBase[TAnalysis, TCandidate]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Optimiser

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[TAnalysis, TCandidate](temp)

    @property
    def bars(self: Self) -> "List[_905.BarForPareto[TAnalysis, TCandidate]]":
        """List[mastapy.gears.gear_set_pareto_optimiser.BarForPareto[TAnalysis, TCandidate]]

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
    def input_sliders(
        self: Self,
    ) -> "List[_917.InputSliderForPareto[TAnalysis, TCandidate]]":
        """List[mastapy.gears.gear_set_pareto_optimiser.InputSliderForPareto[TAnalysis, TCandidate]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputSliders

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

    def add_selected_design(self: Self):
        """Method does not return."""
        self.wrapped.AddSelectedDesign()

    def add_selected_designs(self: Self):
        """Method does not return."""
        self.wrapped.AddSelectedDesigns()

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
    def cast_to(self: Self) -> "ChartInfoBase._Cast_ChartInfoBase":
        return self._Cast_ChartInfoBase(self)
