"""ConnectorModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4666
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConnectorModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.system_deflections import _2736
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4588,
        _4668,
        _4686,
        _4605,
        _4670,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorModalAnalysis",)


Self = TypeVar("Self", bound="ConnectorModalAnalysis")


class ConnectorModalAnalysis(_4666.MountableComponentModalAnalysis):
    """ConnectorModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorModalAnalysis")

    class _Cast_ConnectorModalAnalysis:
        """Special nested class for casting ConnectorModalAnalysis to subclasses."""

        def __init__(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
            parent: "ConnectorModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_4666.MountableComponentModalAnalysis":
            return self._parent._cast(_4666.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_4605.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_4670.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_4588.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BearingModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_4668.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.OilSealModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "_4686.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.ShaftHubConnectionModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "ConnectorModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2736.ConnectorSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis":
        return self._Cast_ConnectorModalAnalysis(self)
