"""StraightBevelGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4752
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "StraightBevelGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.modal_analyses import _4701
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
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
__all__ = ("StraightBevelGearCompoundModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearCompoundModalAnalysis")


class StraightBevelGearCompoundModalAnalysis(_4752.BevelGearCompoundModalAnalysis):
    """StraightBevelGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearCompoundModalAnalysis"
    )

    class _Cast_StraightBevelGearCompoundModalAnalysis:
        """Special nested class for casting StraightBevelGearCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
            parent: "StraightBevelGearCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_modal_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_4752.BevelGearCompoundModalAnalysis":
            return self._parent._cast(_4752.BevelGearCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_4740.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4740,
            )

            return self._parent._cast(_4740.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_4768.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4768,
            )

            return self._parent._cast(_4768.ConicalGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_4794.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(_4794.GearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
        ) -> "StraightBevelGearCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

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
    ) -> "List[_4701.StraightBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearModalAnalysis]

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
    ) -> "List[_4701.StraightBevelGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelGearModalAnalysis]

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
    ) -> "StraightBevelGearCompoundModalAnalysis._Cast_StraightBevelGearCompoundModalAnalysis":
        return self._Cast_StraightBevelGearCompoundModalAnalysis(self)
