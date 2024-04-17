"""SafetyFactorItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_ITEM = python_net_import("SMT.MastaAPI.Materials", "SafetyFactorItem")

if TYPE_CHECKING:
    from mastapy.materials import _253, _256, _257


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorItem",)


Self = TypeVar("Self", bound="SafetyFactorItem")


class SafetyFactorItem(_0.APIBase):
    """SafetyFactorItem

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SafetyFactorItem")

    class _Cast_SafetyFactorItem:
        """Special nested class for casting SafetyFactorItem to subclasses."""

        def __init__(
            self: "SafetyFactorItem._Cast_SafetyFactorItem", parent: "SafetyFactorItem"
        ):
            self._parent = parent

        @property
        def composite_fatigue_safety_factor_item(
            self: "SafetyFactorItem._Cast_SafetyFactorItem",
        ) -> "_253.CompositeFatigueSafetyFactorItem":
            from mastapy.materials import _253

            return self._parent._cast(_253.CompositeFatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item(
            self: "SafetyFactorItem._Cast_SafetyFactorItem",
        ) -> "_256.FatigueSafetyFactorItem":
            from mastapy.materials import _256

            return self._parent._cast(_256.FatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item_base(
            self: "SafetyFactorItem._Cast_SafetyFactorItem",
        ) -> "_257.FatigueSafetyFactorItemBase":
            from mastapy.materials import _257

            return self._parent._cast(_257.FatigueSafetyFactorItemBase)

        @property
        def safety_factor_item(
            self: "SafetyFactorItem._Cast_SafetyFactorItem",
        ) -> "SafetyFactorItem":
            return self._parent

        def __getattr__(self: "SafetyFactorItem._Cast_SafetyFactorItem", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SafetyFactorItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Damage

        if temp is None:
            return 0.0

        return temp

    @property
    def description(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Description

        if temp is None:
            return ""

        return temp

    @property
    def minimum_required_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumRequiredSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Reliability

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
    def time_until_failure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeUntilFailure

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SafetyFactorItem._Cast_SafetyFactorItem":
        return self._Cast_SafetyFactorItem(self)
