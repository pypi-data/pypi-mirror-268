"""ShaftCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6417
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ShaftCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6418,
        _6441,
        _6495,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ShaftCompoundDynamicAnalysis")


class ShaftCompoundDynamicAnalysis(_6417.AbstractShaftCompoundDynamicAnalysis):
    """ShaftCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftCompoundDynamicAnalysis")

    class _Cast_ShaftCompoundDynamicAnalysis:
        """Special nested class for casting ShaftCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
            parent: "ShaftCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_dynamic_analysis(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
        ) -> "_6417.AbstractShaftCompoundDynamicAnalysis":
            return self._parent._cast(_6417.AbstractShaftCompoundDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_compound_dynamic_analysis(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
        ) -> "_6418.AbstractShaftOrHousingCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6418,
            )

            return self._parent._cast(
                _6418.AbstractShaftOrHousingCompoundDynamicAnalysis
            )

        @property
        def component_compound_dynamic_analysis(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
        ) -> "_6441.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
        ) -> "_6495.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def shaft_compound_dynamic_analysis(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
        ) -> "ShaftCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftCompoundDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

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
    ) -> "List[_6382.ShaftDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftDynamicAnalysis]

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
    def planetaries(self: Self) -> "List[ShaftCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ShaftCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_6382.ShaftDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ShaftDynamicAnalysis]

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
    ) -> "ShaftCompoundDynamicAnalysis._Cast_ShaftCompoundDynamicAnalysis":
        return self._Cast_ShaftCompoundDynamicAnalysis(self)
