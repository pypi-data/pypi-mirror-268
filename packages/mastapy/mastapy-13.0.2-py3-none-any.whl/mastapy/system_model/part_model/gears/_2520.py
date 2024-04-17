"""AGMAGleasonConicalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2530
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2522,
        _2524,
        _2525,
        _2526,
        _2541,
        _2550,
        _2552,
        _2554,
        _2556,
        _2557,
        _2560,
        _2537,
    )
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGear",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGear")


class AGMAGleasonConicalGear(_2530.ConicalGear):
    """AGMAGleasonConicalGear

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGear")

    class _Cast_AGMAGleasonConicalGear:
        """Special nested class for casting AGMAGleasonConicalGear to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
            parent: "AGMAGleasonConicalGear",
        ):
            self._parent = parent

        @property
        def conical_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2530.ConicalGear":
            return self._parent._cast(_2530.ConicalGear)

        @property
        def gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bevel_differential_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2522.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2522

            return self._parent._cast(_2522.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2524.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2525.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.BevelDifferentialSunGear)

        @property
        def bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2526.BevelGear":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.BevelGear)

        @property
        def hypoid_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2541.HypoidGear":
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.HypoidGear)

        @property
        def spiral_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2550.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2552.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2554.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2556.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2557.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "_2560.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2560

            return self._parent._cast(_2560.ZerolBevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear",
        ) -> "AGMAGleasonConicalGear":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AGMAGleasonConicalGear._Cast_AGMAGleasonConicalGear":
        return self._Cast_AGMAGleasonConicalGear(self)
