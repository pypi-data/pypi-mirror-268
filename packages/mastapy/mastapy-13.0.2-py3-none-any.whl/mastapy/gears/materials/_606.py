"""PlasticCylindricalGearMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.materials import _594
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLASTIC_CYLINDRICAL_GEAR_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "PlasticCylindricalGearMaterial"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _597
    from mastapy.materials import _272
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("PlasticCylindricalGearMaterial",)


Self = TypeVar("Self", bound="PlasticCylindricalGearMaterial")


class PlasticCylindricalGearMaterial(_594.CylindricalGearMaterial):
    """PlasticCylindricalGearMaterial

    This is a mastapy class.
    """

    TYPE = _PLASTIC_CYLINDRICAL_GEAR_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlasticCylindricalGearMaterial")

    class _Cast_PlasticCylindricalGearMaterial:
        """Special nested class for casting PlasticCylindricalGearMaterial to subclasses."""

        def __init__(
            self: "PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial",
            parent: "PlasticCylindricalGearMaterial",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_material(
            self: "PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial",
        ) -> "_594.CylindricalGearMaterial":
            return self._parent._cast(_594.CylindricalGearMaterial)

        @property
        def gear_material(
            self: "PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial",
        ) -> "_597.GearMaterial":
            from mastapy.gears.materials import _597

            return self._parent._cast(_597.GearMaterial)

        @property
        def material(
            self: "PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial",
        ) -> "_272.Material":
            from mastapy.materials import _272

            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def plastic_cylindrical_gear_material(
            self: "PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial",
        ) -> "PlasticCylindricalGearMaterial":
            return self._parent

        def __getattr__(
            self: "PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlasticCylindricalGearMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def glass_transition_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.GlassTransitionTemperature

        if temp is None:
            return 0.0

        return temp

    @glass_transition_temperature.setter
    @enforce_parameter_types
    def glass_transition_temperature(self: Self, value: "float"):
        self.wrapped.GlassTransitionTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def material_type(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.MaterialType

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @material_type.setter
    @enforce_parameter_types
    def material_type(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.MaterialType = value

    @property
    def melting_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeltingTemperature

        if temp is None:
            return 0.0

        return temp

    @melting_temperature.setter
    @enforce_parameter_types
    def melting_temperature(self: Self, value: "float"):
        self.wrapped.MeltingTemperature = float(value) if value is not None else 0.0

    @property
    def modulus_of_elasticity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModulusOfElasticity

        if temp is None:
            return 0.0

        return temp

    @modulus_of_elasticity.setter
    @enforce_parameter_types
    def modulus_of_elasticity(self: Self, value: "float"):
        self.wrapped.ModulusOfElasticity = float(value) if value is not None else 0.0

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
    def permissible_temperature_for_continuous_operation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PermissibleTemperatureForContinuousOperation

        if temp is None:
            return 0.0

        return temp

    @permissible_temperature_for_continuous_operation.setter
    @enforce_parameter_types
    def permissible_temperature_for_continuous_operation(self: Self, value: "float"):
        self.wrapped.PermissibleTemperatureForContinuousOperation = (
            float(value) if value is not None else 0.0
        )

    @property
    def permissible_temperature_for_intermittent_operation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PermissibleTemperatureForIntermittentOperation

        if temp is None:
            return 0.0

        return temp

    @permissible_temperature_for_intermittent_operation.setter
    @enforce_parameter_types
    def permissible_temperature_for_intermittent_operation(self: Self, value: "float"):
        self.wrapped.PermissibleTemperatureForIntermittentOperation = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_custom_material_for_bending(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseCustomMaterialForBending

        if temp is None:
            return False

        return temp

    @use_custom_material_for_bending.setter
    @enforce_parameter_types
    def use_custom_material_for_bending(self: Self, value: "bool"):
        self.wrapped.UseCustomMaterialForBending = (
            bool(value) if value is not None else False
        )

    @property
    def use_custom_material_for_contact(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseCustomMaterialForContact

        if temp is None:
            return False

        return temp

    @use_custom_material_for_contact.setter
    @enforce_parameter_types
    def use_custom_material_for_contact(self: Self, value: "bool"):
        self.wrapped.UseCustomMaterialForContact = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "PlasticCylindricalGearMaterial._Cast_PlasticCylindricalGearMaterial":
        return self._Cast_PlasticCylindricalGearMaterial(self)
