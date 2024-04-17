"""WheelFinishCutter"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs.conical import _1159
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WHEEL_FINISH_CUTTER = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel.Cutters", "WheelFinishCutter"
)


__docformat__ = "restructuredtext en"
__all__ = ("WheelFinishCutter",)


Self = TypeVar("Self", bound="WheelFinishCutter")


class WheelFinishCutter(_1159.ConicalGearCutter):
    """WheelFinishCutter

    This is a mastapy class.
    """

    TYPE = _WHEEL_FINISH_CUTTER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WheelFinishCutter")

    class _Cast_WheelFinishCutter:
        """Special nested class for casting WheelFinishCutter to subclasses."""

        def __init__(
            self: "WheelFinishCutter._Cast_WheelFinishCutter",
            parent: "WheelFinishCutter",
        ):
            self._parent = parent

        @property
        def conical_gear_cutter(
            self: "WheelFinishCutter._Cast_WheelFinishCutter",
        ) -> "_1159.ConicalGearCutter":
            return self._parent._cast(_1159.ConicalGearCutter)

        @property
        def wheel_finish_cutter(
            self: "WheelFinishCutter._Cast_WheelFinishCutter",
        ) -> "WheelFinishCutter":
            return self._parent

        def __getattr__(self: "WheelFinishCutter._Cast_WheelFinishCutter", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WheelFinishCutter.TYPE"):
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
    def cast_to(self: Self) -> "WheelFinishCutter._Cast_WheelFinishCutter":
        return self._Cast_WheelFinishCutter(self)
