"""BevelDifferentialGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2526
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1186
    from mastapy.system_model.part_model.gears import _2524, _2525, _2520, _2530, _2537
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGear",)


Self = TypeVar("Self", bound="BevelDifferentialGear")


class BevelDifferentialGear(_2526.BevelGear):
    """BevelDifferentialGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGear")

    class _Cast_BevelDifferentialGear:
        """Special nested class for casting BevelDifferentialGear to subclasses."""

        def __init__(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
            parent: "BevelDifferentialGear",
        ):
            self._parent = parent

        @property
        def bevel_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2526.BevelGear":
            return self._parent._cast(_2526.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bevel_differential_planet_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2524.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2524

            return self._parent._cast(_2524.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "_2525.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.BevelDifferentialSunGear)

        @property
        def bevel_differential_gear(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear",
        ) -> "BevelDifferentialGear":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGear._Cast_BevelDifferentialGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_design(self: Self) -> "_1186.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelDifferentialGear._Cast_BevelDifferentialGear":
        return self._Cast_BevelDifferentialGear(self)
