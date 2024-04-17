"""PointLoadCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6009
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PointLoadCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2478
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5804
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5964,
        _5912,
        _5966,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="PointLoadCompoundHarmonicAnalysis")


class PointLoadCompoundHarmonicAnalysis(_6009.VirtualComponentCompoundHarmonicAnalysis):
    """PointLoadCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadCompoundHarmonicAnalysis")

    class _Cast_PointLoadCompoundHarmonicAnalysis:
        """Special nested class for casting PointLoadCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
            parent: "PointLoadCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_harmonic_analysis(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
        ) -> "_6009.VirtualComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_6009.VirtualComponentCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
        ) -> "_5964.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5964,
            )

            return self._parent._cast(_5964.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
        ) -> "_5912.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5912,
            )

            return self._parent._cast(_5912.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
        ) -> "_5966.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5966,
            )

            return self._parent._cast(_5966.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def point_load_compound_harmonic_analysis(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
        ) -> "PointLoadCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "PointLoadCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2478.PointLoad":
        """mastapy.system_model.part_model.PointLoad

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
    ) -> "List[_5804.PointLoadHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PointLoadHarmonicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_5804.PointLoadHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PointLoadHarmonicAnalysis]

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
    ) -> "PointLoadCompoundHarmonicAnalysis._Cast_PointLoadCompoundHarmonicAnalysis":
        return self._Cast_PointLoadCompoundHarmonicAnalysis(self)
