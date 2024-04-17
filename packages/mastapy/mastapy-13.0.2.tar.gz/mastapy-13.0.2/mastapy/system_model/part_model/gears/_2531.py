"""ConicalGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2539
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1162
    from mastapy.system_model.part_model.gears import (
        _2530,
        _2521,
        _2523,
        _2527,
        _2542,
        _2544,
        _2546,
        _2548,
        _2551,
        _2553,
        _2555,
        _2561,
    )
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSet",)


Self = TypeVar("Self", bound="ConicalGearSet")


class ConicalGearSet(_2539.GearSet):
    """ConicalGearSet

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSet")

    class _Cast_ConicalGearSet:
        """Special nested class for casting ConicalGearSet to subclasses."""

        def __init__(
            self: "ConicalGearSet._Cast_ConicalGearSet", parent: "ConicalGearSet"
        ):
            self._parent = parent

        @property
        def gear_set(self: "ConicalGearSet._Cast_ConicalGearSet") -> "_2539.GearSet":
            return self._parent._cast(_2539.GearSet)

        @property
        def specialised_assembly(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "ConicalGearSet._Cast_ConicalGearSet") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def agma_gleason_conical_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2521.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2523.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2527.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.BevelGearSet)

        @property
        def hypoid_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2542.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2544.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2544

            return self._parent._cast(_2544.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2546.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2546

            return self._parent._cast(_2546.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2548.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2548

            return self._parent._cast(_2548.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2551.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2553.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2555.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2561.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.ZerolBevelGearSet)

        @property
        def conical_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "ConicalGearSet":
            return self._parent

        def __getattr__(self: "ConicalGearSet._Cast_ConicalGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self: Self) -> "_1162.ConicalGearSetDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_set_design(self: Self) -> "_1162.ConicalGearSetDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears(self: Self) -> "List[_2530.ConicalGear]":
        """List[mastapy.system_model.part_model.gears.ConicalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConicalGearSet._Cast_ConicalGearSet":
        return self._Cast_ConicalGearSet(self)
