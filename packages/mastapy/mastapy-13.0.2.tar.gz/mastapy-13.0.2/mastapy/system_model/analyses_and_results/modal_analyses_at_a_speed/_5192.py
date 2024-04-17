"""KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5158
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5195,
        _5198,
        _5184,
        _5203,
        _5150,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed")


class KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed(
    _5158.ConicalGearModalAnalysisAtASpeed
):
    """KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
            parent: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_5158.ConicalGearModalAnalysisAtASpeed":
            return self._parent._cast(_5158.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_5184.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(_5184.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_5203.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_5150.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_5195.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5195,
            )

            return self._parent._cast(
                _5195.KlingelnbergCycloPalloidHypoidGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "_5198.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5198,
            )

            return self._parent._cast(
                _5198.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysisAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis_at_a_speed(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
        ) -> "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidConicalGearModalAnalysisAtASpeed(self)
