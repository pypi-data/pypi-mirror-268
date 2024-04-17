"""SpeedTorqueCurveAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPEED_TORQUE_CURVE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "SpeedTorqueCurveAnalysis"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1382
    from mastapy.electric_machines.results import _1348


__docformat__ = "restructuredtext en"
__all__ = ("SpeedTorqueCurveAnalysis",)


Self = TypeVar("Self", bound="SpeedTorqueCurveAnalysis")


class SpeedTorqueCurveAnalysis(_1359.ElectricMachineAnalysis):
    """SpeedTorqueCurveAnalysis

    This is a mastapy class.
    """

    TYPE = _SPEED_TORQUE_CURVE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpeedTorqueCurveAnalysis")

    class _Cast_SpeedTorqueCurveAnalysis:
        """Special nested class for casting SpeedTorqueCurveAnalysis to subclasses."""

        def __init__(
            self: "SpeedTorqueCurveAnalysis._Cast_SpeedTorqueCurveAnalysis",
            parent: "SpeedTorqueCurveAnalysis",
        ):
            self._parent = parent

        @property
        def electric_machine_analysis(
            self: "SpeedTorqueCurveAnalysis._Cast_SpeedTorqueCurveAnalysis",
        ) -> "_1359.ElectricMachineAnalysis":
            return self._parent._cast(_1359.ElectricMachineAnalysis)

        @property
        def speed_torque_curve_analysis(
            self: "SpeedTorqueCurveAnalysis._Cast_SpeedTorqueCurveAnalysis",
        ) -> "SpeedTorqueCurveAnalysis":
            return self._parent

        def __getattr__(
            self: "SpeedTorqueCurveAnalysis._Cast_SpeedTorqueCurveAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpeedTorqueCurveAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BaseSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_torque_at_rated_inverter_current(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTorqueAtRatedInverterCurrent

        if temp is None:
            return 0.0

        return temp

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
    def load_case(self: Self) -> "_1382.SpeedTorqueCurveLoadCase":
        """mastapy.electric_machines.load_cases_and_analyses.SpeedTorqueCurveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_points(self: Self) -> "List[_1348.MaximumTorqueResultsPoints]":
        """List[mastapy.electric_machines.results.MaximumTorqueResultsPoints]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpeedTorqueCurveAnalysis._Cast_SpeedTorqueCurveAnalysis":
        return self._Cast_SpeedTorqueCurveAnalysis(self)
