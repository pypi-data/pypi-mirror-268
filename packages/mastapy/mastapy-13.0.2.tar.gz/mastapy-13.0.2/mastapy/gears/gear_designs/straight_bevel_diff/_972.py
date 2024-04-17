"""StraightBevelDiffMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.bevel import _1189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff",
    "StraightBevelDiffMeshedGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.agma_gleason_conical import _1202
    from mastapy.gears.gear_designs.conical import _1165
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffMeshedGearDesign",)


Self = TypeVar("Self", bound="StraightBevelDiffMeshedGearDesign")


class StraightBevelDiffMeshedGearDesign(_1189.BevelMeshedGearDesign):
    """StraightBevelDiffMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffMeshedGearDesign")

    class _Cast_StraightBevelDiffMeshedGearDesign:
        """Special nested class for casting StraightBevelDiffMeshedGearDesign to subclasses."""

        def __init__(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
            parent: "StraightBevelDiffMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_meshed_gear_design(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "_1189.BevelMeshedGearDesign":
            return self._parent._cast(_1189.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "_1202.AGMAGleasonConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1202

            return self._parent._cast(_1202.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "_1165.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
        ) -> "StraightBevelDiffMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign",
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
        self: Self, instance_to_wrap: "StraightBevelDiffMeshedGearDesign.TYPE"
    ):
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
    def mean_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanTopland

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
    ) -> "StraightBevelDiffMeshedGearDesign._Cast_StraightBevelDiffMeshedGearDesign":
        return self._Cast_StraightBevelDiffMeshedGearDesign(self)
