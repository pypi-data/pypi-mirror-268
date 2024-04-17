"""ISO10300MeshSingleFlankRatingMethodB1"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.iso_10300 import _425
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO10300_MESH_SINGLE_FLANK_RATING_METHOD_B1 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Iso10300", "ISO10300MeshSingleFlankRatingMethodB1"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _396
    from mastapy.gears.rating.conical import _549
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("ISO10300MeshSingleFlankRatingMethodB1",)


Self = TypeVar("Self", bound="ISO10300MeshSingleFlankRatingMethodB1")


class ISO10300MeshSingleFlankRatingMethodB1(
    _425.ISO10300MeshSingleFlankRating["_393.VirtualCylindricalGearISO10300MethodB1"]
):
    """ISO10300MeshSingleFlankRatingMethodB1

    This is a mastapy class.
    """

    TYPE = _ISO10300_MESH_SINGLE_FLANK_RATING_METHOD_B1
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ISO10300MeshSingleFlankRatingMethodB1"
    )

    class _Cast_ISO10300MeshSingleFlankRatingMethodB1:
        """Special nested class for casting ISO10300MeshSingleFlankRatingMethodB1 to subclasses."""

        def __init__(
            self: "ISO10300MeshSingleFlankRatingMethodB1._Cast_ISO10300MeshSingleFlankRatingMethodB1",
            parent: "ISO10300MeshSingleFlankRatingMethodB1",
        ):
            self._parent = parent

        @property
        def iso10300_mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingMethodB1._Cast_ISO10300MeshSingleFlankRatingMethodB1",
        ) -> "_425.ISO10300MeshSingleFlankRating":
            return self._parent._cast(_425.ISO10300MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingMethodB1._Cast_ISO10300MeshSingleFlankRatingMethodB1",
        ) -> "_549.ConicalMeshSingleFlankRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO10300MeshSingleFlankRatingMethodB1._Cast_ISO10300MeshSingleFlankRatingMethodB1",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(
            self: "ISO10300MeshSingleFlankRatingMethodB1._Cast_ISO10300MeshSingleFlankRatingMethodB1",
        ) -> "ISO10300MeshSingleFlankRatingMethodB1":
            return self._parent

        def __getattr__(
            self: "ISO10300MeshSingleFlankRatingMethodB1._Cast_ISO10300MeshSingleFlankRatingMethodB1",
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
        self: Self, instance_to_wrap: "ISO10300MeshSingleFlankRatingMethodB1.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def area_above_the_middle_contact_line_for_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaAboveTheMiddleContactLineForBending

        if temp is None:
            return 0.0

        return temp

    @property
    def area_above_the_middle_contact_line_for_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaAboveTheMiddleContactLineForContact

        if temp is None:
            return 0.0

        return temp

    @property
    def area_above_the_root_contact_line_for_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaAboveTheRootContactLineForBending

        if temp is None:
            return 0.0

        return temp

    @property
    def area_above_the_root_contact_line_for_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaAboveTheRootContactLineForContact

        if temp is None:
            return 0.0

        return temp

    @property
    def area_above_the_tip_contact_line_for_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaAboveTheTipContactLineForBending

        if temp is None:
            return 0.0

        return temp

    @property
    def area_above_the_tip_contact_line_for_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AreaAboveTheTipContactLineForContact

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_value_abs(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryValueABS

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_value_bbs(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryValueBBS

        if temp is None:
            return 0.0

        return temp

    @property
    def auxiliary_value_cbs(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AuxiliaryValueCBS

        if temp is None:
            return 0.0

        return temp

    @property
    def average_tooth_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageToothDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def bevel_gear_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def bevel_spiral_angle_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelSpiralAngleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor_for_bending_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioFactorForBendingMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_use_bevel_slip_factor_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressUseBevelSlipFactorMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def developed_length_of_one_tooth_as_the_face_width_of_the_calculation_model(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DevelopedLengthOfOneToothAsTheFaceWidthOfTheCalculationModel

        if temp is None:
            return 0.0

        return temp

    @property
    def hypoid_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def inclination_angle_of_the_sum_of_velocities_vector(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InclinationAngleOfTheSumOfVelocitiesVector

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_factor_pitting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactorPitting

        if temp is None:
            return 0.0

        return temp

    @property
    def mid_zone_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MidZoneFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_normal_force_of_virtual_cylindrical_gear_at_mean_point_p(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalNormalForceOfVirtualCylindricalGearAtMeanPointP

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_value_of_contact_stress_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalValueOfContactStressMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_value_of_contact_stress_using_bevel_slip_factor_method_b1(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalValueOfContactStressUsingBevelSlipFactorMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def part_of_the_models_face_width_covered_by_the_constance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartOfTheModelsFaceWidthCoveredByTheConstance

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_bevel_slip_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionBevelSlipFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def size_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SizeFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_mean_point_p(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityAtMeanPointP

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_parallel_to_the_contact_line(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityParallelToTheContactLine

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_velocities(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfVelocities

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_velocities_in_lengthwise_direction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfVelocitiesInLengthwiseDirection

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_velocities_in_profile_direction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfVelocitiesInProfileDirection

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_velocities_vertical_to_the_contact_line(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfVelocitiesVerticalToTheContactLine

        if temp is None:
            return 0.0

        return temp

    @property
    def the_ratio_of_maximum_load_over_the_middle_contact_line_and_total_load(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TheRatioOfMaximumLoadOverTheMiddleContactLineAndTotalLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_load_factors_for_bending_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorsForBendingMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_load_factors_for_contact_method_b1(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorsForContactMethodB1

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_bevel_slip_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelBevelSlipFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_cylindrical_gear_set_method_b1(
        self: Self,
    ) -> "_396.VirtualCylindricalGearSetISO10300MethodB1":
        """mastapy.gears.rating.virtual_cylindrical_gears.VirtualCylindricalGearSetISO10300MethodB1

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualCylindricalGearSetMethodB1

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ISO10300MeshSingleFlankRatingMethodB1._Cast_ISO10300MeshSingleFlankRatingMethodB1":
        return self._Cast_ISO10300MeshSingleFlankRatingMethodB1(self)
