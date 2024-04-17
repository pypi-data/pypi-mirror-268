"""BlankRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BLANK_ROW = python_net_import("SMT.MastaAPI.Utility.Report", "BlankRow")

if TYPE_CHECKING:
    from mastapy.utility.report import _1780


__docformat__ = "restructuredtext en"
__all__ = ("BlankRow",)


Self = TypeVar("Self", bound="BlankRow")


class BlankRow(_1785.CustomRow):
    """BlankRow

    This is a mastapy class.
    """

    TYPE = _BLANK_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BlankRow")

    class _Cast_BlankRow:
        """Special nested class for casting BlankRow to subclasses."""

        def __init__(self: "BlankRow._Cast_BlankRow", parent: "BlankRow"):
            self._parent = parent

        @property
        def custom_row(self: "BlankRow._Cast_BlankRow") -> "_1785.CustomRow":
            return self._parent._cast(_1785.CustomRow)

        @property
        def custom_report_property_item(
            self: "BlankRow._Cast_BlankRow",
        ) -> "_1780.CustomReportPropertyItem":
            from mastapy.utility.report import _1780

            return self._parent._cast(_1780.CustomReportPropertyItem)

        @property
        def blank_row(self: "BlankRow._Cast_BlankRow") -> "BlankRow":
            return self._parent

        def __getattr__(self: "BlankRow._Cast_BlankRow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BlankRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BlankRow._Cast_BlankRow":
        return self._Cast_BlankRow(self)
