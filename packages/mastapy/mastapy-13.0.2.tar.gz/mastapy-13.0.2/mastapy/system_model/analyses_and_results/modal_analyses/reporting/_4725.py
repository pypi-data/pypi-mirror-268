"""CampbellDiagramReport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.report import _1763
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAMPBELL_DIAGRAM_REPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Reporting",
    "CampbellDiagramReport",
)

if TYPE_CHECKING:
    from mastapy.utility.report import _1776, _1777, _1778, _1770


__docformat__ = "restructuredtext en"
__all__ = ("CampbellDiagramReport",)


Self = TypeVar("Self", bound="CampbellDiagramReport")


class CampbellDiagramReport(_1763.CustomReportChart):
    """CampbellDiagramReport

    This is a mastapy class.
    """

    TYPE = _CAMPBELL_DIAGRAM_REPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CampbellDiagramReport")

    class _Cast_CampbellDiagramReport:
        """Special nested class for casting CampbellDiagramReport to subclasses."""

        def __init__(
            self: "CampbellDiagramReport._Cast_CampbellDiagramReport",
            parent: "CampbellDiagramReport",
        ):
            self._parent = parent

        @property
        def custom_report_chart(
            self: "CampbellDiagramReport._Cast_CampbellDiagramReport",
        ) -> "_1763.CustomReportChart":
            return self._parent._cast(_1763.CustomReportChart)

        @property
        def custom_report_multi_property_item(
            self: "CampbellDiagramReport._Cast_CampbellDiagramReport",
        ) -> "_1776.CustomReportMultiPropertyItem":
            pass

            from mastapy.utility.report import _1776

            return self._parent._cast(_1776.CustomReportMultiPropertyItem)

        @property
        def custom_report_multi_property_item_base(
            self: "CampbellDiagramReport._Cast_CampbellDiagramReport",
        ) -> "_1777.CustomReportMultiPropertyItemBase":
            from mastapy.utility.report import _1777

            return self._parent._cast(_1777.CustomReportMultiPropertyItemBase)

        @property
        def custom_report_nameable_item(
            self: "CampbellDiagramReport._Cast_CampbellDiagramReport",
        ) -> "_1778.CustomReportNameableItem":
            from mastapy.utility.report import _1778

            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CampbellDiagramReport._Cast_CampbellDiagramReport",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def campbell_diagram_report(
            self: "CampbellDiagramReport._Cast_CampbellDiagramReport",
        ) -> "CampbellDiagramReport":
            return self._parent

        def __getattr__(
            self: "CampbellDiagramReport._Cast_CampbellDiagramReport", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CampbellDiagramReport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CampbellDiagramReport._Cast_CampbellDiagramReport":
        return self._Cast_CampbellDiagramReport(self)
