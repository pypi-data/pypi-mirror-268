"""ISO1328AccuracyGrades"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1144
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO1328_ACCURACY_GRADES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "ISO1328AccuracyGrades",
)

if TYPE_CHECKING:
    from mastapy.gears import _317


__docformat__ = "restructuredtext en"
__all__ = ("ISO1328AccuracyGrades",)


Self = TypeVar("Self", bound="ISO1328AccuracyGrades")


class ISO1328AccuracyGrades(_1144.CylindricalAccuracyGrades):
    """ISO1328AccuracyGrades

    This is a mastapy class.
    """

    TYPE = _ISO1328_ACCURACY_GRADES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO1328AccuracyGrades")

    class _Cast_ISO1328AccuracyGrades:
        """Special nested class for casting ISO1328AccuracyGrades to subclasses."""

        def __init__(
            self: "ISO1328AccuracyGrades._Cast_ISO1328AccuracyGrades",
            parent: "ISO1328AccuracyGrades",
        ):
            self._parent = parent

        @property
        def cylindrical_accuracy_grades(
            self: "ISO1328AccuracyGrades._Cast_ISO1328AccuracyGrades",
        ) -> "_1144.CylindricalAccuracyGrades":
            return self._parent._cast(_1144.CylindricalAccuracyGrades)

        @property
        def accuracy_grades(
            self: "ISO1328AccuracyGrades._Cast_ISO1328AccuracyGrades",
        ) -> "_317.AccuracyGrades":
            from mastapy.gears import _317

            return self._parent._cast(_317.AccuracyGrades)

        @property
        def iso1328_accuracy_grades(
            self: "ISO1328AccuracyGrades._Cast_ISO1328AccuracyGrades",
        ) -> "ISO1328AccuracyGrades":
            return self._parent

        def __getattr__(
            self: "ISO1328AccuracyGrades._Cast_ISO1328AccuracyGrades", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO1328AccuracyGrades.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_iso_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.HelixISOQualityGrade

        if temp is None:
            return 0

        return temp

    @helix_iso_quality_grade.setter
    @enforce_parameter_types
    def helix_iso_quality_grade(self: Self, value: "int"):
        self.wrapped.HelixISOQualityGrade = int(value) if value is not None else 0

    @property
    def pitch_iso_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PitchISOQualityGrade

        if temp is None:
            return 0

        return temp

    @pitch_iso_quality_grade.setter
    @enforce_parameter_types
    def pitch_iso_quality_grade(self: Self, value: "int"):
        self.wrapped.PitchISOQualityGrade = int(value) if value is not None else 0

    @property
    def profile_iso_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ProfileISOQualityGrade

        if temp is None:
            return 0

        return temp

    @profile_iso_quality_grade.setter
    @enforce_parameter_types
    def profile_iso_quality_grade(self: Self, value: "int"):
        self.wrapped.ProfileISOQualityGrade = int(value) if value is not None else 0

    @property
    def radial_iso_quality_grade(self: Self) -> "int":
        """int"""
        temp = self.wrapped.RadialISOQualityGrade

        if temp is None:
            return 0

        return temp

    @radial_iso_quality_grade.setter
    @enforce_parameter_types
    def radial_iso_quality_grade(self: Self, value: "int"):
        self.wrapped.RadialISOQualityGrade = int(value) if value is not None else 0

    @property
    def cast_to(self: Self) -> "ISO1328AccuracyGrades._Cast_ISO1328AccuracyGrades":
        return self._Cast_ISO1328AccuracyGrades(self)
