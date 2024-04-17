"""OpenCircuitElectricMachineResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy.electric_machines.results import _1333
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPEN_CIRCUIT_ELECTRIC_MACHINE_RESULTS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "OpenCircuitElectricMachineResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("OpenCircuitElectricMachineResults",)


Self = TypeVar("Self", bound="OpenCircuitElectricMachineResults")


class OpenCircuitElectricMachineResults(_1333.ElectricMachineResults):
    """OpenCircuitElectricMachineResults

    This is a mastapy class.
    """

    TYPE = _OPEN_CIRCUIT_ELECTRIC_MACHINE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OpenCircuitElectricMachineResults")

    class _Cast_OpenCircuitElectricMachineResults:
        """Special nested class for casting OpenCircuitElectricMachineResults to subclasses."""

        def __init__(
            self: "OpenCircuitElectricMachineResults._Cast_OpenCircuitElectricMachineResults",
            parent: "OpenCircuitElectricMachineResults",
        ):
            self._parent = parent

        @property
        def electric_machine_results(
            self: "OpenCircuitElectricMachineResults._Cast_OpenCircuitElectricMachineResults",
        ) -> "_1333.ElectricMachineResults":
            return self._parent._cast(_1333.ElectricMachineResults)

        @property
        def open_circuit_electric_machine_results(
            self: "OpenCircuitElectricMachineResults._Cast_OpenCircuitElectricMachineResults",
        ) -> "OpenCircuitElectricMachineResults":
            return self._parent

        def __getattr__(
            self: "OpenCircuitElectricMachineResults._Cast_OpenCircuitElectricMachineResults",
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
        self: Self, instance_to_wrap: "OpenCircuitElectricMachineResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def back_emf_constant(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BackEMFConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_back_emf_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineToLineBackEMFPeak

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_back_emfrms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineToLineBackEMFRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_back_emf_total_harmonic_distortion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LineToLineBackEMFTotalHarmonicDistortion

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_back_emf_peak(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseBackEMFPeak

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_back_emfrms(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseBackEMFRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_back_emf_total_harmonic_distortion(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseBackEMFTotalHarmonicDistortion

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "OpenCircuitElectricMachineResults._Cast_OpenCircuitElectricMachineResults":
        return self._Cast_OpenCircuitElectricMachineResults(self)
