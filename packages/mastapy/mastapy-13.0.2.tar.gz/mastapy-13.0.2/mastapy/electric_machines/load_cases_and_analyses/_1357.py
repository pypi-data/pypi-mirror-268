"""EfficiencyMapAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines.load_cases_and_analyses import _1359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_MAP_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "EfficiencyMapAnalysis"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.results import _1329
    from mastapy.electric_machines.load_cases_and_analyses import _1358


__docformat__ = "restructuredtext en"
__all__ = ("EfficiencyMapAnalysis",)


Self = TypeVar("Self", bound="EfficiencyMapAnalysis")


class EfficiencyMapAnalysis(_1359.ElectricMachineAnalysis):
    """EfficiencyMapAnalysis

    This is a mastapy class.
    """

    TYPE = _EFFICIENCY_MAP_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EfficiencyMapAnalysis")

    class _Cast_EfficiencyMapAnalysis:
        """Special nested class for casting EfficiencyMapAnalysis to subclasses."""

        def __init__(
            self: "EfficiencyMapAnalysis._Cast_EfficiencyMapAnalysis",
            parent: "EfficiencyMapAnalysis",
        ):
            self._parent = parent

        @property
        def electric_machine_analysis(
            self: "EfficiencyMapAnalysis._Cast_EfficiencyMapAnalysis",
        ) -> "_1359.ElectricMachineAnalysis":
            return self._parent._cast(_1359.ElectricMachineAnalysis)

        @property
        def efficiency_map_analysis(
            self: "EfficiencyMapAnalysis._Cast_EfficiencyMapAnalysis",
        ) -> "EfficiencyMapAnalysis":
            return self._parent

        def __getattr__(
            self: "EfficiencyMapAnalysis._Cast_EfficiencyMapAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EfficiencyMapAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def permanent_magnet_flux_linkage_at_reference_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermanentMagnetFluxLinkageAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PhaseResistance

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency_map_results(self: Self) -> "_1329.EfficiencyResults":
        """mastapy.electric_machines.results.EfficiencyResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EfficiencyMapResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def load_case(self: Self) -> "_1358.EfficiencyMapLoadCase":
        """mastapy.electric_machines.load_cases_and_analyses.EfficiencyMapLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "EfficiencyMapAnalysis._Cast_EfficiencyMapAnalysis":
        return self._Cast_EfficiencyMapAnalysis(self)
