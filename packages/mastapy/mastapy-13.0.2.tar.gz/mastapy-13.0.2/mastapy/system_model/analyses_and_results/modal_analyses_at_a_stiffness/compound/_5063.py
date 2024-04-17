"""KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5029,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4932,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5066,
        _5069,
        _5055,
        _5061,
        _5031,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
)


class KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness(
    _5029.ConicalGearMeshCompoundModalAnalysisAtAStiffness
):
    """KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
            parent: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5029.ConicalGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5029.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5055.GearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5055,
            )

            return self._parent._cast(_5055.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5061.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5031.ConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(_5031.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(
                _5066.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "_5069.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5069,
            )

            return self._parent._cast(
                _5069.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
        ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4932.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness]

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
    ) -> "List[_4932.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness]

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
    ) -> "KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness(
            self
        )
