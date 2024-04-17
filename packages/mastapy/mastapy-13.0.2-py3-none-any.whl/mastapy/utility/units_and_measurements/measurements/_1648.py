"""FlowRate"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLOW_RATE = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "FlowRate"
)


__docformat__ = "restructuredtext en"
__all__ = ("FlowRate",)


Self = TypeVar("Self", bound="FlowRate")


class FlowRate(_1612.MeasurementBase):
    """FlowRate

    This is a mastapy class.
    """

    TYPE = _FLOW_RATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FlowRate")

    class _Cast_FlowRate:
        """Special nested class for casting FlowRate to subclasses."""

        def __init__(self: "FlowRate._Cast_FlowRate", parent: "FlowRate"):
            self._parent = parent

        @property
        def measurement_base(
            self: "FlowRate._Cast_FlowRate",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def flow_rate(self: "FlowRate._Cast_FlowRate") -> "FlowRate":
            return self._parent

        def __getattr__(self: "FlowRate._Cast_FlowRate", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FlowRate.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FlowRate._Cast_FlowRate":
        return self._Cast_FlowRate(self)
