"""SynchroniserSleeveCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6531
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "SynchroniserSleeveCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2614
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6455,
        _6493,
        _6441,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundDynamicAnalysis")


class SynchroniserSleeveCompoundDynamicAnalysis(
    _6531.SynchroniserPartCompoundDynamicAnalysis
):
    """SynchroniserSleeveCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundDynamicAnalysis"
    )

    class _Cast_SynchroniserSleeveCompoundDynamicAnalysis:
        """Special nested class for casting SynchroniserSleeveCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
            parent: "SynchroniserSleeveCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_dynamic_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "_6531.SynchroniserPartCompoundDynamicAnalysis":
            return self._parent._cast(_6531.SynchroniserPartCompoundDynamicAnalysis)

        @property
        def coupling_half_compound_dynamic_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "_6455.CouplingHalfCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6455,
            )

            return self._parent._cast(_6455.CouplingHalfCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "_6493.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "_6441.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_dynamic_analysis(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
        ) -> "SynchroniserSleeveCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2614.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_6403.SynchroniserSleeveDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserSleeveDynamicAnalysis]

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
    ) -> "List[_6403.SynchroniserSleeveDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.SynchroniserSleeveDynamicAnalysis]

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
    ) -> "SynchroniserSleeveCompoundDynamicAnalysis._Cast_SynchroniserSleeveCompoundDynamicAnalysis":
        return self._Cast_SynchroniserSleeveCompoundDynamicAnalysis(self)
