"""ShaftSafetyFactorSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SAFETY_FACTOR_SETTINGS = python_net_import(
    "SMT.MastaAPI.Shafts", "ShaftSafetyFactorSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSafetyFactorSettings",)


Self = TypeVar("Self", bound="ShaftSafetyFactorSettings")


class ShaftSafetyFactorSettings(_0.APIBase):
    """ShaftSafetyFactorSettings

    This is a mastapy class.
    """

    TYPE = _SHAFT_SAFETY_FACTOR_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSafetyFactorSettings")

    class _Cast_ShaftSafetyFactorSettings:
        """Special nested class for casting ShaftSafetyFactorSettings to subclasses."""

        def __init__(
            self: "ShaftSafetyFactorSettings._Cast_ShaftSafetyFactorSettings",
            parent: "ShaftSafetyFactorSettings",
        ):
            self._parent = parent

        @property
        def shaft_safety_factor_settings(
            self: "ShaftSafetyFactorSettings._Cast_ShaftSafetyFactorSettings",
        ) -> "ShaftSafetyFactorSettings":
            return self._parent

        def __getattr__(
            self: "ShaftSafetyFactorSettings._Cast_ShaftSafetyFactorSettings", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSafetyFactorSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def shaft_fatigue_safety_factor_requirement(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaftFatigueSafetyFactorRequirement

        if temp is None:
            return 0.0

        return temp

    @shaft_fatigue_safety_factor_requirement.setter
    @enforce_parameter_types
    def shaft_fatigue_safety_factor_requirement(self: Self, value: "float"):
        self.wrapped.ShaftFatigueSafetyFactorRequirement = (
            float(value) if value is not None else 0.0
        )

    @property
    def shaft_static_safety_factor_requirement(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaftStaticSafetyFactorRequirement

        if temp is None:
            return 0.0

        return temp

    @shaft_static_safety_factor_requirement.setter
    @enforce_parameter_types
    def shaft_static_safety_factor_requirement(self: Self, value: "float"):
        self.wrapped.ShaftStaticSafetyFactorRequirement = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftSafetyFactorSettings._Cast_ShaftSafetyFactorSettings":
        return self._Cast_ShaftSafetyFactorSettings(self)
