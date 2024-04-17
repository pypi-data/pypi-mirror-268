"""StraightBevelMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.bevel import _1189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevel", "StraightBevelMeshedGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.agma_gleason_conical import _1202
    from mastapy.gears.gear_designs.conical import _1165
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelMeshedGearDesign",)


Self = TypeVar("Self", bound="StraightBevelMeshedGearDesign")


class StraightBevelMeshedGearDesign(_1189.BevelMeshedGearDesign):
    """StraightBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelMeshedGearDesign")

    class _Cast_StraightBevelMeshedGearDesign:
        """Special nested class for casting StraightBevelMeshedGearDesign to subclasses."""

        def __init__(
            self: "StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign",
            parent: "StraightBevelMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_meshed_gear_design(
            self: "StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign",
        ) -> "_1189.BevelMeshedGearDesign":
            return self._parent._cast(_1189.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign",
        ) -> "_1202.AGMAGleasonConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1202

            return self._parent._cast(_1202.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign",
        ) -> "_1165.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def straight_bevel_meshed_gear_design(
            self: "StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign",
        ) -> "StraightBevelMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelMeshedGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_factor_j(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJ

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelMeshedGearDesign._Cast_StraightBevelMeshedGearDesign":
        return self._Cast_StraightBevelMeshedGearDesign(self)
