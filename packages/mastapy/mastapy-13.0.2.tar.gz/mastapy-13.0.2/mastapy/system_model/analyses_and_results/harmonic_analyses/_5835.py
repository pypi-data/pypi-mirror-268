"""SynchroniserHalfHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "SynchroniserHalfHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.static_loads import _6976
    from mastapy.system_model.analyses_and_results.system_deflections import _2829
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5726,
        _5794,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfHarmonicAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfHarmonicAnalysis")


class SynchroniserHalfHarmonicAnalysis(_5837.SynchroniserPartHarmonicAnalysis):
    """SynchroniserHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalfHarmonicAnalysis")

    class _Cast_SynchroniserHalfHarmonicAnalysis:
        """Special nested class for casting SynchroniserHalfHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
            parent: "SynchroniserHalfHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_harmonic_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_5837.SynchroniserPartHarmonicAnalysis":
            return self._parent._cast(_5837.SynchroniserPartHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_5726.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5726,
            )

            return self._parent._cast(_5726.CouplingHalfHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
        ) -> "SynchroniserHalfHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserHalfHarmonicAnalysis.TYPE"):
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
    def component_load_case(self: Self) -> "_6976.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2829.SynchroniserHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfHarmonicAnalysis._Cast_SynchroniserHalfHarmonicAnalysis":
        return self._Cast_SynchroniserHalfHarmonicAnalysis(self)
