"""SpiralBevelMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._math.vector_2d import Vector2D
from mastapy._internal import conversion
from mastapy.gears.gear_designs.bevel import _1189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.SpiralBevel", "SpiralBevelMeshedGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.agma_gleason_conical import _1202
    from mastapy.gears.gear_designs.conical import _1165
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelMeshedGearDesign",)


Self = TypeVar("Self", bound="SpiralBevelMeshedGearDesign")


class SpiralBevelMeshedGearDesign(_1189.BevelMeshedGearDesign):
    """SpiralBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelMeshedGearDesign")

    class _Cast_SpiralBevelMeshedGearDesign:
        """Special nested class for casting SpiralBevelMeshedGearDesign to subclasses."""

        def __init__(
            self: "SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign",
            parent: "SpiralBevelMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_meshed_gear_design(
            self: "SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign",
        ) -> "_1189.BevelMeshedGearDesign":
            return self._parent._cast(_1189.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign",
        ) -> "_1202.AGMAGleasonConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1202

            return self._parent._cast(_1202.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign",
        ) -> "_1165.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign",
        ) -> "SpiralBevelMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelMeshedGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def tip_point_at_mean_section(self: Self) -> "Vector2D":
        """Vector2D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipPointAtMeanSection

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector2d(temp)

        if value is None:
            return None

        return value

    @property
    def tip_thickness_at_mean_section(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipThicknessAtMeanSection

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelMeshedGearDesign._Cast_SpiralBevelMeshedGearDesign":
        return self._Cast_SpiralBevelMeshedGearDesign(self)
