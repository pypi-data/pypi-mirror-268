"""DummyConicalGearCutter"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.conical import _1159
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUMMY_CONICAL_GEAR_CUTTER = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "DummyConicalGearCutter"
)


__docformat__ = "restructuredtext en"
__all__ = ("DummyConicalGearCutter",)


Self = TypeVar("Self", bound="DummyConicalGearCutter")


class DummyConicalGearCutter(_1159.ConicalGearCutter):
    """DummyConicalGearCutter

    This is a mastapy class.
    """

    TYPE = _DUMMY_CONICAL_GEAR_CUTTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DummyConicalGearCutter")

    class _Cast_DummyConicalGearCutter:
        """Special nested class for casting DummyConicalGearCutter to subclasses."""

        def __init__(
            self: "DummyConicalGearCutter._Cast_DummyConicalGearCutter",
            parent: "DummyConicalGearCutter",
        ):
            self._parent = parent

        @property
        def conical_gear_cutter(
            self: "DummyConicalGearCutter._Cast_DummyConicalGearCutter",
        ) -> "_1159.ConicalGearCutter":
            return self._parent._cast(_1159.ConicalGearCutter)

        @property
        def dummy_conical_gear_cutter(
            self: "DummyConicalGearCutter._Cast_DummyConicalGearCutter",
        ) -> "DummyConicalGearCutter":
            return self._parent

        def __getattr__(
            self: "DummyConicalGearCutter._Cast_DummyConicalGearCutter", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DummyConicalGearCutter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_cutter_point_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @finish_cutter_point_width.setter
    @enforce_parameter_types
    def finish_cutter_point_width(self: Self, value: "float"):
        self.wrapped.FinishCutterPointWidth = float(value) if value is not None else 0.0

    @property
    def inner_edge_radius_convex(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InnerEdgeRadiusConvex

        if temp is None:
            return 0.0

        return temp

    @inner_edge_radius_convex.setter
    @enforce_parameter_types
    def inner_edge_radius_convex(self: Self, value: "float"):
        self.wrapped.InnerEdgeRadiusConvex = float(value) if value is not None else 0.0

    @property
    def number_of_blade_groups(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfBladeGroups

        if temp is None:
            return 0

        return temp

    @number_of_blade_groups.setter
    @enforce_parameter_types
    def number_of_blade_groups(self: Self, value: "int"):
        self.wrapped.NumberOfBladeGroups = int(value) if value is not None else 0

    @property
    def outer_edge_radius_concave(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterEdgeRadiusConcave

        if temp is None:
            return 0.0

        return temp

    @outer_edge_radius_concave.setter
    @enforce_parameter_types
    def outer_edge_radius_concave(self: Self, value: "float"):
        self.wrapped.OuterEdgeRadiusConcave = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "DummyConicalGearCutter._Cast_DummyConicalGearCutter":
        return self._Cast_DummyConicalGearCutter(self)
