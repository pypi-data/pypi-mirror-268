"""DutyCycleEfficiencyResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_EFFICIENCY_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "DutyCycleEfficiencyResults",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2785


__docformat__ = "restructuredtext en"
__all__ = ("DutyCycleEfficiencyResults",)


Self = TypeVar("Self", bound="DutyCycleEfficiencyResults")


class DutyCycleEfficiencyResults(_0.APIBase):
    """DutyCycleEfficiencyResults

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_EFFICIENCY_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCycleEfficiencyResults")

    class _Cast_DutyCycleEfficiencyResults:
        """Special nested class for casting DutyCycleEfficiencyResults to subclasses."""

        def __init__(
            self: "DutyCycleEfficiencyResults._Cast_DutyCycleEfficiencyResults",
            parent: "DutyCycleEfficiencyResults",
        ):
            self._parent = parent

        @property
        def duty_cycle_efficiency_results(
            self: "DutyCycleEfficiencyResults._Cast_DutyCycleEfficiencyResults",
        ) -> "DutyCycleEfficiencyResults":
            return self._parent

        def __getattr__(
            self: "DutyCycleEfficiencyResults._Cast_DutyCycleEfficiencyResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DutyCycleEfficiencyResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_input(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyInput

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_lost(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLost

        if temp is None:
            return 0.0

        return temp

    @property
    def energy_output(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyOutput

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def load_case_overall_efficiency_result(
        self: Self,
    ) -> "List[_2785.LoadCaseOverallEfficiencyResult]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.LoadCaseOverallEfficiencyResult]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseOverallEfficiencyResult

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "DutyCycleEfficiencyResults._Cast_DutyCycleEfficiencyResults":
        return self._Cast_DutyCycleEfficiencyResults(self)
