"""CalculateProfileDeviationAccuracy"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CALCULATE_PROFILE_DEVIATION_ACCURACY = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "CalculateProfileDeviationAccuracy",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _681,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CalculateProfileDeviationAccuracy",)


Self = TypeVar("Self", bound="CalculateProfileDeviationAccuracy")


class CalculateProfileDeviationAccuracy(_0.APIBase):
    """CalculateProfileDeviationAccuracy

    This is a mastapy class.
    """

    TYPE = _CALCULATE_PROFILE_DEVIATION_ACCURACY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CalculateProfileDeviationAccuracy")

    class _Cast_CalculateProfileDeviationAccuracy:
        """Special nested class for casting CalculateProfileDeviationAccuracy to subclasses."""

        def __init__(
            self: "CalculateProfileDeviationAccuracy._Cast_CalculateProfileDeviationAccuracy",
            parent: "CalculateProfileDeviationAccuracy",
        ):
            self._parent = parent

        @property
        def calculate_profile_deviation_accuracy(
            self: "CalculateProfileDeviationAccuracy._Cast_CalculateProfileDeviationAccuracy",
        ) -> "CalculateProfileDeviationAccuracy":
            return self._parent

        def __getattr__(
            self: "CalculateProfileDeviationAccuracy._Cast_CalculateProfileDeviationAccuracy",
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
        self: Self, instance_to_wrap: "CalculateProfileDeviationAccuracy.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def achieved_profile_agma20151a01_quality_grade(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AchievedProfileAGMA20151A01QualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def achieved_profile_iso132811995e_quality_grade(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AchievedProfileISO132811995EQualityGrade

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankName

        if temp is None:
            return ""

        return temp

    @property
    def profile_deviation_agma20151a01_quality_grade_designed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileDeviationAGMA20151A01QualityGradeDesigned

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_deviation_iso132811995e_quality_grade_designed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileDeviationISO132811995EQualityGradeDesigned

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation_agma20151a01_quality_grade_obtained(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_form_deviation_iso132811995e_quality_grade_obtained(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormDeviationISO132811995EQualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_slope_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileSlopeDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_slope_deviation_agma20151a01_quality_grade_obtained(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileSlopeDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_slope_deviation_iso132811995e_quality_grade_obtained(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileSlopeDeviationISO132811995EQualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def total_profile_deviation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalProfileDeviation

        if temp is None:
            return 0.0

        return temp

    @property
    def total_profile_deviation_agma20151a01_quality_grade_obtained(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalProfileDeviationAGMA20151A01QualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def total_profile_deviation_iso132811995e_quality_grade_obtained(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalProfileDeviationISO132811995EQualityGradeObtained

        if temp is None:
            return 0.0

        return temp

    @property
    def manufactured_agma20151a01_quality_grades(
        self: Self,
    ) -> "List[_681.ManufacturedQualityGrade]":
        """List[mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ManufacturedQualityGrade]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturedAGMA20151A01QualityGrades

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def manufactured_iso132811995e_quality_grades(
        self: Self,
    ) -> "List[_681.ManufacturedQualityGrade]":
        """List[mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.ManufacturedQualityGrade]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturedISO132811995EQualityGrades

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
    ) -> "CalculateProfileDeviationAccuracy._Cast_CalculateProfileDeviationAccuracy":
        return self._Cast_CalculateProfileDeviationAccuracy(self)
