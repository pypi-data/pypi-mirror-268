"""PermissibleContinuousAxialLoadResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.implicit import overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERMISSIBLE_CONTINUOUS_AXIAL_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "PermissibleContinuousAxialLoadResults",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1949


__docformat__ = "restructuredtext en"
__all__ = ("PermissibleContinuousAxialLoadResults",)


Self = TypeVar("Self", bound="PermissibleContinuousAxialLoadResults")


class PermissibleContinuousAxialLoadResults(_0.APIBase):
    """PermissibleContinuousAxialLoadResults

    This is a mastapy class.
    """

    TYPE = _PERMISSIBLE_CONTINUOUS_AXIAL_LOAD_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PermissibleContinuousAxialLoadResults"
    )

    class _Cast_PermissibleContinuousAxialLoadResults:
        """Special nested class for casting PermissibleContinuousAxialLoadResults to subclasses."""

        def __init__(
            self: "PermissibleContinuousAxialLoadResults._Cast_PermissibleContinuousAxialLoadResults",
            parent: "PermissibleContinuousAxialLoadResults",
        ):
            self._parent = parent

        @property
        def permissible_continuous_axial_load_results(
            self: "PermissibleContinuousAxialLoadResults._Cast_PermissibleContinuousAxialLoadResults",
        ) -> "PermissibleContinuousAxialLoadResults":
            return self._parent

        def __getattr__(
            self: "PermissibleContinuousAxialLoadResults._Cast_PermissibleContinuousAxialLoadResults",
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
        self: Self, instance_to_wrap: "PermissibleContinuousAxialLoadResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_axial_load_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableAxialLoadFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def allowable_constant_axial_load_ntn(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableConstantAxialLoadNTN

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_intermittent_axial_load_ntn(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableIntermittentAxialLoadNTN

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_momentary_axial_load_ntn(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableMomentaryAxialLoadNTN

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def calculation_method(self: Self) -> "_1949.CylindricalRollerMaxAxialLoadMethod":
        """mastapy.bearings.bearing_results.CylindricalRollerMaxAxialLoadMethod

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Bearings.BearingResults.CylindricalRollerMaxAxialLoadMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings.bearing_results._1949",
            "CylindricalRollerMaxAxialLoadMethod",
        )(value)

    @property
    def capacity_lubrication_factor_for_permissible_axial_load_grease(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadGrease

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def capacity_lubrication_factor_for_permissible_axial_load_oil(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CapacityLubricationFactorForPermissibleAxialLoadOil

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def diameter_exponent_factor_for_permissible_axial_load(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterExponentFactorForPermissibleAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def diameter_scaling_factor_for_permissible_axial_load(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DiameterScalingFactorForPermissibleAxialLoad

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def maximum_permissible_axial_load_schaeffler(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPermissibleAxialLoadSchaeffler

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_load_schaeffler(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialLoadSchaeffler

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_load_dimension_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialLoadDimensionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def permissible_axial_load_internal_dimension_factor(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialLoadInternalDimensionFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def permissible_axial_load_under_shaft_deflection_schaeffler(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialLoadUnderShaftDeflectionSchaeffler

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_load_for_brief_periods_skf(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialLoadForBriefPeriodsSKF

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_load_for_occasional_peak_loads_skf(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialLoadForOccasionalPeakLoadsSKF

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_axial_loading_nachi(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleAxialLoadingNACHI

        if temp is None:
            return 0.0

        return temp

    @property
    def permissible_continuous_axial_load_skf(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PermissibleContinuousAxialLoadSKF

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_load_lubrication_factor_for_permissible_axial_load_grease(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadGrease

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def radial_load_lubrication_factor_for_permissible_axial_load_oil(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialLoadLubricationFactorForPermissibleAxialLoadOil

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @property
    def safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "PermissibleContinuousAxialLoadResults._Cast_PermissibleContinuousAxialLoadResults":
        return self._Cast_PermissibleContinuousAxialLoadResults(self)
