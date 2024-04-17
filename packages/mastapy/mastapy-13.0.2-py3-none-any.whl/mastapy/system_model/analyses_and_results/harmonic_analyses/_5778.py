"""HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6813
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_WITH_VARYING_STIFFNESS_STATIC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5774
    from mastapy.system_model.analyses_and_results.static_loads import _6812
    from mastapy.system_model.analyses_and_results import _2658


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",)


Self = TypeVar("Self", bound="HarmonicAnalysisWithVaryingStiffnessStaticLoadCase")


class HarmonicAnalysisWithVaryingStiffnessStaticLoadCase(_6813.StaticLoadCase):
    """HarmonicAnalysisWithVaryingStiffnessStaticLoadCase

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_WITH_VARYING_STIFFNESS_STATIC_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase"
    )

    class _Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase:
        """Special nested class for casting HarmonicAnalysisWithVaryingStiffnessStaticLoadCase to subclasses."""

        def __init__(
            self: "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase._Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
            parent: "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
        ):
            self._parent = parent

        @property
        def static_load_case(
            self: "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase._Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
        ) -> "_6813.StaticLoadCase":
            return self._parent._cast(_6813.StaticLoadCase)

        @property
        def load_case(
            self: "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase._Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
        ) -> "_6812.LoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(_6812.LoadCase)

        @property
        def context(
            self: "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase._Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
        ) -> "_2658.Context":
            from mastapy.system_model.analyses_and_results import _2658

            return self._parent._cast(_2658.Context)

        @property
        def harmonic_analysis_with_varying_stiffness_static_load_case(
            self: "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase._Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
        ) -> "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase._Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase",
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
        self: Self,
        instance_to_wrap: "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_analysis_options(self: Self) -> "_5774.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisWithVaryingStiffnessStaticLoadCase._Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase":
        return self._Cast_HarmonicAnalysisWithVaryingStiffnessStaticLoadCase(self)
