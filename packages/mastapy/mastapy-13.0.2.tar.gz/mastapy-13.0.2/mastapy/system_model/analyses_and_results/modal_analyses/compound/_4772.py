"""ConnectorCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ConnectorCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4616
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4744,
        _4814,
        _4832,
        _4761,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ConnectorCompoundModalAnalysis")


class ConnectorCompoundModalAnalysis(_4813.MountableComponentCompoundModalAnalysis):
    """ConnectorCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorCompoundModalAnalysis")

    class _Cast_ConnectorCompoundModalAnalysis:
        """Special nested class for casting ConnectorCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
            parent: "ConnectorCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_4744.BearingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(_4744.BearingCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_4814.OilSealCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(_4814.OilSealCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "_4832.ShaftHubConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4832,
            )

            return self._parent._cast(_4832.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
        ) -> "ConnectorCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_4616.ConnectorModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConnectorModalAnalysis]

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
    ) -> "List[_4616.ConnectorModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConnectorModalAnalysis]

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
    ) -> "ConnectorCompoundModalAnalysis._Cast_ConnectorCompoundModalAnalysis":
        return self._Cast_ConnectorCompoundModalAnalysis(self)
