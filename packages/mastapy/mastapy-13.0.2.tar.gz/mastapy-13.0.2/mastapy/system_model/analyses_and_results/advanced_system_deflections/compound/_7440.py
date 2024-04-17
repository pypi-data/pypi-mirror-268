"""ConceptCouplingCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7451,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConceptCouplingCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7307,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7512,
        _7414,
        _7493,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundAdvancedSystemDeflection")


class ConceptCouplingCompoundAdvancedSystemDeflection(
    _7451.CouplingCompoundAdvancedSystemDeflection
):
    """ConceptCouplingCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConceptCouplingCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptCouplingCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
            parent: "ConceptCouplingCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_compound_advanced_system_deflection(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7451.CouplingCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7451.CouplingCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7512.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7414.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(
                _7414.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7493.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(_7493.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
        ) -> "ConceptCouplingCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConceptCouplingCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2588.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7307.ConceptCouplingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptCouplingAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7307.ConceptCouplingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptCouplingAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingCompoundAdvancedSystemDeflection._Cast_ConceptCouplingCompoundAdvancedSystemDeflection":
        return self._Cast_ConceptCouplingCompoundAdvancedSystemDeflection(self)
