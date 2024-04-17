"""WormGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGear")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.worm import _961
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("WormGear",)


Self = TypeVar("Self", bound="WormGear")


class WormGear(_2537.Gear):
    """WormGear

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGear")

    class _Cast_WormGear:
        """Special nested class for casting WormGear to subclasses."""

        def __init__(self: "WormGear._Cast_WormGear", parent: "WormGear"):
            self._parent = parent

        @property
        def gear(self: "WormGear._Cast_WormGear") -> "_2537.Gear":
            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "WormGear._Cast_WormGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "WormGear._Cast_WormGear") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "WormGear._Cast_WormGear") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "WormGear._Cast_WormGear") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def worm_gear(self: "WormGear._Cast_WormGear") -> "WormGear":
            return self._parent

        def __getattr__(self: "WormGear._Cast_WormGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_design(self: Self) -> "_961.WormGearDesign":
        """mastapy.gears.gear_designs.worm.WormGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gear_design(self: Self) -> "_961.WormGearDesign":
        """mastapy.gears.gear_designs.worm.WormGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "WormGear._Cast_WormGear":
        return self._Cast_WormGear(self)
