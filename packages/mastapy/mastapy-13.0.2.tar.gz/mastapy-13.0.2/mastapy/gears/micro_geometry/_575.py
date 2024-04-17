"""LeadModification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.micro_geometry import _582
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LEAD_MODIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.MicroGeometry", "LeadModification"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1542
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102, _1103
    from mastapy.gears.gear_designs.conical.micro_geometry import _1180


__docformat__ = "restructuredtext en"
__all__ = ("LeadModification",)


Self = TypeVar("Self", bound="LeadModification")


class LeadModification(_582.Modification):
    """LeadModification

    This is a mastapy class.
    """

    TYPE = _LEAD_MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LeadModification")

    class _Cast_LeadModification:
        """Special nested class for casting LeadModification to subclasses."""

        def __init__(
            self: "LeadModification._Cast_LeadModification", parent: "LeadModification"
        ):
            self._parent = parent

        @property
        def modification(
            self: "LeadModification._Cast_LeadModification",
        ) -> "_582.Modification":
            return self._parent._cast(_582.Modification)

        @property
        def cylindrical_gear_lead_modification(
            self: "LeadModification._Cast_LeadModification",
        ) -> "_1102.CylindricalGearLeadModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1102

            return self._parent._cast(_1102.CylindricalGearLeadModification)

        @property
        def cylindrical_gear_lead_modification_at_profile_position(
            self: "LeadModification._Cast_LeadModification",
        ) -> "_1103.CylindricalGearLeadModificationAtProfilePosition":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1103

            return self._parent._cast(
                _1103.CylindricalGearLeadModificationAtProfilePosition
            )

        @property
        def conical_gear_lead_modification(
            self: "LeadModification._Cast_LeadModification",
        ) -> "_1180.ConicalGearLeadModification":
            from mastapy.gears.gear_designs.conical.micro_geometry import _1180

            return self._parent._cast(_1180.ConicalGearLeadModification)

        @property
        def lead_modification(
            self: "LeadModification._Cast_LeadModification",
        ) -> "LeadModification":
            return self._parent

        def __getattr__(self: "LeadModification._Cast_LeadModification", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LeadModification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CrowningRelief

        if temp is None:
            return 0.0

        return temp

    @crowning_relief.setter
    @enforce_parameter_types
    def crowning_relief(self: Self, value: "float"):
        self.wrapped.CrowningRelief = float(value) if value is not None else 0.0

    @property
    def evaluation_left_limit_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationLeftLimitFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_left_limit_factor.setter
    @enforce_parameter_types
    def evaluation_left_limit_factor(self: Self, value: "float"):
        self.wrapped.EvaluationLeftLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_left_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearLeftReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_left_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_linear_left_relief_factor(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearLeftReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_right_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfLinearRightReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_linear_right_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_linear_right_relief_factor(self: Self, value: "float"):
        self.wrapped.EvaluationOfLinearRightReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_linear_side_relief_factor(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationOfLinearSideReliefFactor

        if temp is None:
            return None

        return temp

    @evaluation_of_linear_side_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_linear_side_relief_factor(self: Self, value: "Optional[float]"):
        self.wrapped.EvaluationOfLinearSideReliefFactor = value

    @property
    def evaluation_of_parabolic_left_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicLeftReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_left_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_left_relief_factor(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicLeftReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_right_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationOfParabolicRightReliefFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_of_parabolic_right_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_right_relief_factor(self: Self, value: "float"):
        self.wrapped.EvaluationOfParabolicRightReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_of_parabolic_side_relief_factor(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationOfParabolicSideReliefFactor

        if temp is None:
            return None

        return temp

    @evaluation_of_parabolic_side_relief_factor.setter
    @enforce_parameter_types
    def evaluation_of_parabolic_side_relief_factor(
        self: Self, value: "Optional[float]"
    ):
        self.wrapped.EvaluationOfParabolicSideReliefFactor = value

    @property
    def evaluation_right_limit_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EvaluationRightLimitFactor

        if temp is None:
            return 0.0

        return temp

    @evaluation_right_limit_factor.setter
    @enforce_parameter_types
    def evaluation_right_limit_factor(self: Self, value: "float"):
        self.wrapped.EvaluationRightLimitFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def evaluation_side_limit_factor(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.EvaluationSideLimitFactor

        if temp is None:
            return None

        return temp

    @evaluation_side_limit_factor.setter
    @enforce_parameter_types
    def evaluation_side_limit_factor(self: Self, value: "Optional[float]"):
        self.wrapped.EvaluationSideLimitFactor = value

    @property
    def linear_left_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearLeftRelief

        if temp is None:
            return 0.0

        return temp

    @linear_left_relief.setter
    @enforce_parameter_types
    def linear_left_relief(self: Self, value: "float"):
        self.wrapped.LinearLeftRelief = float(value) if value is not None else 0.0

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
    def linear_right_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.LinearRightRelief

        if temp is None:
            return 0.0

        return temp

    @linear_right_relief.setter
    @enforce_parameter_types
    def linear_right_relief(self: Self, value: "float"):
        self.wrapped.LinearRightRelief = float(value) if value is not None else 0.0

    @property
    def linear_side_relief(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.LinearSideRelief

        if temp is None:
            return None

        return temp

    @linear_side_relief.setter
    @enforce_parameter_types
    def linear_side_relief(self: Self, value: "Optional[float]"):
        self.wrapped.LinearSideRelief = value

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
    def parabolic_left_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ParabolicLeftRelief

        if temp is None:
            return 0.0

        return temp

    @parabolic_left_relief.setter
    @enforce_parameter_types
    def parabolic_left_relief(self: Self, value: "float"):
        self.wrapped.ParabolicLeftRelief = float(value) if value is not None else 0.0

    @property
    def parabolic_right_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ParabolicRightRelief

        if temp is None:
            return 0.0

        return temp

    @parabolic_right_relief.setter
    @enforce_parameter_types
    def parabolic_right_relief(self: Self, value: "float"):
        self.wrapped.ParabolicRightRelief = float(value) if value is not None else 0.0

    @property
    def parabolic_side_relief(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.ParabolicSideRelief

        if temp is None:
            return None

        return temp

    @parabolic_side_relief.setter
    @enforce_parameter_types
    def parabolic_side_relief(self: Self, value: "Optional[float]"):
        self.wrapped.ParabolicSideRelief = value

    @property
    def start_of_linear_left_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearLeftReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_left_relief_factor.setter
    @enforce_parameter_types
    def start_of_linear_left_relief_factor(self: Self, value: "float"):
        self.wrapped.StartOfLinearLeftReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_right_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfLinearRightReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_linear_right_relief_factor.setter
    @enforce_parameter_types
    def start_of_linear_right_relief_factor(self: Self, value: "float"):
        self.wrapped.StartOfLinearRightReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_linear_side_relief_factor(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.StartOfLinearSideReliefFactor

        if temp is None:
            return None

        return temp

    @start_of_linear_side_relief_factor.setter
    @enforce_parameter_types
    def start_of_linear_side_relief_factor(self: Self, value: "Optional[float]"):
        self.wrapped.StartOfLinearSideReliefFactor = value

    @property
    def start_of_parabolic_left_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicLeftReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_left_relief_factor.setter
    @enforce_parameter_types
    def start_of_parabolic_left_relief_factor(self: Self, value: "float"):
        self.wrapped.StartOfParabolicLeftReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_right_relief_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StartOfParabolicRightReliefFactor

        if temp is None:
            return 0.0

        return temp

    @start_of_parabolic_right_relief_factor.setter
    @enforce_parameter_types
    def start_of_parabolic_right_relief_factor(self: Self, value: "float"):
        self.wrapped.StartOfParabolicRightReliefFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def start_of_parabolic_side_relief_factor(self: Self) -> "Optional[float]":
        """Optional[float]"""
        temp = self.wrapped.StartOfParabolicSideReliefFactor

        if temp is None:
            return None

        return temp

    @start_of_parabolic_side_relief_factor.setter
    @enforce_parameter_types
    def start_of_parabolic_side_relief_factor(self: Self, value: "Optional[float]"):
        self.wrapped.StartOfParabolicSideReliefFactor = value

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
    def cast_to(self: Self) -> "LeadModification._Cast_LeadModification":
        return self._Cast_LeadModification(self)
