"""StraightBevelDiffGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "StraightBevelDiffGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2552
    from mastapy.system_model.analyses_and_results.modal_analyses import _4698
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4847,
        _4848,
        _4740,
        _4768,
        _4794,
        _4813,
        _4761,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundModalAnalysis")


class StraightBevelDiffGearCompoundModalAnalysis(_4752.BevelGearCompoundModalAnalysis):
    """StraightBevelDiffGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearCompoundModalAnalysis"
    )

    class _Cast_StraightBevelDiffGearCompoundModalAnalysis:
        """Special nested class for casting StraightBevelDiffGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
            parent: "StraightBevelDiffGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4752.BevelGearCompoundModalAnalysis":
            return self._parent._cast(_4752.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4740.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4768.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4794.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4847.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4847,
            )

            return self._parent._cast(
                _4847.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "_4848.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
        ) -> "StraightBevelDiffGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2552.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

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
    ) -> "List[_4698.StraightBevelDiffGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis]

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
    ) -> "List[_4698.StraightBevelDiffGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis]

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
    ) -> "StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis":
        return self._Cast_StraightBevelDiffGearCompoundModalAnalysis(self)
