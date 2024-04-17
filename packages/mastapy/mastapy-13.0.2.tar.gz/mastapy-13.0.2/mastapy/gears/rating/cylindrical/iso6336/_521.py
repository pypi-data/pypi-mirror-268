"""ISO6336AbstractMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import _470
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO6336_ABSTRACT_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "ISO6336AbstractMeshSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical import _481
    from mastapy.gears.rating.cylindrical.iso6336 import _520, _515, _517, _519, _523
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493, _495, _497
    from mastapy.gears.rating.cylindrical.din3990 import _536
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("ISO6336AbstractMeshSingleFlankRating",)


Self = TypeVar("Self", bound="ISO6336AbstractMeshSingleFlankRating")


class ISO6336AbstractMeshSingleFlankRating(_470.CylindricalMeshSingleFlankRating):
    """ISO6336AbstractMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO6336_ABSTRACT_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO6336AbstractMeshSingleFlankRating")

    class _Cast_ISO6336AbstractMeshSingleFlankRating:
        """Special nested class for casting ISO6336AbstractMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
            parent: "ISO6336AbstractMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_470.CylindricalMeshSingleFlankRating":
            return self._parent._cast(_470.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_493.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493

            return self._parent._cast(
                _493.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
            )

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_495.PlasticGearVDI2736AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _495

            return self._parent._cast(
                _495.PlasticGearVDI2736AbstractMeshSingleFlankRating
            )

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_497.PlasticPlasticVDI2736MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _497

            return self._parent._cast(_497.PlasticPlasticVDI2736MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_515.ISO63361996MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _515

            return self._parent._cast(_515.ISO63361996MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_517.ISO63362006MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _517

            return self._parent._cast(_517.ISO63362006MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_519.ISO63362019MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _519

            return self._parent._cast(_519.ISO63362019MeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_523.ISO6336AbstractMetalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _523

            return self._parent._cast(_523.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "_536.DIN3990MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _536

            return self._parent._cast(_536.DIN3990MeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
        ) -> "ISO6336AbstractMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating",
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
        self: Self, instance_to_wrap: "ISO6336AbstractMeshSingleFlankRating.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def contact_ratio_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_ratio_factor_for_nominal_root_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioFactorForNominalRootRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_factor_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicFactorSource

        if temp is None:
            return ""

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
    def face_load_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadFactorBending

        if temp is None:
            return 0.0

        return temp

    @property
    def face_load_factor_contact_source(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadFactorContactSource

        if temp is None:
            return ""

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
    def helix_angle_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngleFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_coefficient_of_friction_calculated_constant_flash_temperature_method(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MeanCoefficientOfFrictionCalculatedConstantFlashTemperatureMethod
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_contact_pattern_enhancement(
        self: Self,
    ) -> "_481.MisalignmentContactPatternEnhancements":
        """mastapy.gears.rating.cylindrical.MisalignmentContactPatternEnhancements

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentContactPatternEnhancement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Cylindrical.MisalignmentContactPatternEnhancements",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.cylindrical._481",
            "MisalignmentContactPatternEnhancements",
        )(value)

    @property
    def nominal_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_end_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityAtEndOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_pitch_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityAtPitchPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_velocity_at_start_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityAtStartOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_tangential_velocities_at_end_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfTangentialVelocitiesAtEndOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_tangential_velocities_at_pitch_point(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfTangentialVelocitiesAtPitchPoint

        if temp is None:
            return 0.0

        return temp

    @property
    def sum_of_tangential_velocities_at_start_of_active_profile(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfTangentialVelocitiesAtStartOfActiveProfile

        if temp is None:
            return 0.0

        return temp

    @property
    def total_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_load_factor_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorBending

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
    def gear_single_flank_ratings(
        self: Self,
    ) -> "List[_520.ISO6336AbstractGearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ISO6336AbstractGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def isodin_cylindrical_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_520.ISO6336AbstractGearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ISO6336AbstractGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISODINCylindricalGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ISO6336AbstractMeshSingleFlankRating._Cast_ISO6336AbstractMeshSingleFlankRating":
        return self._Cast_ISO6336AbstractMeshSingleFlankRating(self)
