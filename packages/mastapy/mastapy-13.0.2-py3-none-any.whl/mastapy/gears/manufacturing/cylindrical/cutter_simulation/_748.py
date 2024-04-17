"""ShaperSimulationCalculator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAPER_SIMULATION_CALCULATOR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "ShaperSimulationCalculator",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _729


__docformat__ = "restructuredtext en"
__all__ = ("ShaperSimulationCalculator",)


Self = TypeVar("Self", bound="ShaperSimulationCalculator")


class ShaperSimulationCalculator(_734.CutterSimulationCalc):
    """ShaperSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _SHAPER_SIMULATION_CALCULATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaperSimulationCalculator")

    class _Cast_ShaperSimulationCalculator:
        """Special nested class for casting ShaperSimulationCalculator to subclasses."""

        def __init__(
            self: "ShaperSimulationCalculator._Cast_ShaperSimulationCalculator",
            parent: "ShaperSimulationCalculator",
        ):
            self._parent = parent

        @property
        def cutter_simulation_calc(
            self: "ShaperSimulationCalculator._Cast_ShaperSimulationCalculator",
        ) -> "_734.CutterSimulationCalc":
            return self._parent._cast(_734.CutterSimulationCalc)

        @property
        def shaper_simulation_calculator(
            self: "ShaperSimulationCalculator._Cast_ShaperSimulationCalculator",
        ) -> "ShaperSimulationCalculator":
            return self._parent

        def __getattr__(
            self: "ShaperSimulationCalculator._Cast_ShaperSimulationCalculator",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaperSimulationCalculator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutting_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CuttingCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def cutting_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CuttingPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def shaper_sap_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaperSAPDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaper(self: Self) -> "_729.CylindricalGearShaperTangible":
        """mastapy.gears.manufacturing.cylindrical.cutters.tangibles.CylindricalGearShaperTangible

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaper

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaperSimulationCalculator._Cast_ShaperSimulationCalculator":
        return self._Cast_ShaperSimulationCalculator(self)
