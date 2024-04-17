"""RackSimulationCalculator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACK_SIMULATION_CALCULATOR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "RackSimulationCalculator",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _743, _751


__docformat__ = "restructuredtext en"
__all__ = ("RackSimulationCalculator",)


Self = TypeVar("Self", bound="RackSimulationCalculator")


class RackSimulationCalculator(_734.CutterSimulationCalc):
    """RackSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _RACK_SIMULATION_CALCULATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RackSimulationCalculator")

    class _Cast_RackSimulationCalculator:
        """Special nested class for casting RackSimulationCalculator to subclasses."""

        def __init__(
            self: "RackSimulationCalculator._Cast_RackSimulationCalculator",
            parent: "RackSimulationCalculator",
        ):
            self._parent = parent

        @property
        def cutter_simulation_calc(
            self: "RackSimulationCalculator._Cast_RackSimulationCalculator",
        ) -> "_734.CutterSimulationCalc":
            return self._parent._cast(_734.CutterSimulationCalc)

        @property
        def hob_simulation_calculator(
            self: "RackSimulationCalculator._Cast_RackSimulationCalculator",
        ) -> "_743.HobSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _743

            return self._parent._cast(_743.HobSimulationCalculator)

        @property
        def worm_grinder_simulation_calculator(
            self: "RackSimulationCalculator._Cast_RackSimulationCalculator",
        ) -> "_751.WormGrinderSimulationCalculator":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _751

            return self._parent._cast(_751.WormGrinderSimulationCalculator)

        @property
        def rack_simulation_calculator(
            self: "RackSimulationCalculator._Cast_RackSimulationCalculator",
        ) -> "RackSimulationCalculator":
            return self._parent

        def __getattr__(
            self: "RackSimulationCalculator._Cast_RackSimulationCalculator", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RackSimulationCalculator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hob_working_depth_delta(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HobWorkingDepthDelta

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "RackSimulationCalculator._Cast_RackSimulationCalculator":
        return self._Cast_RackSimulationCalculator(self)
