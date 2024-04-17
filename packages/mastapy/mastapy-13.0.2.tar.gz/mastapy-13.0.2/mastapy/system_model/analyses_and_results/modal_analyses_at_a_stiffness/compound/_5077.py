"""PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5034,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2355
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4947,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5061,
        _5031,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness"
)


class PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness(
    _5034.CouplingConnectionCompoundModalAnalysisAtAStiffness
):
    """PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = (
        _PART_TO_PART_SHEAR_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
            parent: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5034.CouplingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5034.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5061.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_5031.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(_5031.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2355.PartToPartShearCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection

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
    ) -> "List[_4947.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4947.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PartToPartShearCouplingConnectionModalAnalysisAtAStiffness]

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
    ) -> "PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
