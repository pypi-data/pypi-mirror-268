"""PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5294,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5207,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5332,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed")


class PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed(
    _5294.CouplingHalfCompoundModalAnalysisAtASpeed
):
    """PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
            parent: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5294.CouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5294.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
        ) -> "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

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
    ) -> "List[_5207.PartToPartShearCouplingHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PartToPartShearCouplingHalfModalAnalysisAtASpeed]

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
    ) -> "List[_5207.PartToPartShearCouplingHalfModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.PartToPartShearCouplingHalfModalAnalysisAtASpeed]

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
    ) -> "PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed":
        return self._Cast_PartToPartShearCouplingHalfCompoundModalAnalysisAtASpeed(self)
