"""ShavingDynamicsCalculation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Union, Tuple, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable, list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsCalculation",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _765,
        _764,
        _768,
        _755,
        _756,
        _761,
        _762,
        _770,
        _771,
    )
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _735
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.gears.manufacturing.cylindrical.cutters import _718


__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsCalculation",)


Self = TypeVar("Self", bound="ShavingDynamicsCalculation")
T = TypeVar("T", bound="_768.ShavingDynamics")


class ShavingDynamicsCalculation(_0.APIBase, Generic[T]):
    """ShavingDynamicsCalculation

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShavingDynamicsCalculation")

    class _Cast_ShavingDynamicsCalculation:
        """Special nested class for casting ShavingDynamicsCalculation to subclasses."""

        def __init__(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
            parent: "ShavingDynamicsCalculation",
        ):
            self._parent = parent

        @property
        def conventional_shaving_dynamics_calculation_for_designed_gears(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
        ) -> "_755.ConventionalShavingDynamicsCalculationForDesignedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _755,
            )

            return self._parent._cast(
                _755.ConventionalShavingDynamicsCalculationForDesignedGears
            )

        @property
        def conventional_shaving_dynamics_calculation_for_hobbed_gears(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
        ) -> "_756.ConventionalShavingDynamicsCalculationForHobbedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _756,
            )

            return self._parent._cast(
                _756.ConventionalShavingDynamicsCalculationForHobbedGears
            )

        @property
        def plunge_shaving_dynamics_calculation_for_designed_gears(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
        ) -> "_761.PlungeShavingDynamicsCalculationForDesignedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _761,
            )

            return self._parent._cast(
                _761.PlungeShavingDynamicsCalculationForDesignedGears
            )

        @property
        def plunge_shaving_dynamics_calculation_for_hobbed_gears(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
        ) -> "_762.PlungeShavingDynamicsCalculationForHobbedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _762,
            )

            return self._parent._cast(
                _762.PlungeShavingDynamicsCalculationForHobbedGears
            )

        @property
        def shaving_dynamics_calculation_for_designed_gears(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
        ) -> "_770.ShavingDynamicsCalculationForDesignedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _770,
            )

            return self._parent._cast(_770.ShavingDynamicsCalculationForDesignedGears)

        @property
        def shaving_dynamics_calculation_for_hobbed_gears(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
        ) -> "_771.ShavingDynamicsCalculationForHobbedGears":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _771,
            )

            return self._parent._cast(_771.ShavingDynamicsCalculationForHobbedGears)

        @property
        def shaving_dynamics_calculation(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
        ) -> "ShavingDynamicsCalculation":
            return self._parent

        def __getattr__(
            self: "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShavingDynamicsCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_tip_diameter(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedTipDiameter

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def life_cutter_normal_thickness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LifeCutterNormalThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @life_cutter_normal_thickness.setter
    @enforce_parameter_types
    def life_cutter_normal_thickness(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LifeCutterNormalThickness = value

    @property
    def life_cutter_tip_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LifeCutterTipDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @life_cutter_tip_diameter.setter
    @enforce_parameter_types
    def life_cutter_tip_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LifeCutterTipDiameter = value

    @property
    def new_cutter_tip_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NewCutterTipDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def normal_tooth_thickness_reduction_between_redressings(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalToothThicknessReductionBetweenRedressings

        if temp is None:
            return 0.0

        return temp

    @normal_tooth_thickness_reduction_between_redressings.setter
    @enforce_parameter_types
    def normal_tooth_thickness_reduction_between_redressings(
        self: Self, value: "float"
    ):
        self.wrapped.NormalToothThicknessReductionBetweenRedressings = (
            float(value) if value is not None else 0.0
        )

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
    def accuracy_level_iso6(self: Self) -> "_765.RollAngleRangeRelativeToAccuracy":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.RollAngleRangeRelativeToAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccuracyLevelISO6

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def accuracy_level_iso7(self: Self) -> "_765.RollAngleRangeRelativeToAccuracy":
        """mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics.RollAngleRangeRelativeToAccuracy

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccuracyLevelISO7

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def designed_gear(self: Self) -> "_735.CylindricalCutterSimulatableGear":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.CylindricalCutterSimulatableGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignedGear

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def life_cutter_start_of_shaving(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeCutterStartOfShaving

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def life_shaver(self: Self) -> "_718.CylindricalGearShaver":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearShaver

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeShaver

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def new_cutter_start_of_shaving(
        self: Self,
    ) -> "_1029.CylindricalGearProfileMeasurement":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearProfileMeasurement

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NewCutterStartOfShaving

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaver(self: Self) -> "_718.CylindricalGearShaver":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearShaver

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaver

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
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def cutter_simulation_calculation_required(self: Self):
        """Method does not return."""
        self.wrapped.CutterSimulationCalculationRequired()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "ShavingDynamicsCalculation._Cast_ShavingDynamicsCalculation":
        return self._Cast_ShavingDynamicsCalculation(self)
