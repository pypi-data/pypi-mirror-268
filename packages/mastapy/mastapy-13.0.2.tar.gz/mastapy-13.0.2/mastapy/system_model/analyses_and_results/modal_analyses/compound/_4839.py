"""SpringDamperConnectionCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4774
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SpringDamperConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2357
    from mastapy.system_model.analyses_and_results.modal_analyses import _4694
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4801,
        _4771,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionCompoundModalAnalysis")


class SpringDamperConnectionCompoundModalAnalysis(
    _4774.CouplingConnectionCompoundModalAnalysis
):
    """SpringDamperConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpringDamperConnectionCompoundModalAnalysis"
    )

    class _Cast_SpringDamperConnectionCompoundModalAnalysis:
        """Special nested class for casting SpringDamperConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
            parent: "SpringDamperConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
        ) -> "_4774.CouplingConnectionCompoundModalAnalysis":
            return self._parent._cast(_4774.CouplingConnectionCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
        ) -> "_4801.InterMountableComponentConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4801,
            )

            return self._parent._cast(
                _4801.InterMountableComponentConnectionCompoundModalAnalysis
            )

        @property
        def connection_compound_modal_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
        ) -> "_4771.ConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4771,
            )

            return self._parent._cast(_4771.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
        ) -> "SpringDamperConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2357.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2357.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

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
    ) -> "List[_4694.SpringDamperConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperConnectionModalAnalysis]

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
    ) -> "List[_4694.SpringDamperConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SpringDamperConnectionModalAnalysis]

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
    ) -> "SpringDamperConnectionCompoundModalAnalysis._Cast_SpringDamperConnectionCompoundModalAnalysis":
        return self._Cast_SpringDamperConnectionCompoundModalAnalysis(self)
