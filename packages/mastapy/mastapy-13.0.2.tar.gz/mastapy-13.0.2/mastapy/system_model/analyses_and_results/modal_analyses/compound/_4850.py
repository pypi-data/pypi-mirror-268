"""SynchroniserHalfCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4851
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "SynchroniserHalfCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.modal_analyses import _4705
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4775,
        _4813,
        _4761,
        _4815,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundModalAnalysis")


class SynchroniserHalfCompoundModalAnalysis(
    _4851.SynchroniserPartCompoundModalAnalysis
):
    """SynchroniserHalfCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundModalAnalysis"
    )

    class _Cast_SynchroniserHalfCompoundModalAnalysis:
        """Special nested class for casting SynchroniserHalfCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
            parent: "SynchroniserHalfCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "_4851.SynchroniserPartCompoundModalAnalysis":
            return self._parent._cast(_4851.SynchroniserPartCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "_4775.CouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4775,
            )

            return self._parent._cast(_4775.CouplingHalfCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "_4813.MountableComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4813,
            )

            return self._parent._cast(_4813.MountableComponentCompoundModalAnalysis)

        @property
        def component_compound_modal_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "_4761.ComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4761,
            )

            return self._parent._cast(_4761.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "_4815.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
        ) -> "SynchroniserHalfCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserHalfCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_4705.SynchroniserHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserHalfModalAnalysis]

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
    ) -> "List[_4705.SynchroniserHalfModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.SynchroniserHalfModalAnalysis]

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
    ) -> "SynchroniserHalfCompoundModalAnalysis._Cast_SynchroniserHalfCompoundModalAnalysis":
        return self._Cast_SynchroniserHalfCompoundModalAnalysis(self)
