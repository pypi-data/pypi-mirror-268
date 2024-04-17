"""WormGrindingProcessPitchCalculation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _697
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_PITCH_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessPitchCalculation",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _664,
        _683,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessPitchCalculation",)


Self = TypeVar("Self", bound="WormGrindingProcessPitchCalculation")


class WormGrindingProcessPitchCalculation(_697.WormGrindingProcessCalculation):
    """WormGrindingProcessPitchCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_PITCH_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrindingProcessPitchCalculation")

    class _Cast_WormGrindingProcessPitchCalculation:
        """Special nested class for casting WormGrindingProcessPitchCalculation to subclasses."""

        def __init__(
            self: "WormGrindingProcessPitchCalculation._Cast_WormGrindingProcessPitchCalculation",
            parent: "WormGrindingProcessPitchCalculation",
        ):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(
            self: "WormGrindingProcessPitchCalculation._Cast_WormGrindingProcessPitchCalculation",
        ) -> "_697.WormGrindingProcessCalculation":
            return self._parent._cast(_697.WormGrindingProcessCalculation)

        @property
        def process_calculation(
            self: "WormGrindingProcessPitchCalculation._Cast_WormGrindingProcessPitchCalculation",
        ) -> "_683.ProcessCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _683,
            )

            return self._parent._cast(_683.ProcessCalculation)

        @property
        def worm_grinding_process_pitch_calculation(
            self: "WormGrindingProcessPitchCalculation._Cast_WormGrindingProcessPitchCalculation",
        ) -> "WormGrindingProcessPitchCalculation":
            return self._parent

        def __getattr__(
            self: "WormGrindingProcessPitchCalculation._Cast_WormGrindingProcessPitchCalculation",
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
        self: Self, instance_to_wrap: "WormGrindingProcessPitchCalculation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pitch_modification_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def result_z_plane(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ResultZPlane

        if temp is None:
            return 0.0

        return temp

    @result_z_plane.setter
    @enforce_parameter_types
    def result_z_plane(self: Self, value: "float"):
        self.wrapped.ResultZPlane = float(value) if value is not None else 0.0

    @property
    def left_flank(self: Self) -> "_664.CalculatePitchDeviationAccuracy":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.CalculatePitchDeviationAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_664.CalculatePitchDeviationAccuracy":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.CalculatePitchDeviationAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "WormGrindingProcessPitchCalculation._Cast_WormGrindingProcessPitchCalculation"
    ):
        return self._Cast_WormGrindingProcessPitchCalculation(self)
