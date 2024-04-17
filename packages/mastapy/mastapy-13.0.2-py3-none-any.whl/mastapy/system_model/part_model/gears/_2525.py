"""BevelDifferentialSunGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2522
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526, _2520, _2530, _2537
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGear",)


Self = TypeVar("Self", bound="BevelDifferentialSunGear")


class BevelDifferentialSunGear(_2522.BevelDifferentialGear):
    """BevelDifferentialSunGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialSunGear")

    class _Cast_BevelDifferentialSunGear:
        """Special nested class for casting BevelDifferentialSunGear to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
            parent: "BevelDifferentialSunGear",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2522.BevelDifferentialGear":
            return self._parent._cast(_2522.BevelDifferentialGear)

        @property
        def bevel_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2526.BevelGear":
            from mastapy.system_model.part_model.gears import _2526

            return self._parent._cast(_2526.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2520.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2530.ConicalGear":
            from mastapy.system_model.part_model.gears import _2530

            return self._parent._cast(_2530.ConicalGear)

        @property
        def gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2537.Gear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.Gear)

        @property
        def mountable_component(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bevel_differential_sun_gear(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear",
        ) -> "BevelDifferentialSunGear":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialSunGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialSunGear._Cast_BevelDifferentialSunGear":
        return self._Cast_BevelDifferentialSunGear(self)
