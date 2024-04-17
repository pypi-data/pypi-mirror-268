"""HypoidMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.agma_gleason_conical import _1202
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Hypoid", "HypoidMeshedGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1165
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("HypoidMeshedGearDesign",)


Self = TypeVar("Self", bound="HypoidMeshedGearDesign")


class HypoidMeshedGearDesign(_1202.AGMAGleasonConicalMeshedGearDesign):
    """HypoidMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _HYPOID_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidMeshedGearDesign")

    class _Cast_HypoidMeshedGearDesign:
        """Special nested class for casting HypoidMeshedGearDesign to subclasses."""

        def __init__(
            self: "HypoidMeshedGearDesign._Cast_HypoidMeshedGearDesign",
            parent: "HypoidMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "HypoidMeshedGearDesign._Cast_HypoidMeshedGearDesign",
        ) -> "_1202.AGMAGleasonConicalMeshedGearDesign":
            return self._parent._cast(_1202.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "HypoidMeshedGearDesign._Cast_HypoidMeshedGearDesign",
        ) -> "_1165.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "HypoidMeshedGearDesign._Cast_HypoidMeshedGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def hypoid_meshed_gear_design(
            self: "HypoidMeshedGearDesign._Cast_HypoidMeshedGearDesign",
        ) -> "HypoidMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "HypoidMeshedGearDesign._Cast_HypoidMeshedGearDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidMeshedGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "HypoidMeshedGearDesign._Cast_HypoidMeshedGearDesign":
        return self._Cast_HypoidMeshedGearDesign(self)
