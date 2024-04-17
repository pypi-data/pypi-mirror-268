"""PlasticGearVDI2736AbstractMeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical.iso6336 import _521
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_GEAR_VDI2736_ABSTRACT_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "PlasticGearVDI2736AbstractMeshSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1093
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _494, _493, _497
    from mastapy.gears.rating.cylindrical import _470
    from mastapy.gears.rating import _369


__docformat__ = "restructuredtext en"
__all__ = ("PlasticGearVDI2736AbstractMeshSingleFlankRating",)


Self = TypeVar("Self", bound="PlasticGearVDI2736AbstractMeshSingleFlankRating")


class PlasticGearVDI2736AbstractMeshSingleFlankRating(
    _521.ISO6336AbstractMeshSingleFlankRating
):
    """PlasticGearVDI2736AbstractMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _PLASTIC_GEAR_VDI2736_ABSTRACT_MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating"
    )

    class _Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating:
        """Special nested class for casting PlasticGearVDI2736AbstractMeshSingleFlankRating to subclasses."""

        def __init__(
            self: "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating",
            parent: "PlasticGearVDI2736AbstractMeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating",
        ) -> "_521.ISO6336AbstractMeshSingleFlankRating":
            return self._parent._cast(_521.ISO6336AbstractMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating",
        ) -> "_470.CylindricalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _470

            return self._parent._cast(_470.CylindricalMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating",
        ) -> "_369.MeshSingleFlankRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.MeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(
            self: "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating",
        ) -> "_493.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _493

            return self._parent._cast(
                _493.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
            )

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(
            self: "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating",
        ) -> "_497.PlasticPlasticVDI2736MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _497

            return self._parent._cast(_497.PlasticPlasticVDI2736MeshSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(
            self: "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating",
        ) -> "PlasticGearVDI2736AbstractMeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating",
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
        self: Self,
        instance_to_wrap: "PlasticGearVDI2736AbstractMeshSingleFlankRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def air_temperature_ambient_and_assembly(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AirTemperatureAmbientAndAssembly

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_of_friction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def degree_of_tooth_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DegreeOfToothLoss

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
    def face_load_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceLoadFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def factor_for_tooth_flank_loading(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FactorForToothFlankLoading

        if temp is None:
            return 0.0

        return temp

    @property
    def factor_for_tooth_root_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FactorForToothRootLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def heat_dissipating_surface_of_housing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeatDissipatingSurfaceOfHousing

        if temp is None:
            return 0.0

        return temp

    @property
    def heat_transfer_resistance_of_housing(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeatTransferResistanceOfHousing

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
    def percentage_of_openings_in_the_housing_surface(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageOfOpeningsInTheHousingSurface

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
    def relative_tooth_engagement_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeToothEngagementTime

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
    def transverse_load_factor_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseLoadFactorContact

        if temp is None:
            return 0.0

        return temp

    @property
    def type_of_mechanism_housing(self: Self) -> "_1093.TypeOfMechanismHousing":
        """mastapy.gears.gear_designs.cylindrical.TypeOfMechanismHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TypeOfMechanismHousing

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TypeOfMechanismHousing"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1093", "TypeOfMechanismHousing"
        )(value)

    @property
    def wear_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WearCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def isodin_cylindrical_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_494.PlasticGearVDI2736AbstractGearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.plastic_vdi2736.PlasticGearVDI2736AbstractGearSingleFlankRating]

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
    def plastic_vdi2736_cylindrical_gear_single_flank_ratings(
        self: Self,
    ) -> "List[_494.PlasticGearVDI2736AbstractGearSingleFlankRating]":
        """List[mastapy.gears.rating.cylindrical.plastic_vdi2736.PlasticGearVDI2736AbstractGearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlasticVDI2736CylindricalGearSingleFlankRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlasticGearVDI2736AbstractMeshSingleFlankRating._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating":
        return self._Cast_PlasticGearVDI2736AbstractMeshSingleFlankRating(self)
