"""BevelHypoidGearDesignSettingsItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_DESIGN_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "BevelHypoidGearDesignSettingsItem"
)

if TYPE_CHECKING:
    from mastapy.gears import _347


__docformat__ = "restructuredtext en"
__all__ = ("BevelHypoidGearDesignSettingsItem",)


Self = TypeVar("Self", bound="BevelHypoidGearDesignSettingsItem")


class BevelHypoidGearDesignSettingsItem(_1836.NamedDatabaseItem):
    """BevelHypoidGearDesignSettingsItem

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_DESIGN_SETTINGS_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelHypoidGearDesignSettingsItem")

    class _Cast_BevelHypoidGearDesignSettingsItem:
        """Special nested class for casting BevelHypoidGearDesignSettingsItem to subclasses."""

        def __init__(
            self: "BevelHypoidGearDesignSettingsItem._Cast_BevelHypoidGearDesignSettingsItem",
            parent: "BevelHypoidGearDesignSettingsItem",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "BevelHypoidGearDesignSettingsItem._Cast_BevelHypoidGearDesignSettingsItem",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def bevel_hypoid_gear_design_settings_item(
            self: "BevelHypoidGearDesignSettingsItem._Cast_BevelHypoidGearDesignSettingsItem",
        ) -> "BevelHypoidGearDesignSettingsItem":
            return self._parent

        def __getattr__(
            self: "BevelHypoidGearDesignSettingsItem._Cast_BevelHypoidGearDesignSettingsItem",
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
        self: Self, instance_to_wrap: "BevelHypoidGearDesignSettingsItem.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allow_overriding_manufacturing_config_micro_geometry_in_a_load_case(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.AllowOverridingManufacturingConfigMicroGeometryInALoadCase

        if temp is None:
            return False

        return temp

    @allow_overriding_manufacturing_config_micro_geometry_in_a_load_case.setter
    @enforce_parameter_types
    def allow_overriding_manufacturing_config_micro_geometry_in_a_load_case(
        self: Self, value: "bool"
    ):
        self.wrapped.AllowOverridingManufacturingConfigMicroGeometryInALoadCase = (
            bool(value) if value is not None else False
        )

    @property
    def minimum_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumRatio

        if temp is None:
            return 0.0

        return temp

    @minimum_ratio.setter
    @enforce_parameter_types
    def minimum_ratio(self: Self, value: "float"):
        self.wrapped.MinimumRatio = float(value) if value is not None else 0.0

    @property
    def quality_grade_type(self: Self) -> "_347.QualityGradeTypes":
        """mastapy.gears.QualityGradeTypes"""
        temp = self.wrapped.QualityGradeType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.QualityGradeTypes")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._347", "QualityGradeTypes")(
            value
        )

    @quality_grade_type.setter
    @enforce_parameter_types
    def quality_grade_type(self: Self, value: "_347.QualityGradeTypes"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Gears.QualityGradeTypes")
        self.wrapped.QualityGradeType = value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelHypoidGearDesignSettingsItem._Cast_BevelHypoidGearDesignSettingsItem":
        return self._Cast_BevelHypoidGearDesignSettingsItem(self)
