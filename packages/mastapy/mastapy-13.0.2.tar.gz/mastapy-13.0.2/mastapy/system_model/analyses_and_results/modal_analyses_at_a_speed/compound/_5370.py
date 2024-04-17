"""SynchroniserPartCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5294,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "SynchroniserPartCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5241,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5369,
        _5371,
        _5332,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundModalAnalysisAtASpeed")


class SynchroniserPartCompoundModalAnalysisAtASpeed(
    _5294.CouplingHalfCompoundModalAnalysisAtASpeed
):
    """SynchroniserPartCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundModalAnalysisAtASpeed"
    )

    class _Cast_SynchroniserPartCompoundModalAnalysisAtASpeed:
        """Special nested class for casting SynchroniserPartCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
            parent: "SynchroniserPartCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_5294.CouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5294.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis_at_a_speed(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_5369.SynchroniserHalfCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5369,
            )

            return self._parent._cast(
                _5369.SynchroniserHalfCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_speed(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "_5371.SynchroniserSleeveCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5371,
            )

            return self._parent._cast(
                _5371.SynchroniserSleeveCompoundModalAnalysisAtASpeed
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_speed(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
        ) -> "SynchroniserPartCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "SynchroniserPartCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5241.SynchroniserPartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SynchroniserPartModalAnalysisAtASpeed]

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
    ) -> "List[_5241.SynchroniserPartModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.SynchroniserPartModalAnalysisAtASpeed]

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
    ) -> "SynchroniserPartCompoundModalAnalysisAtASpeed._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed":
        return self._Cast_SynchroniserPartCompoundModalAnalysisAtASpeed(self)
