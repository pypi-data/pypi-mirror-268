"""BevelGearISOMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.materials import _590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_ISO_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "BevelGearISOMaterial"
)

if TYPE_CHECKING:
    from mastapy.materials import _281, _272
    from mastapy.gears.materials import _597
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearISOMaterial",)


Self = TypeVar("Self", bound="BevelGearISOMaterial")


class BevelGearISOMaterial(_590.BevelGearMaterial):
    """BevelGearISOMaterial

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_ISO_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearISOMaterial")

    class _Cast_BevelGearISOMaterial:
        """Special nested class for casting BevelGearISOMaterial to subclasses."""

        def __init__(
            self: "BevelGearISOMaterial._Cast_BevelGearISOMaterial",
            parent: "BevelGearISOMaterial",
        ):
            self._parent = parent

        @property
        def bevel_gear_material(
            self: "BevelGearISOMaterial._Cast_BevelGearISOMaterial",
        ) -> "_590.BevelGearMaterial":
            return self._parent._cast(_590.BevelGearMaterial)

        @property
        def gear_material(
            self: "BevelGearISOMaterial._Cast_BevelGearISOMaterial",
        ) -> "_597.GearMaterial":
            from mastapy.gears.materials import _597

            return self._parent._cast(_597.GearMaterial)

        @property
        def material(
            self: "BevelGearISOMaterial._Cast_BevelGearISOMaterial",
        ) -> "_272.Material":
            from mastapy.materials import _272

            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "BevelGearISOMaterial._Cast_BevelGearISOMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def bevel_gear_iso_material(
            self: "BevelGearISOMaterial._Cast_BevelGearISOMaterial",
        ) -> "BevelGearISOMaterial":
            return self._parent

        def __getattr__(
            self: "BevelGearISOMaterial._Cast_BevelGearISOMaterial", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearISOMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AllowableBendingStress

        if temp is None:
            return 0.0

        return temp

    @allowable_bending_stress.setter
    @enforce_parameter_types
    def allowable_bending_stress(self: Self, value: "float"):
        self.wrapped.AllowableBendingStress = float(value) if value is not None else 0.0

    @property
    def allowable_contact_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AllowableContactStress

        if temp is None:
            return 0.0

        return temp

    @allowable_contact_stress.setter
    @enforce_parameter_types
    def allowable_contact_stress(self: Self, value: "float"):
        self.wrapped.AllowableContactStress = float(value) if value is not None else 0.0

    @property
    def iso_material_type(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.ISOMaterialType

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @iso_material_type.setter
    @enforce_parameter_types
    def iso_material_type(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.ISOMaterialType = value

    @property
    def limited_pitting_allowed(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LimitedPittingAllowed

        if temp is None:
            return False

        return temp

    @limited_pitting_allowed.setter
    @enforce_parameter_types
    def limited_pitting_allowed(self: Self, value: "bool"):
        self.wrapped.LimitedPittingAllowed = bool(value) if value is not None else False

    @property
    def long_life_life_factor_bending(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LongLifeLifeFactorBending

        if temp is None:
            return 0.0

        return temp

    @long_life_life_factor_bending.setter
    @enforce_parameter_types
    def long_life_life_factor_bending(self: Self, value: "float"):
        self.wrapped.LongLifeLifeFactorBending = (
            float(value) if value is not None else 0.0
        )

    @property
    def long_life_life_factor_contact(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LongLifeLifeFactorContact

        if temp is None:
            return 0.0

        return temp

    @long_life_life_factor_contact.setter
    @enforce_parameter_types
    def long_life_life_factor_contact(self: Self, value: "float"):
        self.wrapped.LongLifeLifeFactorContact = (
            float(value) if value is not None else 0.0
        )

    @property
    def material_has_a_well_defined_yield_point(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.MaterialHasAWellDefinedYieldPoint

        if temp is None:
            return False

        return temp

    @material_has_a_well_defined_yield_point.setter
    @enforce_parameter_types
    def material_has_a_well_defined_yield_point(self: Self, value: "bool"):
        self.wrapped.MaterialHasAWellDefinedYieldPoint = (
            bool(value) if value is not None else False
        )

    @property
    def n0_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.N0Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def n0_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.N0Contact

        if temp is None:
            return 0.0

        return temp

    @property
    def proof_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ProofStress

        if temp is None:
            return 0.0

        return temp

    @proof_stress.setter
    @enforce_parameter_types
    def proof_stress(self: Self, value: "float"):
        self.wrapped.ProofStress = float(value) if value is not None else 0.0

    @property
    def quality_grade(self: Self) -> "_281.QualityGrade":
        """mastapy.materials.QualityGrade"""
        temp = self.wrapped.QualityGrade

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Materials.QualityGrade")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.materials._281", "QualityGrade")(
            value
        )

    @quality_grade.setter
    @enforce_parameter_types
    def quality_grade(self: Self, value: "_281.QualityGrade"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Materials.QualityGrade")
        self.wrapped.QualityGrade = value

    @property
    def specify_allowable_stress_numbers(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyAllowableStressNumbers

        if temp is None:
            return False

        return temp

    @specify_allowable_stress_numbers.setter
    @enforce_parameter_types
    def specify_allowable_stress_numbers(self: Self, value: "bool"):
        self.wrapped.SpecifyAllowableStressNumbers = (
            bool(value) if value is not None else False
        )

    @property
    def use_iso633652003_material_definitions(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UseISO633652003MaterialDefinitions

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self: Self) -> "BevelGearISOMaterial._Cast_BevelGearISOMaterial":
        return self._Cast_BevelGearISOMaterial(self)
