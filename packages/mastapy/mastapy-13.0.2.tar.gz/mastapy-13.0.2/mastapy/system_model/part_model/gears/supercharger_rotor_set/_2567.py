"""RotorSpeedInputOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROTOR_SPEED_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet",
    "RotorSpeedInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("RotorSpeedInputOptions",)


Self = TypeVar("Self", bound="RotorSpeedInputOptions")


class RotorSpeedInputOptions(_1854.ColumnInputOptions):
    """RotorSpeedInputOptions

    This is a mastapy class.
    """

    TYPE = _ROTOR_SPEED_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RotorSpeedInputOptions")

    class _Cast_RotorSpeedInputOptions:
        """Special nested class for casting RotorSpeedInputOptions to subclasses."""

        def __init__(
            self: "RotorSpeedInputOptions._Cast_RotorSpeedInputOptions",
            parent: "RotorSpeedInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "RotorSpeedInputOptions._Cast_RotorSpeedInputOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def rotor_speed_input_options(
            self: "RotorSpeedInputOptions._Cast_RotorSpeedInputOptions",
        ) -> "RotorSpeedInputOptions":
            return self._parent

        def __getattr__(
            self: "RotorSpeedInputOptions._Cast_RotorSpeedInputOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RotorSpeedInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RotorSpeedInputOptions._Cast_RotorSpeedInputOptions":
        return self._Cast_RotorSpeedInputOptions(self)
