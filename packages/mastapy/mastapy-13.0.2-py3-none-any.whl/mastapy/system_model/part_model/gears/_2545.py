"""KlingelnbergCycloPalloidHypoidGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2543
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _981
    from mastapy.system_model.part_model.gears import _2530, _2537
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGear",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGear")


class KlingelnbergCycloPalloidHypoidGear(_2543.KlingelnbergCycloPalloidConicalGear):
    """KlingelnbergCycloPalloidHypoidGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGear")

    class _Cast_KlingelnbergCycloPalloidHypoidGear:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGear to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
            parent: "KlingelnbergCycloPalloidHypoidGear",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
        ) -> "_2543.KlingelnbergCycloPalloidConicalGear":
            return self._parent._cast(_2543.KlingelnbergCycloPalloidConicalGear)

        @property
        def conical_gear(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
        ) -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def gear(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
        ) -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
        ) -> "KlingelnbergCycloPalloidHypoidGear":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGear.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(
        self: Self,
    ) -> "_981.KlingelnbergCycloPalloidHypoidGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_design(
        self: Self,
    ) -> "_981.KlingelnbergCycloPalloidHypoidGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGear._Cast_KlingelnbergCycloPalloidHypoidGear":
        return self._Cast_KlingelnbergCycloPalloidHypoidGear(self)
