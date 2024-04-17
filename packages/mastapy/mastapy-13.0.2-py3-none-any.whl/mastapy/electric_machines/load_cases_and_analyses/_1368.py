"""ElectricMachineMechanicalLoadCase"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.electric_machines.load_cases_and_analyses import _1366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MECHANICAL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses",
    "ElectricMachineMechanicalLoadCase",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineMechanicalLoadCase",)


Self = TypeVar("Self", bound="ElectricMachineMechanicalLoadCase")


class ElectricMachineMechanicalLoadCase(_1366.ElectricMachineLoadCaseBase):
    """ElectricMachineMechanicalLoadCase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_MECHANICAL_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineMechanicalLoadCase")

    class _Cast_ElectricMachineMechanicalLoadCase:
        """Special nested class for casting ElectricMachineMechanicalLoadCase to subclasses."""

        def __init__(
            self: "ElectricMachineMechanicalLoadCase._Cast_ElectricMachineMechanicalLoadCase",
            parent: "ElectricMachineMechanicalLoadCase",
        ):
            self._parent = parent

        @property
        def electric_machine_load_case_base(
            self: "ElectricMachineMechanicalLoadCase._Cast_ElectricMachineMechanicalLoadCase",
        ) -> "_1366.ElectricMachineLoadCaseBase":
            return self._parent._cast(_1366.ElectricMachineLoadCaseBase)

        @property
        def electric_machine_mechanical_load_case(
            self: "ElectricMachineMechanicalLoadCase._Cast_ElectricMachineMechanicalLoadCase",
        ) -> "ElectricMachineMechanicalLoadCase":
            return self._parent

        def __getattr__(
            self: "ElectricMachineMechanicalLoadCase._Cast_ElectricMachineMechanicalLoadCase",
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
        self: Self, instance_to_wrap: "ElectricMachineMechanicalLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def speed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @speed.setter
    @enforce_parameter_types
    def speed(self: Self, value: "float"):
        self.wrapped.Speed = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineMechanicalLoadCase._Cast_ElectricMachineMechanicalLoadCase":
        return self._Cast_ElectricMachineMechanicalLoadCase(self)
