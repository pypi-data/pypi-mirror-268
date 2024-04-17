"""SpeedInputOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
    _7007,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "SpeedInputOptions",
)

if TYPE_CHECKING:
    from mastapy.utility_gui import _1854


__docformat__ = "restructuredtext en"
__all__ = ("SpeedInputOptions",)


Self = TypeVar("Self", bound="SpeedInputOptions")


class SpeedInputOptions(_7007.PowerLoadInputOptions):
    """SpeedInputOptions

    This is a mastapy class.
    """

    TYPE = _SPEED_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpeedInputOptions")

    class _Cast_SpeedInputOptions:
        """Special nested class for casting SpeedInputOptions to subclasses."""

        def __init__(
            self: "SpeedInputOptions._Cast_SpeedInputOptions",
            parent: "SpeedInputOptions",
        ):
            self._parent = parent

        @property
        def power_load_input_options(
            self: "SpeedInputOptions._Cast_SpeedInputOptions",
        ) -> "_7007.PowerLoadInputOptions":
            return self._parent._cast(_7007.PowerLoadInputOptions)

        @property
        def column_input_options(
            self: "SpeedInputOptions._Cast_SpeedInputOptions",
        ) -> "_1854.ColumnInputOptions":
            from mastapy.utility_gui import _1854

            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def speed_input_options(
            self: "SpeedInputOptions._Cast_SpeedInputOptions",
        ) -> "SpeedInputOptions":
            return self._parent

        def __getattr__(self: "SpeedInputOptions._Cast_SpeedInputOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpeedInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SpeedInputOptions._Cast_SpeedInputOptions":
        return self._Cast_SpeedInputOptions(self)
