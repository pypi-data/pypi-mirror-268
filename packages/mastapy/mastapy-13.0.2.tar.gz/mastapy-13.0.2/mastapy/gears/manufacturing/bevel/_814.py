"""Wheel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WHEEL = python_net_import("SMT.MastaAPI.Gears.Manufacturing.Bevel", "Wheel")

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel.basic_machine_settings import _824
    from mastapy.gears.manufacturing.bevel.cutters import _818


__docformat__ = "restructuredtext en"
__all__ = ("Wheel",)


Self = TypeVar("Self", bound="Wheel")


class Wheel(_0.APIBase):
    """Wheel

    This is a mastapy class.
    """

    TYPE = _WHEEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Wheel")

    class _Cast_Wheel:
        """Special nested class for casting Wheel to subclasses."""

        def __init__(self: "Wheel._Cast_Wheel", parent: "Wheel"):
            self._parent = parent

        @property
        def wheel(self: "Wheel._Cast_Wheel") -> "Wheel":
            return self._parent

        def __getattr__(self: "Wheel._Cast_Wheel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Wheel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_conical_gear_machine_settings(
        self: Self,
    ) -> "_824.BasicConicalGearMachineSettings":
        """mastapy.gears.manufacturing.bevel.basic_machine_settings.BasicConicalGearMachineSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicConicalGearMachineSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_finish_cutter(self: Self) -> "_818.WheelFinishCutter":
        """mastapy.gears.manufacturing.bevel.cutters.WheelFinishCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelFinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Wheel._Cast_Wheel":
        return self._Cast_Wheel(self)
