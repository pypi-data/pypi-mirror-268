"""AGMAGleasonConicalGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2531
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2523,
        _2527,
        _2542,
        _2551,
        _2553,
        _2555,
        _2561,
        _2539,
    )
    from mastapy.system_model.part_model import _2483, _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSet",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSet")


class AGMAGleasonConicalGearSet(_2531.ConicalGearSet):
    """AGMAGleasonConicalGearSet

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSet")

    class _Cast_AGMAGleasonConicalGearSet:
        """Special nested class for casting AGMAGleasonConicalGearSet to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
            parent: "AGMAGleasonConicalGearSet",
        ):
            self._parent = parent

        @property
        def conical_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2531.ConicalGearSet":
            return self._parent._cast(_2531.ConicalGearSet)

        @property
        def gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2539.GearSet":
            from mastapy.system_model.part_model.gears import _2539

            return self._parent._cast(_2539.GearSet)

        @property
        def specialised_assembly(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2483.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2483

            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bevel_differential_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2523.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2523

            return self._parent._cast(_2523.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2527.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.BevelGearSet)

        @property
        def hypoid_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2542.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.HypoidGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2551.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2553.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2555.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2561.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.ZerolBevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "AGMAGleasonConicalGearSet":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet":
        return self._Cast_AGMAGleasonConicalGearSet(self)
