"""ZerolBevelGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2526
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _956
    from mastapy.system_model.part_model.gears import _2520, _2530, _2537
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGear",)


Self = TypeVar("Self", bound="ZerolBevelGear")


class ZerolBevelGear(_2526.BevelGear):
    """ZerolBevelGear

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGear")

    class _Cast_ZerolBevelGear:
        """Special nested class for casting ZerolBevelGear to subclasses."""

        def __init__(
            self: "ZerolBevelGear._Cast_ZerolBevelGear", parent: "ZerolBevelGear"
        ):
            self._parent = parent

        @property
        def bevel_gear(
            self: "ZerolBevelGear._Cast_ZerolBevelGear",
        ) -> "_2526.BevelGear":
            return self._parent._cast(_2526.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "ZerolBevelGear._Cast_ZerolBevelGear",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "ZerolBevelGear._Cast_ZerolBevelGear",
        ) -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def gear(self: "ZerolBevelGear._Cast_ZerolBevelGear") -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "ZerolBevelGear._Cast_ZerolBevelGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "ZerolBevelGear._Cast_ZerolBevelGear") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "ZerolBevelGear._Cast_ZerolBevelGear") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "ZerolBevelGear._Cast_ZerolBevelGear",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def zerol_bevel_gear(
            self: "ZerolBevelGear._Cast_ZerolBevelGear",
        ) -> "ZerolBevelGear":
            return self._parent

        def __getattr__(self: "ZerolBevelGear._Cast_ZerolBevelGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_design(self: Self) -> "_956.ZerolBevelGearDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gear_design(self: Self) -> "_956.ZerolBevelGearDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ZerolBevelGear._Cast_ZerolBevelGear":
        return self._Cast_ZerolBevelGear(self)
