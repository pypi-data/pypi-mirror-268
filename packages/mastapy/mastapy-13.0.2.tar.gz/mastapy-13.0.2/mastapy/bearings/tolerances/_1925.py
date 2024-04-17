"""RoundnessSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROUNDNESS_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "RoundnessSpecification"
)

if TYPE_CHECKING:
    from mastapy.bearings.tolerances import _1926, _1932, _1922
    from mastapy.math_utility import _1542


__docformat__ = "restructuredtext en"
__all__ = ("RoundnessSpecification",)


Self = TypeVar("Self", bound="RoundnessSpecification")


class RoundnessSpecification(
    _1593.IndependentReportablePropertiesBase["RoundnessSpecification"]
):
    """RoundnessSpecification

    This is a mastapy class.
    """

    TYPE = _ROUNDNESS_SPECIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RoundnessSpecification")

    class _Cast_RoundnessSpecification:
        """Special nested class for casting RoundnessSpecification to subclasses."""

        def __init__(
            self: "RoundnessSpecification._Cast_RoundnessSpecification",
            parent: "RoundnessSpecification",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "RoundnessSpecification._Cast_RoundnessSpecification",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def roundness_specification(
            self: "RoundnessSpecification._Cast_RoundnessSpecification",
        ) -> "RoundnessSpecification":
            return self._parent

        def __getattr__(
            self: "RoundnessSpecification._Cast_RoundnessSpecification", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RoundnessSpecification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_first_max_deviation_from_round(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngleOfFirstMaxDeviationFromRound

        if temp is None:
            return 0.0

        return temp

    @angle_of_first_max_deviation_from_round.setter
    @enforce_parameter_types
    def angle_of_first_max_deviation_from_round(self: Self, value: "float"):
        self.wrapped.AngleOfFirstMaxDeviationFromRound = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_deviation_from_round(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumDeviationFromRound

        if temp is None:
            return 0.0

        return temp

    @maximum_deviation_from_round.setter
    @enforce_parameter_types
    def maximum_deviation_from_round(self: Self, value: "float"):
        self.wrapped.MaximumDeviationFromRound = (
            float(value) if value is not None else 0.0
        )

    @property
    def number_of_lobes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfLobes

        if temp is None:
            return 0

        return temp

    @number_of_lobes.setter
    @enforce_parameter_types
    def number_of_lobes(self: Self, value: "int"):
        self.wrapped.NumberOfLobes = int(value) if value is not None else 0

    @property
    def specification_type(self: Self) -> "_1926.RoundnessSpecificationType":
        """mastapy.bearings.tolerances.RoundnessSpecificationType"""
        temp = self.wrapped.SpecificationType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.RoundnessSpecificationType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.tolerances._1926", "RoundnessSpecificationType"
        )(value)

    @specification_type.setter
    @enforce_parameter_types
    def specification_type(self: Self, value: "_1926.RoundnessSpecificationType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.Tolerances.RoundnessSpecificationType"
        )
        self.wrapped.SpecificationType = value

    @property
    def type_of_fit(self: Self) -> "_1932.TypeOfFit":
        """mastapy.bearings.tolerances.TypeOfFit"""
        temp = self.wrapped.TypeOfFit

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.Tolerances.TypeOfFit"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.tolerances._1932", "TypeOfFit"
        )(value)

    @type_of_fit.setter
    @enforce_parameter_types
    def type_of_fit(self: Self, value: "_1932.TypeOfFit"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.Tolerances.TypeOfFit"
        )
        self.wrapped.TypeOfFit = value

    @property
    def user_specified_deviation(self: Self) -> "_1542.Vector2DListAccessor":
        """mastapy.math_utility.Vector2DListAccessor"""
        temp = self.wrapped.UserSpecifiedDeviation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @user_specified_deviation.setter
    @enforce_parameter_types
    def user_specified_deviation(self: Self, value: "_1542.Vector2DListAccessor"):
        self.wrapped.UserSpecifiedDeviation = value.wrapped

    @property
    def roundness_distribution(self: Self) -> "List[_1922.RaceRoundnessAtAngle]":
        """List[mastapy.bearings.tolerances.RaceRoundnessAtAngle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoundnessDistribution

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "RoundnessSpecification._Cast_RoundnessSpecification":
        return self._Cast_RoundnessSpecification(self)
