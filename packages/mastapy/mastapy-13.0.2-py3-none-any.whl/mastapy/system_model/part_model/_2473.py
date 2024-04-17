"""OilSeal"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.materials.efficiency import _303
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2454
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "OilSeal")

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.materials.efficiency import _304
    from mastapy.bearings.bearing_results import _1967
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("OilSeal",)


Self = TypeVar("Self", bound="OilSeal")


class OilSeal(_2454.Connector):
    """OilSeal

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSeal")

    class _Cast_OilSeal:
        """Special nested class for casting OilSeal to subclasses."""

        def __init__(self: "OilSeal._Cast_OilSeal", parent: "OilSeal"):
            self._parent = parent

        @property
        def connector(self: "OilSeal._Cast_OilSeal") -> "_2454.Connector":
            return self._parent._cast(_2454.Connector)

        @property
        def mountable_component(
            self: "OilSeal._Cast_OilSeal",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "OilSeal._Cast_OilSeal") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "OilSeal._Cast_OilSeal") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "OilSeal._Cast_OilSeal") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def oil_seal(self: "OilSeal._Cast_OilSeal") -> "OilSeal":
            return self._parent

        def __getattr__(self: "OilSeal._Cast_OilSeal", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSeal.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def drag_torque_vs_rotational_speed(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.DragTorqueVsRotationalSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @drag_torque_vs_rotational_speed.setter
    @enforce_parameter_types
    def drag_torque_vs_rotational_speed(
        self: Self, value: "_1542.Vector2DListAccessor"
    ):
        self.wrapped.DragTorqueVsRotationalSpeed = value.wrapped

    @property
    def intercept_of_linear_equation_defining_the_effect_of_temperature(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfTemperature

        if temp is None:
            return 0.0

        return temp

    @intercept_of_linear_equation_defining_the_effect_of_temperature.setter
    @enforce_parameter_types
    def intercept_of_linear_equation_defining_the_effect_of_temperature(
        self: Self, value: "float"
    ):
        self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def oil_seal_characteristic_life(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilSealCharacteristicLife

        if temp is None:
            return 0.0

        return temp

    @oil_seal_characteristic_life.setter
    @enforce_parameter_types
    def oil_seal_characteristic_life(self: Self, value: "float"):
        self.wrapped.OilSealCharacteristicLife = (
            float(value) if value is not None else 0.0
        )

    @property
    def oil_seal_frictional_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilSealFrictionalTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_seal_loss_calculation_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_OilSealLossCalculationMethod":
        """EnumWithSelectedValue[mastapy.materials.efficiency.OilSealLossCalculationMethod]"""
        temp = self.wrapped.OilSealLossCalculationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_OilSealLossCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @oil_seal_loss_calculation_method.setter
    @enforce_parameter_types
    def oil_seal_loss_calculation_method(
        self: Self, value: "_303.OilSealLossCalculationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_OilSealLossCalculationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.OilSealLossCalculationMethod = value

    @property
    def oil_seal_material(self: Self) -> "_304.OilSealMaterialType":
        """mastapy.materials.efficiency.OilSealMaterialType"""
        temp = self.wrapped.OilSealMaterial

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.Efficiency.OilSealMaterialType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials.efficiency._304", "OilSealMaterialType"
        )(value)

    @oil_seal_material.setter
    @enforce_parameter_types
    def oil_seal_material(self: Self, value: "_304.OilSealMaterialType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.Efficiency.OilSealMaterialType"
        )
        self.wrapped.OilSealMaterial = value

    @property
    def oil_seal_mean_time_before_failure(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OilSealMeanTimeBeforeFailure

        if temp is None:
            return 0.0

        return temp

    @oil_seal_mean_time_before_failure.setter
    @enforce_parameter_types
    def oil_seal_mean_time_before_failure(self: Self, value: "float"):
        self.wrapped.OilSealMeanTimeBeforeFailure = (
            float(value) if value is not None else 0.0
        )

    @property
    def oil_seal_orientation(self: Self) -> "_1967.Orientations":
        """mastapy.bearings.bearing_results.Orientations"""
        temp = self.wrapped.OilSealOrientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results._1967", "Orientations"
        )(value)

    @oil_seal_orientation.setter
    @enforce_parameter_types
    def oil_seal_orientation(self: Self, value: "_1967.Orientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )
        self.wrapped.OilSealOrientation = value

    @property
    def slope_of_linear_equation_defining_the_effect_of_temperature(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfTemperature

        if temp is None:
            return 0.0

        return temp

    @slope_of_linear_equation_defining_the_effect_of_temperature.setter
    @enforce_parameter_types
    def slope_of_linear_equation_defining_the_effect_of_temperature(
        self: Self, value: "float"
    ):
        self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def width(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Width = value

    @property
    def cast_to(self: Self) -> "OilSeal._Cast_OilSeal":
        return self._Cast_OilSeal(self)
