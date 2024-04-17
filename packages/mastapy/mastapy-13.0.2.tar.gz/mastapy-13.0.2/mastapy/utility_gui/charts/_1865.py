"""ModeConstantLine"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility_gui.charts import _1860
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODE_CONSTANT_LINE = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "ModeConstantLine"
)


__docformat__ = "restructuredtext en"
__all__ = ("ModeConstantLine",)


Self = TypeVar("Self", bound="ModeConstantLine")


class ModeConstantLine(_1860.ConstantLine):
    """ModeConstantLine

    This is a mastapy class.
    """

    TYPE = _MODE_CONSTANT_LINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ModeConstantLine")

    class _Cast_ModeConstantLine:
        """Special nested class for casting ModeConstantLine to subclasses."""

        def __init__(
            self: "ModeConstantLine._Cast_ModeConstantLine", parent: "ModeConstantLine"
        ):
            self._parent = parent

        @property
        def constant_line(
            self: "ModeConstantLine._Cast_ModeConstantLine",
        ) -> "_1860.ConstantLine":
            return self._parent._cast(_1860.ConstantLine)

        @property
        def mode_constant_line(
            self: "ModeConstantLine._Cast_ModeConstantLine",
        ) -> "ModeConstantLine":
            return self._parent

        def __getattr__(self: "ModeConstantLine._Cast_ModeConstantLine", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ModeConstantLine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ModeConstantLine._Cast_ModeConstantLine":
        return self._Cast_ModeConstantLine(self)
