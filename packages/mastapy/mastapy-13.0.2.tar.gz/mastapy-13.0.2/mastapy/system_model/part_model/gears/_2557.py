"""StraightBevelSunGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526, _2520, _2530, _2537
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGear",)


Self = TypeVar("Self", bound="StraightBevelSunGear")


class StraightBevelSunGear(_2552.StraightBevelDiffGear):
    """StraightBevelSunGear

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelSunGear")

    class _Cast_StraightBevelSunGear:
        """Special nested class for casting StraightBevelSunGear to subclasses."""

        def __init__(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
            parent: "StraightBevelSunGear",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2552.StraightBevelDiffGear":
            return self._parent._cast(_2552.StraightBevelDiffGear)

        @property
        def bevel_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2526.BevelGear":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def straight_bevel_sun_gear(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear",
        ) -> "StraightBevelSunGear":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGear._Cast_StraightBevelSunGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelSunGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StraightBevelSunGear._Cast_StraightBevelSunGear":
        return self._Cast_StraightBevelSunGear(self)
