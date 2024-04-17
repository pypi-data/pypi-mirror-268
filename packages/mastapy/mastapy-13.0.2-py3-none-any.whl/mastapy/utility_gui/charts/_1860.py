"""ConstantLine"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONSTANT_LINE = python_net_import("SMT.MastaAPI.UtilityGUI.Charts", "ConstantLine")

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1871, _1865


__docformat__ = "restructuredtext en"
__all__ = ("ConstantLine",)


Self = TypeVar("Self", bound="ConstantLine")


class ConstantLine(_0.APIBase):
    """ConstantLine

    This is a mastapy class.
    """

    TYPE = _CONSTANT_LINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConstantLine")

    class _Cast_ConstantLine:
        """Special nested class for casting ConstantLine to subclasses."""

        def __init__(self: "ConstantLine._Cast_ConstantLine", parent: "ConstantLine"):
            self._parent = parent

        @property
        def mode_constant_line(
            self: "ConstantLine._Cast_ConstantLine",
        ) -> "_1865.ModeConstantLine":
            from mastapy.utility_gui.charts import _1865

            return self._parent._cast(_1865.ModeConstantLine)

        @property
        def constant_line(self: "ConstantLine._Cast_ConstantLine") -> "ConstantLine":
            return self._parent

        def __getattr__(self: "ConstantLine._Cast_ConstantLine", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConstantLine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axis(self: Self) -> "_1871.SMTAxis":
        """mastapy.utility_gui.charts.SMTAxis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Axis

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.UtilityGUI.Charts.SMTAxis")

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility_gui.charts._1871", "SMTAxis"
        )(value)

    @property
    def end(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.End

        if temp is None:
            return 0.0

        return temp

    @property
    def label(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Label

        if temp is None:
            return ""

        return temp

    @property
    def start(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Start

        if temp is None:
            return 0.0

        return temp

    @property
    def value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ConstantLine._Cast_ConstantLine":
        return self._Cast_ConstantLine(self)
