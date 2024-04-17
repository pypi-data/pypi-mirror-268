"""HypoidGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2520
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _989
    from mastapy.system_model.part_model.gears import _2530, _2537
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGear",)


Self = TypeVar("Self", bound="HypoidGear")


class HypoidGear(_2520.AGMAGleasonConicalGear):
    """HypoidGear

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGear")

    class _Cast_HypoidGear:
        """Special nested class for casting HypoidGear to subclasses."""

        def __init__(self: "HypoidGear._Cast_HypoidGear", parent: "HypoidGear"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear(
            self: "HypoidGear._Cast_HypoidGear",
        ) -> "_2520.AGMAGleasonConicalGear":
            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def conical_gear(self: "HypoidGear._Cast_HypoidGear") -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def gear(self: "HypoidGear._Cast_HypoidGear") -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "HypoidGear._Cast_HypoidGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "HypoidGear._Cast_HypoidGear") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "HypoidGear._Cast_HypoidGear") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "HypoidGear._Cast_HypoidGear") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def hypoid_gear(self: "HypoidGear._Cast_HypoidGear") -> "HypoidGear":
            return self._parent

        def __getattr__(self: "HypoidGear._Cast_HypoidGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self: Self) -> "_989.HypoidGearDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_design(self: Self) -> "_989.HypoidGearDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGear._Cast_HypoidGear":
        return self._Cast_HypoidGear(self)
