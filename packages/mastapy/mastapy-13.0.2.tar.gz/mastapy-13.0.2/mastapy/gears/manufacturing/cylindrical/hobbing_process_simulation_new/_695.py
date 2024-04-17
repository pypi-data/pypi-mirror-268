"""WormGrindingCutterCalculation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _697
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_CUTTER_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingCutterCalculation",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _656
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _683,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingCutterCalculation",)


Self = TypeVar("Self", bound="WormGrindingCutterCalculation")


class WormGrindingCutterCalculation(_697.WormGrindingProcessCalculation):
    """WormGrindingCutterCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_CUTTER_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrindingCutterCalculation")

    class _Cast_WormGrindingCutterCalculation:
        """Special nested class for casting WormGrindingCutterCalculation to subclasses."""

        def __init__(
            self: "WormGrindingCutterCalculation._Cast_WormGrindingCutterCalculation",
            parent: "WormGrindingCutterCalculation",
        ):
            self._parent = parent

        @property
        def worm_grinding_process_calculation(
            self: "WormGrindingCutterCalculation._Cast_WormGrindingCutterCalculation",
        ) -> "_697.WormGrindingProcessCalculation":
            return self._parent._cast(_697.WormGrindingProcessCalculation)

        @property
        def process_calculation(
            self: "WormGrindingCutterCalculation._Cast_WormGrindingCutterCalculation",
        ) -> "_683.ProcessCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _683,
            )

            return self._parent._cast(_683.ProcessCalculation)

        @property
        def worm_grinding_cutter_calculation(
            self: "WormGrindingCutterCalculation._Cast_WormGrindingCutterCalculation",
        ) -> "WormGrindingCutterCalculation":
            return self._parent

        def __getattr__(
            self: "WormGrindingCutterCalculation._Cast_WormGrindingCutterCalculation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGrindingCutterCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def grinder_tooth_shape_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GrinderToothShapeChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def use_design_mode_micro_geometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseDesignModeMicroGeometry

        if temp is None:
            return False

        return temp

    @use_design_mode_micro_geometry.setter
    @enforce_parameter_types
    def use_design_mode_micro_geometry(self: Self, value: "bool"):
        self.wrapped.UseDesignModeMicroGeometry = (
            bool(value) if value is not None else False
        )

    @property
    def worm_axial_z(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormAxialZ

        if temp is None:
            return 0.0

        return temp

    @property
    def worm_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def input_gear_point_of_interest(self: Self) -> "_656.PointOfInterest":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.PointOfInterest

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputGearPointOfInterest

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def calculate_grinder_axial_section_tooth_shape(self: Self):
        """Method does not return."""
        self.wrapped.CalculateGrinderAxialSectionToothShape()

    def calculate_point_of_interest(self: Self):
        """Method does not return."""
        self.wrapped.CalculatePointOfInterest()

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingCutterCalculation._Cast_WormGrindingCutterCalculation":
        return self._Cast_WormGrindingCutterCalculation(self)
