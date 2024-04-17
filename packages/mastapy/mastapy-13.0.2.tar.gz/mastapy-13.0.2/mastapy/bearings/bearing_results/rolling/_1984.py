"""ISO153122018Results"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO153122018_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "ISO153122018Results"
)


__docformat__ = "restructuredtext en"
__all__ = ("ISO153122018Results",)


Self = TypeVar("Self", bound="ISO153122018Results")


class ISO153122018Results(_0.APIBase):
    """ISO153122018Results

    This is a mastapy class.
    """

    TYPE = _ISO153122018_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO153122018Results")

    class _Cast_ISO153122018Results:
        """Special nested class for casting ISO153122018Results to subclasses."""

        def __init__(
            self: "ISO153122018Results._Cast_ISO153122018Results",
            parent: "ISO153122018Results",
        ):
            self._parent = parent

        @property
        def iso153122018_results(
            self: "ISO153122018Results._Cast_ISO153122018Results",
        ) -> "ISO153122018Results":
            return self._parent

        def __getattr__(
            self: "ISO153122018Results._Cast_ISO153122018Results", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO153122018Results.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_for_the_load_dependent_friction_moment_for_the_reference_conditions(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.CoefficientForTheLoadDependentFrictionMomentForTheReferenceConditions
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def coefficient_for_the_load_independent_friction_moment_for_the_reference_conditions(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.CoefficientForTheLoadIndependentFrictionMomentForTheReferenceConditions
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def heat_emitting_reference_surface_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeatEmittingReferenceSurfaceArea

        if temp is None:
            return 0.0

        return temp

    @property
    def load_dependent_frictional_moment_under_reference_conditions_at_the_thermal_speed_rating(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LoadDependentFrictionalMomentUnderReferenceConditionsAtTheThermalSpeedRating
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def load_independent_frictional_moment_under_reference_conditions_at_the_thermal_speed_rating(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.LoadIndependentFrictionalMomentUnderReferenceConditionsAtTheThermalSpeedRating
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def power_loss_under_reference_conditions_at_the_thermal_speed_rating(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLossUnderReferenceConditionsAtTheThermalSpeedRating

        if temp is None:
            return 0.0

        return temp

    @property
    def reason_for_invalidity(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonForInvalidity

        if temp is None:
            return ""

        return temp

    @property
    def reference_heat_flow(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceHeatFlow

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_heat_flow_density(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceHeatFlowDensity

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def thermal_speed_rating(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThermalSpeedRating

        if temp is None:
            return 0.0

        return temp

    @property
    def viscosity_of_reference_oil(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ViscosityOfReferenceOil

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "ISO153122018Results._Cast_ISO153122018Results":
        return self._Cast_ISO153122018Results(self)
