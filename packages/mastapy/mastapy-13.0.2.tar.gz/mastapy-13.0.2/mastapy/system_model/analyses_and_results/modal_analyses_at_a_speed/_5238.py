"""StraightBevelSunGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "StraightBevelSunGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2557
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5142,
        _5130,
        _5158,
        _5184,
        _5203,
        _5150,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelSunGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="StraightBevelSunGearModalAnalysisAtASpeed")


class StraightBevelSunGearModalAnalysisAtASpeed(
    _5232.StraightBevelDiffGearModalAnalysisAtASpeed
):
    """StraightBevelSunGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearModalAnalysisAtASpeed"
    )

    class _Cast_StraightBevelSunGearModalAnalysisAtASpeed:
        """Special nested class for casting StraightBevelSunGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
            parent: "StraightBevelSunGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5232.StraightBevelDiffGearModalAnalysisAtASpeed":
            return self._parent._cast(_5232.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5142.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.BevelGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5130.AGMAGleasonConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5130,
            )

            return self._parent._cast(_5130.AGMAGleasonConicalGearModalAnalysisAtASpeed)

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5158.ConicalGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5158,
            )

            return self._parent._cast(_5158.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5184.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(_5184.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5203.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5150.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
        ) -> "StraightBevelSunGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "StraightBevelSunGearModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2557.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

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
    ) -> "StraightBevelSunGearModalAnalysisAtASpeed._Cast_StraightBevelSunGearModalAnalysisAtASpeed":
        return self._Cast_StraightBevelSunGearModalAnalysisAtASpeed(self)
