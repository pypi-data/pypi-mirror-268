"""ConceptCouplingConnectionDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ConceptCouplingConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2351
    from mastapy.system_model.analyses_and_results.static_loads import _6847
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352, _6320
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionDynamicAnalysis")


class ConceptCouplingConnectionDynamicAnalysis(_6322.CouplingConnectionDynamicAnalysis):
    """ConceptCouplingConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionDynamicAnalysis"
    )

    class _Cast_ConceptCouplingConnectionDynamicAnalysis:
        """Special nested class for casting ConceptCouplingConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
            parent: "ConceptCouplingConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_dynamic_analysis(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_6322.CouplingConnectionDynamicAnalysis":
            return self._parent._cast(_6322.CouplingConnectionDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_6352.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_6320.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
        ) -> "ConceptCouplingConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingConnectionDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6847.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionDynamicAnalysis._Cast_ConceptCouplingConnectionDynamicAnalysis":
        return self._Cast_ConceptCouplingConnectionDynamicAnalysis(self)
