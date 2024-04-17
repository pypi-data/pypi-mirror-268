"""CustomReportCadDrawing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1778
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CAD_DRAWING = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportCadDrawing"
)

if TYPE_CHECKING:
    from mastapy.utility.cad_export import _1840
    from mastapy.utility.report import _1770


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportCadDrawing",)


Self = TypeVar("Self", bound="CustomReportCadDrawing")


class CustomReportCadDrawing(_1778.CustomReportNameableItem):
    """CustomReportCadDrawing

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CAD_DRAWING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomReportCadDrawing")

    class _Cast_CustomReportCadDrawing:
        """Special nested class for casting CustomReportCadDrawing to subclasses."""

        def __init__(
            self: "CustomReportCadDrawing._Cast_CustomReportCadDrawing",
            parent: "CustomReportCadDrawing",
        ):
            self._parent = parent

        @property
        def custom_report_nameable_item(
            self: "CustomReportCadDrawing._Cast_CustomReportCadDrawing",
        ) -> "_1778.CustomReportNameableItem":
            return self._parent._cast(_1778.CustomReportNameableItem)

        @property
        def custom_report_item(
            self: "CustomReportCadDrawing._Cast_CustomReportCadDrawing",
        ) -> "_1770.CustomReportItem":
            from mastapy.utility.report import _1770

            return self._parent._cast(_1770.CustomReportItem)

        @property
        def custom_report_cad_drawing(
            self: "CustomReportCadDrawing._Cast_CustomReportCadDrawing",
        ) -> "CustomReportCadDrawing":
            return self._parent

        def __getattr__(
            self: "CustomReportCadDrawing._Cast_CustomReportCadDrawing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomReportCadDrawing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def scale(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Scale

        if temp is None:
            return 0.0

        return temp

    @scale.setter
    @enforce_parameter_types
    def scale(self: Self, value: "float"):
        self.wrapped.Scale = float(value) if value is not None else 0.0

    @property
    def stock_drawing(self: Self) -> "_1840.StockDrawings":
        """mastapy.utility.cad_export.StockDrawings"""
        temp = self.wrapped.StockDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.CadExport.StockDrawings"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.cad_export._1840", "StockDrawings"
        )(value)

    @stock_drawing.setter
    @enforce_parameter_types
    def stock_drawing(self: Self, value: "_1840.StockDrawings"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.CadExport.StockDrawings"
        )
        self.wrapped.StockDrawing = value

    @property
    def use_stock_drawing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseStockDrawing

        if temp is None:
            return False

        return temp

    @use_stock_drawing.setter
    @enforce_parameter_types
    def use_stock_drawing(self: Self, value: "bool"):
        self.wrapped.UseStockDrawing = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "CustomReportCadDrawing._Cast_CustomReportCadDrawing":
        return self._Cast_CustomReportCadDrawing(self)
