"""CylindricalGearMeshRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import _363
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalGearMeshRating"
)

if TYPE_CHECKING:
    from mastapy.gears import _326, _344
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.rating.cylindrical.agma import _538
    from mastapy.gears.gear_designs.cylindrical import _1022
    from mastapy.gears.rating.cylindrical import _470, _467, _463
    from mastapy.gears.rating.cylindrical.iso6336 import _523
    from mastapy.gears.load_case.cylindrical import _887
    from mastapy.gears.rating.cylindrical.vdi import _492
    from mastapy.gears.rating import _356
    from mastapy.gears.analysis import _1222


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshRating",)


Self = TypeVar("Self", bound="CylindricalGearMeshRating")


class CylindricalGearMeshRating(_363.GearMeshRating):
    """CylindricalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshRating")

    class _Cast_CylindricalGearMeshRating:
        """Special nested class for casting CylindricalGearMeshRating to subclasses."""

        def __init__(
            self: "CylindricalGearMeshRating._Cast_CylindricalGearMeshRating",
            parent: "CylindricalGearMeshRating",
        ):
            self._parent = parent

        @property
        def gear_mesh_rating(
            self: "CylindricalGearMeshRating._Cast_CylindricalGearMeshRating",
        ) -> "_363.GearMeshRating":
            return self._parent._cast(_363.GearMeshRating)

        @property
        def abstract_gear_mesh_rating(
            self: "CylindricalGearMeshRating._Cast_CylindricalGearMeshRating",
        ) -> "_356.AbstractGearMeshRating":
            from mastapy.gears.rating import _356

            return self._parent._cast(_356.AbstractGearMeshRating)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalGearMeshRating._Cast_CylindricalGearMeshRating",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_rating(
            self: "CylindricalGearMeshRating._Cast_CylindricalGearMeshRating",
        ) -> "CylindricalGearMeshRating":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshRating._Cast_CylindricalGearMeshRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMeshRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self: Self) -> "_326.CylindricalFlanks":
        """mastapy.gears.CylindricalFlanks

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.CylindricalFlanks")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._326", "CylindricalFlanks")(
            value
        )

    @property
    def load_intensity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadIntensity

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def load_sharing_factor_source(
        self: Self,
    ) -> "_344.PlanetaryRatingLoadSharingOption":
        """mastapy.gears.PlanetaryRatingLoadSharingOption

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingFactorSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.PlanetaryRatingLoadSharingOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._344", "PlanetaryRatingLoadSharingOption"
        )(value)

    @property
    def mechanical_advantage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MechanicalAdvantage

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_benedict_and_kelley(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionBenedictAndKelley

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_drozdov_and_gavrikov(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionDrozdovAndGavrikov

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotc60(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionISOTC60

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417912001(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417912001

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417912001_with_surface_roughness_parameter(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MeshCoefficientOfFrictionISOTR1417912001WithSurfaceRoughnessParameter
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417922001_martins_et_al(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417922001MartinsEtAl

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_isotr1417922001(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionISOTR1417922001

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_misharin(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionMisharin

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_o_donoghue_and_cameron(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionODonoghueAndCameron

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_coefficient_of_friction_at_diameter_benedict_and_kelley(
        self: Self,
    ) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshCoefficientOfFrictionAtDiameterBenedictAndKelley

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sliding_ratio_at_end_of_recess(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingRatioAtEndOfRecess

        if temp is None:
            return 0.0

        return temp

    @property
    def sliding_ratio_at_start_of_approach(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingRatioAtStartOfApproach

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_loss_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothLossFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def agma_cylindrical_mesh_single_flank_rating(
        self: Self,
    ) -> "_538.AGMA2101MeshSingleFlankRating":
        """mastapy.gears.rating.cylindrical.agma.AGMA2101MeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMACylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_mesh(self: Self) -> "_1022.CylindricalGearMeshDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_mesh_single_flank_rating(
        self: Self,
    ) -> "_470.CylindricalMeshSingleFlankRating":
        """mastapy.gears.rating.cylindrical.CylindricalMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_rating(self: Self) -> "_467.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def isodin_cylindrical_mesh_single_flank_rating(
        self: Self,
    ) -> "_523.ISO6336AbstractMetalMeshSingleFlankRating":
        """mastapy.gears.rating.cylindrical.iso6336.ISO6336AbstractMetalMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISODINCylindricalMeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_load_case(self: Self) -> "_887.CylindricalMeshLoadCase":
        """mastapy.gears.load_case.cylindrical.CylindricalMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_single_flank_rating(self: Self) -> "_470.CylindricalMeshSingleFlankRating":
        """mastapy.gears.rating.cylindrical.CylindricalMeshSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def vdi_cylindrical_gear_single_flank_rating(
        self: Self,
    ) -> "_492.VDI2737InternalGearSingleFlankRating":
        """mastapy.gears.rating.cylindrical.vdi.VDI2737InternalGearSingleFlankRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VDICylindricalGearSingleFlankRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_ratings(self: Self) -> "List[_463.CylindricalGearRating]":
        """List[mastapy.gears.rating.cylindrical.CylindricalGearRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshRating._Cast_CylindricalGearMeshRating":
        return self._Cast_CylindricalGearMeshRating(self)
