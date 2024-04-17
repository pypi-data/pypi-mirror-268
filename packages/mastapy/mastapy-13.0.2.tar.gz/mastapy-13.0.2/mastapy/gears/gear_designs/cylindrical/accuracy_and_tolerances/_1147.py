"""ISO132811995AccuracyGrader"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO132811995_ACCURACY_GRADER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "ISO132811995AccuracyGrader",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1151,
        _1143,
        _1142,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISO132811995AccuracyGrader",)


Self = TypeVar("Self", bound="ISO132811995AccuracyGrader")


class ISO132811995AccuracyGrader(_1149.ISO1328AccuracyGraderCommon):
    """ISO132811995AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _ISO132811995_ACCURACY_GRADER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO132811995AccuracyGrader")

    class _Cast_ISO132811995AccuracyGrader:
        """Special nested class for casting ISO132811995AccuracyGrader to subclasses."""

        def __init__(
            self: "ISO132811995AccuracyGrader._Cast_ISO132811995AccuracyGrader",
            parent: "ISO132811995AccuracyGrader",
        ):
            self._parent = parent

        @property
        def iso1328_accuracy_grader_common(
            self: "ISO132811995AccuracyGrader._Cast_ISO132811995AccuracyGrader",
        ) -> "_1149.ISO1328AccuracyGraderCommon":
            return self._parent._cast(_1149.ISO1328AccuracyGraderCommon)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(
            self: "ISO132811995AccuracyGrader._Cast_ISO132811995AccuracyGrader",
        ) -> "_1143.CylindricalAccuracyGraderWithProfileFormAndSlope":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1143,
            )

            return self._parent._cast(
                _1143.CylindricalAccuracyGraderWithProfileFormAndSlope
            )

        @property
        def cylindrical_accuracy_grader(
            self: "ISO132811995AccuracyGrader._Cast_ISO132811995AccuracyGrader",
        ) -> "_1142.CylindricalAccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1142,
            )

            return self._parent._cast(_1142.CylindricalAccuracyGrader)

        @property
        def iso132811995_accuracy_grader(
            self: "ISO132811995AccuracyGrader._Cast_ISO132811995AccuracyGrader",
        ) -> "ISO132811995AccuracyGrader":
            return self._parent

        def __getattr__(
            self: "ISO132811995AccuracyGrader._Cast_ISO132811995AccuracyGrader",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO132811995AccuracyGrader.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cumulative_pitch_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CumulativePitchDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def helix_form_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixFormDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def helix_slope_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixSlopeDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_form_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_slope_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileSlopeDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def runout(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Runout

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def single_pitch_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SinglePitchDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_cumulative_pitch_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalCumulativePitchDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_helix_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalHelixDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_profile_deviation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalProfileDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ISO132811995AccuracyGrader._Cast_ISO132811995AccuracyGrader":
        return self._Cast_ISO132811995AccuracyGrader(self)
