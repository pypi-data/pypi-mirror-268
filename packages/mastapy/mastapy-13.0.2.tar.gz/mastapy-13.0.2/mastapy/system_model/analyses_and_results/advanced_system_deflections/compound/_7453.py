"""CouplingHalfCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7491,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7321,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7437,
        _7442,
        _7456,
        _7496,
        _7502,
        _7506,
        _7518,
        _7528,
        _7529,
        _7530,
        _7533,
        _7534,
        _7439,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfCompoundAdvancedSystemDeflection")


class CouplingHalfCompoundAdvancedSystemDeflection(
    _7491.MountableComponentCompoundAdvancedSystemDeflection
):
    """CouplingHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_CouplingHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
            parent: "CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7491.MountableComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7491.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7439.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(_7439.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7437.ClutchHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7437,
            )

            return self._parent._cast(_7437.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7442.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7456.CVTPulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7456,
            )

            return self._parent._cast(_7456.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7496.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(
                _7496.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def pulley_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7502.PulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(_7502.PulleyCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7506.RollingRingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(_7506.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7518.SpringDamperHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7528.SynchroniserHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7529.SynchroniserPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(
                _7529.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7530.SynchroniserSleeveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7533.TorqueConverterPumpCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(
                _7533.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7534.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "CouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "CouplingHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7321.CouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingHalfAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7321.CouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingHalfAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection":
        return self._Cast_CouplingHalfCompoundAdvancedSystemDeflection(self)
