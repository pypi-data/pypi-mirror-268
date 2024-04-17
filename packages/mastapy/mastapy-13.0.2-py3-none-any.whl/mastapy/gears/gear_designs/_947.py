"""BevelHypoidGearRatingSettingsItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS_ITEM = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "BevelHypoidGearRatingSettingsItem"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _608
    from mastapy.gears.rating.iso_10300 import _423, _438, _431
    from mastapy.gears.rating.hypoid import _444


__docformat__ = "restructuredtext en"
__all__ = ("BevelHypoidGearRatingSettingsItem",)


Self = TypeVar("Self", bound="BevelHypoidGearRatingSettingsItem")


class BevelHypoidGearRatingSettingsItem(_1836.NamedDatabaseItem):
    """BevelHypoidGearRatingSettingsItem

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelHypoidGearRatingSettingsItem")

    class _Cast_BevelHypoidGearRatingSettingsItem:
        """Special nested class for casting BevelHypoidGearRatingSettingsItem to subclasses."""

        def __init__(
            self: "BevelHypoidGearRatingSettingsItem._Cast_BevelHypoidGearRatingSettingsItem",
            parent: "BevelHypoidGearRatingSettingsItem",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "BevelHypoidGearRatingSettingsItem._Cast_BevelHypoidGearRatingSettingsItem",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def bevel_hypoid_gear_rating_settings_item(
            self: "BevelHypoidGearRatingSettingsItem._Cast_BevelHypoidGearRatingSettingsItem",
        ) -> "BevelHypoidGearRatingSettingsItem":
            return self._parent

        def __getattr__(
            self: "BevelHypoidGearRatingSettingsItem._Cast_BevelHypoidGearRatingSettingsItem",
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
        self: Self, instance_to_wrap: "BevelHypoidGearRatingSettingsItem.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_rating_method(self: Self) -> "_608.RatingMethods":
        """mastapy.gears.materials.RatingMethods"""
        temp = self.wrapped.BevelGearRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Materials.RatingMethods"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.materials._608", "RatingMethods"
        )(value)

    @bevel_gear_rating_method.setter
    @enforce_parameter_types
    def bevel_gear_rating_method(self: Self, value: "_608.RatingMethods"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Materials.RatingMethods"
        )
        self.wrapped.BevelGearRatingMethod = value

    @property
    def bevel_general_load_factors_k_method(
        self: Self,
    ) -> "_423.GeneralLoadFactorCalculationMethod":
        """mastapy.gears.rating.isoGeneralLoadFactorCalculationMethod"""
        temp = self.wrapped.BevelGeneralLoadFactorsKMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._423", "GeneralLoadFactorCalculationMethod"
        )(value)

    @bevel_general_load_factors_k_method.setter
    @enforce_parameter_types
    def bevel_general_load_factors_k_method(
        self: Self, value: "_423.GeneralLoadFactorCalculationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod",
        )
        self.wrapped.BevelGeneralLoadFactorsKMethod = value

    @property
    def bevel_pitting_factor_calculation_method(
        self: Self,
    ) -> "_438.PittingFactorCalculationMethod":
        """mastapy.gears.rating.isoPittingFactorCalculationMethod"""
        temp = self.wrapped.BevelPittingFactorCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._438", "PittingFactorCalculationMethod"
        )(value)

    @bevel_pitting_factor_calculation_method.setter
    @enforce_parameter_types
    def bevel_pitting_factor_calculation_method(
        self: Self, value: "_438.PittingFactorCalculationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod"
        )
        self.wrapped.BevelPittingFactorCalculationMethod = value

    @property
    def hypoid_gear_rating_method(self: Self) -> "_444.HypoidRatingMethod":
        """mastapy.gears.rating.hypoid.HypoidRatingMethod"""
        temp = self.wrapped.HypoidGearRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Hypoid.HypoidRatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating.hypoid._444", "HypoidRatingMethod"
        )(value)

    @hypoid_gear_rating_method.setter
    @enforce_parameter_types
    def hypoid_gear_rating_method(self: Self, value: "_444.HypoidRatingMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Hypoid.HypoidRatingMethod"
        )
        self.wrapped.HypoidGearRatingMethod = value

    @property
    def hypoid_general_load_factors_k_method(
        self: Self,
    ) -> "_423.GeneralLoadFactorCalculationMethod":
        """mastapy.gears.rating.isoGeneralLoadFactorCalculationMethod"""
        temp = self.wrapped.HypoidGeneralLoadFactorsKMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._423", "GeneralLoadFactorCalculationMethod"
        )(value)

    @hypoid_general_load_factors_k_method.setter
    @enforce_parameter_types
    def hypoid_general_load_factors_k_method(
        self: Self, value: "_423.GeneralLoadFactorCalculationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Rating.Iso10300.GeneralLoadFactorCalculationMethod",
        )
        self.wrapped.HypoidGeneralLoadFactorsKMethod = value

    @property
    def hypoid_pitting_factor_calculation_method(
        self: Self,
    ) -> "_438.PittingFactorCalculationMethod":
        """mastapy.gears.rating.isoPittingFactorCalculationMethod"""
        temp = self.wrapped.HypoidPittingFactorCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._438", "PittingFactorCalculationMethod"
        )(value)

    @hypoid_pitting_factor_calculation_method.setter
    @enforce_parameter_types
    def hypoid_pitting_factor_calculation_method(
        self: Self, value: "_438.PittingFactorCalculationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.PittingFactorCalculationMethod"
        )
        self.wrapped.HypoidPittingFactorCalculationMethod = value

    @property
    def iso_rating_method_for_bevel_gears(self: Self) -> "_431.ISO10300RatingMethod":
        """mastapy.gears.rating.isoISO10300RatingMethod"""
        temp = self.wrapped.ISORatingMethodForBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._431", "ISO10300RatingMethod"
        )(value)

    @iso_rating_method_for_bevel_gears.setter
    @enforce_parameter_types
    def iso_rating_method_for_bevel_gears(
        self: Self, value: "_431.ISO10300RatingMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod"
        )
        self.wrapped.ISORatingMethodForBevelGears = value

    @property
    def iso_rating_method_for_hypoid_gears(self: Self) -> "_431.ISO10300RatingMethod":
        """mastapy.gears.rating.isoISO10300RatingMethod"""
        temp = self.wrapped.ISORatingMethodForHypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.rating._431", "ISO10300RatingMethod"
        )(value)

    @iso_rating_method_for_hypoid_gears.setter
    @enforce_parameter_types
    def iso_rating_method_for_hypoid_gears(
        self: Self, value: "_431.ISO10300RatingMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.Rating.Iso10300.ISO10300RatingMethod"
        )
        self.wrapped.ISORatingMethodForHypoidGears = value

    @property
    def include_mesh_node_misalignments_in_default_report(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport

        if temp is None:
            return False

        return temp

    @include_mesh_node_misalignments_in_default_report.setter
    @enforce_parameter_types
    def include_mesh_node_misalignments_in_default_report(self: Self, value: "bool"):
        self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "BevelHypoidGearRatingSettingsItem._Cast_BevelHypoidGearRatingSettingsItem":
        return self._Cast_BevelHypoidGearRatingSettingsItem(self)
