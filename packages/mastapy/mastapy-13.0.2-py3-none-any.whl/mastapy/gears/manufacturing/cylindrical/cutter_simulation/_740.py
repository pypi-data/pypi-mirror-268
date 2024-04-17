"""FinishStockPoint"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINISH_STOCK_POINT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation", "FinishStockPoint"
)


__docformat__ = "restructuredtext en"
__all__ = ("FinishStockPoint",)


Self = TypeVar("Self", bound="FinishStockPoint")


class FinishStockPoint(_0.APIBase):
    """FinishStockPoint

    This is a mastapy class.
    """

    TYPE = _FINISH_STOCK_POINT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FinishStockPoint")

    class _Cast_FinishStockPoint:
        """Special nested class for casting FinishStockPoint to subclasses."""

        def __init__(
            self: "FinishStockPoint._Cast_FinishStockPoint", parent: "FinishStockPoint"
        ):
            self._parent = parent

        @property
        def finish_stock_point(
            self: "FinishStockPoint._Cast_FinishStockPoint",
        ) -> "FinishStockPoint":
            return self._parent

        def __getattr__(self: "FinishStockPoint._Cast_FinishStockPoint", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FinishStockPoint.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_stock_arc_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishStockArcLength

        if temp is None:
            return 0.0

        return temp

    @property
    def finish_stock_tangent_to_the_base_circle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishStockTangentToTheBaseCircle

        if temp is None:
            return 0.0

        return temp

    @property
    def index(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Index

        if temp is None:
            return ""

        return temp

    @index.setter
    @enforce_parameter_types
    def index(self: Self, value: "str"):
        self.wrapped.Index = str(value) if value is not None else ""

    @property
    def radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "FinishStockPoint._Cast_FinishStockPoint":
        return self._Cast_FinishStockPoint(self)
