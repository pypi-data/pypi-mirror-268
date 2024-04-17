"""PinionRoughCutter"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.conical import _1159
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_ROUGH_CUTTER = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.Cutters", "PinionRoughCutter"
)


__docformat__ = "restructuredtext en"
__all__ = ("PinionRoughCutter",)


Self = TypeVar("Self", bound="PinionRoughCutter")


class PinionRoughCutter(_1159.ConicalGearCutter):
    """PinionRoughCutter

    This is a mastapy class.
    """

    TYPE = _PINION_ROUGH_CUTTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PinionRoughCutter")

    class _Cast_PinionRoughCutter:
        """Special nested class for casting PinionRoughCutter to subclasses."""

        def __init__(
            self: "PinionRoughCutter._Cast_PinionRoughCutter",
            parent: "PinionRoughCutter",
        ):
            self._parent = parent

        @property
        def conical_gear_cutter(
            self: "PinionRoughCutter._Cast_PinionRoughCutter",
        ) -> "_1159.ConicalGearCutter":
            return self._parent._cast(_1159.ConicalGearCutter)

        @property
        def pinion_rough_cutter(
            self: "PinionRoughCutter._Cast_PinionRoughCutter",
        ) -> "PinionRoughCutter":
            return self._parent

        def __getattr__(self: "PinionRoughCutter._Cast_PinionRoughCutter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PinionRoughCutter.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self: Self) -> "PinionRoughCutter._Cast_PinionRoughCutter":
        return self._Cast_PinionRoughCutter(self)
