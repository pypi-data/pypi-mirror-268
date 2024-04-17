"""ConnectorCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6493
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConnectorCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6424,
        _6494,
        _6512,
        _6441,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConnectorCompoundDynamicAnalysis")


class ConnectorCompoundDynamicAnalysis(_6493.MountableComponentCompoundDynamicAnalysis):
    """ConnectorCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundDynamicAnalysis")

    class _Cast_ConnectorCompoundDynamicAnalysis:
        """Special nested class for casting ConnectorCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
            parent: "ConnectorCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_6493.MountableComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6493.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_6441.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_6424.BearingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BearingCompoundDynamicAnalysis)

        @property
        def oil_seal_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_6494.OilSealCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.OilSealCompoundDynamicAnalysis)

        @property
        def shaft_hub_connection_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "_6512.ShaftHubConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6512,
            )

            return self._parent._cast(_6512.ShaftHubConnectionCompoundDynamicAnalysis)

        @property
        def connector_compound_dynamic_analysis(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
        ) -> "ConnectorCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6321.ConnectorDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectorDynamicAnalysis]

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
    ) -> "List[_6321.ConnectorDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectorDynamicAnalysis]

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
    ) -> "ConnectorCompoundDynamicAnalysis._Cast_ConnectorCompoundDynamicAnalysis":
        return self._Cast_ConnectorCompoundDynamicAnalysis(self)
