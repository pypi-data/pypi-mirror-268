"""ConceptCouplingConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7452,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2351
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7308,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7479,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="ConceptCouplingConnectionCompoundAdvancedSystemDeflection"
)


class ConceptCouplingConnectionCompoundAdvancedSystemDeflection(
    _7452.CouplingConnectionCompoundAdvancedSystemDeflection
):
    """ConceptCouplingConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptCouplingConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
            parent: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7452.CouplingConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7452.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2351.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2351.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7308.ConceptCouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptCouplingConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7308.ConceptCouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptCouplingConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection(
            self
        )
