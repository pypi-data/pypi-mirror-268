"""ConceptCouplingHalfCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6455
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConceptCouplingHalfCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6493,
        _6441,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingHalfCompoundDynamicAnalysis")


class ConceptCouplingHalfCompoundDynamicAnalysis(
    _6455.CouplingHalfCompoundDynamicAnalysis
):
    """ConceptCouplingHalfCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfCompoundDynamicAnalysis"
    )

    class _Cast_ConceptCouplingHalfCompoundDynamicAnalysis:
        """Special nested class for casting ConceptCouplingHalfCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
            parent: "ConceptCouplingHalfCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
        ) -> "_6455.CouplingHalfCompoundDynamicAnalysis":
            return self._parent._cast(_6455.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
        ) -> "_6493.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
        ) -> "_6441.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_dynamic_analysis(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
        ) -> "ConceptCouplingHalfCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingHalfCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2589.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

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
    ) -> "List[_6313.ConceptCouplingHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingHalfDynamicAnalysis]

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
    ) -> "List[_6313.ConceptCouplingHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConceptCouplingHalfDynamicAnalysis]

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
    ) -> "ConceptCouplingHalfCompoundDynamicAnalysis._Cast_ConceptCouplingHalfCompoundDynamicAnalysis":
        return self._Cast_ConceptCouplingHalfCompoundDynamicAnalysis(self)
