"""CylindricalPlasticGearRatingSettingsItem"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical", "CylindricalPlasticGearRatingSettingsItem"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlasticGearRatingSettingsItem",)


Self = TypeVar("Self", bound="CylindricalPlasticGearRatingSettingsItem")


class CylindricalPlasticGearRatingSettingsItem(_1836.NamedDatabaseItem):
    """CylindricalPlasticGearRatingSettingsItem

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_ITEM
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlasticGearRatingSettingsItem"
    )

    class _Cast_CylindricalPlasticGearRatingSettingsItem:
        """Special nested class for casting CylindricalPlasticGearRatingSettingsItem to subclasses."""

        def __init__(
            self: "CylindricalPlasticGearRatingSettingsItem._Cast_CylindricalPlasticGearRatingSettingsItem",
            parent: "CylindricalPlasticGearRatingSettingsItem",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "CylindricalPlasticGearRatingSettingsItem._Cast_CylindricalPlasticGearRatingSettingsItem",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def cylindrical_plastic_gear_rating_settings_item(
            self: "CylindricalPlasticGearRatingSettingsItem._Cast_CylindricalPlasticGearRatingSettingsItem",
        ) -> "CylindricalPlasticGearRatingSettingsItem":
            return self._parent

        def __getattr__(
            self: "CylindricalPlasticGearRatingSettingsItem._Cast_CylindricalPlasticGearRatingSettingsItem",
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
        self: Self, instance_to_wrap: "CylindricalPlasticGearRatingSettingsItem.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def use_approximate_value_of_10_for_spiral_helix_angle_factor_for_contact_rating(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseApproximateValueOf10ForSpiralHelixAngleFactorForContactRating
        )

        if temp is None:
            return False

        return temp

    @use_approximate_value_of_10_for_spiral_helix_angle_factor_for_contact_rating.setter
    @enforce_parameter_types
    def use_approximate_value_of_10_for_spiral_helix_angle_factor_for_contact_rating(
        self: Self, value: "bool"
    ):
        self.wrapped.UseApproximateValueOf10ForSpiralHelixAngleFactorForContactRating = (
            bool(value) if value is not None else False
        )

    @property
    def use_approximate_value_of_double_the_normal_module_for_profile_line_length_of_the_active_tooth_flank(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseApproximateValueOfDoubleTheNormalModuleForProfileLineLengthOfTheActiveToothFlank
        )

        if temp is None:
            return False

        return temp

    @use_approximate_value_of_double_the_normal_module_for_profile_line_length_of_the_active_tooth_flank.setter
    @enforce_parameter_types
    def use_approximate_value_of_double_the_normal_module_for_profile_line_length_of_the_active_tooth_flank(
        self: Self, value: "bool"
    ):
        self.wrapped.UseApproximateValueOfDoubleTheNormalModuleForProfileLineLengthOfTheActiveToothFlank = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlasticGearRatingSettingsItem._Cast_CylindricalPlasticGearRatingSettingsItem":
        return self._Cast_CylindricalPlasticGearRatingSettingsItem(self)
