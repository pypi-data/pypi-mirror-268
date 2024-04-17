"""WormGrindingProcessSimulationNew"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _689
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_NEW = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessSimulationNew",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _695,
        _698,
        _696,
        _699,
        _700,
        _701,
        _705,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessSimulationNew",)


Self = TypeVar("Self", bound="WormGrindingProcessSimulationNew")


class WormGrindingProcessSimulationNew(
    _689.ProcessSimulationNew["_702.WormGrindingProcessSimulationInput"]
):
    """WormGrindingProcessSimulationNew

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_NEW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrindingProcessSimulationNew")

    class _Cast_WormGrindingProcessSimulationNew:
        """Special nested class for casting WormGrindingProcessSimulationNew to subclasses."""

        def __init__(
            self: "WormGrindingProcessSimulationNew._Cast_WormGrindingProcessSimulationNew",
            parent: "WormGrindingProcessSimulationNew",
        ):
            self._parent = parent

        @property
        def process_simulation_new(
            self: "WormGrindingProcessSimulationNew._Cast_WormGrindingProcessSimulationNew",
        ) -> "_689.ProcessSimulationNew":
            return self._parent._cast(_689.ProcessSimulationNew)

        @property
        def worm_grinding_process_simulation_new(
            self: "WormGrindingProcessSimulationNew._Cast_WormGrindingProcessSimulationNew",
        ) -> "WormGrindingProcessSimulationNew":
            return self._parent

        def __getattr__(
            self: "WormGrindingProcessSimulationNew._Cast_WormGrindingProcessSimulationNew",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGrindingProcessSimulationNew.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinding_cutter_calculation(
        self: Self,
    ) -> "_695.WormGrindingCutterCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.WormGrindingCutterCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrindingCutterCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_grinding_process_gear_shape_calculation(
        self: Self,
    ) -> "_698.WormGrindingProcessGearShape":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.WormGrindingProcessGearShape

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrindingProcessGearShapeCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_grinding_process_lead_calculation(
        self: Self,
    ) -> "_696.WormGrindingLeadCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.WormGrindingLeadCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrindingProcessLeadCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_grinding_process_mark_on_shaft_calculation(
        self: Self,
    ) -> "_699.WormGrindingProcessMarkOnShaft":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.WormGrindingProcessMarkOnShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrindingProcessMarkOnShaftCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_grinding_process_pitch_calculation(
        self: Self,
    ) -> "_700.WormGrindingProcessPitchCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.WormGrindingProcessPitchCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrindingProcessPitchCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_grinding_process_profile_calculation(
        self: Self,
    ) -> "_701.WormGrindingProcessProfileCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.WormGrindingProcessProfileCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrindingProcessProfileCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_grinding_process_total_modification_calculation(
        self: Self,
    ) -> "_705.WormGrindingProcessTotalModificationCalculation":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.WormGrindingProcessTotalModificationCalculation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrindingProcessTotalModificationCalculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingProcessSimulationNew._Cast_WormGrindingProcessSimulationNew":
        return self._Cast_WormGrindingProcessSimulationNew(self)
