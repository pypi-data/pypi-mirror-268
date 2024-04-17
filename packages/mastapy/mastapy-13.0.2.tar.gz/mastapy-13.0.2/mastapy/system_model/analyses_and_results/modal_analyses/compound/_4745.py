"""BeltConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4801
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BeltConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2275
    from mastapy.system_model.analyses_and_results.modal_analyses import _4589
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4776,
        _4771,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BeltConnectionCompoundModalAnalysis")


class BeltConnectionCompoundModalAnalysis(
    _4801.InterMountableComponentConnectionCompoundModalAnalysis
):
    """BeltConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltConnectionCompoundModalAnalysis")

    class _Cast_BeltConnectionCompoundModalAnalysis:
        """Special nested class for casting BeltConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
            parent: "BeltConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
        ) -> "_4801.InterMountableComponentConnectionCompoundModalAnalysis":
            return self._parent._cast(
                _4801.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
        ) -> "_4776.CVTBeltConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4776,
            )

            return self._parent._cast(_4776.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def belt_connection_compound_modal_analysis(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
        ) -> "BeltConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "BeltConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2275.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2275.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

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
    ) -> "List[_4589.BeltConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BeltConnectionModalAnalysis]

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
    ) -> "List[_4589.BeltConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BeltConnectionModalAnalysis]

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
    ) -> (
        "BeltConnectionCompoundModalAnalysis._Cast_BeltConnectionCompoundModalAnalysis"
    ):
        return self._Cast_BeltConnectionCompoundModalAnalysis(self)
