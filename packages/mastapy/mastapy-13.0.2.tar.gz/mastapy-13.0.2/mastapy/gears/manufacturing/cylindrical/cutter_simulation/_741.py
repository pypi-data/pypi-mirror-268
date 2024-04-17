"""FormWheelGrindingSimulationCalculator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _734
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FORM_WHEEL_GRINDING_SIMULATION_CALCULATOR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "FormWheelGrindingSimulationCalculator",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _727


__docformat__ = "restructuredtext en"
__all__ = ("FormWheelGrindingSimulationCalculator",)


Self = TypeVar("Self", bound="FormWheelGrindingSimulationCalculator")


class FormWheelGrindingSimulationCalculator(_734.CutterSimulationCalc):
    """FormWheelGrindingSimulationCalculator

    This is a mastapy class.
    """

    TYPE = _FORM_WHEEL_GRINDING_SIMULATION_CALCULATOR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FormWheelGrindingSimulationCalculator"
    )

    class _Cast_FormWheelGrindingSimulationCalculator:
        """Special nested class for casting FormWheelGrindingSimulationCalculator to subclasses."""

        def __init__(
            self: "FormWheelGrindingSimulationCalculator._Cast_FormWheelGrindingSimulationCalculator",
            parent: "FormWheelGrindingSimulationCalculator",
        ):
            self._parent = parent

        @property
        def cutter_simulation_calc(
            self: "FormWheelGrindingSimulationCalculator._Cast_FormWheelGrindingSimulationCalculator",
        ) -> "_734.CutterSimulationCalc":
            return self._parent._cast(_734.CutterSimulationCalc)

        @property
        def form_wheel_grinding_simulation_calculator(
            self: "FormWheelGrindingSimulationCalculator._Cast_FormWheelGrindingSimulationCalculator",
        ) -> "FormWheelGrindingSimulationCalculator":
            return self._parent

        def __getattr__(
            self: "FormWheelGrindingSimulationCalculator._Cast_FormWheelGrindingSimulationCalculator",
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
        self: Self, instance_to_wrap: "FormWheelGrindingSimulationCalculator.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def finish_depth_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishDepthRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def limiting_finish_depth_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitingFinishDepthRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_root_fillet_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseRootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def profiled_grinding_wheel(
        self: Self,
    ) -> "_727.CylindricalGearFormedWheelGrinderTangible":
        """mastapy.gears.manufacturing.cylindrical.cutters.tangibles.CylindricalGearFormedWheelGrinderTangible

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfiledGrindingWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "FormWheelGrindingSimulationCalculator._Cast_FormWheelGrindingSimulationCalculator":
        return self._Cast_FormWheelGrindingSimulationCalculator(self)
