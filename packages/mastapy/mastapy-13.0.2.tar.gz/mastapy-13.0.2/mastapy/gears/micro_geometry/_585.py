"""ProfileModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.micro_geometry import _576, _577, _578, _579, _582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PROFILE_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry", "ProfileModification"
)

if TYPE_CHECKING:
    from mastapy.gears.micro_geometry import _580, _581, _583, _584
    from mastapy.math_utility import _1542
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111, _1112
    from mastapy.gears.gear_designs.conical.micro_geometry import _1181


__docformat__ = "restructuredtext en"
__all__ = ("ProfileModification",)


Self = TypeVar("Self", bound="ProfileModification")


class ProfileModification(_582.Modification):
    """ProfileModification

    This is a mastapy class.
    """

    TYPE = _PROFILE_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ProfileModification")

    class _Cast_ProfileModification:
        """Special nested class for casting ProfileModification to subclasses."""

        def __init__(
            self: "ProfileModification._Cast_ProfileModification",
            parent: "ProfileModification",
        ):
            self._parent = parent

        @property
        def modification(
            self: "ProfileModification._Cast_ProfileModification",
        ) -> "_582.Modification":
            return self._parent._cast(_582.Modification)

        @property
        def cylindrical_gear_profile_modification(
            self: "ProfileModification._Cast_ProfileModification",
        ) -> "_1111.CylindricalGearProfileModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111

            return self._parent._cast(_1111.CylindricalGearProfileModification)

        @property
        def cylindrical_gear_profile_modification_at_face_width_position(
            self: "ProfileModification._Cast_ProfileModification",
        ) -> "_1112.CylindricalGearProfileModificationAtFaceWidthPosition":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1112

            return self._parent._cast(
                _1112.CylindricalGearProfileModificationAtFaceWidthPosition
            )

        @property
        def conical_gear_profile_modification(
            self: "ProfileModification._Cast_ProfileModification",
        ) -> "_1181.ConicalGearProfileModification":
            from mastapy.gears.gear_designs.conical.micro_geometry import _1181

            return self._parent._cast(_1181.ConicalGearProfileModification)

        @property
        def profile_modification(
            self: "ProfileModification._Cast_ProfileModification",
        ) -> "ProfileModification":
            return self._parent

        def __getattr__(
            self: "ProfileModification._Cast_ProfileModification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ProfileModification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def barrelling_peak_point_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BarrellingPeakPointFactor

        if temp is None:
            return 0.0

        return temp

    @barrelling_peak_point_factor.setter
    @enforce_parameter_types
    def barrelling_peak_point_factor(self: Self, value: "float"):
        self.wrapped.BarrellingPeakPointFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def barrelling_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BarrellingRelief

        if temp is None:
            return 0.0

        return temp

    @barrelling_relief.setter
    @enforce_parameter_types
    def barrelling_relief(self: Self, value: "float"):
        self.wrapped.BarrellingRelief = float(value) if value is not None else 0.0

    @property
    def evaluation_lower_limit_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_factor.setter
    @enforce_parameter_types
    def evaluation_lower_limit_factor(self: Self, value: "float"):
        self.wrapped.EvaluationLowerLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_lower_limit_factor_for_zero_root_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLowerLimitFactorForZeroRootRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_lower_limit_factor_for_zero_root_relief.setter
    @enforce_parameter_types
    def evaluation_lower_limit_factor_for_zero_root_relief(self: Self, value: "float"):
        self.wrapped.EvaluationLowerLimitFactorForZeroRootRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_factor.setter
    @enforce_parameter_types
    def evaluation_upper_limit_factor(self: Self, value: "float"):
        self.wrapped.EvaluationUpperLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_upper_limit_factor_for_zero_tip_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationUpperLimitFactorForZeroTipRelief

        if temp is None:
            return 0.0

        return temp

    @evaluation_upper_limit_factor_for_zero_tip_relief.setter
    @enforce_parameter_types
    def evaluation_upper_limit_factor_for_zero_tip_relief(self: Self, value: "float"):
        self.wrapped.EvaluationUpperLimitFactorForZeroTipRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_root_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRootReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_root_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_linear_root_relief_factor(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearRootReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_tip_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearTipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_tip_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_linear_tip_relief_factor(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearTipReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_root_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRootReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_root_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_root_relief_factor(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicRootReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_tip_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicTipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_tip_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_tip_relief_factor(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicTipReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def linear_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearRelief

        if temp is None:
            return 0.0

        return temp

    @linear_relief.setter
    @enforce_parameter_types
    def linear_relief(self: Self, value: "float"):
        self.wrapped.LinearRelief = float(value) if value is not None else 0.0

    @property
    def linear_root_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearRootRelief

        if temp is None:
            return 0.0

        return temp

    @linear_root_relief.setter
    @enforce_parameter_types
    def linear_root_relief(self: Self, value: "float"):
        self.wrapped.LinearRootRelief = float(value) if value is not None else 0.0

    @property
    def linear_tip_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearTipRelief

        if temp is None:
            return 0.0

        return temp

    @linear_tip_relief.setter
    @enforce_parameter_types
    def linear_tip_relief(self: Self, value: "float"):
        self.wrapped.LinearTipRelief = float(value) if value is not None else 0.0

    @property
    def location_of_evaluation_lower_limit(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit"
    ):
        """EnumWithSelectedValue[mastapy.gears.micro_geometry.LocationOfEvaluationLowerLimit]"""
        temp = self.wrapped.LocationOfEvaluationLowerLimit

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_evaluation_lower_limit.setter
    @enforce_parameter_types
    def location_of_evaluation_lower_limit(
        self: Self, value: "_576.LocationOfEvaluationLowerLimit"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfEvaluationLowerLimit = value

    @property
    def location_of_evaluation_lower_limit_for_zero_root_relief(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit"
    ):
        """EnumWithSelectedValue[mastapy.gears.micro_geometry.LocationOfEvaluationLowerLimit]"""
        temp = self.wrapped.LocationOfEvaluationLowerLimitForZeroRootRelief

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_evaluation_lower_limit_for_zero_root_relief.setter
    @enforce_parameter_types
    def location_of_evaluation_lower_limit_for_zero_root_relief(
        self: Self, value: "_576.LocationOfEvaluationLowerLimit"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationLowerLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfEvaluationLowerLimitForZeroRootRelief = value

    @property
    def location_of_evaluation_upper_limit(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit"
    ):
        """EnumWithSelectedValue[mastapy.gears.micro_geometry.LocationOfEvaluationUpperLimit]"""
        temp = self.wrapped.LocationOfEvaluationUpperLimit

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_evaluation_upper_limit.setter
    @enforce_parameter_types
    def location_of_evaluation_upper_limit(
        self: Self, value: "_577.LocationOfEvaluationUpperLimit"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfEvaluationUpperLimit = value

    @property
    def location_of_evaluation_upper_limit_for_zero_tip_relief(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit"
    ):
        """EnumWithSelectedValue[mastapy.gears.micro_geometry.LocationOfEvaluationUpperLimit]"""
        temp = self.wrapped.LocationOfEvaluationUpperLimitForZeroTipRelief

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_evaluation_upper_limit_for_zero_tip_relief.setter
    @enforce_parameter_types
    def location_of_evaluation_upper_limit_for_zero_tip_relief(
        self: Self, value: "_577.LocationOfEvaluationUpperLimit"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfEvaluationUpperLimit.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfEvaluationUpperLimitForZeroTipRelief = value

    @property
    def location_of_root_modification_start(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation"
    ):
        """EnumWithSelectedValue[mastapy.gears.micro_geometry.LocationOfRootReliefEvaluation]"""
        temp = self.wrapped.LocationOfRootModificationStart

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_root_modification_start.setter
    @enforce_parameter_types
    def location_of_root_modification_start(
        self: Self, value: "_578.LocationOfRootReliefEvaluation"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfRootModificationStart = value

    @property
    def location_of_root_relief_evaluation(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation"
    ):
        """EnumWithSelectedValue[mastapy.gears.micro_geometry.LocationOfRootReliefEvaluation]"""
        temp = self.wrapped.LocationOfRootReliefEvaluation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_root_relief_evaluation.setter
    @enforce_parameter_types
    def location_of_root_relief_evaluation(
        self: Self, value: "_578.LocationOfRootReliefEvaluation"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfRootReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfRootReliefEvaluation = value

    @property
    def location_of_tip_relief_evaluation(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation":
        """EnumWithSelectedValue[mastapy.gears.micro_geometry.LocationOfTipReliefEvaluation]"""
        temp = self.wrapped.LocationOfTipReliefEvaluation

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_tip_relief_evaluation.setter
    @enforce_parameter_types
    def location_of_tip_relief_evaluation(
        self: Self, value: "_579.LocationOfTipReliefEvaluation"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfTipReliefEvaluation = value

    @property
    def location_of_tip_relief_start(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation":
        """EnumWithSelectedValue[mastapy.gears.micro_geometry.LocationOfTipReliefEvaluation]"""
        temp = self.wrapped.LocationOfTipReliefStart

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @location_of_tip_relief_start.setter
    @enforce_parameter_types
    def location_of_tip_relief_start(
        self: Self, value: "_579.LocationOfTipReliefEvaluation"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_LocationOfTipReliefEvaluation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LocationOfTipReliefStart = value

    @property
    def main_profile_modification_ends_at_the_start_of_root_relief(
        self: Self,
    ) -> "_580.MainProfileReliefEndsAtTheStartOfRootReliefOption":
        """mastapy.gears.micro_geometry.MainProfileReliefEndsAtTheStartOfRootReliefOption"""
        temp = self.wrapped.MainProfileModificationEndsAtTheStartOfRootRelief

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.micro_geometry._580",
            "MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )(value)

    @main_profile_modification_ends_at_the_start_of_root_relief.setter
    @enforce_parameter_types
    def main_profile_modification_ends_at_the_start_of_root_relief(
        self: Self, value: "_580.MainProfileReliefEndsAtTheStartOfRootReliefOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfRootReliefOption",
        )
        self.wrapped.MainProfileModificationEndsAtTheStartOfRootRelief = value

    @property
    def main_profile_modification_ends_at_the_start_of_tip_relief(
        self: Self,
    ) -> "_581.MainProfileReliefEndsAtTheStartOfTipReliefOption":
        """mastapy.gears.micro_geometry.MainProfileReliefEndsAtTheStartOfTipReliefOption"""
        temp = self.wrapped.MainProfileModificationEndsAtTheStartOfTipRelief

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.micro_geometry._581",
            "MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )(value)

    @main_profile_modification_ends_at_the_start_of_tip_relief.setter
    @enforce_parameter_types
    def main_profile_modification_ends_at_the_start_of_tip_relief(
        self: Self, value: "_581.MainProfileReliefEndsAtTheStartOfTipReliefOption"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.MainProfileReliefEndsAtTheStartOfTipReliefOption",
        )
        self.wrapped.MainProfileModificationEndsAtTheStartOfTipRelief = value

    @property
    def measure_root_reliefs_from_extrapolated_linear_relief(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.MeasureRootReliefsFromExtrapolatedLinearRelief

        if temp is None:
            return False

        return temp

    @measure_root_reliefs_from_extrapolated_linear_relief.setter
    @enforce_parameter_types
    def measure_root_reliefs_from_extrapolated_linear_relief(self: Self, value: "bool"):
        self.wrapped.MeasureRootReliefsFromExtrapolatedLinearRelief = (
            bool(value) if value is not None else False
        )

    @property
    def measure_tip_reliefs_from_extrapolated_linear_relief(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.MeasureTipReliefsFromExtrapolatedLinearRelief

        if temp is None:
            return False

        return temp

    @measure_tip_reliefs_from_extrapolated_linear_relief.setter
    @enforce_parameter_types
    def measure_tip_reliefs_from_extrapolated_linear_relief(self: Self, value: "bool"):
        self.wrapped.MeasureTipReliefsFromExtrapolatedLinearRelief = (
            bool(value) if value is not None else False
        )

    @property
    def measured_data(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.MeasuredData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @measured_data.setter
    @enforce_parameter_types
    def measured_data(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.MeasuredData = value.wrapped

    @property
    def parabolic_root_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ParabolicRootRelief

        if temp is None:
            return 0.0

        return temp

    @parabolic_root_relief.setter
    @enforce_parameter_types
    def parabolic_root_relief(self: Self, value: "float"):
        self.wrapped.ParabolicRootRelief = float(value) if value is not None else 0.0

    @property
    def parabolic_root_relief_starts_tangent_to_main_profile_relief(
        self: Self,
    ) -> "_583.ParabolicRootReliefStartsTangentToMainProfileRelief":
        """mastapy.gears.micro_geometry.ParabolicRootReliefStartsTangentToMainProfileRelief"""
        temp = self.wrapped.ParabolicRootReliefStartsTangentToMainProfileRelief

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicRootReliefStartsTangentToMainProfileRelief",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.micro_geometry._583",
            "ParabolicRootReliefStartsTangentToMainProfileRelief",
        )(value)

    @parabolic_root_relief_starts_tangent_to_main_profile_relief.setter
    @enforce_parameter_types
    def parabolic_root_relief_starts_tangent_to_main_profile_relief(
        self: Self, value: "_583.ParabolicRootReliefStartsTangentToMainProfileRelief"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicRootReliefStartsTangentToMainProfileRelief",
        )
        self.wrapped.ParabolicRootReliefStartsTangentToMainProfileRelief = value

    @property
    def parabolic_tip_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ParabolicTipRelief

        if temp is None:
            return 0.0

        return temp

    @parabolic_tip_relief.setter
    @enforce_parameter_types
    def parabolic_tip_relief(self: Self, value: "float"):
        self.wrapped.ParabolicTipRelief = float(value) if value is not None else 0.0

    @property
    def parabolic_tip_relief_starts_tangent_to_main_profile_relief(
        self: Self,
    ) -> "_584.ParabolicTipReliefStartsTangentToMainProfileRelief":
        """mastapy.gears.micro_geometry.ParabolicTipReliefStartsTangentToMainProfileRelief"""
        temp = self.wrapped.ParabolicTipReliefStartsTangentToMainProfileRelief

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicTipReliefStartsTangentToMainProfileRelief",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.micro_geometry._584",
            "ParabolicTipReliefStartsTangentToMainProfileRelief",
        )(value)

    @parabolic_tip_relief_starts_tangent_to_main_profile_relief.setter
    @enforce_parameter_types
    def parabolic_tip_relief_starts_tangent_to_main_profile_relief(
        self: Self, value: "_584.ParabolicTipReliefStartsTangentToMainProfileRelief"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.MicroGeometry.ParabolicTipReliefStartsTangentToMainProfileRelief",
        )
        self.wrapped.ParabolicTipReliefStartsTangentToMainProfileRelief = value

    @property
    def start_of_linear_root_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRootReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_root_relief_factor.setter
    @enforce_parameter_types
    def start_of_linear_root_relief_factor(self: Self, value: "float"):
        self.wrapped.StartOfLinearRootReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_tip_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearTipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_tip_relief_factor.setter
    @enforce_parameter_types
    def start_of_linear_tip_relief_factor(self: Self, value: "float"):
        self.wrapped.StartOfLinearTipReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_root_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRootReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_root_relief_factor.setter
    @enforce_parameter_types
    def start_of_parabolic_root_relief_factor(self: Self, value: "float"):
        self.wrapped.StartOfParabolicRootReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_tip_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicTipReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_tip_relief_factor.setter
    @enforce_parameter_types
    def start_of_parabolic_tip_relief_factor(self: Self, value: "float"):
        self.wrapped.StartOfParabolicTipReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def use_measured_data(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseMeasuredData

        if temp is None:
            return False

        return temp

    @use_measured_data.setter
    @enforce_parameter_types
    def use_measured_data(self: Self, value: "bool"):
        self.wrapped.UseMeasuredData = bool(value) if value is not None else False

    @property
    def use_user_specified_barrelling_peak_point(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseUserSpecifiedBarrellingPeakPoint

        if temp is None:
            return False

        return temp

    @use_user_specified_barrelling_peak_point.setter
    @enforce_parameter_types
    def use_user_specified_barrelling_peak_point(self: Self, value: "bool"):
        self.wrapped.UseUserSpecifiedBarrellingPeakPoint = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "ProfileModification._Cast_ProfileModification":
        return self._Cast_ProfileModification(self)
