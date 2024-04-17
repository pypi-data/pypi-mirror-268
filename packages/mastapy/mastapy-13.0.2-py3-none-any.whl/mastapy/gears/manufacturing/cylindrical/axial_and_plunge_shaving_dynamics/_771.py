"""ShavingDynamicsCalculationForHobbedGears"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.gear_designs.cylindrical import _1029
from mastapy._internal.python_net import python_net_import
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _769,
)
from mastapy._internal.cast_exception import CastException

_REPORTING_OVERRIDABLE = python_net_import(
    "SMT.MastaAPI.Utility.Property", "ReportingOverridable"
)
_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsCalculationForHobbedGears",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _767,
        _764,
        _768,
        _756,
        _762,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsCalculationForHobbedGears",)


Self = TypeVar("Self", bound="ShavingDynamicsCalculationForHobbedGears")
T = TypeVar("T", bound="_768.ShavingDynamics")


class ShavingDynamicsCalculationForHobbedGears(_769.ShavingDynamicsCalculation[T]):
    """ShavingDynamicsCalculationForHobbedGears

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShavingDynamicsCalculationForHobbedGears"
    )

    class _Cast_ShavingDynamicsCalculationForHobbedGears:
        """Special nested class for casting ShavingDynamicsCalculationForHobbedGears to subclasses."""

        def __init__(
            self: "ShavingDynamicsCalculationForHobbedGears._Cast_ShavingDynamicsCalculationForHobbedGears",
            parent: "ShavingDynamicsCalculationForHobbedGears",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_calculation(
            self: "ShavingDynamicsCalculationForHobbedGears._Cast_ShavingDynamicsCalculationForHobbedGears",
        ) -> "_769.ShavingDynamicsCalculation":
            return self._parent._cast(_769.ShavingDynamicsCalculation)

        @property
        def conventional_shaving_dynamics_calculation_for_hobbed_gears(
            self: "ShavingDynamicsCalculationForHobbedGears._Cast_ShavingDynamicsCalculationForHobbedGears",
        ) -> "_756.ConventionalShavingDynamicsCalculationForHobbedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _756,
            )

            return self._parent._cast(
                _756.ConventionalShavingDynamicsCalculationForHobbedGears
            )

        @property
        def plunge_shaving_dynamics_calculation_for_hobbed_gears(
            self: "ShavingDynamicsCalculationForHobbedGears._Cast_ShavingDynamicsCalculationForHobbedGears",
        ) -> "_762.PlungeShavingDynamicsCalculationForHobbedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _762,
            )

            return self._parent._cast(
                _762.PlungeShavingDynamicsCalculationForHobbedGears
            )

        @property
        def shaving_dynamics_calculation_for_hobbed_gears(
            self: "ShavingDynamicsCalculationForHobbedGears._Cast_ShavingDynamicsCalculationForHobbedGears",
        ) -> "ShavingDynamicsCalculationForHobbedGears":
            return self._parent

        def __getattr__(
            self: "ShavingDynamicsCalculationForHobbedGears._Cast_ShavingDynamicsCalculationForHobbedGears",
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
        self: Self, instance_to_wrap: "ShavingDynamicsCalculationForHobbedGears.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def redressing_chart_maximum_start_and_end_of_shaving_profile(
        self: Self,
    ) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingChartMaximumStartAndEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def redressing_chart_maximum_start_and_minimum_end_of_shaving_profile(
        self: Self,
    ) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingChartMaximumStartAndMinimumEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def redressing_chart_minimum_start_and_end_of_shaving_profile(
        self: Self,
    ) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingChartMinimumStartAndEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def redressing_chart_minimum_start_and_maximum_end_of_shaving_profile(
        self: Self,
    ) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingChartMinimumStartAndMaximumEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def selected_redressing(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_T":
        """ListWithSelectedItem[T]"""
        temp = self.wrapped.SelectedRedressing

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_T",
        )(temp)

    @selected_redressing.setter
    @enforce_parameter_types
    def selected_redressing(self: Self, value: "T"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_T.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_T.implicit_type()
        value = wrapper_type[enclosed_type](value if value is not None else None)
        self.wrapped.SelectedRedressing = value

    @property
    def maximum_end_of_shaving_profile(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEndOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_start_of_shaving_profile(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumStartOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_end_of_shaving_profile(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEndOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_start_of_shaving_profile(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumStartOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def redressing_at_maximum_start_and_end_of_shaving_profile(
        self: Self,
    ) -> "_767.ShaverRedressing[T]":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShaverRedressing[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingAtMaximumStartAndEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp)

    @property
    def redressing_at_maximum_start_and_minimum_end_of_shaving_profile(
        self: Self,
    ) -> "_767.ShaverRedressing[T]":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShaverRedressing[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingAtMaximumStartAndMinimumEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp)

    @property
    def redressing_at_minimum_start_and_end_of_shaving_profile(
        self: Self,
    ) -> "_767.ShaverRedressing[T]":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShaverRedressing[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingAtMinimumStartAndEndOfShavingProfile

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp)

    @property
    def redressing_at_minimum_start_and_maximum_end_of_shaving_profile(
        self: Self,
    ) -> "_767.ShaverRedressing[T]":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShaverRedressing[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RedressingAtMinimumStartAndMaximumEndOfShavingProfile

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

    @property
    def cast_to(
        self: Self,
    ) -> "ShavingDynamicsCalculationForHobbedGears._Cast_ShavingDynamicsCalculationForHobbedGears":
        return self._Cast_ShavingDynamicsCalculationForHobbedGears(self)
