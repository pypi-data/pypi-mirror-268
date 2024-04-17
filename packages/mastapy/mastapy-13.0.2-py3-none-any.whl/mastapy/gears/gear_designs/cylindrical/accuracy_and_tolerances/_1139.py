"""AGMA20151A01AccuracyGrader"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1143
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA20151A01_ACCURACY_GRADER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "AGMA20151A01AccuracyGrader",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1151,
        _1142,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMA20151A01AccuracyGrader",)


Self = TypeVar("Self", bound="AGMA20151A01AccuracyGrader")


class AGMA20151A01AccuracyGrader(
    _1143.CylindricalAccuracyGraderWithProfileFormAndSlope
):
    """AGMA20151A01AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _AGMA20151A01_ACCURACY_GRADER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA20151A01AccuracyGrader")

    class _Cast_AGMA20151A01AccuracyGrader:
        """Special nested class for casting AGMA20151A01AccuracyGrader to subclasses."""

        def __init__(
            self: "AGMA20151A01AccuracyGrader._Cast_AGMA20151A01AccuracyGrader",
            parent: "AGMA20151A01AccuracyGrader",
        ):
            self._parent = parent

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(
            self: "AGMA20151A01AccuracyGrader._Cast_AGMA20151A01AccuracyGrader",
        ) -> "_1143.CylindricalAccuracyGraderWithProfileFormAndSlope":
            return self._parent._cast(
                _1143.CylindricalAccuracyGraderWithProfileFormAndSlope
            )

        @property
        def cylindrical_accuracy_grader(
            self: "AGMA20151A01AccuracyGrader._Cast_AGMA20151A01AccuracyGrader",
        ) -> "_1142.CylindricalAccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1142,
            )

            return self._parent._cast(_1142.CylindricalAccuracyGrader)

        @property
        def agma20151a01_accuracy_grader(
            self: "AGMA20151A01AccuracyGrader._Cast_AGMA20151A01AccuracyGrader",
        ) -> "AGMA20151A01AccuracyGrader":
            return self._parent

        def __getattr__(
            self: "AGMA20151A01AccuracyGrader._Cast_AGMA20151A01AccuracyGrader",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMA20151A01AccuracyGrader.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def helix_form_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixFormTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def helix_slope_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixSlopeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_form_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileFormTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_slope_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileSlopeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def runout_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunoutTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sector_pitch_deviation_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SectorPitchDeviationTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def single_flank_toothto_tooth_composite_tolerance(
        self: Self,
    ) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleFlankToothtoToothCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def single_flank_total_composite_tolerance(
        self: Self,
    ) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleFlankTotalCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def single_pitch_deviation_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SinglePitchDeviationTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def toothto_tooth_radial_composite_tolerance(
        self: Self,
    ) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothtoToothRadialCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_cumulative_pitch_deviation_tolerance(
        self: Self,
    ) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalCumulativePitchDeviationTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_helix_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalHelixTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_profile_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalProfileTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_radial_composite_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalRadialCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMA20151A01AccuracyGrader._Cast_AGMA20151A01AccuracyGrader":
        return self._Cast_AGMA20151A01AccuracyGrader(self)
