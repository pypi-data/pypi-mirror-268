"""AGMAGleasonConicalAccuracyGrades"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears import _317
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_ACCURACY_GRADES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical",
    "AGMAGleasonConicalAccuracyGrades",
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalAccuracyGrades",)


Self = TypeVar("Self", bound="AGMAGleasonConicalAccuracyGrades")


class AGMAGleasonConicalAccuracyGrades(_317.AccuracyGrades):
    """AGMAGleasonConicalAccuracyGrades

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_ACCURACY_GRADES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalAccuracyGrades")

    class _Cast_AGMAGleasonConicalAccuracyGrades:
        """Special nested class for casting AGMAGleasonConicalAccuracyGrades to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalAccuracyGrades._Cast_AGMAGleasonConicalAccuracyGrades",
            parent: "AGMAGleasonConicalAccuracyGrades",
        ):
            self._parent = parent

        @property
        def accuracy_grades(
            self: "AGMAGleasonConicalAccuracyGrades._Cast_AGMAGleasonConicalAccuracyGrades",
        ) -> "_317.AccuracyGrades":
            return self._parent._cast(_317.AccuracyGrades)

        @property
        def agma_gleason_conical_accuracy_grades(
            self: "AGMAGleasonConicalAccuracyGrades._Cast_AGMAGleasonConicalAccuracyGrades",
        ) -> "AGMAGleasonConicalAccuracyGrades":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalAccuracyGrades._Cast_AGMAGleasonConicalAccuracyGrades",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalAccuracyGrades.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def agma_quality_grade_new(self: Self) -> "int":
        """int"""
        temp = self.wrapped.AGMAQualityGradeNew

        if temp is None:
            return 0

        return temp

    @agma_quality_grade_new.setter
    @enforce_parameter_types
    def agma_quality_grade_new(self: Self, value: "int"):
        self.wrapped.AGMAQualityGradeNew = int(value) if value is not None else 0

    @property
    def agma_quality_grade_old(self: Self) -> "int":
        """int"""
        temp = self.wrapped.AGMAQualityGradeOld

        if temp is None:
            return 0

        return temp

    @agma_quality_grade_old.setter
    @enforce_parameter_types
    def agma_quality_grade_old(self: Self, value: "int"):
        self.wrapped.AGMAQualityGradeOld = int(value) if value is not None else 0

    @property
    def single_pitch_deviation(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SinglePitchDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @single_pitch_deviation.setter
    @enforce_parameter_types
    def single_pitch_deviation(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SinglePitchDeviation = value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalAccuracyGrades._Cast_AGMAGleasonConicalAccuracyGrades":
        return self._Cast_AGMAGleasonConicalAccuracyGrades(self)
