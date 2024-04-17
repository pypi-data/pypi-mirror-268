"""SafetyFactorResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "SafetyFactorResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorResults",)


Self = TypeVar("Self", bound="SafetyFactorResults")


class SafetyFactorResults(_0.APIBase):
    """SafetyFactorResults

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SafetyFactorResults")

    class _Cast_SafetyFactorResults:
        """Special nested class for casting SafetyFactorResults to subclasses."""

        def __init__(
            self: "SafetyFactorResults._Cast_SafetyFactorResults",
            parent: "SafetyFactorResults",
        ):
            self._parent = parent

        @property
        def safety_factor_results(
            self: "SafetyFactorResults._Cast_SafetyFactorResults",
        ) -> "SafetyFactorResults":
            return self._parent

        def __getattr__(
            self: "SafetyFactorResults._Cast_SafetyFactorResults", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SafetyFactorResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fatigue_bending_safety_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FatigueBendingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @fatigue_bending_safety_factor.setter
    @enforce_parameter_types
    def fatigue_bending_safety_factor(self: Self, value: "float"):
        self.wrapped.FatigueBendingSafetyFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def fatigue_contact_safety_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FatigueContactSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @fatigue_contact_safety_factor.setter
    @enforce_parameter_types
    def fatigue_contact_safety_factor(self: Self, value: "float"):
        self.wrapped.FatigueContactSafetyFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def fatigue_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def static_bending_safety_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StaticBendingSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @static_bending_safety_factor.setter
    @enforce_parameter_types
    def static_bending_safety_factor(self: Self, value: "float"):
        self.wrapped.StaticBendingSafetyFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def static_contact_safety_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StaticContactSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @static_contact_safety_factor.setter
    @enforce_parameter_types
    def static_contact_safety_factor(self: Self, value: "float"):
        self.wrapped.StaticContactSafetyFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def static_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SafetyFactorResults._Cast_SafetyFactorResults":
        return self._Cast_SafetyFactorResults(self)
