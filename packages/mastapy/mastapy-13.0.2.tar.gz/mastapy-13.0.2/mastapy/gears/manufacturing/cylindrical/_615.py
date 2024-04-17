"""CylindricalGearManufacturingConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.gears.manufacturing.cylindrical import _626, _627
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.analysis import _1227
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CYLINDRICAL_GEAR_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "CylindricalGearManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1016
    from mastapy.gears.manufacturing.cylindrical.cutters import _716
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
        _742,
        _745,
        _736,
    )
    from mastapy.gears.manufacturing.cylindrical.process_simulation import _642
    from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
        _1095,
    )
    from mastapy.gears.manufacturing.cylindrical import _614
    from mastapy.gears.analysis import _1224, _1221


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearManufacturingConfig",)


Self = TypeVar("Self", bound="CylindricalGearManufacturingConfig")


class CylindricalGearManufacturingConfig(_1227.GearImplementationDetail):
    """CylindricalGearManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearManufacturingConfig")

    class _Cast_CylindricalGearManufacturingConfig:
        """Special nested class for casting CylindricalGearManufacturingConfig to subclasses."""

        def __init__(
            self: "CylindricalGearManufacturingConfig._Cast_CylindricalGearManufacturingConfig",
            parent: "CylindricalGearManufacturingConfig",
        ):
            self._parent = parent

        @property
        def gear_implementation_detail(
            self: "CylindricalGearManufacturingConfig._Cast_CylindricalGearManufacturingConfig",
        ) -> "_1227.GearImplementationDetail":
            return self._parent._cast(_1227.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "CylindricalGearManufacturingConfig._Cast_CylindricalGearManufacturingConfig",
        ) -> "_1224.GearDesignAnalysis":
            from mastapy.gears.analysis import _1224

            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalGearManufacturingConfig._Cast_CylindricalGearManufacturingConfig",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "CylindricalGearManufacturingConfig._Cast_CylindricalGearManufacturingConfig",
        ) -> "CylindricalGearManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "CylindricalGearManufacturingConfig._Cast_CylindricalGearManufacturingConfig",
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
        self: Self, instance_to_wrap: "CylindricalGearManufacturingConfig.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_cutter_database_selector(self: Self) -> "str":
        """str"""
        temp = self.wrapped.FinishCutterDatabaseSelector.SelectedItemName

        if temp is None:
            return ""

        return temp

    @finish_cutter_database_selector.setter
    @enforce_parameter_types
    def finish_cutter_database_selector(self: Self, value: "str"):
        self.wrapped.FinishCutterDatabaseSelector.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def finishing_method(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods"
    ):
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.CylindricalMftFinishingMethods]"""
        temp = self.wrapped.FinishingMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @finishing_method.setter
    @enforce_parameter_types
    def finishing_method(self: Self, value: "_626.CylindricalMftFinishingMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FinishingMethod = value

    @property
    def limiting_finish_depth_radius_mean(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LimitingFinishDepthRadiusMean

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_finish_depth_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanFinishDepthRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_finish_cutter_gear_root_clearance_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumFinishCutterGearRootClearanceFactor

        if temp is None:
            return 0.0

        return temp

    @minimum_finish_cutter_gear_root_clearance_factor.setter
    @enforce_parameter_types
    def minimum_finish_cutter_gear_root_clearance_factor(self: Self, value: "float"):
        self.wrapped.MinimumFinishCutterGearRootClearanceFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_finish_depth_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumFinishDepthRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_points_for_reporting_main_profile_finish_stock(
        self: Self,
    ) -> "overridable.Overridable_int":
        """Overridable[int]"""
        temp = self.wrapped.NumberOfPointsForReportingMainProfileFinishStock

        if temp is None:
            return 0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_int"
        )(temp)

    @number_of_points_for_reporting_main_profile_finish_stock.setter
    @enforce_parameter_types
    def number_of_points_for_reporting_main_profile_finish_stock(
        self: Self, value: "Union[int, Tuple[int, bool]]"
    ):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0, is_overridden
        )
        self.wrapped.NumberOfPointsForReportingMainProfileFinishStock = value

    @property
    def rough_cutter_database_selector(self: Self) -> "str":
        """str"""
        temp = self.wrapped.RoughCutterDatabaseSelector.SelectedItemName

        if temp is None:
            return ""

        return temp

    @rough_cutter_database_selector.setter
    @enforce_parameter_types
    def rough_cutter_database_selector(self: Self, value: "str"):
        self.wrapped.RoughCutterDatabaseSelector.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def roughing_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods":
        """EnumWithSelectedValue[mastapy.gears.manufacturing.cylindrical.CylindricalMftRoughingMethods]"""
        temp = self.wrapped.RoughingMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @roughing_method.setter
    @enforce_parameter_types
    def roughing_method(self: Self, value: "_627.CylindricalMftRoughingMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RoughingMethod = value

    @property
    def design(self: Self) -> "_1016.CylindricalGearDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Design

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def finish_cutter(self: Self) -> "_716.CylindricalGearRealCutterDesign":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearRealCutterDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def finish_cutter_simulation(self: Self) -> "_742.GearCutterSimulation":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.GearCutterSimulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishCutterSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def finish_manufacturing_process_controls(
        self: Self,
    ) -> "_745.ManufacturingProcessControls":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.ManufacturingProcessControls

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishManufacturingProcessControls

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def finish_process_simulation(self: Self) -> "_642.CutterProcessSimulation":
        """mastapy.gears.manufacturing.cylindrical.process_simulation.CutterProcessSimulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishProcessSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def finish_stock_specification(self: Self) -> "_1095.FinishStockSpecification":
        """mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash.FinishStockSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishStockSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def finished_gear_specification(self: Self) -> "_736.CylindricalGearSpecification":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalGearSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishedGearSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_blank(self: Self) -> "_614.CylindricalGearBlank":
        """mastapy.gears.manufacturing.cylindrical.CylindricalGearBlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rough_cutter(self: Self) -> "_716.CylindricalGearRealCutterDesign":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearRealCutterDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rough_cutter_simulation(self: Self) -> "_742.GearCutterSimulation":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.GearCutterSimulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughCutterSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rough_gear_specification(self: Self) -> "_736.CylindricalGearSpecification":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalGearSpecification

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughGearSpecification

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rough_manufacturing_process_controls(
        self: Self,
    ) -> "_745.ManufacturingProcessControls":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.ManufacturingProcessControls

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughManufacturingProcessControls

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rough_process_simulation(self: Self) -> "_642.CutterProcessSimulation":
        """mastapy.gears.manufacturing.cylindrical.process_simulation.CutterProcessSimulation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughProcessSimulation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_new_finish_cutter_compatible_with_gear_in_design_mode(self: Self):
        """Method does not return."""
        self.wrapped.CreateNewFinishCutterCompatibleWithGearInDesignMode()

    def create_new_rough_cutter_compatible_with_gear_in_design_mode(self: Self):
        """Method does not return."""
        self.wrapped.CreateNewRoughCutterCompatibleWithGearInDesignMode()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearManufacturingConfig._Cast_CylindricalGearManufacturingConfig":
        return self._Cast_CylindricalGearManufacturingConfig(self)
