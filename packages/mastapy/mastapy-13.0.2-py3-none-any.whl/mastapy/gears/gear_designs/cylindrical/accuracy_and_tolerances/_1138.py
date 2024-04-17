"""AGMA2000A88AccuracyGrader"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1142
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA2000A88_ACCURACY_GRADER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "AGMA2000A88AccuracyGrader",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1151


__docformat__ = "restructuredtext en"
__all__ = ("AGMA2000A88AccuracyGrader",)


Self = TypeVar("Self", bound="AGMA2000A88AccuracyGrader")


class AGMA2000A88AccuracyGrader(_1142.CylindricalAccuracyGrader):
    """AGMA2000A88AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _AGMA2000A88_ACCURACY_GRADER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMA2000A88AccuracyGrader")

    class _Cast_AGMA2000A88AccuracyGrader:
        """Special nested class for casting AGMA2000A88AccuracyGrader to subclasses."""

        def __init__(
            self: "AGMA2000A88AccuracyGrader._Cast_AGMA2000A88AccuracyGrader",
            parent: "AGMA2000A88AccuracyGrader",
        ):
            self._parent = parent

        @property
        def cylindrical_accuracy_grader(
            self: "AGMA2000A88AccuracyGrader._Cast_AGMA2000A88AccuracyGrader",
        ) -> "_1142.CylindricalAccuracyGrader":
            return self._parent._cast(_1142.CylindricalAccuracyGrader)

        @property
        def agma2000a88_accuracy_grader(
            self: "AGMA2000A88AccuracyGrader._Cast_AGMA2000A88AccuracyGrader",
        ) -> "AGMA2000A88AccuracyGrader":
            return self._parent

        def __getattr__(
            self: "AGMA2000A88AccuracyGrader._Cast_AGMA2000A88AccuracyGrader", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMA2000A88AccuracyGrader.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_number_of_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedNumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_pitch_variation(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowablePitchVariation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def profile_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def radial_runout_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialRunoutTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def tooth_alignment_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothAlignmentTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def toothto_tooth_composite_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothtoToothCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_composite_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMA2000A88AccuracyGrader._Cast_AGMA2000A88AccuracyGrader":
        return self._Cast_AGMA2000A88AccuracyGrader(self)
