"""CustomTableAndChart"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_TABLE_AND_CHART = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Charts", "CustomTableAndChart"
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1776, _1777, _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomTableAndChart",)


Self = TypeVar("Self", bound="CustomTableAndChart")


class CustomTableAndChart(_1787.CustomTable):
    """CustomTableAndChart

    This is a mastapy class.
    """

    TYPE = _CUSTOM_TABLE_AND_CHART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomTableAndChart")

    class _Cast_CustomTableAndChart:
        """Special nested class for casting CustomTableAndChart to subclasses."""

        def __init__(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
            parent: "CustomTableAndChart",
        ):
            self._parent = parent

        @property
        def custom_table(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ) -> "_1787.CustomTable":
            return self._parent._cast(_1787.CustomTable)

        @property
        def custom_report_multi_property_item(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ) -> "_1776.CustomReportMultiPropertyItem":
            pass

            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ) -> "_1777.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_table_and_chart(
            self: "CustomTableAndChart._Cast_CustomTableAndChart",
        ) -> "CustomTableAndChart":
            return self._parent

        def __getattr__(
            self: "CustomTableAndChart._Cast_CustomTableAndChart", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomTableAndChart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CustomTableAndChart._Cast_CustomTableAndChart":
        return self._Cast_CustomTableAndChart(self)
