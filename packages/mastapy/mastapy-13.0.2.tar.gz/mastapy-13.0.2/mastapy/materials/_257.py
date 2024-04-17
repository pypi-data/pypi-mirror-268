"""FatigueSafetyFactorItemBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FATIGUE_SAFETY_FACTOR_ITEM_BASE = python_net_import(
    "SMT.MastaAPI.Materials", "FatigueSafetyFactorItemBase"
)

if TYPE_CHECKING:
    from mastapy.materials import _253, _256


__docformat__ = "restructuredtext en"
__all__ = ("FatigueSafetyFactorItemBase",)


Self = TypeVar("Self", bound="FatigueSafetyFactorItemBase")


class FatigueSafetyFactorItemBase(_283.SafetyFactorItem):
    """FatigueSafetyFactorItemBase

    This is a mastapy class.
    """

    TYPE = _FATIGUE_SAFETY_FACTOR_ITEM_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FatigueSafetyFactorItemBase")

    class _Cast_FatigueSafetyFactorItemBase:
        """Special nested class for casting FatigueSafetyFactorItemBase to subclasses."""

        def __init__(
            self: "FatigueSafetyFactorItemBase._Cast_FatigueSafetyFactorItemBase",
            parent: "FatigueSafetyFactorItemBase",
        ):
            self._parent = parent

        @property
        def safety_factor_item(
            self: "FatigueSafetyFactorItemBase._Cast_FatigueSafetyFactorItemBase",
        ) -> "_283.SafetyFactorItem":
            return self._parent._cast(_283.SafetyFactorItem)

        @property
        def composite_fatigue_safety_factor_item(
            self: "FatigueSafetyFactorItemBase._Cast_FatigueSafetyFactorItemBase",
        ) -> "_253.CompositeFatigueSafetyFactorItem":
            from mastapy.materials import _253

            return self._parent._cast(_253.CompositeFatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item(
            self: "FatigueSafetyFactorItemBase._Cast_FatigueSafetyFactorItemBase",
        ) -> "_256.FatigueSafetyFactorItem":
            from mastapy.materials import _256

            return self._parent._cast(_256.FatigueSafetyFactorItem)

        @property
        def fatigue_safety_factor_item_base(
            self: "FatigueSafetyFactorItemBase._Cast_FatigueSafetyFactorItemBase",
        ) -> "FatigueSafetyFactorItemBase":
            return self._parent

        def __getattr__(
            self: "FatigueSafetyFactorItemBase._Cast_FatigueSafetyFactorItemBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FatigueSafetyFactorItemBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "FatigueSafetyFactorItemBase._Cast_FatigueSafetyFactorItemBase":
        return self._Cast_FatigueSafetyFactorItemBase(self)
