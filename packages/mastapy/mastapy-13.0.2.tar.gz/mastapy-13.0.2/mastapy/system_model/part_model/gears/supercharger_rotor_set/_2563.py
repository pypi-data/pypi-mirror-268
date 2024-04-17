"""InputPowerInputOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INPUT_POWER_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet",
    "InputPowerInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("InputPowerInputOptions",)


Self = TypeVar("Self", bound="InputPowerInputOptions")


class InputPowerInputOptions(_1854.ColumnInputOptions):
    """InputPowerInputOptions

    This is a mastapy class.
    """

    TYPE = _INPUT_POWER_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InputPowerInputOptions")

    class _Cast_InputPowerInputOptions:
        """Special nested class for casting InputPowerInputOptions to subclasses."""

        def __init__(
            self: "InputPowerInputOptions._Cast_InputPowerInputOptions",
            parent: "InputPowerInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "InputPowerInputOptions._Cast_InputPowerInputOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def input_power_input_options(
            self: "InputPowerInputOptions._Cast_InputPowerInputOptions",
        ) -> "InputPowerInputOptions":
            return self._parent

        def __getattr__(
            self: "InputPowerInputOptions._Cast_InputPowerInputOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InputPowerInputOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InputPowerInputOptions._Cast_InputPowerInputOptions":
        return self._Cast_InputPowerInputOptions(self)
