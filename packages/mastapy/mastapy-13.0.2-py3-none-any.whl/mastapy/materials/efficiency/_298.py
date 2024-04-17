"""IndependentPowerLoss"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.materials.efficiency import _305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INDEPENDENT_POWER_LOSS = python_net_import(
    "SMT.MastaAPI.Materials.Efficiency", "IndependentPowerLoss"
)


__docformat__ = "restructuredtext en"
__all__ = ("IndependentPowerLoss",)


Self = TypeVar("Self", bound="IndependentPowerLoss")


class IndependentPowerLoss(_305.PowerLoss):
    """IndependentPowerLoss

    This is a mastapy class.
    """

    TYPE = _INDEPENDENT_POWER_LOSS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_IndependentPowerLoss")

    class _Cast_IndependentPowerLoss:
        """Special nested class for casting IndependentPowerLoss to subclasses."""

        def __init__(
            self: "IndependentPowerLoss._Cast_IndependentPowerLoss",
            parent: "IndependentPowerLoss",
        ):
            self._parent = parent

        @property
        def power_loss(
            self: "IndependentPowerLoss._Cast_IndependentPowerLoss",
        ) -> "_305.PowerLoss":
            return self._parent._cast(_305.PowerLoss)

        @property
        def independent_power_loss(
            self: "IndependentPowerLoss._Cast_IndependentPowerLoss",
        ) -> "IndependentPowerLoss":
            return self._parent

        def __getattr__(
            self: "IndependentPowerLoss._Cast_IndependentPowerLoss", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "IndependentPowerLoss.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_dependent_power_loss(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LoadDependentPowerLoss

        if temp is None:
            return 0.0

        return temp

    @load_dependent_power_loss.setter
    @enforce_parameter_types
    def load_dependent_power_loss(self: Self, value: "float"):
        self.wrapped.LoadDependentPowerLoss = float(value) if value is not None else 0.0

    @property
    def speed_dependent_power_loss(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpeedDependentPowerLoss

        if temp is None:
            return 0.0

        return temp

    @speed_dependent_power_loss.setter
    @enforce_parameter_types
    def speed_dependent_power_loss(self: Self, value: "float"):
        self.wrapped.SpeedDependentPowerLoss = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "IndependentPowerLoss._Cast_IndependentPowerLoss":
        return self._Cast_IndependentPowerLoss(self)
