"""MagnetForLayer"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.electric_machines import _1287
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNET_FOR_LAYER = python_net_import("SMT.MastaAPI.ElectricMachines", "MagnetForLayer")


__docformat__ = "restructuredtext en"
__all__ = ("MagnetForLayer",)


Self = TypeVar("Self", bound="MagnetForLayer")


class MagnetForLayer(_1287.MagnetDesign):
    """MagnetForLayer

    This is a mastapy class.
    """

    TYPE = _MAGNET_FOR_LAYER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagnetForLayer")

    class _Cast_MagnetForLayer:
        """Special nested class for casting MagnetForLayer to subclasses."""

        def __init__(
            self: "MagnetForLayer._Cast_MagnetForLayer", parent: "MagnetForLayer"
        ):
            self._parent = parent

        @property
        def magnet_design(
            self: "MagnetForLayer._Cast_MagnetForLayer",
        ) -> "_1287.MagnetDesign":
            return self._parent._cast(_1287.MagnetDesign)

        @property
        def magnet_for_layer(
            self: "MagnetForLayer._Cast_MagnetForLayer",
        ) -> "MagnetForLayer":
            return self._parent

        def __getattr__(self: "MagnetForLayer._Cast_MagnetForLayer", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagnetForLayer.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_segments_along_width(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSegmentsAlongWidth

        if temp is None:
            return 0

        return temp

    @number_of_segments_along_width.setter
    @enforce_parameter_types
    def number_of_segments_along_width(self: Self, value: "int"):
        self.wrapped.NumberOfSegmentsAlongWidth = int(value) if value is not None else 0

    @property
    def thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Thickness

        if temp is None:
            return 0.0

        return temp

    @thickness.setter
    @enforce_parameter_types
    def thickness(self: Self, value: "float"):
        self.wrapped.Thickness = float(value) if value is not None else 0.0

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def width_of_each_segment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WidthOfEachSegment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "MagnetForLayer._Cast_MagnetForLayer":
        return self._Cast_MagnetForLayer(self)
