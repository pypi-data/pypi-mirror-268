"""SAESplineTolerances"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_TOLERANCES = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.TolerancesAndDeviations",
    "SAESplineTolerances",
)


__docformat__ = "restructuredtext en"
__all__ = ("SAESplineTolerances",)


Self = TypeVar("Self", bound="SAESplineTolerances")


class SAESplineTolerances(_0.APIBase):
    """SAESplineTolerances

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_TOLERANCES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SAESplineTolerances")

    class _Cast_SAESplineTolerances:
        """Special nested class for casting SAESplineTolerances to subclasses."""

        def __init__(
            self: "SAESplineTolerances._Cast_SAESplineTolerances",
            parent: "SAESplineTolerances",
        ):
            self._parent = parent

        @property
        def sae_spline_tolerances(
            self: "SAESplineTolerances._Cast_SAESplineTolerances",
        ) -> "SAESplineTolerances":
            return self._parent

        def __getattr__(
            self: "SAESplineTolerances._Cast_SAESplineTolerances", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SAESplineTolerances.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def internal_major_diameter_tolerance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InternalMajorDiameterTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def lead_variation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def machining_variation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MachiningVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def major_diameter_tolerance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MajorDiameterTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def minor_diameter_tolerance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinorDiameterTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def multiplier_f(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultiplierF

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_variation_f_fm(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileVariationF_fm

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_variation_f_fp(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ProfileVariationF_fp

        if temp is None:
            return 0.0

        return temp

    @property
    def total_index_variation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalIndexVariation

        if temp is None:
            return 0.0

        return temp

    @property
    def variation_tolerance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VariationTolerance

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "SAESplineTolerances._Cast_SAESplineTolerances":
        return self._Cast_SAESplineTolerances(self)
