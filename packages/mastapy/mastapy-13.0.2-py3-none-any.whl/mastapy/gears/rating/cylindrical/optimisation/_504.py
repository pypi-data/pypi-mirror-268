"""CylindricalGearSetRatingOptimisationHelper"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.rating.cylindrical.optimisation import _508, _509, _510
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_RATING_OPTIMISATION_HELPER = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation",
    "CylindricalGearSetRatingOptimisationHelper",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.optimisation import _505, _506


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetRatingOptimisationHelper",)


Self = TypeVar("Self", bound="CylindricalGearSetRatingOptimisationHelper")


class CylindricalGearSetRatingOptimisationHelper(_0.APIBase):
    """CylindricalGearSetRatingOptimisationHelper

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_RATING_OPTIMISATION_HELPER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetRatingOptimisationHelper"
    )

    class _Cast_CylindricalGearSetRatingOptimisationHelper:
        """Special nested class for casting CylindricalGearSetRatingOptimisationHelper to subclasses."""

        def __init__(
            self: "CylindricalGearSetRatingOptimisationHelper._Cast_CylindricalGearSetRatingOptimisationHelper",
            parent: "CylindricalGearSetRatingOptimisationHelper",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_rating_optimisation_helper(
            self: "CylindricalGearSetRatingOptimisationHelper._Cast_CylindricalGearSetRatingOptimisationHelper",
        ) -> "CylindricalGearSetRatingOptimisationHelper":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetRatingOptimisationHelper._Cast_CylindricalGearSetRatingOptimisationHelper",
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
        self: Self, instance_to_wrap: "CylindricalGearSetRatingOptimisationHelper.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_angle_optimisation_results(
        self: Self,
    ) -> "_505.OptimisationResultsPair[_508.SafetyFactorOptimisationStepResultAngle]":
        """mastapy.gears.rating.cylindrical.optimisation.OptimisationResultsPair[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultAngle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleOptimisationResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _508.SafetyFactorOptimisationStepResultAngle
        ](temp)

    @property
    def maximum_transverse_contact_ratio_optimisation_results(
        self: Self,
    ) -> "_505.OptimisationResultsPair[_509.SafetyFactorOptimisationStepResultNumber]":
        """mastapy.gears.rating.cylindrical.optimisation.OptimisationResultsPair[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultNumber]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTransverseContactRatioOptimisationResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _509.SafetyFactorOptimisationStepResultNumber
        ](temp)

    @property
    def normal_module_optimisation_results(
        self: Self,
    ) -> "_505.OptimisationResultsPair[_510.SafetyFactorOptimisationStepResultShortLength]":
        """mastapy.gears.rating.cylindrical.optimisation.OptimisationResultsPair[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultShortLength]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalModuleOptimisationResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _510.SafetyFactorOptimisationStepResultShortLength
        ](temp)

    @property
    def pressure_angle_optimisation_results(
        self: Self,
    ) -> "_505.OptimisationResultsPair[_508.SafetyFactorOptimisationStepResultAngle]":
        """mastapy.gears.rating.cylindrical.optimisation.OptimisationResultsPair[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultAngle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureAngleOptimisationResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _508.SafetyFactorOptimisationStepResultAngle
        ](temp)

    @property
    def profile_shift_coefficient_optimisation_results(
        self: Self,
    ) -> "_505.OptimisationResultsPair[_509.SafetyFactorOptimisationStepResultNumber]":
        """mastapy.gears.rating.cylindrical.optimisation.OptimisationResultsPair[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultNumber]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileShiftCoefficientOptimisationResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _509.SafetyFactorOptimisationStepResultNumber
        ](temp)

    @property
    def all_helix_angle_optimisation_results(
        self: Self,
    ) -> "List[_506.SafetyFactorOptimisationResults[_508.SafetyFactorOptimisationStepResultAngle]]":
        """List[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationResults[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultAngle]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllHelixAngleOptimisationResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_normal_module_optimisation_results(
        self: Self,
    ) -> "List[_506.SafetyFactorOptimisationResults[_510.SafetyFactorOptimisationStepResultShortLength]]":
        """List[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationResults[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultShortLength]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllNormalModuleOptimisationResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_normal_pressure_angle_optimisation_results(
        self: Self,
    ) -> "List[_506.SafetyFactorOptimisationResults[_508.SafetyFactorOptimisationStepResultAngle]]":
        """List[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationResults[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultAngle]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllNormalPressureAngleOptimisationResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def all_profile_shift_optimisation_results(
        self: Self,
    ) -> "List[_506.SafetyFactorOptimisationResults[_509.SafetyFactorOptimisationStepResultNumber]]":
        """List[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationResults[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultNumber]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllProfileShiftOptimisationResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def helix_angle_and_normal_pressure_angle_optimisation_results(
        self: Self,
    ) -> "List[_506.SafetyFactorOptimisationResults[_508.SafetyFactorOptimisationStepResultAngle]]":
        """List[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationResults[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultAngle]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleAndNormalPressureAngleOptimisationResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_transverse_contact_ratio_results(
        self: Self,
    ) -> "List[_506.SafetyFactorOptimisationResults[_509.SafetyFactorOptimisationStepResultNumber]]":
        """List[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationResults[mastapy.gears.rating.cylindrical.optimisation.SafetyFactorOptimisationStepResultNumber]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsTransverseContactRatioResults

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

    def calculate_optimisation_charts(self: Self):
        """Method does not return."""
        self.wrapped.CalculateOptimisationCharts()

    def create_optimisation_report(self: Self):
        """Method does not return."""
        self.wrapped.CreateOptimisationReport()

    def set_face_widths_for_required_safety_factor(self: Self):
        """Method does not return."""
        self.wrapped.SetFaceWidthsForRequiredSafetyFactor()

    def set_helix_angle_for_maximum_safety_factor(self: Self):
        """Method does not return."""
        self.wrapped.SetHelixAngleForMaximumSafetyFactor()

    def set_normal_module_for_maximum_safety_factor(self: Self):
        """Method does not return."""
        self.wrapped.SetNormalModuleForMaximumSafetyFactor()

    def set_pressure_angle_for_maximum_safety_factor(self: Self):
        """Method does not return."""
        self.wrapped.SetPressureAngleForMaximumSafetyFactor()

    def set_profile_shift_coefficient_for_maximum_safety_factor(self: Self):
        """Method does not return."""
        self.wrapped.SetProfileShiftCoefficientForMaximumSafetyFactor()

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
    ) -> "CylindricalGearSetRatingOptimisationHelper._Cast_CylindricalGearSetRatingOptimisationHelper":
        return self._Cast_CylindricalGearSetRatingOptimisationHelper(self)
