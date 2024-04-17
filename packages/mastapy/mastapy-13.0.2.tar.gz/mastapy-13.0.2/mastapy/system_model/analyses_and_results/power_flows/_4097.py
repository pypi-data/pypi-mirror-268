"""FastPowerFlow"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FAST_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "FastPowerFlow"
)


__docformat__ = "restructuredtext en"
__all__ = ("FastPowerFlow",)


Self = TypeVar("Self", bound="FastPowerFlow")


class FastPowerFlow(_0.APIBase):
    """FastPowerFlow

    This is a mastapy class.
    """

    TYPE = _FAST_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FastPowerFlow")

    class _Cast_FastPowerFlow:
        """Special nested class for casting FastPowerFlow to subclasses."""

        def __init__(
            self: "FastPowerFlow._Cast_FastPowerFlow", parent: "FastPowerFlow"
        ):
            self._parent = parent

        @property
        def fast_power_flow(
            self: "FastPowerFlow._Cast_FastPowerFlow",
        ) -> "FastPowerFlow":
            return self._parent

        def __getattr__(self: "FastPowerFlow._Cast_FastPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FastPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FastPowerFlow._Cast_FastPowerFlow":
        return self._Cast_FastPowerFlow(self)
