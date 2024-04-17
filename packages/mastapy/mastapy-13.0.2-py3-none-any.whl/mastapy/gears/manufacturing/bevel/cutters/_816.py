"""PinionFinishCutter"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.conical import _1159
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_FINISH_CUTTER = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.Cutters", "PinionFinishCutter"
)


__docformat__ = "restructuredtext en"
__all__ = ("PinionFinishCutter",)


Self = TypeVar("Self", bound="PinionFinishCutter")


class PinionFinishCutter(_1159.ConicalGearCutter):
    """PinionFinishCutter

    This is a mastapy class.
    """

    TYPE = _PINION_FINISH_CUTTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PinionFinishCutter")

    class _Cast_PinionFinishCutter:
        """Special nested class for casting PinionFinishCutter to subclasses."""

        def __init__(
            self: "PinionFinishCutter._Cast_PinionFinishCutter",
            parent: "PinionFinishCutter",
        ):
            self._parent = parent

        @property
        def conical_gear_cutter(
            self: "PinionFinishCutter._Cast_PinionFinishCutter",
        ) -> "_1159.ConicalGearCutter":
            return self._parent._cast(_1159.ConicalGearCutter)

        @property
        def pinion_finish_cutter(
            self: "PinionFinishCutter._Cast_PinionFinishCutter",
        ) -> "PinionFinishCutter":
            return self._parent

        def __getattr__(self: "PinionFinishCutter._Cast_PinionFinishCutter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PinionFinishCutter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "float"):
        self.wrapped.Radius = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "PinionFinishCutter._Cast_PinionFinishCutter":
        return self._Cast_PinionFinishCutter(self)
