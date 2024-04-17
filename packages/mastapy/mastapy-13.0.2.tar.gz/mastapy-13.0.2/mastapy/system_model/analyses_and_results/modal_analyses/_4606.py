"""ConceptCouplingConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4618
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConceptCouplingConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2351
    from mastapy.system_model.analyses_and_results.static_loads import _6847
    from mastapy.system_model.analyses_and_results.system_deflections import _2725
    from mastapy.system_model.analyses_and_results.modal_analyses import _4650, _4615
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionModalAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionModalAnalysis")


class ConceptCouplingConnectionModalAnalysis(_4618.CouplingConnectionModalAnalysis):
    """ConceptCouplingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionModalAnalysis"
    )

    class _Cast_ConceptCouplingConnectionModalAnalysis:
        """Special nested class for casting ConceptCouplingConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
            parent: "ConceptCouplingConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "_4618.CouplingConnectionModalAnalysis":
            return self._parent._cast(_4618.CouplingConnectionModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "_4650.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(
                _4650.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "_4615.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4615

            return self._parent._cast(_4615.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
        ) -> "ConceptCouplingConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingConnectionModalAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2725.ConceptCouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionModalAnalysis._Cast_ConceptCouplingConnectionModalAnalysis":
        return self._Cast_ConceptCouplingConnectionModalAnalysis(self)
