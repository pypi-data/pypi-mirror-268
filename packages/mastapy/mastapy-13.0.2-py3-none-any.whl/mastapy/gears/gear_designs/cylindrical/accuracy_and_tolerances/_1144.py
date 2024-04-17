"""CylindricalAccuracyGrades"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears import _317
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_ACCURACY_GRADES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "CylindricalAccuracyGrades",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1140,
        _1150,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalAccuracyGrades",)


Self = TypeVar("Self", bound="CylindricalAccuracyGrades")


class CylindricalAccuracyGrades(_317.AccuracyGrades):
    """CylindricalAccuracyGrades

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_ACCURACY_GRADES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalAccuracyGrades")

    class _Cast_CylindricalAccuracyGrades:
        """Special nested class for casting CylindricalAccuracyGrades to subclasses."""

        def __init__(
            self: "CylindricalAccuracyGrades._Cast_CylindricalAccuracyGrades",
            parent: "CylindricalAccuracyGrades",
        ):
            self._parent = parent

        @property
        def accuracy_grades(
            self: "CylindricalAccuracyGrades._Cast_CylindricalAccuracyGrades",
        ) -> "_317.AccuracyGrades":
            return self._parent._cast(_317.AccuracyGrades)

        @property
        def agma20151_accuracy_grades(
            self: "CylindricalAccuracyGrades._Cast_CylindricalAccuracyGrades",
        ) -> "_1140.AGMA20151AccuracyGrades":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1140,
            )

            return self._parent._cast(_1140.AGMA20151AccuracyGrades)

        @property
        def iso1328_accuracy_grades(
            self: "CylindricalAccuracyGrades._Cast_CylindricalAccuracyGrades",
        ) -> "_1150.ISO1328AccuracyGrades":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1150,
            )

            return self._parent._cast(_1150.ISO1328AccuracyGrades)

        @property
        def cylindrical_accuracy_grades(
            self: "CylindricalAccuracyGrades._Cast_CylindricalAccuracyGrades",
        ) -> "CylindricalAccuracyGrades":
            return self._parent

        def __getattr__(
            self: "CylindricalAccuracyGrades._Cast_CylindricalAccuracyGrades", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalAccuracyGrades.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.HelixQualityGrade

        if temp is None:
            return 0

        return temp

    @helix_quality_grade.setter
    @enforce_parameter_types
    def helix_quality_grade(self: Self, value: "int"):
        self.wrapped.HelixQualityGrade = int(value) if value is not None else 0

    @property
    def pitch_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PitchQualityGrade

        if temp is None:
            return 0

        return temp

    @pitch_quality_grade.setter
    @enforce_parameter_types
    def pitch_quality_grade(self: Self, value: "int"):
        self.wrapped.PitchQualityGrade = int(value) if value is not None else 0

    @property
    def profile_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ProfileQualityGrade

        if temp is None:
            return 0

        return temp

    @profile_quality_grade.setter
    @enforce_parameter_types
    def profile_quality_grade(self: Self, value: "int"):
        self.wrapped.ProfileQualityGrade = int(value) if value is not None else 0

    @property
    def radial_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RadialQualityGrade

        if temp is None:
            return 0

        return temp

    @radial_quality_grade.setter
    @enforce_parameter_types
    def radial_quality_grade(self: Self, value: "int"):
        self.wrapped.RadialQualityGrade = int(value) if value is not None else 0

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalAccuracyGrades._Cast_CylindricalAccuracyGrades":
        return self._Cast_CylindricalAccuracyGrades(self)
