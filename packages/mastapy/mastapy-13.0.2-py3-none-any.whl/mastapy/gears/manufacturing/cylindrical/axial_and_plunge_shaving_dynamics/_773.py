"""ShavingDynamicsViewModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.gear_designs.cylindrical import _1085
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _774,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsViewModel",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _752,
        _769,
        _764,
        _768,
        _757,
        _763,
    )
    from mastapy.gears.gear_designs.cylindrical import _1030
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.manufacturing.cylindrical import _631


__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsViewModel",)


Self = TypeVar("Self", bound="ShavingDynamicsViewModel")
T = TypeVar("T", bound="_768.ShavingDynamics")


class ShavingDynamicsViewModel(_774.ShavingDynamicsViewModelBase, Generic[T]):
    """ShavingDynamicsViewModel

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_VIEW_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShavingDynamicsViewModel")

    class _Cast_ShavingDynamicsViewModel:
        """Special nested class for casting ShavingDynamicsViewModel to subclasses."""

        def __init__(
            self: "ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel",
            parent: "ShavingDynamicsViewModel",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_view_model_base(
            self: "ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel",
        ) -> "_774.ShavingDynamicsViewModelBase":
            return self._parent._cast(_774.ShavingDynamicsViewModelBase)

        @property
        def gear_manufacturing_configuration_view_model(
            self: "ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel",
        ) -> "_631.GearManufacturingConfigurationViewModel":
            from mastapy.gears.manufacturing.cylindrical import _631

            return self._parent._cast(_631.GearManufacturingConfigurationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel",
        ) -> "_757.ConventionalShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _757,
            )

            return self._parent._cast(_757.ConventionalShavingDynamicsViewModel)

        @property
        def plunge_shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel",
        ) -> "_763.PlungeShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _763,
            )

            return self._parent._cast(_763.PlungeShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel",
        ) -> "ShavingDynamicsViewModel":
            return self._parent

        def __getattr__(
            self: "ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShavingDynamicsViewModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_profile_range_calculation_source(
        self: Self,
    ) -> "_752.ActiveProfileRangeCalculationSource":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ActiveProfileRangeCalculationSource"""
        temp = self.wrapped.ActiveProfileRangeCalculationSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.ActiveProfileRangeCalculationSource",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics._752",
            "ActiveProfileRangeCalculationSource",
        )(value)

    @active_profile_range_calculation_source.setter
    @enforce_parameter_types
    def active_profile_range_calculation_source(
        self: Self, value: "_752.ActiveProfileRangeCalculationSource"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics.ActiveProfileRangeCalculationSource",
        )
        self.wrapped.ActiveProfileRangeCalculationSource = value

    @property
    def chart_display_method(
        self: Self,
    ) -> "_1030.CylindricalGearProfileMeasurementType":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurementType"""
        temp = self.wrapped.ChartDisplayMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1030",
            "CylindricalGearProfileMeasurementType",
        )(value)

    @chart_display_method.setter
    @enforce_parameter_types
    def chart_display_method(
        self: Self, value: "_1030.CylindricalGearProfileMeasurementType"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.CylindricalGearProfileMeasurementType",
        )
        self.wrapped.ChartDisplayMethod = value

    @property
    def redressing_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_measurement_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ThicknessType":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.cylindrical.ThicknessType]"""
        temp = self.wrapped.SelectedMeasurementMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ThicknessType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @selected_measurement_method.setter
    @enforce_parameter_types
    def selected_measurement_method(self: Self, value: "_1085.ThicknessType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ThicknessType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SelectedMeasurementMethod = value

    @property
    def shaver_tip_diameter_adjustment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ShaverTipDiameterAdjustment

        if temp is None:
            return 0.0

        return temp

    @shaver_tip_diameter_adjustment.setter
    @enforce_parameter_types
    def shaver_tip_diameter_adjustment(self: Self, value: "float"):
        self.wrapped.ShaverTipDiameterAdjustment = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_shaver_from_database(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseShaverFromDatabase

        if temp is None:
            return False

        return temp

    @use_shaver_from_database.setter
    @enforce_parameter_types
    def use_shaver_from_database(self: Self, value: "bool"):
        self.wrapped.UseShaverFromDatabase = bool(value) if value is not None else False

    @property
    def calculation(self: Self) -> "_769.ShavingDynamicsCalculation[T]":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShavingDynamicsCalculation[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Calculation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp)

    @property
    def redressing_settings(self: Self) -> "List[_764.RedressingSettings[T]]":
        """List[mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.RedressingSettings[T]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingSettings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def add_shaver_to_database(self: Self):
        """Method does not return."""
        self.wrapped.AddShaverToDatabase()

    def calculate(self: Self):
        """Method does not return."""
        self.wrapped.Calculate()

    @property
    def cast_to(
        self: Self,
    ) -> "ShavingDynamicsViewModel._Cast_ShavingDynamicsViewModel":
        return self._Cast_ShavingDynamicsViewModel(self)
