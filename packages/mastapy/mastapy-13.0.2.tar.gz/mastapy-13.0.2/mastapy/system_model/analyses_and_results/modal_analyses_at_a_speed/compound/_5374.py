"""TorqueConverterPumpCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5294,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "TorqueConverterPumpCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5245,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5332,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterPumpCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="TorqueConverterPumpCompoundModalAnalysisAtASpeed")


class TorqueConverterPumpCompoundModalAnalysisAtASpeed(
    _5294.CouplingHalfCompoundModalAnalysisAtASpeed
):
    """TorqueConverterPumpCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed"
    )

    class _Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed:
        """Special nested class for casting TorqueConverterPumpCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
            parent: "TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ) -> "_5294.CouplingHalfCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5294.CouplingHalfCompoundModalAnalysisAtASpeed)

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5332,
            )

            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_speed(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
        ) -> "TorqueConverterPumpCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "TorqueConverterPumpCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2616.TorqueConverterPump":
        """mastapy.system_model.part_model.couplings.TorqueConverterPump

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
    ) -> "List[_5245.TorqueConverterPumpModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.TorqueConverterPumpModalAnalysisAtASpeed]

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
    ) -> "List[_5245.TorqueConverterPumpModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.TorqueConverterPumpModalAnalysisAtASpeed]

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
    ) -> "TorqueConverterPumpCompoundModalAnalysisAtASpeed._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed":
        return self._Cast_TorqueConverterPumpCompoundModalAnalysisAtASpeed(self)
