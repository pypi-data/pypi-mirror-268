"""TESetUpForDynamicAnalysisOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TE_SET_UP_FOR_DYNAMIC_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults", "TESetUpForDynamicAnalysisOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("TESetUpForDynamicAnalysisOptions",)


Self = TypeVar("Self", bound="TESetUpForDynamicAnalysisOptions")


class TESetUpForDynamicAnalysisOptions(_0.APIBase):
    """TESetUpForDynamicAnalysisOptions

    This is a mastapy class.
    """

    TYPE = _TE_SET_UP_FOR_DYNAMIC_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TESetUpForDynamicAnalysisOptions")

    class _Cast_TESetUpForDynamicAnalysisOptions:
        """Special nested class for casting TESetUpForDynamicAnalysisOptions to subclasses."""

        def __init__(
            self: "TESetUpForDynamicAnalysisOptions._Cast_TESetUpForDynamicAnalysisOptions",
            parent: "TESetUpForDynamicAnalysisOptions",
        ):
            self._parent = parent

        @property
        def te_set_up_for_dynamic_analysis_options(
            self: "TESetUpForDynamicAnalysisOptions._Cast_TESetUpForDynamicAnalysisOptions",
        ) -> "TESetUpForDynamicAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "TESetUpForDynamicAnalysisOptions._Cast_TESetUpForDynamicAnalysisOptions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TESetUpForDynamicAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def include_misalignment_excitation(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeMisalignmentExcitation

        if temp is None:
            return False

        return temp

    @include_misalignment_excitation.setter
    @enforce_parameter_types
    def include_misalignment_excitation(self: Self, value: "bool"):
        self.wrapped.IncludeMisalignmentExcitation = (
            bool(value) if value is not None else False
        )

    @property
    def use_data_logger_for_advanced_system_deflection_single_tooth_pass_harmonic_excitation_type_options(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseDataLoggerForAdvancedSystemDeflectionSingleToothPassHarmonicExcitationTypeOptions
        )

        if temp is None:
            return False

        return temp

    @use_data_logger_for_advanced_system_deflection_single_tooth_pass_harmonic_excitation_type_options.setter
    @enforce_parameter_types
    def use_data_logger_for_advanced_system_deflection_single_tooth_pass_harmonic_excitation_type_options(
        self: Self, value: "bool"
    ):
        self.wrapped.UseDataLoggerForAdvancedSystemDeflectionSingleToothPassHarmonicExcitationTypeOptions = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "TESetUpForDynamicAnalysisOptions._Cast_TESetUpForDynamicAnalysisOptions":
        return self._Cast_TESetUpForDynamicAnalysisOptions(self)
