"""ISO10300SingleFlankRatingMethodB2"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.rating.iso_10300 import _432
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_SINGLE_FLANK_RATING_METHOD_B2 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300SingleFlankRatingMethodB2"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.iso_10300 import _433, _434
    from mastapy.gears.rating.conical import _546
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300SingleFlankRatingMethodB2",)


Self = TypeVar("Self", bound="ISO10300SingleFlankRatingMethodB2")


class ISO10300SingleFlankRatingMethodB2(
    _432.ISO10300SingleFlankRating["_394.VirtualCylindricalGearISO10300MethodB2"]
):
    """ISO10300SingleFlankRatingMethodB2

    This is a mastapy class.
    """

    TYPE = _ISO10300_SINGLE_FLANK_RATING_METHOD_B2
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO10300SingleFlankRatingMethodB2")

    class _Cast_ISO10300SingleFlankRatingMethodB2:
        """Special nested class for casting ISO10300SingleFlankRatingMethodB2 to subclasses."""

        def __init__(
            self: "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2",
            parent: "ISO10300SingleFlankRatingMethodB2",
        ):
            self._parent = parent

        @property
        def iso10300_single_flank_rating(
            self: "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2",
        ) -> "_432.ISO10300SingleFlankRating":
            return self._parent._cast(_432.ISO10300SingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2",
        ) -> "_546.ConicalGearSingleFlankRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def iso10300_single_flank_rating_bevel_method_b2(
            self: "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2",
        ) -> "_433.ISO10300SingleFlankRatingBevelMethodB2":
            from mastapy.gears.rating.iso_10300 import _433

            return self._parent._cast(_433.ISO10300SingleFlankRatingBevelMethodB2)

        @property
        def iso10300_single_flank_rating_hypoid_method_b2(
            self: "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2",
        ) -> "_434.ISO10300SingleFlankRatingHypoidMethodB2":
            from mastapy.gears.rating.iso_10300 import _434

            return self._parent._cast(_434.ISO10300SingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_single_flank_rating_method_b2(
            self: "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2",
        ) -> "ISO10300SingleFlankRatingMethodB2":
            return self._parent

        def __getattr__(
            self: "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2",
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
        self: Self, instance_to_wrap: "ISO10300SingleFlankRatingMethodB2.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def combined_geometry_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CombinedGeometryFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_adjustment_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressAdjustmentFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cos_pressure_angle_at_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CosPressureAngleAtPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def effective_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def heel_increment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeelIncrement

        if temp is None:
            return 0.0

        return temp

    @property
    def heel_increment_delta_be(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeelIncrementDeltaBe

        if temp is None:
            return 0.0

        return temp

    @property
    def inertia_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InertiaFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def L(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.L

        if temp is None:
            return 0.0

        return temp

    @property
    def m(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.M

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_value_of_root_stress_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalValueOfRootStressMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def o(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.O

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContactStressMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_root_stress_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleToothRootStressMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def pressure_angle_at_point_of_load_application(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureAngleAtPointOfLoadApplication

        if temp is None:
            return 0.0

        return temp

    @property
    def projected_length_of_the_instantaneous_contact_line_in_the_tooth_lengthwise_direction(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.ProjectedLengthOfTheInstantaneousContactLineInTheToothLengthwiseDirection
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def radius_of_curvature_difference_between_point_of_load_and_mean_point(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusOfCurvatureDifferenceBetweenPointOfLoadAndMeanPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_fillet_radius_at_root_of_tooth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeFilletRadiusAtRootOfTooth

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_notch_sensitivity_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeNotchSensitivityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_surface_condition_factor_for_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeSurfaceConditionFactorForMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def root_stress_adjustment_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootStressAdjustmentFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_bending_for_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorBendingForMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_contact_for_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorContactForMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_concentration_and_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressConcentrationAndCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def toe_increment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToeIncrement

        if temp is None:
            return 0.0

        return temp

    @property
    def toe_increment_delta_bi(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToeIncrementDeltaBi

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_root_stress_method_b2(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressMethodB2

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ISO10300SingleFlankRatingMethodB2._Cast_ISO10300SingleFlankRatingMethodB2":
        return self._Cast_ISO10300SingleFlankRatingMethodB2(self)
