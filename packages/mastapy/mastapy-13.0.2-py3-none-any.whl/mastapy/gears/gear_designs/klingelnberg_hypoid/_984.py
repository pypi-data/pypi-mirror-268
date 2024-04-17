"""KlingelnbergCycloPalloidHypoidMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.klingelnberg_conical import _988
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidMeshedGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1165
    from mastapy.gears.gear_designs import _952


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidMeshedGearDesign",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidMeshedGearDesign")


class KlingelnbergCycloPalloidHypoidMeshedGearDesign(
    _988.KlingelnbergConicalMeshedGearDesign
):
    """KlingelnbergCycloPalloidHypoidMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidMeshedGearDesign to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign",
            parent: "KlingelnbergCycloPalloidHypoidMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_meshed_gear_design(
            self: "KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign",
        ) -> "_988.KlingelnbergConicalMeshedGearDesign":
            return self._parent._cast(_988.KlingelnbergConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign",
        ) -> "_1165.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1165

            return self._parent._cast(_1165.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
            self: "KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign",
        ) -> "KlingelnbergCycloPalloidHypoidMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidMeshedGearDesign.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidMeshedGearDesign._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign":
        return self._Cast_KlingelnbergCycloPalloidHypoidMeshedGearDesign(self)
