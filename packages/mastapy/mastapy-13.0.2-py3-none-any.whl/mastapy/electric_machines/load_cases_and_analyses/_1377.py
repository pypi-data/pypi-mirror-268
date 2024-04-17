"""SingleOperatingPointAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_OPERATING_POINT_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "SingleOperatingPointAnalysis"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.results import _1337
    from mastapy.electric_machines.load_cases_and_analyses import _1365, _1378, _1363


__docformat__ = "restructuredtext en"
__all__ = ("SingleOperatingPointAnalysis",)


Self = TypeVar("Self", bound="SingleOperatingPointAnalysis")


class SingleOperatingPointAnalysis(_1359.ElectricMachineAnalysis):
    """SingleOperatingPointAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGLE_OPERATING_POINT_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SingleOperatingPointAnalysis")

    class _Cast_SingleOperatingPointAnalysis:
        """Special nested class for casting SingleOperatingPointAnalysis to subclasses."""

        def __init__(
            self: "SingleOperatingPointAnalysis._Cast_SingleOperatingPointAnalysis",
            parent: "SingleOperatingPointAnalysis",
        ):
            self._parent = parent

        @property
        def electric_machine_analysis(
            self: "SingleOperatingPointAnalysis._Cast_SingleOperatingPointAnalysis",
        ) -> "_1359.ElectricMachineAnalysis":
            return self._parent._cast(_1359.ElectricMachineAnalysis)

        @property
        def electric_machine_fe_analysis(
            self: "SingleOperatingPointAnalysis._Cast_SingleOperatingPointAnalysis",
        ) -> "_1363.ElectricMachineFEAnalysis":
            from mastapy.electric_machines.load_cases_and_analyses import _1363

            return self._parent._cast(_1363.ElectricMachineFEAnalysis)

        @property
        def single_operating_point_analysis(
            self: "SingleOperatingPointAnalysis._Cast_SingleOperatingPointAnalysis",
        ) -> "SingleOperatingPointAnalysis":
            return self._parent

        def __getattr__(
            self: "SingleOperatingPointAnalysis._Cast_SingleOperatingPointAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SingleOperatingPointAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CurrentAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_frequency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricalFrequency

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_period(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricalPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def mechanical_period(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MechanicalPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_line_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakLineCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_phase_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakPhaseCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_current_drms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseCurrentDRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_current_qrms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseCurrentQRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def rms_phase_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RMSPhaseCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def slot_passing_period(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlotPassingPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def time_step_increment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeStepIncrement

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_results(
        self: Self,
    ) -> "_1337.ElectricMachineResultsForOpenCircuitAndOnLoad":
        """mastapy.electric_machines.results.ElectricMachineResultsForOpenCircuitAndOnLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_case(self: Self) -> "_1365.ElectricMachineLoadCase":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def slot_section_details_for_analysis(
        self: Self,
    ) -> "List[_1378.SlotDetailForAnalysis]":
        """List[mastapy.electric_machines.load_cases_and_analyses.SlotDetailForAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlotSectionDetailsForAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SingleOperatingPointAnalysis._Cast_SingleOperatingPointAnalysis":
        return self._Cast_SingleOperatingPointAnalysis(self)
