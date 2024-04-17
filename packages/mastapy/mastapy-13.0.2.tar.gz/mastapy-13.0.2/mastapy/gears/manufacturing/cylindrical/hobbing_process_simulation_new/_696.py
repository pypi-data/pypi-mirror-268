"""WormGrindingLeadCalculation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _697
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_LEAD_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingLeadCalculation",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _663,
        _683,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingLeadCalculation",)


Self = TypeVar("Self", bound="WormGrindingLeadCalculation")


class WormGrindingLeadCalculation(_697.WormGrindingProcessCalculation):
    """WormGrindingLeadCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_LEAD_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrindingLeadCalculation")

    class _Cast_WormGrindingLeadCalculation:
        """Special nested class for casting WormGrindingLeadCalculation to subclasses."""

        def __init__(
            self: "WormGrindingLeadCalculation._Cast_WormGrindingLeadCalculation",
            parent: "WormGrindingLeadCalculation",
        ):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(
            self: "WormGrindingLeadCalculation._Cast_WormGrindingLeadCalculation",
        ) -> "_697.WormGrindingProcessCalculation":
            return self._parent._cast(_697.WormGrindingProcessCalculation)

        @property
        def process_calculation(
            self: "WormGrindingLeadCalculation._Cast_WormGrindingLeadCalculation",
        ) -> "_683.ProcessCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _683,
            )

            return self._parent._cast(_683.ProcessCalculation)

        @property
        def worm_grinding_lead_calculation(
            self: "WormGrindingLeadCalculation._Cast_WormGrindingLeadCalculation",
        ) -> "WormGrindingLeadCalculation":
            return self._parent

        def __getattr__(
            self: "WormGrindingLeadCalculation._Cast_WormGrindingLeadCalculation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGrindingLeadCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_lead_modification_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankLeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def radius_for_lead_modification_calculation(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RadiusForLeadModificationCalculation

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radius_for_lead_modification_calculation.setter
    @enforce_parameter_types
    def radius_for_lead_modification_calculation(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RadiusForLeadModificationCalculation = value

    @property
    def right_flank_lead_modification_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankLeadModificationChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank(self: Self) -> "_663.CalculateLeadDeviationAccuracy":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.CalculateLeadDeviationAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank(self: Self) -> "_663.CalculateLeadDeviationAccuracy":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.CalculateLeadDeviationAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingLeadCalculation._Cast_WormGrindingLeadCalculation":
        return self._Cast_WormGrindingLeadCalculation(self)
