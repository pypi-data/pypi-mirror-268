"""WormGrindingProcessTotalModificationCalculation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _697
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_TOTAL_MODIFICATION_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessTotalModificationCalculation",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1872
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _683,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessTotalModificationCalculation",)


Self = TypeVar("Self", bound="WormGrindingProcessTotalModificationCalculation")


class WormGrindingProcessTotalModificationCalculation(
    _697.WormGrindingProcessCalculation
):
    """WormGrindingProcessTotalModificationCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_TOTAL_MODIFICATION_CALCULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGrindingProcessTotalModificationCalculation"
    )

    class _Cast_WormGrindingProcessTotalModificationCalculation:
        """Special nested class for casting WormGrindingProcessTotalModificationCalculation to subclasses."""

        def __init__(
            self: "WormGrindingProcessTotalModificationCalculation._Cast_WormGrindingProcessTotalModificationCalculation",
            parent: "WormGrindingProcessTotalModificationCalculation",
        ):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(
            self: "WormGrindingProcessTotalModificationCalculation._Cast_WormGrindingProcessTotalModificationCalculation",
        ) -> "_697.WormGrindingProcessCalculation":
            return self._parent._cast(_697.WormGrindingProcessCalculation)

        @property
        def process_calculation(
            self: "WormGrindingProcessTotalModificationCalculation._Cast_WormGrindingProcessTotalModificationCalculation",
        ) -> "_683.ProcessCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _683,
            )

            return self._parent._cast(_683.ProcessCalculation)

        @property
        def worm_grinding_process_total_modification_calculation(
            self: "WormGrindingProcessTotalModificationCalculation._Cast_WormGrindingProcessTotalModificationCalculation",
        ) -> "WormGrindingProcessTotalModificationCalculation":
            return self._parent

        def __getattr__(
            self: "WormGrindingProcessTotalModificationCalculation._Cast_WormGrindingProcessTotalModificationCalculation",
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
        self: Self,
        instance_to_wrap: "WormGrindingProcessTotalModificationCalculation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_range_max(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeadRangeMax

        if temp is None:
            return 0.0

        return temp

    @lead_range_max.setter
    @enforce_parameter_types
    def lead_range_max(self: Self, value: "float"):
        self.wrapped.LeadRangeMax = float(value) if value is not None else 0.0

    @property
    def lead_range_min(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LeadRangeMin

        if temp is None:
            return 0.0

        return temp

    @lead_range_min.setter
    @enforce_parameter_types
    def lead_range_min(self: Self, value: "float"):
        self.wrapped.LeadRangeMin = float(value) if value is not None else 0.0

    @property
    def number_of_lead_bands(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfLeadBands

        if temp is None:
            return 0

        return temp

    @number_of_lead_bands.setter
    @enforce_parameter_types
    def number_of_lead_bands(self: Self, value: "int"):
        self.wrapped.NumberOfLeadBands = int(value) if value is not None else 0

    @property
    def number_of_profile_bands(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfProfileBands

        if temp is None:
            return 0

        return temp

    @number_of_profile_bands.setter
    @enforce_parameter_types
    def number_of_profile_bands(self: Self, value: "int"):
        self.wrapped.NumberOfProfileBands = int(value) if value is not None else 0

    @property
    def total_errors_chart_left_flank(self: Self) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalErrorsChartLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_errors_chart_right_flank(self: Self) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalErrorsChartRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingProcessTotalModificationCalculation._Cast_WormGrindingProcessTotalModificationCalculation":
        return self._Cast_WormGrindingProcessTotalModificationCalculation(self)
