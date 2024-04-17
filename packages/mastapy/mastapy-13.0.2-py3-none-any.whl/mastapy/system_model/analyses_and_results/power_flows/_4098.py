"""FastPowerFlowSolution"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FAST_POWER_FLOW_SOLUTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "FastPowerFlowSolution"
)


__docformat__ = "restructuredtext en"
__all__ = ("FastPowerFlowSolution",)


Self = TypeVar("Self", bound="FastPowerFlowSolution")


class FastPowerFlowSolution(_0.APIBase):
    """FastPowerFlowSolution

    This is a mastapy class.
    """

    TYPE = _FAST_POWER_FLOW_SOLUTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FastPowerFlowSolution")

    class _Cast_FastPowerFlowSolution:
        """Special nested class for casting FastPowerFlowSolution to subclasses."""

        def __init__(
            self: "FastPowerFlowSolution._Cast_FastPowerFlowSolution",
            parent: "FastPowerFlowSolution",
        ):
            self._parent = parent

        @property
        def fast_power_flow_solution(
            self: "FastPowerFlowSolution._Cast_FastPowerFlowSolution",
        ) -> "FastPowerFlowSolution":
            return self._parent

        def __getattr__(
            self: "FastPowerFlowSolution._Cast_FastPowerFlowSolution", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FastPowerFlowSolution.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FastPowerFlowSolution._Cast_FastPowerFlowSolution":
        return self._Cast_FastPowerFlowSolution(self)
