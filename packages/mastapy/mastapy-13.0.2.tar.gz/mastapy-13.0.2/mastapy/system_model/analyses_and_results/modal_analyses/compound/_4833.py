"""ShaftToMountableComponentConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4739
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ShaftToMountableComponentConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4689
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4760,
        _4780,
        _4819,
        _4771,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionCompoundModalAnalysis")


class ShaftToMountableComponentConnectionCompoundModalAnalysis(
    _4739.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
):
    """ShaftToMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4739.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis":
            return self._parent._cast(
                _4739.AbstractShaftToMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4760.CoaxialConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4760,
            )

            return self._parent._cast(_4760.CoaxialConnectionCompoundModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4780.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(
                _4780.CycloidalDiscCentralBearingConnectionCompoundModalAnalysis
            )

        @property
        def planetary_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "_4819.PlanetaryConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.PlanetaryConnectionCompoundModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_compound_modal_analysis(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4689.ShaftToMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4689.ShaftToMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ShaftToMountableComponentConnectionModalAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundModalAnalysis._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCompoundModalAnalysis(self)
