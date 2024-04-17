"""VirtualComponentCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5332,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "VirtualComponentCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5248,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5330,
        _5331,
        _5341,
        _5342,
        _5376,
        _5280,
        _5334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="VirtualComponentCompoundModalAnalysisAtASpeed")


class VirtualComponentCompoundModalAnalysisAtASpeed(
    _5332.MountableComponentCompoundModalAnalysisAtASpeed
):
    """VirtualComponentCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundModalAnalysisAtASpeed"
    )

    class _Cast_VirtualComponentCompoundModalAnalysisAtASpeed:
        """Special nested class for casting VirtualComponentCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
            parent: "VirtualComponentCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5332.MountableComponentCompoundModalAnalysisAtASpeed":
            return self._parent._cast(
                _5332.MountableComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def component_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5280.ComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5280,
            )

            return self._parent._cast(_5280.ComponentCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5334.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5334,
            )

            return self._parent._cast(_5334.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def mass_disc_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5330.MassDiscCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.MassDiscCompoundModalAnalysisAtASpeed)

        @property
        def measurement_component_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5331.MeasurementComponentCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5331,
            )

            return self._parent._cast(
                _5331.MeasurementComponentCompoundModalAnalysisAtASpeed
            )

        @property
        def point_load_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5341.PointLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5341,
            )

            return self._parent._cast(_5341.PointLoadCompoundModalAnalysisAtASpeed)

        @property
        def power_load_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5342.PowerLoadCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5342,
            )

            return self._parent._cast(_5342.PowerLoadCompoundModalAnalysisAtASpeed)

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "_5376.UnbalancedMassCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5376,
            )

            return self._parent._cast(_5376.UnbalancedMassCompoundModalAnalysisAtASpeed)

        @property
        def virtual_component_compound_modal_analysis_at_a_speed(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
        ) -> "VirtualComponentCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "VirtualComponentCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5248.VirtualComponentModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.VirtualComponentModalAnalysisAtASpeed]

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
    ) -> "List[_5248.VirtualComponentModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.VirtualComponentModalAnalysisAtASpeed]

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
    ) -> "VirtualComponentCompoundModalAnalysisAtASpeed._Cast_VirtualComponentCompoundModalAnalysisAtASpeed":
        return self._Cast_VirtualComponentCompoundModalAnalysisAtASpeed(self)
