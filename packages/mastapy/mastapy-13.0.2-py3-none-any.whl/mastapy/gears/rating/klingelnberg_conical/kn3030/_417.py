"""KlingelnbergConicalMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating import _369
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030",
    "KlingelnbergConicalMeshSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import _390
    from mastapy.gears.rating.klingelnberg_conical.kn3030 import _421, _422


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalMeshSingleFlankRating",)


Self = TypeVar("Self", bound="KlingelnbergConicalMeshSingleFlankRating")


class KlingelnbergConicalMeshSingleFlankRating(_369.MeshSingleFlankRating):
    """KlingelnbergConicalMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergConicalMeshSingleFlankRating"
    )

    class _Cast_KlingelnbergConicalMeshSingleFlankRating:
        """Special nested class for casting KlingelnbergConicalMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "KlingelnbergConicalMeshSingleFlankRating._Cast_KlingelnbergConicalMeshSingleFlankRating",
            parent: "KlingelnbergConicalMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def mesh_single_flank_rating(
            self: "KlingelnbergConicalMeshSingleFlankRating._Cast_KlingelnbergConicalMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_mesh_single_flank_rating(
            self: "KlingelnbergConicalMeshSingleFlankRating._Cast_KlingelnbergConicalMeshSingleFlankRating",
        ) -> "_421.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _421

            return self._parent._cast(
                _421.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_mesh_single_flank_rating(
            self: "KlingelnbergConicalMeshSingleFlankRating._Cast_KlingelnbergConicalMeshSingleFlankRating",
        ) -> "_422.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _422

            return self._parent._cast(
                _422.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating
            )

        @property
        def klingelnberg_conical_mesh_single_flank_rating(
            self: "KlingelnbergConicalMeshSingleFlankRating._Cast_KlingelnbergConicalMeshSingleFlankRating",
        ) -> "KlingelnbergConicalMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "KlingelnbergConicalMeshSingleFlankRating._Cast_KlingelnbergConicalMeshSingleFlankRating",
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
        self: Self, instance_to_wrap: "KlingelnbergConicalMeshSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_integral_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActualIntegralTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress_number(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStressNumber

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_scuffing_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableScuffingTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def alternating_load_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AlternatingLoadFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def application_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def bevel_gear_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def bevel_gear_factor_pitting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearFactorPitting

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor_pitting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioFactorPitting

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_stress_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_viscosity_at_sump_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicViscosityAtSumpTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def elasticity_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticityFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def helical_load_distribution_factor_scuffing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelicalLoadDistributionFactorScuffing

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_angle_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_angle_factor_pitting(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleFactorPitting

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_longitudinal(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadDistributionFactorLongitudinal

        if temp is None:
            return 0.0

        return temp

    @property
    def lubrication_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def lubrication_speed_ampersand_roughness_factor_product(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LubricationSpeedAmpersandRoughnessFactorProduct

        if temp is None:
            return 0.0

        return temp

    @property
    def material_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def meshing_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def operating_oil_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingOilTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_torque_of_test_gear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionTorqueOfTestGear

        if temp is None:
            return 0.0

        return temp

    @property
    def rated_tangential_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatedTangentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def relating_factor_for_the_mass_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelatingFactorForTheMassTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def roughness_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughnessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def running_in_allowance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RunningInAllowance

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_scuffing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForScuffing

        if temp is None:
            return 0.0

        return temp

    @property
    def single_meshing_factor_pinion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleMeshingFactorPinion

        if temp is None:
            return 0.0

        return temp

    @property
    def single_meshing_factor_wheel(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleMeshingFactorWheel

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
    def specific_line_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificLineLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_correction_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressCorrectionFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def sump_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumpTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_relief_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def zone_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZoneFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_cylindrical_gear_set(
        self: Self,
    ) -> "_390.KlingelnbergVirtualCylindricalGearSet":
        """mastapy.gears.rating.virtual_cylindrical_gears.KlingelnbergVirtualCylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualCylindricalGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergConicalMeshSingleFlankRating._Cast_KlingelnbergConicalMeshSingleFlankRating":
        return self._Cast_KlingelnbergConicalMeshSingleFlankRating(self)
