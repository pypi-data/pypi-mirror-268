"""AGMA20151AccuracyGrades"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1144
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA20151_ACCURACY_GRADES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "AGMA20151AccuracyGrades",
)

if TYPE_CHECKING:
    from mastapy.gears import _317


__docformat__ = "restructuredtext en"
__all__ = ("AGMA20151AccuracyGrades",)


Self = TypeVar("Self", bound="AGMA20151AccuracyGrades")


class AGMA20151AccuracyGrades(_1144.CylindricalAccuracyGrades):
    """AGMA20151AccuracyGrades

    This is a mastapy class.
    """

    TYPE = _AGMA20151_ACCURACY_GRADES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA20151AccuracyGrades")

    class _Cast_AGMA20151AccuracyGrades:
        """Special nested class for casting AGMA20151AccuracyGrades to subclasses."""

        def __init__(
            self: "AGMA20151AccuracyGrades._Cast_AGMA20151AccuracyGrades",
            parent: "AGMA20151AccuracyGrades",
        ):
            self._parent = parent

        @property
        def cylindrical_accuracy_grades(
            self: "AGMA20151AccuracyGrades._Cast_AGMA20151AccuracyGrades",
        ) -> "_1144.CylindricalAccuracyGrades":
            return self._parent._cast(_1144.CylindricalAccuracyGrades)

        @property
        def accuracy_grades(
            self: "AGMA20151AccuracyGrades._Cast_AGMA20151AccuracyGrades",
        ) -> "_317.AccuracyGrades":
            from mastapy.gears import _317

            return self._parent._cast(_317.AccuracyGrades)

        @property
        def agma20151_accuracy_grades(
            self: "AGMA20151AccuracyGrades._Cast_AGMA20151AccuracyGrades",
        ) -> "AGMA20151AccuracyGrades":
            return self._parent

        def __getattr__(
            self: "AGMA20151AccuracyGrades._Cast_AGMA20151AccuracyGrades", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMA20151AccuracyGrades.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_agma_quality_grade_new(self: Self) -> "int":
        """int"""
        temp = self.wrapped.HelixAGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @helix_agma_quality_grade_new.setter
    @enforce_parameter_types
    def helix_agma_quality_grade_new(self: Self, value: "int"):
        self.wrapped.HelixAGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def helix_agma_quality_grade_old(self: Self) -> "int":
        """int"""
        temp = self.wrapped.HelixAGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @helix_agma_quality_grade_old.setter
    @enforce_parameter_types
    def helix_agma_quality_grade_old(self: Self, value: "int"):
        self.wrapped.HelixAGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def pitch_agma_quality_grade_new(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PitchAGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @pitch_agma_quality_grade_new.setter
    @enforce_parameter_types
    def pitch_agma_quality_grade_new(self: Self, value: "int"):
        self.wrapped.PitchAGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def pitch_agma_quality_grade_old(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PitchAGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @pitch_agma_quality_grade_old.setter
    @enforce_parameter_types
    def pitch_agma_quality_grade_old(self: Self, value: "int"):
        self.wrapped.PitchAGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def profile_agma_quality_grade_new(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ProfileAGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @profile_agma_quality_grade_new.setter
    @enforce_parameter_types
    def profile_agma_quality_grade_new(self: Self, value: "int"):
        self.wrapped.ProfileAGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def profile_agma_quality_grade_old(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ProfileAGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @profile_agma_quality_grade_old.setter
    @enforce_parameter_types
    def profile_agma_quality_grade_old(self: Self, value: "int"):
        self.wrapped.ProfileAGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def radial_agma_quality_grade_new(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RadialAGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @radial_agma_quality_grade_new.setter
    @enforce_parameter_types
    def radial_agma_quality_grade_new(self: Self, value: "int"):
        self.wrapped.RadialAGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def radial_agma_quality_grade_old(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RadialAGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @radial_agma_quality_grade_old.setter
    @enforce_parameter_types
    def radial_agma_quality_grade_old(self: Self, value: "int"):
        self.wrapped.RadialAGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def cast_to(self: Self) -> "AGMA20151AccuracyGrades._Cast_AGMA20151AccuracyGrades":
        return self._Cast_AGMA20151AccuracyGrades(self)
