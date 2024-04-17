"""DesignSpaceSearchBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.gear_set_pareto_optimiser import _906
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_DESIGN_SPACE_SEARCH_BASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "DesignSpaceSearchBase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import (
        _918,
        _907,
        _926,
        _941,
        _908,
        _911,
        _915,
        _916,
        _919,
        _923,
        _942,
        _943,
    )
    from mastapy.math_utility.optimisation import _1556, _1553, _1548
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("DesignSpaceSearchBase",)


Self = TypeVar("Self", bound="DesignSpaceSearchBase")
TAnalysis = TypeVar("TAnalysis", bound="_1223.AbstractGearSetAnalysis")
TCandidate = TypeVar("TCandidate")


class DesignSpaceSearchBase(_0.APIBase, Generic[TAnalysis, TCandidate]):
    """DesignSpaceSearchBase

    This is a mastapy class.

    Generic Types:
        TAnalysis
        TCandidate
    """

    TYPE = _DESIGN_SPACE_SEARCH_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignSpaceSearchBase")

    class _Cast_DesignSpaceSearchBase:
        """Special nested class for casting DesignSpaceSearchBase to subclasses."""

        def __init__(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
            parent: "DesignSpaceSearchBase",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_pareto_optimiser(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "_908.CylindricalGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _908

            return self._parent._cast(_908.CylindricalGearSetParetoOptimiser)

        @property
        def face_gear_set_pareto_optimiser(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "_911.FaceGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _911

            return self._parent._cast(_911.FaceGearSetParetoOptimiser)

        @property
        def gear_set_pareto_optimiser(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "_915.GearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _915

            return self._parent._cast(_915.GearSetParetoOptimiser)

        @property
        def hypoid_gear_set_pareto_optimiser(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "_916.HypoidGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _916

            return self._parent._cast(_916.HypoidGearSetParetoOptimiser)

        @property
        def micro_geometry_design_space_search(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "_919.MicroGeometryDesignSpaceSearch":
            from mastapy.gears.gear_set_pareto_optimiser import _919

            return self._parent._cast(_919.MicroGeometryDesignSpaceSearch)

        @property
        def micro_geometry_gear_set_design_space_search(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "_923.MicroGeometryGearSetDesignSpaceSearch":
            from mastapy.gears.gear_set_pareto_optimiser import _923

            return self._parent._cast(_923.MicroGeometryGearSetDesignSpaceSearch)

        @property
        def spiral_bevel_gear_set_pareto_optimiser(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "_942.SpiralBevelGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _942

            return self._parent._cast(_942.SpiralBevelGearSetParetoOptimiser)

        @property
        def straight_bevel_gear_set_pareto_optimiser(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "_943.StraightBevelGearSetParetoOptimiser":
            from mastapy.gears.gear_set_pareto_optimiser import _943

            return self._parent._cast(_943.StraightBevelGearSetParetoOptimiser)

        @property
        def design_space_search_base(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase",
        ) -> "DesignSpaceSearchBase":
            return self._parent

        def __getattr__(
            self: "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignSpaceSearchBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_space_search_strategy_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignSpaceSearchStrategyDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @design_space_search_strategy_database.setter
    @enforce_parameter_types
    def design_space_search_strategy_database(self: Self, value: "str"):
        self.wrapped.DesignSpaceSearchStrategyDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def design_space_search_strategy_database_duty_cycle(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DesignSpaceSearchStrategyDatabaseDutyCycle.SelectedItemName

        if temp is None:
            return ""

        return temp

    @design_space_search_strategy_database_duty_cycle.setter
    @enforce_parameter_types
    def design_space_search_strategy_database_duty_cycle(self: Self, value: "str"):
        self.wrapped.DesignSpaceSearchStrategyDatabaseDutyCycle.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def display_candidates(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CandidateDisplayChoice":
        """EnumWithSelectedValue[mastapy.gears.gear_set_pareto_optimiser.CandidateDisplayChoice]"""
        temp = self.wrapped.DisplayCandidates

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CandidateDisplayChoice.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @display_candidates.setter
    @enforce_parameter_types
    def display_candidates(self: Self, value: "_906.CandidateDisplayChoice"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CandidateDisplayChoice.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DisplayCandidates = value

    @property
    def maximum_number_of_candidates_to_display(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfCandidatesToDisplay

        if temp is None:
            return 0

        return temp

    @maximum_number_of_candidates_to_display.setter
    @enforce_parameter_types
    def maximum_number_of_candidates_to_display(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfCandidatesToDisplay = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_candidates_after_filtering(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCandidatesAfterFiltering

        if temp is None:
            return 0

        return temp

    @property
    def number_of_dominant_candidates(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfDominantCandidates

        if temp is None:
            return 0

        return temp

    @property
    def number_of_feasible_candidates(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfFeasibleCandidates

        if temp is None:
            return 0

        return temp

    @property
    def number_of_unfiltered_candidates(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfUnfilteredCandidates

        if temp is None:
            return 0

        return temp

    @property
    def number_of_unrateable_designs(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfUnrateableDesigns

        if temp is None:
            return 0

        return temp

    @property
    def remove_candidates_with(self: Self) -> "_918.LargerOrSmaller":
        """mastapy.gears.gear_set_pareto_optimiser.LargerOrSmaller"""
        temp = self.wrapped.RemoveCandidatesWith

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearSetParetoOptimiser.LargerOrSmaller"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_set_pareto_optimiser._918", "LargerOrSmaller"
        )(value)

    @remove_candidates_with.setter
    @enforce_parameter_types
    def remove_candidates_with(self: Self, value: "_918.LargerOrSmaller"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearSetParetoOptimiser.LargerOrSmaller"
        )
        self.wrapped.RemoveCandidatesWith = value

    @property
    def reporting_string_for_too_many_candidates_to_be_evaluated(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportingStringForTooManyCandidatesToBeEvaluated

        if temp is None:
            return ""

        return temp

    @property
    def selected_points(self: Self) -> "List[int]":
        """List[int]"""
        temp = self.wrapped.SelectedPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value

    @selected_points.setter
    @enforce_parameter_types
    def selected_points(self: Self, value: "List[int]"):
        value = conversion.mp_to_pn_objects_in_list(value)
        self.wrapped.SelectedPoints = value

    @property
    def total_number_of_candidates_to_be_evaluated(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalNumberOfCandidatesToBeEvaluated

        if temp is None:
            return 0

        return temp

    @property
    def viewing_candidates_selected_in_chart(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ViewingCandidatesSelectedInChart

        if temp is None:
            return False

        return temp

    @property
    def load_case_duty_cycle(self: Self) -> "TAnalysis":
        """TAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseDutyCycle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_candidate(self: Self) -> "TAnalysis":
        """TAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedCandidate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_design_space_search_strategy(
        self: Self,
    ) -> "_1556.ParetoOptimisationStrategy":
        """mastapy.math_utility.optimisation.ParetoOptimisationStrategy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedDesignSpaceSearchStrategy

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def all_candidate_designs_including_original_design(
        self: Self,
    ) -> "List[TCandidate]":
        """List[TCandidate]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllCandidateDesignsIncludingOriginalDesign

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_candidate_designs_to_display(self: Self) -> "List[TCandidate]":
        """List[TCandidate]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllCandidateDesignsToDisplay

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_candidate_designs_to_display_without_original_design(
        self: Self,
    ) -> "List[TCandidate]":
        """List[TCandidate]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllCandidateDesignsToDisplayWithoutOriginalDesign

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def candidate_designs_to_display(self: Self) -> "List[TCandidate]":
        """List[TCandidate]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CandidateDesignsToDisplay

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def chart_details(self: Self) -> "List[_907.ChartInfoBase[TAnalysis, TCandidate]]":
        """List[mastapy.gears.gear_set_pareto_optimiser.ChartInfoBase[TAnalysis, TCandidate]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ChartDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def filters(self: Self) -> "List[_1553.ParetoOptimisationFilter]":
        """List[mastapy.math_utility.optimisation.ParetoOptimisationFilter]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Filters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def input_setters(self: Self) -> "List[_1548.InputSetter[TAnalysis]]":
        """List[mastapy.math_utility.optimisation.InputSetter[TAnalysis]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputSetters

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def optimisation_targets(self: Self) -> "List[_926.OptimisationTarget[TAnalysis]]":
        """List[mastapy.gears.gear_set_pareto_optimiser.OptimisationTarget[TAnalysis]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OptimisationTargets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def reasons_for_invalid_candidates(
        self: Self,
    ) -> "List[_941.ReasonsForInvalidDesigns]":
        """List[mastapy.gears.gear_set_pareto_optimiser.ReasonsForInvalidDesigns]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonsForInvalidCandidates

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

    def add_table_filter(self: Self):
        """Method does not return."""
        self.wrapped.AddTableFilter()

    def find_dominant_candidates(self: Self):
        """Method does not return."""
        self.wrapped.FindDominantCandidates()

    def load_strategy(self: Self):
        """Method does not return."""
        self.wrapped.LoadStrategy()

    def save_results(self: Self):
        """Method does not return."""
        self.wrapped.SaveResults()

    def save_strategy(self: Self):
        """Method does not return."""
        self.wrapped.SaveStrategy()

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
    def cast_to(self: Self) -> "DesignSpaceSearchBase._Cast_DesignSpaceSearchBase":
        return self._Cast_DesignSpaceSearchBase(self)
