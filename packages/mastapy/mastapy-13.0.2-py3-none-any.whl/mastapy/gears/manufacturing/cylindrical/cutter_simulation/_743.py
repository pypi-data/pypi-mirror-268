"""HobSimulationCalculator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _746
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOB_SIMULATION_CALCULATOR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "HobSimulationCalculator",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _728
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734


__docformat__ = "restructuredtext en"
__all__ = ("HobSimulationCalculator",)


Self = TypeVar("Self", bound="HobSimulationCalculator")


class HobSimulationCalculator(_746.RackSimulationCalculator):
    """HobSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _HOB_SIMULATION_CALCULATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobSimulationCalculator")

    class _Cast_HobSimulationCalculator:
        """Special nested class for casting HobSimulationCalculator to subclasses."""

        def __init__(
            self: "HobSimulationCalculator._Cast_HobSimulationCalculator",
            parent: "HobSimulationCalculator",
        ):
            self._parent = parent

        @property
        def rack_simulation_calculator(
            self: "HobSimulationCalculator._Cast_HobSimulationCalculator",
        ) -> "_746.RackSimulationCalculator":
            return self._parent._cast(_746.RackSimulationCalculator)

        @property
        def cutter_simulation_calc(
            self: "HobSimulationCalculator._Cast_HobSimulationCalculator",
        ) -> "_734.CutterSimulationCalc":
            from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734

            return self._parent._cast(_734.CutterSimulationCalc)

        @property
        def hob_simulation_calculator(
            self: "HobSimulationCalculator._Cast_HobSimulationCalculator",
        ) -> "HobSimulationCalculator":
            return self._parent

        def __getattr__(
            self: "HobSimulationCalculator._Cast_HobSimulationCalculator", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobSimulationCalculator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hob(self: Self) -> "_728.CylindricalGearHobShape":
        """mastapy.gears.manufacturing.cylindrical.cutters.tangibles.CylindricalGearHobShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Hob

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HobSimulationCalculator._Cast_HobSimulationCalculator":
        return self._Cast_HobSimulationCalculator(self)
