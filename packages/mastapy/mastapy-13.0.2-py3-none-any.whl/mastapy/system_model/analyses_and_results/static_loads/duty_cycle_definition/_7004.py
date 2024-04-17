"""MomentInputOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
    _7006,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOMENT_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "MomentInputOptions",
)

if TYPE_CHECKING:
    from mastapy.utility_gui import _1854


__docformat__ = "restructuredtext en"
__all__ = ("MomentInputOptions",)


Self = TypeVar("Self", bound="MomentInputOptions")


class MomentInputOptions(_7006.PointLoadInputOptions):
    """MomentInputOptions

    This is a mastapy class.
    """

    TYPE = _MOMENT_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MomentInputOptions")

    class _Cast_MomentInputOptions:
        """Special nested class for casting MomentInputOptions to subclasses."""

        def __init__(
            self: "MomentInputOptions._Cast_MomentInputOptions",
            parent: "MomentInputOptions",
        ):
            self._parent = parent

        @property
        def point_load_input_options(
            self: "MomentInputOptions._Cast_MomentInputOptions",
        ) -> "_7006.PointLoadInputOptions":
            return self._parent._cast(_7006.PointLoadInputOptions)

        @property
        def column_input_options(
            self: "MomentInputOptions._Cast_MomentInputOptions",
        ) -> "_1854.ColumnInputOptions":
            from mastapy.utility_gui import _1854

            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def moment_input_options(
            self: "MomentInputOptions._Cast_MomentInputOptions",
        ) -> "MomentInputOptions":
            return self._parent

        def __getattr__(self: "MomentInputOptions._Cast_MomentInputOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MomentInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MomentInputOptions._Cast_MomentInputOptions":
        return self._Cast_MomentInputOptions(self)
