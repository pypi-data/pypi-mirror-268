"""DynamicForceAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1359
from mastapy.electric_machines.results import _1346
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "DynamicForceAnalysis"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.load_cases_and_analyses import _1353, _1363
    from mastapy.electric_machines.results import _1328


__docformat__ = "restructuredtext en"
__all__ = ("DynamicForceAnalysis",)


Self = TypeVar("Self", bound="DynamicForceAnalysis")


class DynamicForceAnalysis(
    _1359.ElectricMachineAnalysis, _1346.IHaveDynamicForceResults
):
    """DynamicForceAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicForceAnalysis")

    class _Cast_DynamicForceAnalysis:
        """Special nested class for casting DynamicForceAnalysis to subclasses."""

        def __init__(
            self: "DynamicForceAnalysis._Cast_DynamicForceAnalysis",
            parent: "DynamicForceAnalysis",
        ):
            self._parent = parent

        @property
        def electric_machine_analysis(
            self: "DynamicForceAnalysis._Cast_DynamicForceAnalysis",
        ) -> "_1359.ElectricMachineAnalysis":
            return self._parent._cast(_1359.ElectricMachineAnalysis)

        @property
        def dynamic_force_analysis(
            self: "DynamicForceAnalysis._Cast_DynamicForceAnalysis",
        ) -> "DynamicForceAnalysis":
            return self._parent

        def __getattr__(
            self: "DynamicForceAnalysis._Cast_DynamicForceAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicForceAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_steps_per_operating_point(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfStepsPerOperatingPoint

        if temp is None:
            return 0

        return temp

    @property
    def load_case(self: Self) -> "_1353.BasicDynamicForceLoadCase":
        """mastapy.electric_machines.load_cases_and_analyses.BasicDynamicForceLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results(self: Self) -> "_1328.DynamicForceResults":
        """mastapy.electric_machines.results.DynamicForceResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Results

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def single_operating_point_analyses(
        self: Self,
    ) -> "List[_1363.ElectricMachineFEAnalysis]":
        """List[mastapy.electric_machines.load_cases_and_analyses.ElectricMachineFEAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleOperatingPointAnalyses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "DynamicForceAnalysis._Cast_DynamicForceAnalysis":
        return self._Cast_DynamicForceAnalysis(self)
