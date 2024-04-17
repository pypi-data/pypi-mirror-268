"""CriticalSpeedAnalysisOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CRITICAL_SPEED_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CriticalSpeedAnalysisOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("CriticalSpeedAnalysisOptions",)


Self = TypeVar("Self", bound="CriticalSpeedAnalysisOptions")


class CriticalSpeedAnalysisOptions(_0.APIBase):
    """CriticalSpeedAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _CRITICAL_SPEED_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CriticalSpeedAnalysisOptions")

    class _Cast_CriticalSpeedAnalysisOptions:
        """Special nested class for casting CriticalSpeedAnalysisOptions to subclasses."""

        def __init__(
            self: "CriticalSpeedAnalysisOptions._Cast_CriticalSpeedAnalysisOptions",
            parent: "CriticalSpeedAnalysisOptions",
        ):
            self._parent = parent

        @property
        def critical_speed_analysis_options(
            self: "CriticalSpeedAnalysisOptions._Cast_CriticalSpeedAnalysisOptions",
        ) -> "CriticalSpeedAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "CriticalSpeedAnalysisOptions._Cast_CriticalSpeedAnalysisOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CriticalSpeedAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness.setter
    @enforce_parameter_types
    def axial_stiffness(self: Self, value: "float"):
        self.wrapped.AxialStiffness = float(value) if value is not None else 0.0

    @property
    def final_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FinalStiffness

        if temp is None:
            return 0.0

        return temp

    @final_stiffness.setter
    @enforce_parameter_types
    def final_stiffness(self: Self, value: "float"):
        self.wrapped.FinalStiffness = float(value) if value is not None else 0.0

    @property
    def include_damping_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeDampingEffects

        if temp is None:
            return False

        return temp

    @include_damping_effects.setter
    @enforce_parameter_types
    def include_damping_effects(self: Self, value: "bool"):
        self.wrapped.IncludeDampingEffects = bool(value) if value is not None else False

    @property
    def include_gyroscopic_effects(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeGyroscopicEffects

        if temp is None:
            return False

        return temp

    @include_gyroscopic_effects.setter
    @enforce_parameter_types
    def include_gyroscopic_effects(self: Self, value: "bool"):
        self.wrapped.IncludeGyroscopicEffects = (
            bool(value) if value is not None else False
        )

    @property
    def initial_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InitialStiffness

        if temp is None:
            return 0.0

        return temp

    @initial_stiffness.setter
    @enforce_parameter_types
    def initial_stiffness(self: Self, value: "float"):
        self.wrapped.InitialStiffness = float(value) if value is not None else 0.0

    @property
    def number_of_modes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfModes

        if temp is None:
            return 0

        return temp

    @number_of_modes.setter
    @enforce_parameter_types
    def number_of_modes(self: Self, value: "int"):
        self.wrapped.NumberOfModes = int(value) if value is not None else 0

    @property
    def number_of_stiffnesses(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStiffnesses

        if temp is None:
            return 0

        return temp

    @number_of_stiffnesses.setter
    @enforce_parameter_types
    def number_of_stiffnesses(self: Self, value: "int"):
        self.wrapped.NumberOfStiffnesses = int(value) if value is not None else 0

    @property
    def sort_modes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SortModes

        if temp is None:
            return False

        return temp

    @sort_modes.setter
    @enforce_parameter_types
    def sort_modes(self: Self, value: "bool"):
        self.wrapped.SortModes = bool(value) if value is not None else False

    @property
    def tilt_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness.setter
    @enforce_parameter_types
    def tilt_stiffness(self: Self, value: "float"):
        self.wrapped.TiltStiffness = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "CriticalSpeedAnalysisOptions._Cast_CriticalSpeedAnalysisOptions":
        return self._Cast_CriticalSpeedAnalysisOptions(self)
