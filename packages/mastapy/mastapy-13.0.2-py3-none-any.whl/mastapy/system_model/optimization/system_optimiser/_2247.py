"""SystemOptimiserDetails"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_OPTIMISER_DETAILS = python_net_import(
    "SMT.MastaAPI.SystemModel.Optimization.SystemOptimiser", "SystemOptimiserDetails"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.load_case_groups import _5678, _5677
    from mastapy.system_model.optimization.system_optimiser import _2245, _2244


__docformat__ = "restructuredtext en"
__all__ = ("SystemOptimiserDetails",)


Self = TypeVar("Self", bound="SystemOptimiserDetails")


class SystemOptimiserDetails(_0.APIBase):
    """SystemOptimiserDetails

    This is a mastapy class.
    """

    TYPE = _SYSTEM_OPTIMISER_DETAILS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemOptimiserDetails")

    class _Cast_SystemOptimiserDetails:
        """Special nested class for casting SystemOptimiserDetails to subclasses."""

        def __init__(
            self: "SystemOptimiserDetails._Cast_SystemOptimiserDetails",
            parent: "SystemOptimiserDetails",
        ):
            self._parent = parent

        @property
        def system_optimiser_details(
            self: "SystemOptimiserDetails._Cast_SystemOptimiserDetails",
        ) -> "SystemOptimiserDetails":
            return self._parent

        def __getattr__(
            self: "SystemOptimiserDetails._Cast_SystemOptimiserDetails", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemOptimiserDetails.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def avoid_specific_orders(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AvoidSpecificOrders

        if temp is None:
            return False

        return temp

    @avoid_specific_orders.setter
    @enforce_parameter_types
    def avoid_specific_orders(self: Self, value: "bool"):
        self.wrapped.AvoidSpecificOrders = bool(value) if value is not None else False

    @property
    def check_passing_order_separation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CheckPassingOrderSeparation

        if temp is None:
            return False

        return temp

    @check_passing_order_separation.setter
    @enforce_parameter_types
    def check_passing_order_separation(self: Self, value: "bool"):
        self.wrapped.CheckPassingOrderSeparation = (
            bool(value) if value is not None else False
        )

    @property
    def criteria_for_selecting_configurations_to_keep(
        self: Self,
    ) -> "_5678.SystemOptimiserTargets":
        """mastapy.system_model.analyses_and_results.load_case_groups.SystemOptimiserTargets"""
        temp = self.wrapped.CriteriaForSelectingConfigurationsToKeep

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.SystemOptimiserTargets",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.load_case_groups._5678",
            "SystemOptimiserTargets",
        )(value)

    @criteria_for_selecting_configurations_to_keep.setter
    @enforce_parameter_types
    def criteria_for_selecting_configurations_to_keep(
        self: Self, value: "_5678.SystemOptimiserTargets"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.SystemOptimiserTargets",
        )
        self.wrapped.CriteriaForSelectingConfigurationsToKeep = value

    @property
    def filter_designs_on_estimated_maximum_achievable_transverse_contact_ratio(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.FilterDesignsOnEstimatedMaximumAchievableTransverseContactRatio
        )

        if temp is None:
            return False

        return temp

    @filter_designs_on_estimated_maximum_achievable_transverse_contact_ratio.setter
    @enforce_parameter_types
    def filter_designs_on_estimated_maximum_achievable_transverse_contact_ratio(
        self: Self, value: "bool"
    ):
        self.wrapped.FilterDesignsOnEstimatedMaximumAchievableTransverseContactRatio = (
            bool(value) if value is not None else False
        )

    @property
    def gear_set_optimisation(self: Self) -> "_5677.SystemOptimiserGearSetOptimisation":
        """mastapy.system_model.analyses_and_results.load_case_groups.SystemOptimiserGearSetOptimisation"""
        temp = self.wrapped.GearSetOptimisation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.SystemOptimiserGearSetOptimisation",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.load_case_groups._5677",
            "SystemOptimiserGearSetOptimisation",
        )(value)

    @gear_set_optimisation.setter
    @enforce_parameter_types
    def gear_set_optimisation(
        self: Self, value: "_5677.SystemOptimiserGearSetOptimisation"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.SystemOptimiserGearSetOptimisation",
        )
        self.wrapped.GearSetOptimisation = value

    @property
    def maximum_number_of_configurations_to_create(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfConfigurationsToCreate

        if temp is None:
            return 0

        return temp

    @maximum_number_of_configurations_to_create.setter
    @enforce_parameter_types
    def maximum_number_of_configurations_to_create(self: Self, value: "int"):
        self.wrapped.MaximumNumberOfConfigurationsToCreate = (
            int(value) if value is not None else 0
        )

    @property
    def maximum_number_of_solutions(self: Self) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.MaximumNumberOfSolutions

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @maximum_number_of_solutions.setter
    @enforce_parameter_types
    def maximum_number_of_solutions(self: Self, value: "Union[int, Tuple[int, bool]]"):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.MaximumNumberOfSolutions = value

    @property
    def minimum_number_of_solutions(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MinimumNumberOfSolutions

        if temp is None:
            return 0

        return temp

    @minimum_number_of_solutions.setter
    @enforce_parameter_types
    def minimum_number_of_solutions(self: Self, value: "int"):
        self.wrapped.MinimumNumberOfSolutions = int(value) if value is not None else 0

    @property
    def modify_face_widths(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ModifyFaceWidths

        if temp is None:
            return False

        return temp

    @modify_face_widths.setter
    @enforce_parameter_types
    def modify_face_widths(self: Self, value: "bool"):
        self.wrapped.ModifyFaceWidths = bool(value) if value is not None else False

    @property
    def number_of_orders_to_avoid(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfOrdersToAvoid

        if temp is None:
            return 0

        return temp

    @number_of_orders_to_avoid.setter
    @enforce_parameter_types
    def number_of_orders_to_avoid(self: Self, value: "int"):
        self.wrapped.NumberOfOrdersToAvoid = int(value) if value is not None else 0

    @property
    def number_of_harmonics_for_passing_order_separation_test(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfHarmonicsForPassingOrderSeparationTest

        if temp is None:
            return 0

        return temp

    @number_of_harmonics_for_passing_order_separation_test.setter
    @enforce_parameter_types
    def number_of_harmonics_for_passing_order_separation_test(self: Self, value: "int"):
        self.wrapped.NumberOfHarmonicsForPassingOrderSeparationTest = (
            int(value) if value is not None else 0
        )

    @property
    def number_of_solutions(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfSolutions

        if temp is None:
            return 0

        return temp

    @property
    def required_normalised_safety_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredNormalisedSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @required_normalised_safety_factor.setter
    @enforce_parameter_types
    def required_normalised_safety_factor(self: Self, value: "float"):
        self.wrapped.RequiredNormalisedSafetyFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def required_passing_order_separation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredPassingOrderSeparation

        if temp is None:
            return 0.0

        return temp

    @required_passing_order_separation.setter
    @enforce_parameter_types
    def required_passing_order_separation(self: Self, value: "float"):
        self.wrapped.RequiredPassingOrderSeparation = (
            float(value) if value is not None else 0.0
        )

    @property
    def show_ratio_as_speed_increasing(self: Self) -> "overridable.Overridable_bool":
        """Overridable[bool]"""
        temp = self.wrapped.ShowRatioAsSpeedIncreasing

        if temp is None:
            return False

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_bool"
        )(temp)

    @show_ratio_as_speed_increasing.setter
    @enforce_parameter_types
    def show_ratio_as_speed_increasing(
        self: Self, value: "Union[bool, Tuple[bool, bool]]"
    ):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else False, is_overridden
        )
        self.wrapped.ShowRatioAsSpeedIncreasing = value

    @property
    def target_maximum_absolute_cylindrical_gear_profile_shift_coefficient(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.TargetMaximumAbsoluteCylindricalGearProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @target_maximum_absolute_cylindrical_gear_profile_shift_coefficient.setter
    @enforce_parameter_types
    def target_maximum_absolute_cylindrical_gear_profile_shift_coefficient(
        self: Self, value: "float"
    ):
        self.wrapped.TargetMaximumAbsoluteCylindricalGearProfileShiftCoefficient = (
            float(value) if value is not None else 0.0
        )

    @property
    def tolerance_for_combining_duty_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ToleranceForCombiningDutyCycles

        if temp is None:
            return 0.0

        return temp

    @tolerance_for_combining_duty_cycles.setter
    @enforce_parameter_types
    def tolerance_for_combining_duty_cycles(self: Self, value: "float"):
        self.wrapped.ToleranceForCombiningDutyCycles = (
            float(value) if value is not None else 0.0
        )

    @property
    def planet_gear_options(self: Self) -> "List[_2245.PlanetGearOptions]":
        """List[mastapy.system_model.optimization.system_optimiser.PlanetGearOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetGearOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def target_ratios(self: Self) -> "List[_2244.DesignStateTargetRatio]":
        """List[mastapy.system_model.optimization.system_optimiser.DesignStateTargetRatio]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TargetRatios

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

    def create_designs(self: Self):
        """Method does not return."""
        self.wrapped.CreateDesigns()

    def determine_ratio_tolerances(self: Self):
        """Method does not return."""
        self.wrapped.DetermineRatioTolerances()

    def find_solutions_from_current_ratio_tolerances(self: Self):
        """Method does not return."""
        self.wrapped.FindSolutionsFromCurrentRatioTolerances()

    def perform_system_optimisation(self: Self):
        """Method does not return."""
        self.wrapped.PerformSystemOptimisation()

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
    def cast_to(self: Self) -> "SystemOptimiserDetails._Cast_SystemOptimiserDetails":
        return self._Cast_SystemOptimiserDetails(self)
