"""CylindricalAccuracyGraderWithProfileFormAndSlope"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_ACCURACY_GRADER_WITH_PROFILE_FORM_AND_SLOPE = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "CylindricalAccuracyGraderWithProfileFormAndSlope",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1139,
        _1141,
        _1147,
        _1148,
        _1149,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalAccuracyGraderWithProfileFormAndSlope",)


Self = TypeVar("Self", bound="CylindricalAccuracyGraderWithProfileFormAndSlope")


class CylindricalAccuracyGraderWithProfileFormAndSlope(_1142.CylindricalAccuracyGrader):
    """CylindricalAccuracyGraderWithProfileFormAndSlope

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_ACCURACY_GRADER_WITH_PROFILE_FORM_AND_SLOPE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalAccuracyGraderWithProfileFormAndSlope"
    )

    class _Cast_CylindricalAccuracyGraderWithProfileFormAndSlope:
        """Special nested class for casting CylindricalAccuracyGraderWithProfileFormAndSlope to subclasses."""

        def __init__(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
            parent: "CylindricalAccuracyGraderWithProfileFormAndSlope",
        ):
            self._parent = parent

        @property
        def cylindrical_accuracy_grader(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
        ) -> "_1142.CylindricalAccuracyGrader":
            return self._parent._cast(_1142.CylindricalAccuracyGrader)

        @property
        def agma20151a01_accuracy_grader(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
        ) -> "_1139.AGMA20151A01AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1139,
            )

            return self._parent._cast(_1139.AGMA20151A01AccuracyGrader)

        @property
        def agmaiso13281b14_accuracy_grader(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
        ) -> "_1141.AGMAISO13281B14AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1141,
            )

            return self._parent._cast(_1141.AGMAISO13281B14AccuracyGrader)

        @property
        def iso132811995_accuracy_grader(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
        ) -> "_1147.ISO132811995AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1147,
            )

            return self._parent._cast(_1147.ISO132811995AccuracyGrader)

        @property
        def iso132812013_accuracy_grader(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
        ) -> "_1148.ISO132812013AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1148,
            )

            return self._parent._cast(_1148.ISO132812013AccuracyGrader)

        @property
        def iso1328_accuracy_grader_common(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
        ) -> "_1149.ISO1328AccuracyGraderCommon":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1149,
            )

            return self._parent._cast(_1149.ISO1328AccuracyGraderCommon)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
        ) -> "CylindricalAccuracyGraderWithProfileFormAndSlope":
            return self._parent

        def __getattr__(
            self: "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope",
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
        self: Self,
        instance_to_wrap: "CylindricalAccuracyGraderWithProfileFormAndSlope.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_slope_deviation_per_inch_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixSlopeDeviationPerInchFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_pitches_for_sector_pitch_deviation(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfPitchesForSectorPitchDeviation

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalAccuracyGraderWithProfileFormAndSlope._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope":
        return self._Cast_CylindricalAccuracyGraderWithProfileFormAndSlope(self)
