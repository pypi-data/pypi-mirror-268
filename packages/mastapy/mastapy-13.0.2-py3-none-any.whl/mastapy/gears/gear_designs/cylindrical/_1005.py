"""CaseHardeningProperties"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CASE_HARDENING_PROPERTIES = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CaseHardeningProperties"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1056, _1057


__docformat__ = "restructuredtext en"
__all__ = ("CaseHardeningProperties",)


Self = TypeVar("Self", bound="CaseHardeningProperties")


class CaseHardeningProperties(_0.APIBase):
    """CaseHardeningProperties

    This is a mastapy class.
    """

    TYPE = _CASE_HARDENING_PROPERTIES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CaseHardeningProperties")

    class _Cast_CaseHardeningProperties:
        """Special nested class for casting CaseHardeningProperties to subclasses."""

        def __init__(
            self: "CaseHardeningProperties._Cast_CaseHardeningProperties",
            parent: "CaseHardeningProperties",
        ):
            self._parent = parent

        @property
        def case_hardening_properties(
            self: "CaseHardeningProperties._Cast_CaseHardeningProperties",
        ) -> "CaseHardeningProperties":
            return self._parent

        def __getattr__(
            self: "CaseHardeningProperties._Cast_CaseHardeningProperties", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CaseHardeningProperties.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def depth_at_maximum_hardness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DepthAtMaximumHardness

        if temp is None:
            return 0.0

        return temp

    @depth_at_maximum_hardness.setter
    @enforce_parameter_types
    def depth_at_maximum_hardness(self: Self, value: "float"):
        self.wrapped.DepthAtMaximumHardness = float(value) if value is not None else 0.0

    @property
    def effective_case_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EffectiveCaseDepth

        if temp is None:
            return 0.0

        return temp

    @effective_case_depth.setter
    @enforce_parameter_types
    def effective_case_depth(self: Self, value: "float"):
        self.wrapped.EffectiveCaseDepth = float(value) if value is not None else 0.0

    @property
    def hardness_profile_calculation_method(
        self: Self,
    ) -> "_1056.HardnessProfileCalculationMethod":
        """mastapy.gears.gear_designs.cylindrical.HardnessProfileCalculationMethod"""
        temp = self.wrapped.HardnessProfileCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.HardnessProfileCalculationMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1056",
            "HardnessProfileCalculationMethod",
        )(value)

    @hardness_profile_calculation_method.setter
    @enforce_parameter_types
    def hardness_profile_calculation_method(
        self: Self, value: "_1056.HardnessProfileCalculationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.HardnessProfileCalculationMethod",
        )
        self.wrapped.HardnessProfileCalculationMethod = value

    @property
    def heat_treatment_type(self: Self) -> "_1057.HeatTreatmentType":
        """mastapy.gears.gear_designs.cylindrical.HeatTreatmentType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeatTreatmentType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.HeatTreatmentType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1057", "HeatTreatmentType"
        )(value)

    @property
    def total_case_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TotalCaseDepth

        if temp is None:
            return 0.0

        return temp

    @total_case_depth.setter
    @enforce_parameter_types
    def total_case_depth(self: Self, value: "float"):
        self.wrapped.TotalCaseDepth = float(value) if value is not None else 0.0

    @property
    def vickers_hardness_hv_at_effective_case_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.VickersHardnessHVAtEffectiveCaseDepth

        if temp is None:
            return 0.0

        return temp

    @vickers_hardness_hv_at_effective_case_depth.setter
    @enforce_parameter_types
    def vickers_hardness_hv_at_effective_case_depth(self: Self, value: "float"):
        self.wrapped.VickersHardnessHVAtEffectiveCaseDepth = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "CaseHardeningProperties._Cast_CaseHardeningProperties":
        return self._Cast_CaseHardeningProperties(self)
