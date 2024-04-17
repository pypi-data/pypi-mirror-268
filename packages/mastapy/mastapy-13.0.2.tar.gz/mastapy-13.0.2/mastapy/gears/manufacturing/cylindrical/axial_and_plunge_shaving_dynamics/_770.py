"""ShavingDynamicsCalculationForDesignedGears"""

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
_SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsCalculationForDesignedGears",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _767,
        _764,
        _768,
        _755,
        _761,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsCalculationForDesignedGears",)


Self = TypeVar("Self", bound="ShavingDynamicsCalculationForDesignedGears")
T = TypeVar("T", bound="_768.ShavingDynamics")


class ShavingDynamicsCalculationForDesignedGears(_769.ShavingDynamicsCalculation[T]):
    """ShavingDynamicsCalculationForDesignedGears

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_CALCULATION_FOR_DESIGNED_GEARS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShavingDynamicsCalculationForDesignedGears"
    )

    class _Cast_ShavingDynamicsCalculationForDesignedGears:
        """Special nested class for casting ShavingDynamicsCalculationForDesignedGears to subclasses."""

        def __init__(
            self: "ShavingDynamicsCalculationForDesignedGears._Cast_ShavingDynamicsCalculationForDesignedGears",
            parent: "ShavingDynamicsCalculationForDesignedGears",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_calculation(
            self: "ShavingDynamicsCalculationForDesignedGears._Cast_ShavingDynamicsCalculationForDesignedGears",
        ) -> "_769.ShavingDynamicsCalculation":
            return self._parent._cast(_769.ShavingDynamicsCalculation)

        @property
        def conventional_shaving_dynamics_calculation_for_designed_gears(
            self: "ShavingDynamicsCalculationForDesignedGears._Cast_ShavingDynamicsCalculationForDesignedGears",
        ) -> "_755.ConventionalShavingDynamicsCalculationForDesignedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _755,
            )

            return self._parent._cast(
                _755.ConventionalShavingDynamicsCalculationForDesignedGears
            )

        @property
        def plunge_shaving_dynamics_calculation_for_designed_gears(
            self: "ShavingDynamicsCalculationForDesignedGears._Cast_ShavingDynamicsCalculationForDesignedGears",
        ) -> "_761.PlungeShavingDynamicsCalculationForDesignedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _761,
            )

            return self._parent._cast(
                _761.PlungeShavingDynamicsCalculationForDesignedGears
            )

        @property
        def shaving_dynamics_calculation_for_designed_gears(
            self: "ShavingDynamicsCalculationForDesignedGears._Cast_ShavingDynamicsCalculationForDesignedGears",
        ) -> "ShavingDynamicsCalculationForDesignedGears":
            return self._parent

        def __getattr__(
            self: "ShavingDynamicsCalculationForDesignedGears._Cast_ShavingDynamicsCalculationForDesignedGears",
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
        self: Self, instance_to_wrap: "ShavingDynamicsCalculationForDesignedGears.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def end_of_shaving_profile(self: Self) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EndOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def redressing(self: Self) -> "_767.ShaverRedressing[T]":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.ShaverRedressing[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Redressing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp)

    @property
    def start_of_shaving_profile(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StartOfShavingProfile.Value

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    ) -> "ShavingDynamicsCalculationForDesignedGears._Cast_ShavingDynamicsCalculationForDesignedGears":
        return self._Cast_ShavingDynamicsCalculationForDesignedGears(self)
