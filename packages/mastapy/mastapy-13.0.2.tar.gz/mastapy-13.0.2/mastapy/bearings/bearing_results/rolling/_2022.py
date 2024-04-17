"""LoadedFourPointContactBallBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2026
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedFourPointContactBallBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2007, _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedFourPointContactBallBearingElement",)


Self = TypeVar("Self", bound="LoadedFourPointContactBallBearingElement")


class LoadedFourPointContactBallBearingElement(
    _2026.LoadedMultiPointContactBallBearingElement
):
    """LoadedFourPointContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedFourPointContactBallBearingElement"
    )

    class _Cast_LoadedFourPointContactBallBearingElement:
        """Special nested class for casting LoadedFourPointContactBallBearingElement to subclasses."""

        def __init__(
            self: "LoadedFourPointContactBallBearingElement._Cast_LoadedFourPointContactBallBearingElement",
            parent: "LoadedFourPointContactBallBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_multi_point_contact_ball_bearing_element(
            self: "LoadedFourPointContactBallBearingElement._Cast_LoadedFourPointContactBallBearingElement",
        ) -> "_2026.LoadedMultiPointContactBallBearingElement":
            return self._parent._cast(_2026.LoadedMultiPointContactBallBearingElement)

        @property
        def loaded_ball_bearing_element(
            self: "LoadedFourPointContactBallBearingElement._Cast_LoadedFourPointContactBallBearingElement",
        ) -> "_2007.LoadedBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(_2007.LoadedBallBearingElement)

        @property
        def loaded_element(
            self: "LoadedFourPointContactBallBearingElement._Cast_LoadedFourPointContactBallBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_four_point_contact_ball_bearing_element(
            self: "LoadedFourPointContactBallBearingElement._Cast_LoadedFourPointContactBallBearingElement",
        ) -> "LoadedFourPointContactBallBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedFourPointContactBallBearingElement._Cast_LoadedFourPointContactBallBearingElement",
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
        self: Self, instance_to_wrap: "LoadedFourPointContactBallBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def approximate_percentage_of_friction_used_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproximatePercentageOfFrictionUsedOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def approximate_percentage_of_friction_used_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproximatePercentageOfFrictionUsedOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureMomentOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureMomentOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_pressure_force_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicPressureForceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_pressure_force_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicPressureForceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicRollingResistanceForceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicRollingResistanceForceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_smearing_intensity_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumSmearingIntensityOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalLoadOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalLoadOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PivotingMomentOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PivotingMomentOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToElasticRollingResistanceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToElasticRollingResistanceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_outer_left(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_outer_right(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMajorAxisOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMajorAxisOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMinorAxisOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMinorAxisOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMajorAxisOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMajorAxisOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_outer_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMinorAxisOuterLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_outer_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMinorAxisOuterRight

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedFourPointContactBallBearingElement._Cast_LoadedFourPointContactBallBearingElement":
        return self._Cast_LoadedFourPointContactBallBearingElement(self)
