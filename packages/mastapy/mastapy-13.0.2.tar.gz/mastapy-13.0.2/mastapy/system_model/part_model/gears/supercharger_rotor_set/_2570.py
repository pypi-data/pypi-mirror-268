"""SuperchargerRotorSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SUPERCHARGER_ROTOR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet",
    "SuperchargerRotorSet",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1872
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
        _2572,
        _2562,
        _2565,
        _2563,
        _2564,
        _2567,
        _2566,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SuperchargerRotorSet",)


Self = TypeVar("Self", bound="SuperchargerRotorSet")


class SuperchargerRotorSet(_1836.NamedDatabaseItem):
    """SuperchargerRotorSet

    This is a mastapy class.
    """

    TYPE = _SUPERCHARGER_ROTOR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SuperchargerRotorSet")

    class _Cast_SuperchargerRotorSet:
        """Special nested class for casting SuperchargerRotorSet to subclasses."""

        def __init__(
            self: "SuperchargerRotorSet._Cast_SuperchargerRotorSet",
            parent: "SuperchargerRotorSet",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "SuperchargerRotorSet._Cast_SuperchargerRotorSet",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def supercharger_rotor_set(
            self: "SuperchargerRotorSet._Cast_SuperchargerRotorSet",
        ) -> "SuperchargerRotorSet":
            return self._parent

        def __getattr__(
            self: "SuperchargerRotorSet._Cast_SuperchargerRotorSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SuperchargerRotorSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_reaction_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialReactionForce

        if temp is None:
            return 0.0

        return temp

    @axial_reaction_force.setter
    @enforce_parameter_types
    def axial_reaction_force(self: Self, value: "float"):
        self.wrapped.AxialReactionForce = float(value) if value is not None else 0.0

    @property
    def dynamic_load_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DynamicLoadFactor

        if temp is None:
            return 0.0

        return temp

    @dynamic_load_factor.setter
    @enforce_parameter_types
    def dynamic_load_factor(self: Self, value: "float"):
        self.wrapped.DynamicLoadFactor = float(value) if value is not None else 0.0

    @property
    def lateral_reaction_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LateralReactionForce

        if temp is None:
            return 0.0

        return temp

    @lateral_reaction_force.setter
    @enforce_parameter_types
    def lateral_reaction_force(self: Self, value: "float"):
        self.wrapped.LateralReactionForce = float(value) if value is not None else 0.0

    @property
    def lateral_reaction_moment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LateralReactionMoment

        if temp is None:
            return 0.0

        return temp

    @lateral_reaction_moment.setter
    @enforce_parameter_types
    def lateral_reaction_moment(self: Self, value: "float"):
        self.wrapped.LateralReactionMoment = float(value) if value is not None else 0.0

    @property
    def selected_file_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SelectedFileName

        if temp is None:
            return ""

        return temp

    @property
    def supercharger_map_chart(self: Self) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SuperchargerMapChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def vertical_reaction_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VerticalReactionForce

        if temp is None:
            return 0.0

        return temp

    @vertical_reaction_force.setter
    @enforce_parameter_types
    def vertical_reaction_force(self: Self, value: "float"):
        self.wrapped.VerticalReactionForce = float(value) if value is not None else 0.0

    @property
    def vertical_reaction_moment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VerticalReactionMoment

        if temp is None:
            return 0.0

        return temp

    @vertical_reaction_moment.setter
    @enforce_parameter_types
    def vertical_reaction_moment(self: Self, value: "float"):
        self.wrapped.VerticalReactionMoment = float(value) if value is not None else 0.0

    @property
    def y_variable_for_imported_data(self: Self) -> "_2572.YVariableForImportedData":
        """mastapy.system_model.part_model.gears.supercharger_rotor_set.YVariableForImportedData"""
        temp = self.wrapped.YVariableForImportedData

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet.YVariableForImportedData",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.gears.supercharger_rotor_set._2572",
            "YVariableForImportedData",
        )(value)

    @y_variable_for_imported_data.setter
    @enforce_parameter_types
    def y_variable_for_imported_data(
        self: Self, value: "_2572.YVariableForImportedData"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet.YVariableForImportedData",
        )
        self.wrapped.YVariableForImportedData = value

    @property
    def boost_pressure(self: Self) -> "_2562.BoostPressureInputOptions":
        """mastapy.system_model.part_model.gears.supercharger_rotor_set.BoostPressureInputOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BoostPressure

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def file(self: Self) -> "_2565.RotorSetDataInputFileOptions":
        """mastapy.system_model.part_model.gears.supercharger_rotor_set.RotorSetDataInputFileOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.File

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def input_power(self: Self) -> "_2563.InputPowerInputOptions":
        """mastapy.system_model.part_model.gears.supercharger_rotor_set.InputPowerInputOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputPower

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pressure_ratio(self: Self) -> "_2564.PressureRatioInputOptions":
        """mastapy.system_model.part_model.gears.supercharger_rotor_set.PressureRatioInputOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureRatio

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotor_speed(self: Self) -> "_2567.RotorSpeedInputOptions":
        """mastapy.system_model.part_model.gears.supercharger_rotor_set.RotorSpeedInputOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotorSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def measured_points(self: Self) -> "List[_2566.RotorSetMeasuredPoint]":
        """List[mastapy.system_model.part_model.gears.supercharger_rotor_set.RotorSetMeasuredPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasuredPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def select_different_file(self: Self):
        """Method does not return."""
        self.wrapped.SelectDifferentFile()

    @property
    def cast_to(self: Self) -> "SuperchargerRotorSet._Cast_SuperchargerRotorSet":
        return self._Cast_SuperchargerRotorSet(self)
