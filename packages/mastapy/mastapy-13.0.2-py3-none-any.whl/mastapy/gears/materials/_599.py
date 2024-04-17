"""GearMaterialExpertSystemFactorSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility import _1601
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL_EXPERT_SYSTEM_FACTOR_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "GearMaterialExpertSystemFactorSettings"
)

if TYPE_CHECKING:
    from mastapy.utility import _1602


__docformat__ = "restructuredtext en"
__all__ = ("GearMaterialExpertSystemFactorSettings",)


Self = TypeVar("Self", bound="GearMaterialExpertSystemFactorSettings")


class GearMaterialExpertSystemFactorSettings(_1601.PerMachineSettings):
    """GearMaterialExpertSystemFactorSettings

    This is a mastapy class.
    """

    TYPE = _GEAR_MATERIAL_EXPERT_SYSTEM_FACTOR_SETTINGS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearMaterialExpertSystemFactorSettings"
    )

    class _Cast_GearMaterialExpertSystemFactorSettings:
        """Special nested class for casting GearMaterialExpertSystemFactorSettings to subclasses."""

        def __init__(
            self: "GearMaterialExpertSystemFactorSettings._Cast_GearMaterialExpertSystemFactorSettings",
            parent: "GearMaterialExpertSystemFactorSettings",
        ):
            self._parent = parent

        @property
        def per_machine_settings(
            self: "GearMaterialExpertSystemFactorSettings._Cast_GearMaterialExpertSystemFactorSettings",
        ) -> "_1601.PerMachineSettings":
            return self._parent._cast(_1601.PerMachineSettings)

        @property
        def persistent_singleton(
            self: "GearMaterialExpertSystemFactorSettings._Cast_GearMaterialExpertSystemFactorSettings",
        ) -> "_1602.PersistentSingleton":
            from mastapy.utility import _1602

            return self._parent._cast(_1602.PersistentSingleton)

        @property
        def gear_material_expert_system_factor_settings(
            self: "GearMaterialExpertSystemFactorSettings._Cast_GearMaterialExpertSystemFactorSettings",
        ) -> "GearMaterialExpertSystemFactorSettings":
            return self._parent

        def __getattr__(
            self: "GearMaterialExpertSystemFactorSettings._Cast_GearMaterialExpertSystemFactorSettings",
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
        self: Self, instance_to_wrap: "GearMaterialExpertSystemFactorSettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_damage(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumDamage

        if temp is None:
            return 0.0

        return temp

    @maximum_damage.setter
    @enforce_parameter_types
    def maximum_damage(self: Self, value: "float"):
        self.wrapped.MaximumDamage = float(value) if value is not None else 0.0

    @property
    def maximum_safety_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @maximum_safety_factor.setter
    @enforce_parameter_types
    def maximum_safety_factor(self: Self, value: "float"):
        self.wrapped.MaximumSafetyFactor = float(value) if value is not None else 0.0

    @property
    def minimum_damage(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumDamage

        if temp is None:
            return 0.0

        return temp

    @minimum_damage.setter
    @enforce_parameter_types
    def minimum_damage(self: Self, value: "float"):
        self.wrapped.MinimumDamage = float(value) if value is not None else 0.0

    @property
    def minimum_safety_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @minimum_safety_factor.setter
    @enforce_parameter_types
    def minimum_safety_factor(self: Self, value: "float"):
        self.wrapped.MinimumSafetyFactor = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "GearMaterialExpertSystemFactorSettings._Cast_GearMaterialExpertSystemFactorSettings":
        return self._Cast_GearMaterialExpertSystemFactorSettings(self)
