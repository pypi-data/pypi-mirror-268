"""MaterialsSettingsItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy.materials import _277
from mastapy._internal import conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIALS_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.Materials", "MaterialsSettingsItem"
)

if TYPE_CHECKING:
    from mastapy.utility.property import _1850


__docformat__ = "restructuredtext en"
__all__ = ("MaterialsSettingsItem",)


Self = TypeVar("Self", bound="MaterialsSettingsItem")


class MaterialsSettingsItem(_1836.NamedDatabaseItem):
    """MaterialsSettingsItem

    This is a mastapy class.
    """

    TYPE = _MATERIALS_SETTINGS_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaterialsSettingsItem")

    class _Cast_MaterialsSettingsItem:
        """Special nested class for casting MaterialsSettingsItem to subclasses."""

        def __init__(
            self: "MaterialsSettingsItem._Cast_MaterialsSettingsItem",
            parent: "MaterialsSettingsItem",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "MaterialsSettingsItem._Cast_MaterialsSettingsItem",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def materials_settings_item(
            self: "MaterialsSettingsItem._Cast_MaterialsSettingsItem",
        ) -> "MaterialsSettingsItem":
            return self._parent

        def __getattr__(
            self: "MaterialsSettingsItem._Cast_MaterialsSettingsItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaterialsSettingsItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def available_material_standards(
        self: Self,
    ) -> "List[_1850.EnumWithBoolean[_277.MaterialStandards]]":
        """List[mastapy.utility.property.EnumWithBoolean[mastapy.materials.MaterialStandards]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AvailableMaterialStandards

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "MaterialsSettingsItem._Cast_MaterialsSettingsItem":
        return self._Cast_MaterialsSettingsItem(self)
