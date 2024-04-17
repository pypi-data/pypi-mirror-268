"""OilSealCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5291,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "OilSealCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2473
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5204,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5332,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("OilSealCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="OilSealCompoundModalAnalysisAtASpeed")


class OilSealCompoundModalAnalysisAtASpeed(
    _5291.ConnectorCompoundModalAnalysisAtASpeed
):
    """OilSealCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealCompoundModalAnalysisAtASpeed")

    class _Cast_OilSealCompoundModalAnalysisAtASpeed:
        """Special nested class for casting OilSealCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
            parent: "OilSealCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def connector_compound_modal_analysis_at_a_speed(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
        ) -> "_5291.ConnectorCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5291.ConnectorCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def oil_seal_compound_modal_analysis_at_a_speed(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
        ) -> "OilSealCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "OilSealCompoundModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2473.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5204.OilSealModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.OilSealModalAnalysisAtASpeed]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5204.OilSealModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.OilSealModalAnalysisAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "OilSealCompoundModalAnalysisAtASpeed._Cast_OilSealCompoundModalAnalysisAtASpeed":
        return self._Cast_OilSealCompoundModalAnalysisAtASpeed(self)
