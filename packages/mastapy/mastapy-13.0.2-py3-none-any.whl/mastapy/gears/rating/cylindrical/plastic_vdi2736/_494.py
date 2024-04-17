"""PlasticGearVDI2736AbstractGearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.cylindrical.iso6336 import _520
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_GEAR_VDI2736_ABSTRACT_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736",
    "PlasticGearVDI2736AbstractGearSingleFlankRating",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _498, _499, _500
    from mastapy.materials import _288, _289
    from mastapy.gears.rating.cylindrical import _468
    from mastapy.gears.rating import _367


__docformat__ = "restructuredtext en"
__all__ = ("PlasticGearVDI2736AbstractGearSingleFlankRating",)


Self = TypeVar("Self", bound="PlasticGearVDI2736AbstractGearSingleFlankRating")


class PlasticGearVDI2736AbstractGearSingleFlankRating(
    _520.ISO6336AbstractGearSingleFlankRating
):
    """PlasticGearVDI2736AbstractGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _PLASTIC_GEAR_VDI2736_ABSTRACT_GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlasticGearVDI2736AbstractGearSingleFlankRating"
    )

    class _Cast_PlasticGearVDI2736AbstractGearSingleFlankRating:
        """Special nested class for casting PlasticGearVDI2736AbstractGearSingleFlankRating to subclasses."""

        def __init__(
            self: "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating",
            parent: "PlasticGearVDI2736AbstractGearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating",
        ) -> "_520.ISO6336AbstractGearSingleFlankRating":
            return self._parent._cast(_520.ISO6336AbstractGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(
            self: "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating",
        ) -> "_468.CylindricalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _468

            return self._parent._cast(_468.CylindricalGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating",
        ) -> "_367.GearSingleFlankRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearSingleFlankRating)

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(
            self: "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating",
        ) -> (
            "_499.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh"
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _499

            return self._parent._cast(
                _499.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh
            )

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(
            self: "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating",
        ) -> "_500.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _500

            return self._parent._cast(
                _500.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
            )

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(
            self: "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating",
        ) -> "PlasticGearVDI2736AbstractGearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating",
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
        instance_to_wrap: "PlasticGearVDI2736AbstractGearSingleFlankRating.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressNumberBending

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_stress_number_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableStressNumberContact

        if temp is None:
            return 0.0

        return temp

    @property
    def averaged_linear_wear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AveragedLinearWear

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_heat_transfer_coefficient(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankHeatTransferCoefficient

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def flank_temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FlankTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @flank_temperature.setter
    @enforce_parameter_types
    def flank_temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FlankTemperature = value

    @property
    def important_note_on_contact_durability_of_pom(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImportantNoteOnContactDurabilityOfPOM

        if temp is None:
            return ""

        return temp

    @property
    def minimum_factor_of_safety_bending_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFactorOfSafetyBendingFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_factor_of_safety_pitting_fatigue(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFactorOfSafetyPittingFatigue

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_factor_of_safety_wear(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFactorOfSafetyWear

        if temp is None:
            return 0.0

        return temp

    @property
    def nominal_tooth_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalToothRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_tooth_root_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleToothRootBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def pitting_stress_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PittingStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_line_length_of_the_active_tooth_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileLineLengthOfTheActiveToothFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def root_heat_transfer_coefficient(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootHeatTransferCoefficient

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def root_temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RootTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @root_temperature.setter
    @enforce_parameter_types
    def root_temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RootTemperature = value

    @property
    def tooth_root_stress_limit(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothRootStressLimit

        if temp is None:
            return 0.0

        return temp

    @property
    def standard_plastic_sn_curve_for_the_specified_operating_conditions(
        self: Self,
    ) -> "_498.PlasticSNCurveForTheSpecifiedOperatingConditions":
        """mastapy.gears.rating.cylindrical.plastic_vdi2736.PlasticSNCurveForTheSpecifiedOperatingConditions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StandardPlasticSNCurveForTheSpecifiedOperatingConditions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bending_stress_cycle_data_for_damage_tables(
        self: Self,
    ) -> "List[_288.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]":
        """List[mastapy.materials.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStressCycleDataForDamageTables

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def contact_stress_cycle_data_for_damage_tables(
        self: Self,
    ) -> "List[_289.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]":
        """List[mastapy.materials.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactStressCycleDataForDamageTables

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlasticGearVDI2736AbstractGearSingleFlankRating._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating":
        return self._Cast_PlasticGearVDI2736AbstractGearSingleFlankRating(self)
