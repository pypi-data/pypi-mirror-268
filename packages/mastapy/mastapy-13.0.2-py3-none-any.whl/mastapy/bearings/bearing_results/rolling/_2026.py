"""LoadedMultiPointContactBallBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2007
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_MULTI_POINT_CONTACT_BALL_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedMultiPointContactBallBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2022, _2057, _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedMultiPointContactBallBearingElement",)


Self = TypeVar("Self", bound="LoadedMultiPointContactBallBearingElement")


class LoadedMultiPointContactBallBearingElement(_2007.LoadedBallBearingElement):
    """LoadedMultiPointContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_MULTI_POINT_CONTACT_BALL_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedMultiPointContactBallBearingElement"
    )

    class _Cast_LoadedMultiPointContactBallBearingElement:
        """Special nested class for casting LoadedMultiPointContactBallBearingElement to subclasses."""

        def __init__(
            self: "LoadedMultiPointContactBallBearingElement._Cast_LoadedMultiPointContactBallBearingElement",
            parent: "LoadedMultiPointContactBallBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_ball_bearing_element(
            self: "LoadedMultiPointContactBallBearingElement._Cast_LoadedMultiPointContactBallBearingElement",
        ) -> "_2007.LoadedBallBearingElement":
            return self._parent._cast(_2007.LoadedBallBearingElement)

        @property
        def loaded_element(
            self: "LoadedMultiPointContactBallBearingElement._Cast_LoadedMultiPointContactBallBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_four_point_contact_ball_bearing_element(
            self: "LoadedMultiPointContactBallBearingElement._Cast_LoadedMultiPointContactBallBearingElement",
        ) -> "_2022.LoadedFourPointContactBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2022

            return self._parent._cast(_2022.LoadedFourPointContactBallBearingElement)

        @property
        def loaded_three_point_contact_ball_bearing_element(
            self: "LoadedMultiPointContactBallBearingElement._Cast_LoadedMultiPointContactBallBearingElement",
        ) -> "_2057.LoadedThreePointContactBallBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2057

            return self._parent._cast(_2057.LoadedThreePointContactBallBearingElement)

        @property
        def loaded_multi_point_contact_ball_bearing_element(
            self: "LoadedMultiPointContactBallBearingElement._Cast_LoadedMultiPointContactBallBearingElement",
        ) -> "LoadedMultiPointContactBallBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedMultiPointContactBallBearingElement._Cast_LoadedMultiPointContactBallBearingElement",
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
        self: Self, instance_to_wrap: "LoadedMultiPointContactBallBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def approximate_percentage_of_friction_used_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproximatePercentageOfFrictionUsedInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def approximate_percentage_of_friction_used_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApproximatePercentageOfFrictionUsedInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_angle_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactAngleInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureMomentInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def curvature_moment_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurvatureMomentInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_major_dimension_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMajorDimensionInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_semi_minor_dimension_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HertzianSemiMinorDimensionInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_pressure_force_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicPressureForceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_pressure_force_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicPressureForceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicRollingResistanceForceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def hydrodynamic_rolling_resistance_force_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HydrodynamicRollingResistanceForceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumShearStressInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_smearing_intensity_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumSmearingIntensityInner

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_lubricating_film_thickness_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLubricatingFilmThicknessInner

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalLoadInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_load_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalLoadInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PivotingMomentInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def pivoting_moment_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PivotingMomentInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToElasticRollingResistanceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_elastic_rolling_resistance_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToElasticRollingResistanceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_inner_left(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_due_to_hydrodynamic_rolling_resistance_inner_right(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossDueToHydrodynamicRollingResistanceInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMajorAxisInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_major_axis_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMajorAxisInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMinorAxisInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_parallel_to_minor_axis_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossParallelToMinorAxisInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMajorAxisInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMajorAxisInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_inner_left(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMinorAxisInnerLeft

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_inner_right(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingForceParallelToTheMinorAxisInnerRight

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedMultiPointContactBallBearingElement._Cast_LoadedMultiPointContactBallBearingElement":
        return self._Cast_LoadedMultiPointContactBallBearingElement(self)
