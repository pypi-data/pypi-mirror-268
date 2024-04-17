"""WheelRoughCutter"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.conical import _1159
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WHEEL_ROUGH_CUTTER = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.Cutters", "WheelRoughCutter"
)


__docformat__ = "restructuredtext en"
__all__ = ("WheelRoughCutter",)


Self = TypeVar("Self", bound="WheelRoughCutter")


class WheelRoughCutter(_1159.ConicalGearCutter):
    """WheelRoughCutter

    This is a mastapy class.
    """

    TYPE = _WHEEL_ROUGH_CUTTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WheelRoughCutter")

    class _Cast_WheelRoughCutter:
        """Special nested class for casting WheelRoughCutter to subclasses."""

        def __init__(
            self: "WheelRoughCutter._Cast_WheelRoughCutter", parent: "WheelRoughCutter"
        ):
            self._parent = parent

        @property
        def conical_gear_cutter(
            self: "WheelRoughCutter._Cast_WheelRoughCutter",
        ) -> "_1159.ConicalGearCutter":
            return self._parent._cast(_1159.ConicalGearCutter)

        @property
        def wheel_rough_cutter(
            self: "WheelRoughCutter._Cast_WheelRoughCutter",
        ) -> "WheelRoughCutter":
            return self._parent

        def __getattr__(self: "WheelRoughCutter._Cast_WheelRoughCutter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WheelRoughCutter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def delta_bg(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaBG

        if temp is None:
            return 0.0

        return temp

    @delta_bg.setter
    @enforce_parameter_types
    def delta_bg(self: Self, value: "float"):
        self.wrapped.DeltaBG = float(value) if value is not None else 0.0

    @property
    def inner_blade_point_radius_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerBladePointRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_blade_point_radius_convex.setter
    @enforce_parameter_types
    def inner_blade_point_radius_convex(self: Self, value: "float"):
        self.wrapped.InnerBladePointRadiusConvex = (
            float(value) if value is not None else 0.0
        )

    @property
    def outer_blade_point_radius_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterBladePointRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_blade_point_radius_concave.setter
    @enforce_parameter_types
    def outer_blade_point_radius_concave(self: Self, value: "float"):
        self.wrapped.OuterBladePointRadiusConcave = (
            float(value) if value is not None else 0.0
        )

    @property
    def point_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PointWidth

        if temp is None:
            return 0.0

        return temp

    @point_width.setter
    @enforce_parameter_types
    def point_width(self: Self, value: "float"):
        self.wrapped.PointWidth = float(value) if value is not None else 0.0

    @property
    def stock_allowance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StockAllowance

        if temp is None:
            return 0.0

        return temp

    @stock_allowance.setter
    @enforce_parameter_types
    def stock_allowance(self: Self, value: "float"):
        self.wrapped.StockAllowance = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "WheelRoughCutter._Cast_WheelRoughCutter":
        return self._Cast_WheelRoughCutter(self)
