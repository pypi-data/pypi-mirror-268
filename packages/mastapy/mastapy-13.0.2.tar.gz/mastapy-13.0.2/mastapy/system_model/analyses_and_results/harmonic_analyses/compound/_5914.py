"""ConceptCouplingConnectionCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5925
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConceptCouplingConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2351
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5714
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5952,
        _5922,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionCompoundHarmonicAnalysis")


class ConceptCouplingConnectionCompoundHarmonicAnalysis(
    _5925.CouplingConnectionCompoundHarmonicAnalysis
):
    """ConceptCouplingConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis"
    )

    class _Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting ConceptCouplingConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
            parent: "ConceptCouplingConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
        ) -> "_5925.CouplingConnectionCompoundHarmonicAnalysis":
            return self._parent._cast(_5925.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
        ) -> "_5952.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
        ) -> "_5922.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
        ) -> "ConceptCouplingConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundHarmonicAnalysis.TYPE",
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
    ) -> "List[_5714.ConceptCouplingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingConnectionHarmonicAnalysis]

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
    ) -> "List[_5714.ConceptCouplingConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingConnectionHarmonicAnalysis]

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
    ) -> "ConceptCouplingConnectionCompoundHarmonicAnalysis._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis":
        return self._Cast_ConceptCouplingConnectionCompoundHarmonicAnalysis(self)
