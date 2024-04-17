"""ISO132812013AccuracyGrader"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1149
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO132812013_ACCURACY_GRADER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances",
    "ISO132812013AccuracyGrader",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
        _1151,
        _1141,
        _1143,
        _1142,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ISO132812013AccuracyGrader",)


Self = TypeVar("Self", bound="ISO132812013AccuracyGrader")


class ISO132812013AccuracyGrader(_1149.ISO1328AccuracyGraderCommon):
    """ISO132812013AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _ISO132812013_ACCURACY_GRADER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO132812013AccuracyGrader")

    class _Cast_ISO132812013AccuracyGrader:
        """Special nested class for casting ISO132812013AccuracyGrader to subclasses."""

        def __init__(
            self: "ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader",
            parent: "ISO132812013AccuracyGrader",
        ):
            self._parent = parent

        @property
        def iso1328_accuracy_grader_common(
            self: "ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader",
        ) -> "_1149.ISO1328AccuracyGraderCommon":
            return self._parent._cast(_1149.ISO1328AccuracyGraderCommon)

        @property
        def cylindrical_accuracy_grader_with_profile_form_and_slope(
            self: "ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader",
        ) -> "_1143.CylindricalAccuracyGraderWithProfileFormAndSlope":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1143,
            )

            return self._parent._cast(
                _1143.CylindricalAccuracyGraderWithProfileFormAndSlope
            )

        @property
        def cylindrical_accuracy_grader(
            self: "ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader",
        ) -> "_1142.CylindricalAccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1142,
            )

            return self._parent._cast(_1142.CylindricalAccuracyGrader)

        @property
        def agmaiso13281b14_accuracy_grader(
            self: "ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader",
        ) -> "_1141.AGMAISO13281B14AccuracyGrader":
            from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
                _1141,
            )

            return self._parent._cast(_1141.AGMAISO13281B14AccuracyGrader)

        @property
        def iso132812013_accuracy_grader(
            self: "ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader",
        ) -> "ISO132812013AccuracyGrader":
            return self._parent

        def __getattr__(
            self: "ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO132812013AccuracyGrader.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_value_for_toothto_tooth_single_flank_composite_deviation(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DesignValueForToothtoToothSingleFlankCompositeDeviation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @design_value_for_toothto_tooth_single_flank_composite_deviation.setter
    @enforce_parameter_types
    def design_value_for_toothto_tooth_single_flank_composite_deviation(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DesignValueForToothtoToothSingleFlankCompositeDeviation = value

    @property
    def adjacent_pitch_difference_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjacentPitchDifferenceTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def sector_pitch_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SectorPitchTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def single_pitch_tolerance(self: Self) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SinglePitchTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def toothto_tooth_single_flank_composite_tolerance_maximum(
        self: Self,
    ) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothtoToothSingleFlankCompositeToleranceMaximum

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def toothto_tooth_single_flank_composite_tolerance_minimum(
        self: Self,
    ) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothtoToothSingleFlankCompositeToleranceMinimum

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_cumulative_pitch_index_tolerance(
        self: Self,
    ) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalCumulativePitchIndexTolerance

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
    def total_single_flank_composite_tolerance(
        self: Self,
    ) -> "_1151.OverridableTolerance":
        """mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances.OverridableTolerance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalSingleFlankCompositeTolerance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ISO132812013AccuracyGrader._Cast_ISO132812013AccuracyGrader":
        return self._Cast_ISO132812013AccuracyGrader(self)
