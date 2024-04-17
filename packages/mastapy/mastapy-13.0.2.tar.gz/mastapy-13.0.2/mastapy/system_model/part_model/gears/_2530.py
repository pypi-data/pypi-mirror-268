"""ConicalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2537
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2538,
        _2520,
        _2522,
        _2524,
        _2525,
        _2526,
        _2541,
        _2543,
        _2545,
        _2547,
        _2550,
        _2552,
        _2554,
        _2556,
        _2557,
        _2560,
    )
    from mastapy.gears.gear_designs.conical import _1160
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGear",)


Self = TypeVar("Self", bound="ConicalGear")


class ConicalGear(_2537.Gear):
    """ConicalGear

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGear")

    class _Cast_ConicalGear:
        """Special nested class for casting ConicalGear to subclasses."""

        def __init__(self: "ConicalGear._Cast_ConicalGear", parent: "ConicalGear"):
            self._parent = parent

        @property
        def gear(self: "ConicalGear._Cast_ConicalGear") -> "_2537.Gear":
            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "ConicalGear._Cast_ConicalGear") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "ConicalGear._Cast_ConicalGear") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def agma_gleason_conical_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2522.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2524.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2525.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "ConicalGear._Cast_ConicalGear") -> "_2526.BevelGear":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.BevelGear)

        @property
        def hypoid_gear(self: "ConicalGear._Cast_ConicalGear") -> "_2541.HypoidGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2543.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2545.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2547.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2550.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2552.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2554.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2556.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2557.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2560.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.ZerolBevelGear)

        @property
        def conical_gear(self: "ConicalGear._Cast_ConicalGear") -> "ConicalGear":
            return self._parent

        def __getattr__(self: "ConicalGear._Cast_ConicalGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def orientation(self: Self) -> "_2538.GearOrientations":
        """mastapy.system_model.part_model.gears.GearOrientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.gears._2538", "GearOrientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "_2538.GearOrientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self: Self) -> "_1160.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_design(self: Self) -> "_1160.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGear._Cast_ConicalGear":
        return self._Cast_ConicalGear(self)
