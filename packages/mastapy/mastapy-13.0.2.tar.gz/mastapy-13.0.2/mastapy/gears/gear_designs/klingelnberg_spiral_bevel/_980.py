"""KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.klingelnberg_conical import _988
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergSpiralBevel",
    "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1165
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign")


class KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign(
    _988.KlingelnbergConicalMeshedGearDesign
):
    """KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
            parent: "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_meshed_gear_design(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
        ) -> "_988.KlingelnbergConicalMeshedGearDesign":
            return self._parent._cast(_988.KlingelnbergConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
        ) -> "_1165.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
        ) -> "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign(self)
