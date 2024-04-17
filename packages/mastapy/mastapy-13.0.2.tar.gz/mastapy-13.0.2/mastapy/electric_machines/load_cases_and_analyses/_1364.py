"""ElectricMachineFEMechanicalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines.load_cases_and_analyses import _1359
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_FE_MECHANICAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses",
    "ElectricMachineFEMechanicalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.elmer import _175


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineFEMechanicalAnalysis",)


Self = TypeVar("Self", bound="ElectricMachineFEMechanicalAnalysis")


class ElectricMachineFEMechanicalAnalysis(_1359.ElectricMachineAnalysis):
    """ElectricMachineFEMechanicalAnalysis

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_FE_MECHANICAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineFEMechanicalAnalysis")

    class _Cast_ElectricMachineFEMechanicalAnalysis:
        """Special nested class for casting ElectricMachineFEMechanicalAnalysis to subclasses."""

        def __init__(
            self: "ElectricMachineFEMechanicalAnalysis._Cast_ElectricMachineFEMechanicalAnalysis",
            parent: "ElectricMachineFEMechanicalAnalysis",
        ):
            self._parent = parent

        @property
        def electric_machine_analysis(
            self: "ElectricMachineFEMechanicalAnalysis._Cast_ElectricMachineFEMechanicalAnalysis",
        ) -> "_1359.ElectricMachineAnalysis":
            return self._parent._cast(_1359.ElectricMachineAnalysis)

        @property
        def electric_machine_fe_mechanical_analysis(
            self: "ElectricMachineFEMechanicalAnalysis._Cast_ElectricMachineFEMechanicalAnalysis",
        ) -> "ElectricMachineFEMechanicalAnalysis":
            return self._parent

        def __getattr__(
            self: "ElectricMachineFEMechanicalAnalysis._Cast_ElectricMachineFEMechanicalAnalysis",
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
        self: Self, instance_to_wrap: "ElectricMachineFEMechanicalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def viewable(self: Self) -> "_175.ElmerResultsViewable":
        """mastapy.nodal_analysis.elmer.ElmerResultsViewable

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Viewable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ElectricMachineFEMechanicalAnalysis._Cast_ElectricMachineFEMechanicalAnalysis"
    ):
        return self._Cast_ElectricMachineFEMechanicalAnalysis(self)
