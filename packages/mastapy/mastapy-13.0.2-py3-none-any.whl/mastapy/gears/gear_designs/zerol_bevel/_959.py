"""ZerolBevelMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.bevel import _1189
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.ZerolBevel", "ZerolBevelMeshedGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.agma_gleason_conical import _1202
    from mastapy.gears.gear_designs.conical import _1165
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelMeshedGearDesign",)


Self = TypeVar("Self", bound="ZerolBevelMeshedGearDesign")


class ZerolBevelMeshedGearDesign(_1189.BevelMeshedGearDesign):
    """ZerolBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelMeshedGearDesign")

    class _Cast_ZerolBevelMeshedGearDesign:
        """Special nested class for casting ZerolBevelMeshedGearDesign to subclasses."""

        def __init__(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
            parent: "ZerolBevelMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def bevel_meshed_gear_design(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ) -> "_1189.BevelMeshedGearDesign":
            return self._parent._cast(_1189.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ) -> "_1202.AGMAGleasonConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1202

            return self._parent._cast(_1202.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ) -> "_1165.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
        ) -> "ZerolBevelMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ZerolBevelMeshedGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelMeshedGearDesign._Cast_ZerolBevelMeshedGearDesign":
        return self._Cast_ZerolBevelMeshedGearDesign(self)
