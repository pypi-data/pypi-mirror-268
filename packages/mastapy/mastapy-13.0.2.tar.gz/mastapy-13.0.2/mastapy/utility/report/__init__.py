"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1749 import AdHocCustomTable
    from ._1750 import AxisSettings
    from ._1751 import BlankRow
    from ._1752 import CadPageOrientation
    from ._1753 import CadPageSize
    from ._1754 import CadTableBorderType
    from ._1755 import ChartDefinition
    from ._1756 import SMTChartPointShape
    from ._1757 import CustomChart
    from ._1758 import CustomDrawing
    from ._1759 import CustomGraphic
    from ._1760 import CustomImage
    from ._1761 import CustomReport
    from ._1762 import CustomReportCadDrawing
    from ._1763 import CustomReportChart
    from ._1764 import CustomReportChartItem
    from ._1765 import CustomReportColumn
    from ._1766 import CustomReportColumns
    from ._1767 import CustomReportDefinitionItem
    from ._1768 import CustomReportHorizontalLine
    from ._1769 import CustomReportHtmlItem
    from ._1770 import CustomReportItem
    from ._1771 import CustomReportItemContainer
    from ._1772 import CustomReportItemContainerCollection
    from ._1773 import CustomReportItemContainerCollectionBase
    from ._1774 import CustomReportItemContainerCollectionItem
    from ._1775 import CustomReportKey
    from ._1776 import CustomReportMultiPropertyItem
    from ._1777 import CustomReportMultiPropertyItemBase
    from ._1778 import CustomReportNameableItem
    from ._1779 import CustomReportNamedItem
    from ._1780 import CustomReportPropertyItem
    from ._1781 import CustomReportStatusItem
    from ._1782 import CustomReportTab
    from ._1783 import CustomReportTabs
    from ._1784 import CustomReportText
    from ._1785 import CustomRow
    from ._1786 import CustomSubReport
    from ._1787 import CustomTable
    from ._1788 import DefinitionBooleanCheckOptions
    from ._1789 import DynamicCustomReportItem
    from ._1790 import FontStyle
    from ._1791 import FontWeight
    from ._1792 import HeadingSize
    from ._1793 import SimpleChartDefinition
    from ._1794 import UserTextRow
else:
    import_structure = {
        "_1749": ["AdHocCustomTable"],
        "_1750": ["AxisSettings"],
        "_1751": ["BlankRow"],
        "_1752": ["CadPageOrientation"],
        "_1753": ["CadPageSize"],
        "_1754": ["CadTableBorderType"],
        "_1755": ["ChartDefinition"],
        "_1756": ["SMTChartPointShape"],
        "_1757": ["CustomChart"],
        "_1758": ["CustomDrawing"],
        "_1759": ["CustomGraphic"],
        "_1760": ["CustomImage"],
        "_1761": ["CustomReport"],
        "_1762": ["CustomReportCadDrawing"],
        "_1763": ["CustomReportChart"],
        "_1764": ["CustomReportChartItem"],
        "_1765": ["CustomReportColumn"],
        "_1766": ["CustomReportColumns"],
        "_1767": ["CustomReportDefinitionItem"],
        "_1768": ["CustomReportHorizontalLine"],
        "_1769": ["CustomReportHtmlItem"],
        "_1770": ["CustomReportItem"],
        "_1771": ["CustomReportItemContainer"],
        "_1772": ["CustomReportItemContainerCollection"],
        "_1773": ["CustomReportItemContainerCollectionBase"],
        "_1774": ["CustomReportItemContainerCollectionItem"],
        "_1775": ["CustomReportKey"],
        "_1776": ["CustomReportMultiPropertyItem"],
        "_1777": ["CustomReportMultiPropertyItemBase"],
        "_1778": ["CustomReportNameableItem"],
        "_1779": ["CustomReportNamedItem"],
        "_1780": ["CustomReportPropertyItem"],
        "_1781": ["CustomReportStatusItem"],
        "_1782": ["CustomReportTab"],
        "_1783": ["CustomReportTabs"],
        "_1784": ["CustomReportText"],
        "_1785": ["CustomRow"],
        "_1786": ["CustomSubReport"],
        "_1787": ["CustomTable"],
        "_1788": ["DefinitionBooleanCheckOptions"],
        "_1789": ["DynamicCustomReportItem"],
        "_1790": ["FontStyle"],
        "_1791": ["FontWeight"],
        "_1792": ["HeadingSize"],
        "_1793": ["SimpleChartDefinition"],
        "_1794": ["UserTextRow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdHocCustomTable",
    "AxisSettings",
    "BlankRow",
    "CadPageOrientation",
    "CadPageSize",
    "CadTableBorderType",
    "ChartDefinition",
    "SMTChartPointShape",
    "CustomChart",
    "CustomDrawing",
    "CustomGraphic",
    "CustomImage",
    "CustomReport",
    "CustomReportCadDrawing",
    "CustomReportChart",
    "CustomReportChartItem",
    "CustomReportColumn",
    "CustomReportColumns",
    "CustomReportDefinitionItem",
    "CustomReportHorizontalLine",
    "CustomReportHtmlItem",
    "CustomReportItem",
    "CustomReportItemContainer",
    "CustomReportItemContainerCollection",
    "CustomReportItemContainerCollectionBase",
    "CustomReportItemContainerCollectionItem",
    "CustomReportKey",
    "CustomReportMultiPropertyItem",
    "CustomReportMultiPropertyItemBase",
    "CustomReportNameableItem",
    "CustomReportNamedItem",
    "CustomReportPropertyItem",
    "CustomReportStatusItem",
    "CustomReportTab",
    "CustomReportTabs",
    "CustomReportText",
    "CustomRow",
    "CustomSubReport",
    "CustomTable",
    "DefinitionBooleanCheckOptions",
    "DynamicCustomReportItem",
    "FontStyle",
    "FontWeight",
    "HeadingSize",
    "SimpleChartDefinition",
    "UserTextRow",
)
