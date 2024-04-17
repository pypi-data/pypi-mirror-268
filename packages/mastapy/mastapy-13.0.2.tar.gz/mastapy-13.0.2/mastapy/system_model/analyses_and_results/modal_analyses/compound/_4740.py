"""AGMAGleasonConicalGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4768
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4585
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4747,
        _4750,
        _4751,
        _4752,
        _4798,
        _4835,
        _4841,
        _4844,
        _4847,
        _4848,
        _4862,
        _4794,
        _4813,
        _4761,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundModalAnalysis")


class AGMAGleasonConicalGearCompoundModalAnalysis(
    _4768.ConicalGearCompoundModalAnalysis
):
    """AGMAGleasonConicalGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearCompoundModalAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearCompoundModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
            parent: "AGMAGleasonConicalGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4768.ConicalGearCompoundModalAnalysis":
            return self._parent._cast(_4768.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4794.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4747.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4747,
            )

            return self._parent._cast(_4747.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4750.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4750,
            )

            return self._parent._cast(
                _4750.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4751.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(
                _4751.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4752.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4752,
            )

            return self._parent._cast(_4752.BevelGearCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4798.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4798,
            )

            return self._parent._cast(_4798.HypoidGearCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4835.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.SpiralBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4841.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(_4841.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4844.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4847.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(
                _4847.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4848.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "_4862.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4862,
            )

            return self._parent._cast(_4862.ZerolBevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
        ) -> "AGMAGleasonConicalGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4585.AGMAGleasonConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis]

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
    ) -> "List[_4585.AGMAGleasonConicalGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearModalAnalysis]

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
    ) -> "AGMAGleasonConicalGearCompoundModalAnalysis._Cast_AGMAGleasonConicalGearCompoundModalAnalysis":
        return self._Cast_AGMAGleasonConicalGearCompoundModalAnalysis(self)
