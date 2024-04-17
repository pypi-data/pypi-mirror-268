"""CustomReportHorizontalLine"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.report import _1770
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_HORIZONTAL_LINE = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportHorizontalLine"
)


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportHorizontalLine",)


Self = TypeVar("Self", bound="CustomReportHorizontalLine")


class CustomReportHorizontalLine(_1770.CustomReportItem):
    """CustomReportHorizontalLine

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_HORIZONTAL_LINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportHorizontalLine")

    class _Cast_CustomReportHorizontalLine:
        """Special nested class for casting CustomReportHorizontalLine to subclasses."""

        def __init__(
            self: "CustomReportHorizontalLine._Cast_CustomReportHorizontalLine",
            parent: "CustomReportHorizontalLine",
        ):
            self._parent = parent

        @property
        def custom_report_item(
            self: "CustomReportHorizontalLine._Cast_CustomReportHorizontalLine",
        ) -> "_1770.CustomReportItem":
            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_horizontal_line(
            self: "CustomReportHorizontalLine._Cast_CustomReportHorizontalLine",
        ) -> "CustomReportHorizontalLine":
            return self._parent

        def __getattr__(
            self: "CustomReportHorizontalLine._Cast_CustomReportHorizontalLine",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportHorizontalLine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CustomReportHorizontalLine._Cast_CustomReportHorizontalLine":
        return self._Cast_CustomReportHorizontalLine(self)
