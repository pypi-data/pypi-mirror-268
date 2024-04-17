"""EfficiencyMapLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.electric_machines.load_cases_and_analyses import _1374
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_MAP_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "EfficiencyMapLoadCase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1362, _1357, _1366
    from mastapy.electric_machines import _1273


__docformat__ = "restructuredtext en"
__all__ = ("EfficiencyMapLoadCase",)


Self = TypeVar("Self", bound="EfficiencyMapLoadCase")


class EfficiencyMapLoadCase(_1374.NonLinearDQModelMultipleOperatingPointsLoadCase):
    """EfficiencyMapLoadCase

    This is a mastapy class.
    """

    TYPE = _EFFICIENCY_MAP_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EfficiencyMapLoadCase")

    class _Cast_EfficiencyMapLoadCase:
        """Special nested class for casting EfficiencyMapLoadCase to subclasses."""

        def __init__(
            self: "EfficiencyMapLoadCase._Cast_EfficiencyMapLoadCase",
            parent: "EfficiencyMapLoadCase",
        ):
            self._parent = parent

        @property
        def non_linear_dq_model_multiple_operating_points_load_case(
            self: "EfficiencyMapLoadCase._Cast_EfficiencyMapLoadCase",
        ) -> "_1374.NonLinearDQModelMultipleOperatingPointsLoadCase":
            return self._parent._cast(
                _1374.NonLinearDQModelMultipleOperatingPointsLoadCase
            )

        @property
        def electric_machine_load_case_base(
            self: "EfficiencyMapLoadCase._Cast_EfficiencyMapLoadCase",
        ) -> "_1366.ElectricMachineLoadCaseBase":
            from mastapy.electric_machines.load_cases_and_analyses import _1366

            return self._parent._cast(_1366.ElectricMachineLoadCaseBase)

        @property
        def efficiency_map_load_case(
            self: "EfficiencyMapLoadCase._Cast_EfficiencyMapLoadCase",
        ) -> "EfficiencyMapLoadCase":
            return self._parent

        def __getattr__(
            self: "EfficiencyMapLoadCase._Cast_EfficiencyMapLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EfficiencyMapLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def efficiency_map_settings(
        self: Self,
    ) -> "_1362.ElectricMachineEfficiencyMapSettings":
        """mastapy.electric_machines.load_cases_and_analyses.ElectricMachineEfficiencyMapSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EfficiencyMapSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def analysis_for(
        self: Self, setup: "_1273.ElectricMachineSetup"
    ) -> "_1357.EfficiencyMapAnalysis":
        """mastapy.electric_machines.load_cases_and_analyses.EfficiencyMapAnalysis

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
        """
        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "EfficiencyMapLoadCase._Cast_EfficiencyMapLoadCase":
        return self._Cast_EfficiencyMapLoadCase(self)
