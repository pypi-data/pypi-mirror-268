"""LoadAndSpeedCombinedPowerLoss"""

from __future__ import annotations

from typing import TypeVar

from mastapy.materials.efficiency import _305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOAD_AND_SPEED_COMBINED_POWER_LOSS = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "LoadAndSpeedCombinedPowerLoss"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadAndSpeedCombinedPowerLoss",)


Self = TypeVar("Self", bound="LoadAndSpeedCombinedPowerLoss")


class LoadAndSpeedCombinedPowerLoss(_305.PowerLoss):
    """LoadAndSpeedCombinedPowerLoss

    This is a mastapy class.
    """

    TYPE = _LOAD_AND_SPEED_COMBINED_POWER_LOSS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadAndSpeedCombinedPowerLoss")

    class _Cast_LoadAndSpeedCombinedPowerLoss:
        """Special nested class for casting LoadAndSpeedCombinedPowerLoss to subclasses."""

        def __init__(
            self: "LoadAndSpeedCombinedPowerLoss._Cast_LoadAndSpeedCombinedPowerLoss",
            parent: "LoadAndSpeedCombinedPowerLoss",
        ):
            self._parent = parent

        @property
        def power_loss(
            self: "LoadAndSpeedCombinedPowerLoss._Cast_LoadAndSpeedCombinedPowerLoss",
        ) -> "_305.PowerLoss":
            return self._parent._cast(_305.PowerLoss)

        @property
        def load_and_speed_combined_power_loss(
            self: "LoadAndSpeedCombinedPowerLoss._Cast_LoadAndSpeedCombinedPowerLoss",
        ) -> "LoadAndSpeedCombinedPowerLoss":
            return self._parent

        def __getattr__(
            self: "LoadAndSpeedCombinedPowerLoss._Cast_LoadAndSpeedCombinedPowerLoss",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadAndSpeedCombinedPowerLoss.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadAndSpeedCombinedPowerLoss._Cast_LoadAndSpeedCombinedPowerLoss":
        return self._Cast_LoadAndSpeedCombinedPowerLoss(self)
