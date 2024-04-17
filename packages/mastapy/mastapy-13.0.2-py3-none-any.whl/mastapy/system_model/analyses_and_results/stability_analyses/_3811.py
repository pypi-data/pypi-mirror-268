"""CriticalSpeed"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRITICAL_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses", "CriticalSpeed"
)


__docformat__ = "restructuredtext en"
__all__ = ("CriticalSpeed",)


Self = TypeVar("Self", bound="CriticalSpeed")


class CriticalSpeed(_0.APIBase):
    """CriticalSpeed

    This is a mastapy class.
    """

    TYPE = _CRITICAL_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CriticalSpeed")

    class _Cast_CriticalSpeed:
        """Special nested class for casting CriticalSpeed to subclasses."""

        def __init__(
            self: "CriticalSpeed._Cast_CriticalSpeed", parent: "CriticalSpeed"
        ):
            self._parent = parent

        @property
        def critical_speed(
            self: "CriticalSpeed._Cast_CriticalSpeed",
        ) -> "CriticalSpeed":
            return self._parent

        def __getattr__(self: "CriticalSpeed._Cast_CriticalSpeed", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CriticalSpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def critical_speed_as_frequency(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CriticalSpeedAsFrequency

        if temp is None:
            return 0.0

        return temp

    @critical_speed_as_frequency.setter
    @enforce_parameter_types
    def critical_speed_as_frequency(self: Self, value: "float"):
        self.wrapped.CriticalSpeedAsFrequency = (
            float(value) if value is not None else 0.0
        )

    @property
    def critical_speed_as_shaft_speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CriticalSpeedAsShaftSpeed

        if temp is None:
            return 0.0

        return temp

    @critical_speed_as_shaft_speed.setter
    @enforce_parameter_types
    def critical_speed_as_shaft_speed(self: Self, value: "float"):
        self.wrapped.CriticalSpeedAsShaftSpeed = (
            float(value) if value is not None else 0.0
        )

    @property
    def mode_index(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ModeIndex

        if temp is None:
            return 0

        return temp

    @mode_index.setter
    @enforce_parameter_types
    def mode_index(self: Self, value: "int"):
        self.wrapped.ModeIndex = int(value) if value is not None else 0

    @property
    def shaft_harmonic_index(self: Self) -> "int":
        """int"""
        temp = self.wrapped.ShaftHarmonicIndex

        if temp is None:
            return 0

        return temp

    @shaft_harmonic_index.setter
    @enforce_parameter_types
    def shaft_harmonic_index(self: Self, value: "int"):
        self.wrapped.ShaftHarmonicIndex = int(value) if value is not None else 0

    @property
    def cast_to(self: Self) -> "CriticalSpeed._Cast_CriticalSpeed":
        return self._Cast_CriticalSpeed(self)
