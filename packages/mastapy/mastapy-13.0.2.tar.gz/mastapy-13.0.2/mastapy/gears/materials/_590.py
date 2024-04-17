"""BevelGearMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.materials import _597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MATERIAL = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "BevelGearMaterial"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _611, _588
    from mastapy.materials import _272
    from mastapy.utility.databases import _1836


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMaterial",)


Self = TypeVar("Self", bound="BevelGearMaterial")


class BevelGearMaterial(_597.GearMaterial):
    """BevelGearMaterial

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMaterial")

    class _Cast_BevelGearMaterial:
        """Special nested class for casting BevelGearMaterial to subclasses."""

        def __init__(
            self: "BevelGearMaterial._Cast_BevelGearMaterial",
            parent: "BevelGearMaterial",
        ):
            self._parent = parent

        @property
        def gear_material(
            self: "BevelGearMaterial._Cast_BevelGearMaterial",
        ) -> "_597.GearMaterial":
            return self._parent._cast(_597.GearMaterial)

        @property
        def material(
            self: "BevelGearMaterial._Cast_BevelGearMaterial",
        ) -> "_272.Material":
            from mastapy.materials import _272

            return self._parent._cast(_272.Material)

        @property
        def named_database_item(
            self: "BevelGearMaterial._Cast_BevelGearMaterial",
        ) -> "_1836.NamedDatabaseItem":
            from mastapy.utility.databases import _1836

            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def bevel_gear_iso_material(
            self: "BevelGearMaterial._Cast_BevelGearMaterial",
        ) -> "_588.BevelGearISOMaterial":
            from mastapy.gears.materials import _588

            return self._parent._cast(_588.BevelGearISOMaterial)

        @property
        def bevel_gear_material(
            self: "BevelGearMaterial._Cast_BevelGearMaterial",
        ) -> "BevelGearMaterial":
            return self._parent

        def __getattr__(self: "BevelGearMaterial._Cast_BevelGearMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMaterial.TYPE"):
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
    def sn_curve_definition(self: Self) -> "_611.SNCurveDefinition":
        """mastapy.gears.materials.SNCurveDefinition"""
        temp = self.wrapped.SNCurveDefinition

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.SNCurveDefinition"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.materials._611", "SNCurveDefinition"
        )(value)

    @sn_curve_definition.setter
    @enforce_parameter_types
    def sn_curve_definition(self: Self, value: "_611.SNCurveDefinition"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.SNCurveDefinition"
        )
        self.wrapped.SNCurveDefinition = value

    @property
    def thermal_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "BevelGearMaterial._Cast_BevelGearMaterial":
        return self._Cast_BevelGearMaterial(self)
