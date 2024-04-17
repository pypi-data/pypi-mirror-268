"""FatigueSafetyFactorItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _257
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FATIGUE_SAFETY_FACTOR_ITEM = python_net_import(
    "SMT.MastaAPI.Materials", "FatigueSafetyFactorItem"
)

if TYPE_CHECKING:
    from mastapy.materials import _253, _283


__docformat__ = "restructuredtext en"
__all__ = ("FatigueSafetyFactorItem",)


Self = TypeVar("Self", bound="FatigueSafetyFactorItem")


class FatigueSafetyFactorItem(_257.FatigueSafetyFactorItemBase):
    """FatigueSafetyFactorItem

    This is a mastapy class.
    """

    TYPE = _FATIGUE_SAFETY_FACTOR_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FatigueSafetyFactorItem")

    class _Cast_FatigueSafetyFactorItem:
        """Special nested class for casting FatigueSafetyFactorItem to subclasses."""

        def __init__(
            self: "FatigueSafetyFactorItem._Cast_FatigueSafetyFactorItem",
            parent: "FatigueSafetyFactorItem",
        ):
            self._parent = parent

        @property
        def fatigue_safety_factor_item_base(
            self: "FatigueSafetyFactorItem._Cast_FatigueSafetyFactorItem",
        ) -> "_257.FatigueSafetyFactorItemBase":
            return self._parent._cast(_257.FatigueSafetyFactorItemBase)

        @property
        def safety_factor_item(
            self: "FatigueSafetyFactorItem._Cast_FatigueSafetyFactorItem",
        ) -> "_283.SafetyFactorItem":
            from mastapy.materials import _283

            return self._parent._cast(_283.SafetyFactorItem)

        @property
        def composite_fatigue_safety_factor_item(
            self: "FatigueSafetyFactorItem._Cast_FatigueSafetyFactorItem",
        ) -> "_253.CompositeFatigueSafetyFactorItem":
            from mastapy.materials import _253

            return self._parent._cast(_253.CompositeFatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item(
            self: "FatigueSafetyFactorItem._Cast_FatigueSafetyFactorItem",
        ) -> "FatigueSafetyFactorItem":
            return self._parent

        def __getattr__(
            self: "FatigueSafetyFactorItem._Cast_FatigueSafetyFactorItem", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FatigueSafetyFactorItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FatigueSafetyFactorItem._Cast_FatigueSafetyFactorItem":
        return self._Cast_FatigueSafetyFactorItem(self)
