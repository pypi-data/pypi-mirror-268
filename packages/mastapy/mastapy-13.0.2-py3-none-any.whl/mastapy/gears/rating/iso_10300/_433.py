"""ISO10300SingleFlankRatingBevelMethodB2"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.iso_10300 import _436
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_SINGLE_FLANK_RATING_BEVEL_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300SingleFlankRatingBevelMethodB2"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _432
    from mastapy.gears.rating.conical import _546
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300SingleFlankRatingBevelMethodB2",)


Self = TypeVar("Self", bound="ISO10300SingleFlankRatingBevelMethodB2")


class ISO10300SingleFlankRatingBevelMethodB2(_436.ISO10300SingleFlankRatingMethodB2):
    """ISO10300SingleFlankRatingBevelMethodB2

    This is a mastapy class.
    """

    TYPE = _ISO10300_SINGLE_FLANK_RATING_BEVEL_METHOD_B2
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISO10300SingleFlankRatingBevelMethodB2"
    )

    class _Cast_ISO10300SingleFlankRatingBevelMethodB2:
        """Special nested class for casting ISO10300SingleFlankRatingBevelMethodB2 to subclasses."""

        def __init__(
            self: "ISO10300SingleFlankRatingBevelMethodB2._Cast_ISO10300SingleFlankRatingBevelMethodB2",
            parent: "ISO10300SingleFlankRatingBevelMethodB2",
        ):
            self._parent = parent

        @property
        def iso10300_single_flank_rating_method_b2(
            self: "ISO10300SingleFlankRatingBevelMethodB2._Cast_ISO10300SingleFlankRatingBevelMethodB2",
        ) -> "_436.ISO10300SingleFlankRatingMethodB2":
            return self._parent._cast(_436.ISO10300SingleFlankRatingMethodB2)

        @property
        def iso10300_single_flank_rating(
            self: "ISO10300SingleFlankRatingBevelMethodB2._Cast_ISO10300SingleFlankRatingBevelMethodB2",
        ) -> "_432.ISO10300SingleFlankRating":
            pass

            from mastapy.gears.rating.iso_10300 import _432

            return self._parent._cast(_432.ISO10300SingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "ISO10300SingleFlankRatingBevelMethodB2._Cast_ISO10300SingleFlankRatingBevelMethodB2",
        ) -> "_546.ConicalGearSingleFlankRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO10300SingleFlankRatingBevelMethodB2._Cast_ISO10300SingleFlankRatingBevelMethodB2",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def iso10300_single_flank_rating_bevel_method_b2(
            self: "ISO10300SingleFlankRatingBevelMethodB2._Cast_ISO10300SingleFlankRatingBevelMethodB2",
        ) -> "ISO10300SingleFlankRatingBevelMethodB2":
            return self._parent

        def __getattr__(
            self: "ISO10300SingleFlankRatingBevelMethodB2._Cast_ISO10300SingleFlankRatingBevelMethodB2",
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
        self: Self, instance_to_wrap: "ISO10300SingleFlankRatingBevelMethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_tangent_of_root_fillet_at_weakest_point_and_centreline_of_tooth(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.AngleBetweenTangentOfRootFilletAtWeakestPointAndCentrelineOfTooth
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def assumed_angle_in_locating_weakest_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssumedAngleInLocatingWeakestSection

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_from_mean_section_to_point_of_load_application_for_spiral_bevel_pinions(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceFromMeanSectionToPointOfLoadApplicationForSpiralBevelPinions
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_from_mean_section_to_point_of_load_application_for_spiral_bevel_wheels(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceFromMeanSectionToPointOfLoadApplicationForSpiralBevelWheels
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_from_mean_section_to_point_of_load_application_for_straight_bevel_and_zerol_bevel_gear(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.DistanceFromMeanSectionToPointOfLoadApplicationForStraightBevelAndZerolBevelGear
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def initial_guess_gf_0(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InitialGuessGf0

        if temp is None:
            return 0.0

        return temp

    @property
    def iteration_balance_value_for_tooth_form_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IterationBalanceValueForToothFormFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_height_from_critical_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadHeightFromCriticalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_transverse_radius_to_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTransverseRadiusToPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle_at_point_of_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngleAtPointOfLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def one_half_of_angle_subtended_by_normal_circular_tooth_thickness_at_point_of_load_application(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.OneHalfOfAngleSubtendedByNormalCircularToothThicknessAtPointOfLoadApplication
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def one_half_tooth_thickness_at_critical_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OneHalfToothThicknessAtCriticalSection

        if temp is None:
            return 0.0

        return temp

    @property
    def point_of_load_application_on_path_of_action_for_maximum_root_stress_for_spiral_bevel_pinions(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PointOfLoadApplicationOnPathOfActionForMaximumRootStressForSpiralBevelPinions
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def point_of_load_application_on_path_of_action_for_maximum_root_stress_for_spiral_bevel_wheels(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PointOfLoadApplicationOnPathOfActionForMaximumRootStressForSpiralBevelWheels
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def point_of_load_application_on_path_of_action_for_maximum_root_stress_for_straight_bevel_and_zerol_bevel_gear(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.PointOfLoadApplicationOnPathOfActionForMaximumRootStressForStraightBevelAndZerolBevelGear
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_distance_from_pitch_circle_to_pinion_point_of_load_and_the_wheel_tooth_centreline(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.RelativeDistanceFromPitchCircleToPinionPointOfLoadAndTheWheelToothCentreline
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_form_factor_for_bevel_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothFormFactorForBevelGear

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_strength_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothStrengthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def g0(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.G0

        if temp is None:
            return 0.0

        return temp

    @property
    def gxb(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gxb

        if temp is None:
            return 0.0

        return temp

    @property
    def gyb(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gyb

        if temp is None:
            return 0.0

        return temp

    @property
    def gza(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gza

        if temp is None:
            return 0.0

        return temp

    @property
    def gzb(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gzb

        if temp is None:
            return 0.0

        return temp

    @property
    def alphah(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Alphah

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO10300SingleFlankRatingBevelMethodB2._Cast_ISO10300SingleFlankRatingBevelMethodB2":
        return self._Cast_ISO10300SingleFlankRatingBevelMethodB2(self)
