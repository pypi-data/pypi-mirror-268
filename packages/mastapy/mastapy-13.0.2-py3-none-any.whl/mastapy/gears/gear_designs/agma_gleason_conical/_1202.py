"""AGMAGleasonConicalMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.conical import _1165
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical",
    "AGMAGleasonConicalMeshedGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _959
    from mastapy.gears.gear_designs.straight_bevel import _968
    from mastapy.gears.gear_designs.straight_bevel_diff import _972
    from mastapy.gears.gear_designs.spiral_bevel import _976
    from mastapy.gears.gear_designs.hypoid import _992
    from mastapy.gears.gear_designs.bevel import _1189
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalMeshedGearDesign",)


Self = TypeVar("Self", bound="AGMAGleasonConicalMeshedGearDesign")


class AGMAGleasonConicalMeshedGearDesign(_1165.ConicalMeshedGearDesign):
    """AGMAGleasonConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalMeshedGearDesign")

    class _Cast_AGMAGleasonConicalMeshedGearDesign:
        """Special nested class for casting AGMAGleasonConicalMeshedGearDesign to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
            parent: "AGMAGleasonConicalMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def conical_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_1165.ConicalMeshedGearDesign":
            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_959.ZerolBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _959

            return self._parent._cast(_959.ZerolBevelMeshedGearDesign)

        @property
        def straight_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_968.StraightBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _968

            return self._parent._cast(_968.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_972.StraightBevelDiffMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _972

            return self._parent._cast(_972.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_976.SpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _976

            return self._parent._cast(_976.SpiralBevelMeshedGearDesign)

        @property
        def hypoid_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_992.HypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.hypoid import _992

            return self._parent._cast(_992.HypoidMeshedGearDesign)

        @property
        def bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_1189.BevelMeshedGearDesign":
            from mastapy.gears.gear_designs.bevel import _1189

            return self._parent._cast(_1189.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "AGMAGleasonConicalMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalMeshedGearDesign.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_normal_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_topland_to_module_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumToplandToModuleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def required_mean_normal_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredMeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign":
        return self._Cast_AGMAGleasonConicalMeshedGearDesign(self)
