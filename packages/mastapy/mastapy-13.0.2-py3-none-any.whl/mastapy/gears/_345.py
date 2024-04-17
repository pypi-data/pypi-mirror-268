"""PocketingPowerLossCoefficients"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1517
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.utility.databases import _1836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POCKETING_POWER_LOSS_COEFFICIENTS = python_net_import(
    "SMT.MastaAPI.Gears", "PocketingPowerLossCoefficients"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_data import _1572
    from mastapy.gears import _349


__docformat__ = "restructuredtext en"
__all__ = ("PocketingPowerLossCoefficients",)


Self = TypeVar("Self", bound="PocketingPowerLossCoefficients")


class PocketingPowerLossCoefficients(_1836.NamedDatabaseItem):
    """PocketingPowerLossCoefficients

    This is a mastapy class.
    """

    TYPE = _POCKETING_POWER_LOSS_COEFFICIENTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PocketingPowerLossCoefficients")

    class _Cast_PocketingPowerLossCoefficients:
        """Special nested class for casting PocketingPowerLossCoefficients to subclasses."""

        def __init__(
            self: "PocketingPowerLossCoefficients._Cast_PocketingPowerLossCoefficients",
            parent: "PocketingPowerLossCoefficients",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "PocketingPowerLossCoefficients._Cast_PocketingPowerLossCoefficients",
        ) -> "_1836.NamedDatabaseItem":
            return self._parent._cast(_1836.NamedDatabaseItem)

        @property
        def pocketing_power_loss_coefficients(
            self: "PocketingPowerLossCoefficients._Cast_PocketingPowerLossCoefficients",
        ) -> "PocketingPowerLossCoefficients":
            return self._parent

        def __getattr__(
            self: "PocketingPowerLossCoefficients._Cast_PocketingPowerLossCoefficients",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PocketingPowerLossCoefficients.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extrapolation_options(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions":
        """EnumWithSelectedValue[mastapy.math_utility.ExtrapolationOptions]"""
        temp = self.wrapped.ExtrapolationOptions

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @extrapolation_options.setter
    @enforce_parameter_types
    def extrapolation_options(self: Self, value: "_1517.ExtrapolationOptions"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ExtrapolationOptions = value

    @property
    def intercept_of_linear_equation_defining_the_effect_of_gear_face_width(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfGearFaceWidth

        if temp is None:
            return 0.0

        return temp

    @intercept_of_linear_equation_defining_the_effect_of_gear_face_width.setter
    @enforce_parameter_types
    def intercept_of_linear_equation_defining_the_effect_of_gear_face_width(
        self: Self, value: "float"
    ):
        self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfGearFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def intercept_of_linear_equation_defining_the_effect_of_helix_angle(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfHelixAngle

        if temp is None:
            return 0.0

        return temp

    @intercept_of_linear_equation_defining_the_effect_of_helix_angle.setter
    @enforce_parameter_types
    def intercept_of_linear_equation_defining_the_effect_of_helix_angle(
        self: Self, value: "float"
    ):
        self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfHelixAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def lower_bound_for_oil_kinematic_viscosity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LowerBoundForOilKinematicViscosity

        if temp is None:
            return 0.0

        return temp

    @lower_bound_for_oil_kinematic_viscosity.setter
    @enforce_parameter_types
    def lower_bound_for_oil_kinematic_viscosity(self: Self, value: "float"):
        self.wrapped.LowerBoundForOilKinematicViscosity = (
            float(value) if value is not None else 0.0
        )

    @property
    def raw_pocketing_power_loss_lookup_table(
        self: Self,
    ) -> "_1572.GriddedSurfaceAccessor":
        """mastapy.math_utility.measured_data.GriddedSurfaceAccessor"""
        temp = self.wrapped.RawPocketingPowerLossLookupTable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @raw_pocketing_power_loss_lookup_table.setter
    @enforce_parameter_types
    def raw_pocketing_power_loss_lookup_table(
        self: Self, value: "_1572.GriddedSurfaceAccessor"
    ):
        self.wrapped.RawPocketingPowerLossLookupTable = value.wrapped

    @property
    def reference_gear_outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReferenceGearOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @reference_gear_outer_diameter.setter
    @enforce_parameter_types
    def reference_gear_outer_diameter(self: Self, value: "float"):
        self.wrapped.ReferenceGearOuterDiameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def reference_gear_pocket_dimension(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ReferenceGearPocketDimension

        if temp is None:
            return 0.0

        return temp

    @reference_gear_pocket_dimension.setter
    @enforce_parameter_types
    def reference_gear_pocket_dimension(self: Self, value: "float"):
        self.wrapped.ReferenceGearPocketDimension = (
            float(value) if value is not None else 0.0
        )

    @property
    def slope_of_linear_equation_defining_the_effect_of_gear_face_width(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfGearFaceWidth

        if temp is None:
            return 0.0

        return temp

    @slope_of_linear_equation_defining_the_effect_of_gear_face_width.setter
    @enforce_parameter_types
    def slope_of_linear_equation_defining_the_effect_of_gear_face_width(
        self: Self, value: "float"
    ):
        self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfGearFaceWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def slope_of_linear_equation_defining_the_effect_of_helix_angle(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfHelixAngle

        if temp is None:
            return 0.0

        return temp

    @slope_of_linear_equation_defining_the_effect_of_helix_angle.setter
    @enforce_parameter_types
    def slope_of_linear_equation_defining_the_effect_of_helix_angle(
        self: Self, value: "float"
    ):
        self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfHelixAngle = (
            float(value) if value is not None else 0.0
        )

    @property
    def upper_bound_for_oil_kinematic_viscosity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UpperBoundForOilKinematicViscosity

        if temp is None:
            return 0.0

        return temp

    @upper_bound_for_oil_kinematic_viscosity.setter
    @enforce_parameter_types
    def upper_bound_for_oil_kinematic_viscosity(self: Self, value: "float"):
        self.wrapped.UpperBoundForOilKinematicViscosity = (
            float(value) if value is not None else 0.0
        )

    @property
    def specifications_for_the_effect_of_oil_kinematic_viscosity(
        self: Self,
    ) -> "List[_349.SpecificationForTheEffectOfOilKinematicViscosity]":
        """List[mastapy.gears.SpecificationForTheEffectOfOilKinematicViscosity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificationsForTheEffectOfOilKinematicViscosity

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PocketingPowerLossCoefficients._Cast_PocketingPowerLossCoefficients":
        return self._Cast_PocketingPowerLossCoefficients(self)
