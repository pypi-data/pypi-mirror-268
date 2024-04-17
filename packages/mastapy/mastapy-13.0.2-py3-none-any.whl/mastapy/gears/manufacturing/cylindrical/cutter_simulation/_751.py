"""WormGrinderSimulationCalculator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _746
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDER_SIMULATION_CALCULATOR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "WormGrinderSimulationCalculator",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _731
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734


__docformat__ = "restructuredtext en"
__all__ = ("WormGrinderSimulationCalculator",)


Self = TypeVar("Self", bound="WormGrinderSimulationCalculator")


class WormGrinderSimulationCalculator(_746.RackSimulationCalculator):
    """WormGrinderSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDER_SIMULATION_CALCULATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrinderSimulationCalculator")

    class _Cast_WormGrinderSimulationCalculator:
        """Special nested class for casting WormGrinderSimulationCalculator to subclasses."""

        def __init__(
            self: "WormGrinderSimulationCalculator._Cast_WormGrinderSimulationCalculator",
            parent: "WormGrinderSimulationCalculator",
        ):
            self._parent = parent

        @property
        def rack_simulation_calculator(
            self: "WormGrinderSimulationCalculator._Cast_WormGrinderSimulationCalculator",
        ) -> "_746.RackSimulationCalculator":
            return self._parent._cast(_746.RackSimulationCalculator)

        @property
        def cutter_simulation_calc(
            self: "WormGrinderSimulationCalculator._Cast_WormGrinderSimulationCalculator",
        ) -> "_734.CutterSimulationCalc":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734

            return self._parent._cast(_734.CutterSimulationCalc)

        @property
        def worm_grinder_simulation_calculator(
            self: "WormGrinderSimulationCalculator._Cast_WormGrinderSimulationCalculator",
        ) -> "WormGrinderSimulationCalculator":
            return self._parent

        def __getattr__(
            self: "WormGrinderSimulationCalculator._Cast_WormGrinderSimulationCalculator",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGrinderSimulationCalculator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinder(self: Self) -> "_731.CylindricalGearWormGrinderShape":
        """mastapy.gears.manufacturing.cylindrical.cutters.tangibles.CylindricalGearWormGrinderShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrinder

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrinderSimulationCalculator._Cast_WormGrinderSimulationCalculator":
        return self._Cast_WormGrinderSimulationCalculator(self)
