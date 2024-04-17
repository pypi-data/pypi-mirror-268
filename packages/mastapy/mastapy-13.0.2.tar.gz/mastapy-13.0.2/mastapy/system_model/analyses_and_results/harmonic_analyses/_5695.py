"""BearingHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5724
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BearingHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.system_model.analyses_and_results.static_loads import _6828
    from mastapy.bearings.bearing_results.rolling import _2078
    from mastapy.system_model.analyses_and_results.system_deflections import _2706
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5794,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BearingHarmonicAnalysis",)


Self = TypeVar("Self", bound="BearingHarmonicAnalysis")


class BearingHarmonicAnalysis(_5724.ConnectorHarmonicAnalysis):
    """BearingHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEARING_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingHarmonicAnalysis")

    class _Cast_BearingHarmonicAnalysis:
        """Special nested class for casting BearingHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
            parent: "BearingHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connector_harmonic_analysis(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_5724.ConnectorHarmonicAnalysis":
            return self._parent._cast(_5724.ConnectorHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis",
        ) -> "BearingHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2446.Bearing":
        """mastapy.system_model.part_model.Bearing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6828.BearingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rolling_bearing_speed_results(self: Self) -> "_2078.RollingBearingSpeedResults":
        """mastapy.bearings.bearing_results.rolling.RollingBearingSpeedResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingBearingSpeedResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2706.BearingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[BearingHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BearingHarmonicAnalysis]

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
    def cast_to(self: Self) -> "BearingHarmonicAnalysis._Cast_BearingHarmonicAnalysis":
        return self._Cast_BearingHarmonicAnalysis(self)
