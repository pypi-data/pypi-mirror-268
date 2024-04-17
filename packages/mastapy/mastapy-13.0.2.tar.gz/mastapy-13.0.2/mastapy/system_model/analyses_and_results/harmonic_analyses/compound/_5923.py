"""ConnectorCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5964
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "ConnectorCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5724
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5895,
        _5965,
        _5983,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConnectorCompoundHarmonicAnalysis")


class ConnectorCompoundHarmonicAnalysis(
    _5964.MountableComponentCompoundHarmonicAnalysis
):
    """ConnectorCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundHarmonicAnalysis")

    class _Cast_ConnectorCompoundHarmonicAnalysis:
        """Special nested class for casting ConnectorCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
            parent: "ConnectorCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_compound_harmonic_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_5895.BearingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5895,
            )

            return self._parent._cast(_5895.BearingCompoundHarmonicAnalysis)

        @property
        def oil_seal_compound_harmonic_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_5965.OilSealCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(_5965.OilSealCompoundHarmonicAnalysis)

        @property
        def shaft_hub_connection_compound_harmonic_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "_5983.ShaftHubConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5983,
            )

            return self._parent._cast(_5983.ShaftHubConnectionCompoundHarmonicAnalysis)

        @property
        def connector_compound_harmonic_analysis(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
        ) -> "ConnectorCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ConnectorCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_5724.ConnectorHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectorHarmonicAnalysis]

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
    ) -> "List[_5724.ConnectorHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectorHarmonicAnalysis]

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
    ) -> "ConnectorCompoundHarmonicAnalysis._Cast_ConnectorCompoundHarmonicAnalysis":
        return self._Cast_ConnectorCompoundHarmonicAnalysis(self)
