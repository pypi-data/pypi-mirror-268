"""RampOrSteadyStateInputOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RAMP_OR_STEADY_STATE_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "RampOrSteadyStateInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("RampOrSteadyStateInputOptions",)


Self = TypeVar("Self", bound="RampOrSteadyStateInputOptions")


class RampOrSteadyStateInputOptions(_1854.ColumnInputOptions):
    """RampOrSteadyStateInputOptions

    This is a mastapy class.
    """

    TYPE = _RAMP_OR_STEADY_STATE_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RampOrSteadyStateInputOptions")

    class _Cast_RampOrSteadyStateInputOptions:
        """Special nested class for casting RampOrSteadyStateInputOptions to subclasses."""

        def __init__(
            self: "RampOrSteadyStateInputOptions._Cast_RampOrSteadyStateInputOptions",
            parent: "RampOrSteadyStateInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "RampOrSteadyStateInputOptions._Cast_RampOrSteadyStateInputOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def ramp_or_steady_state_input_options(
            self: "RampOrSteadyStateInputOptions._Cast_RampOrSteadyStateInputOptions",
        ) -> "RampOrSteadyStateInputOptions":
            return self._parent

        def __getattr__(
            self: "RampOrSteadyStateInputOptions._Cast_RampOrSteadyStateInputOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RampOrSteadyStateInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RampOrSteadyStateInputOptions._Cast_RampOrSteadyStateInputOptions":
        return self._Cast_RampOrSteadyStateInputOptions(self)
