"""CoaxialConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4833
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "CoaxialConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2276
    from mastapy.system_model.analyses_and_results.modal_analyses import _4604
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4780,
        _4739,
        _4771,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundModalAnalysis")


class CoaxialConnectionCompoundModalAnalysis(
    _4833.ShaftToMountableComponentConnectionCompoundModalAnalysis
):
    """CoaxialConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundModalAnalysis"
    )

    class _Cast_CoaxialConnectionCompoundModalAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
            parent: "CoaxialConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
        ) -> "_4833.ShaftToMountableComponentConnectionCompoundModalAnalysis":
            return self._parent._cast(
                _4833.ShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
        ) -> "_4739.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4739,
            )

            return self._parent._cast(
                _4739.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
        ) -> "_4780.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(
                _4780.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
            )

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
        ) -> "CoaxialConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "CoaxialConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2276.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "List[_4604.CoaxialConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CoaxialConnectionModalAnalysis]

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
    ) -> "List[_4604.CoaxialConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.CoaxialConnectionModalAnalysis]

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
    ) -> "CoaxialConnectionCompoundModalAnalysis._Cast_CoaxialConnectionCompoundModalAnalysis":
        return self._Cast_CoaxialConnectionCompoundModalAnalysis(self)
