"""AGMAGleasonConicalGearModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5158
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "AGMAGleasonConicalGearModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5137,
        _5139,
        _5140,
        _5142,
        _5188,
        _5226,
        _5232,
        _5235,
        _5237,
        _5238,
        _5253,
        _5184,
        _5203,
        _5150,
        _5205,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearModalAnalysisAtASpeed")


class AGMAGleasonConicalGearModalAnalysisAtASpeed(
    _5158.ConicalGearModalAnalysisAtASpeed
):
    """AGMAGleasonConicalGearModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed"
    )

    class _Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed:
        """Special nested class for casting AGMAGleasonConicalGearModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
            parent: "AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def conical_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5158.ConicalGearModalAnalysisAtASpeed":
            return self._parent._cast(_5158.ConicalGearModalAnalysisAtASpeed)

        @property
        def gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5184.GearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5184,
            )

            return self._parent._cast(_5184.GearModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5203.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5203,
            )

            return self._parent._cast(_5203.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5150.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5150,
            )

            return self._parent._cast(_5150.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5205.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5205,
            )

            return self._parent._cast(_5205.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5137.BevelDifferentialGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5137,
            )

            return self._parent._cast(_5137.BevelDifferentialGearModalAnalysisAtASpeed)

        @property
        def bevel_differential_planet_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5139.BevelDifferentialPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5139,
            )

            return self._parent._cast(
                _5139.BevelDifferentialPlanetGearModalAnalysisAtASpeed
            )

        @property
        def bevel_differential_sun_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5140.BevelDifferentialSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5140,
            )

            return self._parent._cast(
                _5140.BevelDifferentialSunGearModalAnalysisAtASpeed
            )

        @property
        def bevel_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5142.BevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5142,
            )

            return self._parent._cast(_5142.BevelGearModalAnalysisAtASpeed)

        @property
        def hypoid_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5188.HypoidGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5188,
            )

            return self._parent._cast(_5188.HypoidGearModalAnalysisAtASpeed)

        @property
        def spiral_bevel_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5226.SpiralBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5226,
            )

            return self._parent._cast(_5226.SpiralBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_diff_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5232.StraightBevelDiffGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5232,
            )

            return self._parent._cast(_5232.StraightBevelDiffGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5235.StraightBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5235,
            )

            return self._parent._cast(_5235.StraightBevelGearModalAnalysisAtASpeed)

        @property
        def straight_bevel_planet_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5237.StraightBevelPlanetGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5237,
            )

            return self._parent._cast(
                _5237.StraightBevelPlanetGearModalAnalysisAtASpeed
            )

        @property
        def straight_bevel_sun_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5238.StraightBevelSunGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5238,
            )

            return self._parent._cast(_5238.StraightBevelSunGearModalAnalysisAtASpeed)

        @property
        def zerol_bevel_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "_5253.ZerolBevelGearModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5253,
            )

            return self._parent._cast(_5253.ZerolBevelGearModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_modal_analysis_at_a_speed(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
        ) -> "AGMAGleasonConicalGearModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2520.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

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
    ) -> "AGMAGleasonConicalGearModalAnalysisAtASpeed._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed":
        return self._Cast_AGMAGleasonConicalGearModalAnalysisAtASpeed(self)
