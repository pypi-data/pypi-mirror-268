"""ShaftSectionEndResultsSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SECTION_END_RESULTS_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ShaftSectionEndResultsSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.shafts import _16
    from mastapy.math_utility.measured_vectors import _1571


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSectionEndResultsSystemDeflection",)


Self = TypeVar("Self", bound="ShaftSectionEndResultsSystemDeflection")


class ShaftSectionEndResultsSystemDeflection(_0.APIBase):
    """ShaftSectionEndResultsSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_SECTION_END_RESULTS_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftSectionEndResultsSystemDeflection"
    )

    class _Cast_ShaftSectionEndResultsSystemDeflection:
        """Special nested class for casting ShaftSectionEndResultsSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftSectionEndResultsSystemDeflection._Cast_ShaftSectionEndResultsSystemDeflection",
            parent: "ShaftSectionEndResultsSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_section_end_results_system_deflection(
            self: "ShaftSectionEndResultsSystemDeflection._Cast_ShaftSectionEndResultsSystemDeflection",
        ) -> "ShaftSectionEndResultsSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftSectionEndResultsSystemDeflection._Cast_ShaftSectionEndResultsSystemDeflection",
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
        self: Self, instance_to_wrap: "ShaftSectionEndResultsSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cross_sectional_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrossSectionalArea

        if temp is None:
            return 0.0

        return temp

    @property
    def inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def offset(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def outer_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_area_moment_of_inertia(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PolarAreaMomentOfInertia

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_roughness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceRoughness

        if temp is None:
            return 0.0

        return temp

    @property
    def din743201212_fatigue_notch_factor_beta_sigma_beta_tau(
        self: Self,
    ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN743201212FatigueNotchFactorBetaSigmaBetaTau

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din743201212_geometrical_influence_factor_for_size_k2d(
        self: Self,
    ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN743201212GeometricalInfluenceFactorForSizeK2d

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din743201212_increase_factor_for_yield_point_gamma_f(
        self: Self,
    ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN743201212IncreaseFactorForYieldPointGammaF

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din743201212_static_support_factor_k2f(
        self: Self,
    ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN743201212StaticSupportFactorK2F

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din743201212_surface_roughness_influence_factor_kf_sigma_kf_tau(
        self: Self,
    ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN743201212SurfaceRoughnessInfluenceFactorKFSigmaKFTau

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def din743201212_total_influence_factor_k_sigma_k_tau(
        self: Self,
    ) -> "_16.ShaftAxialBendingTorsionalComponentValues":
        """mastapy.shafts.ShaftAxialBendingTorsionalComponentValues

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DIN743201212TotalInfluenceFactorKSigmaKTau

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def displacements(self: Self) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Displacements

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def forces(self: Self) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Forces

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftSectionEndResultsSystemDeflection._Cast_ShaftSectionEndResultsSystemDeflection":
        return self._Cast_ShaftSectionEndResultsSystemDeflection(self)
