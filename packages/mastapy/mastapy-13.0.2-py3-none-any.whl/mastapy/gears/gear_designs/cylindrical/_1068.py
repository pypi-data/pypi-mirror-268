"""MullerResidualStressDefinition"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULLER_RESIDUAL_STRESS_DEFINITION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "MullerResidualStressDefinition"
)


__docformat__ = "restructuredtext en"
__all__ = ("MullerResidualStressDefinition",)


Self = TypeVar("Self", bound="MullerResidualStressDefinition")


class MullerResidualStressDefinition(
    _1593.IndependentReportablePropertiesBase["MullerResidualStressDefinition"]
):
    """MullerResidualStressDefinition

    This is a mastapy class.
    """

    TYPE = _MULLER_RESIDUAL_STRESS_DEFINITION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MullerResidualStressDefinition")

    class _Cast_MullerResidualStressDefinition:
        """Special nested class for casting MullerResidualStressDefinition to subclasses."""

        def __init__(
            self: "MullerResidualStressDefinition._Cast_MullerResidualStressDefinition",
            parent: "MullerResidualStressDefinition",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "MullerResidualStressDefinition._Cast_MullerResidualStressDefinition",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def muller_residual_stress_definition(
            self: "MullerResidualStressDefinition._Cast_MullerResidualStressDefinition",
        ) -> "MullerResidualStressDefinition":
            return self._parent

        def __getattr__(
            self: "MullerResidualStressDefinition._Cast_MullerResidualStressDefinition",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MullerResidualStressDefinition.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compressive_residual_stress_at_surface(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CompressiveResidualStressAtSurface

        if temp is None:
            return 0.0

        return temp

    @compressive_residual_stress_at_surface.setter
    @enforce_parameter_types
    def compressive_residual_stress_at_surface(self: Self, value: "float"):
        self.wrapped.CompressiveResidualStressAtSurface = (
            float(value) if value is not None else 0.0
        )

    @property
    def depth_of_maximum_compressive_residual_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DepthOfMaximumCompressiveResidualStress

        if temp is None:
            return 0.0

        return temp

    @depth_of_maximum_compressive_residual_stress.setter
    @enforce_parameter_types
    def depth_of_maximum_compressive_residual_stress(self: Self, value: "float"):
        self.wrapped.DepthOfMaximumCompressiveResidualStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def depth_of_transition_from_compressive_to_tensile(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DepthOfTransitionFromCompressiveToTensile

        if temp is None:
            return 0.0

        return temp

    @depth_of_transition_from_compressive_to_tensile.setter
    @enforce_parameter_types
    def depth_of_transition_from_compressive_to_tensile(self: Self, value: "float"):
        self.wrapped.DepthOfTransitionFromCompressiveToTensile = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_compressive_residual_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumCompressiveResidualStress

        if temp is None:
            return 0.0

        return temp

    @maximum_compressive_residual_stress.setter
    @enforce_parameter_types
    def maximum_compressive_residual_stress(self: Self, value: "float"):
        self.wrapped.MaximumCompressiveResidualStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_tensile_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumTensileStress

        if temp is None:
            return 0.0

        return temp

    @maximum_tensile_stress.setter
    @enforce_parameter_types
    def maximum_tensile_stress(self: Self, value: "float"):
        self.wrapped.MaximumTensileStress = float(value) if value is not None else 0.0

    @property
    def parameter_delta(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterDelta

        if temp is None:
            return 0.0

        return temp

    @property
    def parameter_for_the_slope_in_the_transition_from_compressive_to_tensile_residual_stresses(
        self: Self,
    ) -> "float":
        """float"""
        temp = (
            self.wrapped.ParameterForTheSlopeInTheTransitionFromCompressiveToTensileResidualStresses
        )

        if temp is None:
            return 0.0

        return temp

    @parameter_for_the_slope_in_the_transition_from_compressive_to_tensile_residual_stresses.setter
    @enforce_parameter_types
    def parameter_for_the_slope_in_the_transition_from_compressive_to_tensile_residual_stresses(
        self: Self, value: "float"
    ):
        self.wrapped.ParameterForTheSlopeInTheTransitionFromCompressiveToTensileResidualStresses = (
            float(value) if value is not None else 0.0
        )

    @property
    def parameter_k(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterK

        if temp is None:
            return 0.0

        return temp

    @property
    def parameter_to_adjust_the_compressive_residual_stresses(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ParameterToAdjustTheCompressiveResidualStresses

        if temp is None:
            return 0.0

        return temp

    @parameter_to_adjust_the_compressive_residual_stresses.setter
    @enforce_parameter_types
    def parameter_to_adjust_the_compressive_residual_stresses(
        self: Self, value: "float"
    ):
        self.wrapped.ParameterToAdjustTheCompressiveResidualStresses = (
            float(value) if value is not None else 0.0
        )

    @property
    def parameter_to_define_compressive_residual_stresses_at_surface(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParameterToDefineCompressiveResidualStressesAtSurface

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "MullerResidualStressDefinition._Cast_MullerResidualStressDefinition":
        return self._Cast_MullerResidualStressDefinition(self)
