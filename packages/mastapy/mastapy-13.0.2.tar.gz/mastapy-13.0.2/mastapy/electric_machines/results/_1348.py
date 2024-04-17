"""MaximumTorqueResultsPoints"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAXIMUM_TORQUE_RESULTS_POINTS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "MaximumTorqueResultsPoints"
)


__docformat__ = "restructuredtext en"
__all__ = ("MaximumTorqueResultsPoints",)


Self = TypeVar("Self", bound="MaximumTorqueResultsPoints")


class MaximumTorqueResultsPoints(_0.APIBase):
    """MaximumTorqueResultsPoints

    This is a mastapy class.
    """

    TYPE = _MAXIMUM_TORQUE_RESULTS_POINTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaximumTorqueResultsPoints")

    class _Cast_MaximumTorqueResultsPoints:
        """Special nested class for casting MaximumTorqueResultsPoints to subclasses."""

        def __init__(
            self: "MaximumTorqueResultsPoints._Cast_MaximumTorqueResultsPoints",
            parent: "MaximumTorqueResultsPoints",
        ):
            self._parent = parent

        @property
        def maximum_torque_results_points(
            self: "MaximumTorqueResultsPoints._Cast_MaximumTorqueResultsPoints",
        ) -> "MaximumTorqueResultsPoints":
            return self._parent

        def __getattr__(
            self: "MaximumTorqueResultsPoints._Cast_MaximumTorqueResultsPoints",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaximumTorqueResultsPoints.TYPE"):
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
    def d_axis_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DAxisVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricalSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_phase_current_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakPhaseCurrentMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_phase_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakPhaseVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Power

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
    def q_axis_flux_linkage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_voltage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QAxisVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "MaximumTorqueResultsPoints._Cast_MaximumTorqueResultsPoints":
        return self._Cast_MaximumTorqueResultsPoints(self)
