"""CouplingConnectionCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5320,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CouplingConnectionCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5162,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5277,
        _5282,
        _5336,
        _5358,
        _5373,
        _5290,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CouplingConnectionCompoundModalAnalysisAtASpeed")


class CouplingConnectionCompoundModalAnalysisAtASpeed(
    _5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
):
    """CouplingConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CouplingConnectionCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CouplingConnectionCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
            parent: "CouplingConnectionCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5320.InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5290.ConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5290,
            )

            return self._parent._cast(_5290.ConnectionCompoundModalAnalysisAtASpeed)

        @property
        def connection_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5277.ClutchConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5277,
            )

            return self._parent._cast(
                _5277.ClutchConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5282.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5282,
            )

            return self._parent._cast(
                _5282.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5336.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5336,
            )

            return self._parent._cast(
                _5336.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5358.SpringDamperConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5358,
            )

            return self._parent._cast(
                _5358.SpringDamperConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "_5373.TorqueConverterConnectionCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5373,
            )

            return self._parent._cast(
                _5373.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_speed(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
        ) -> "CouplingConnectionCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "CouplingConnectionCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5162.CouplingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5162.CouplingConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CouplingConnectionModalAnalysisAtASpeed]

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
    ) -> "CouplingConnectionCompoundModalAnalysisAtASpeed._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed":
        return self._Cast_CouplingConnectionCompoundModalAnalysisAtASpeed(self)
