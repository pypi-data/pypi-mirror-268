"""HypoidGearSetHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5693
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "HypoidGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6916
    from mastapy.system_model.analyses_and_results.system_deflections import _2772
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5779,
        _5780,
        _5722,
        _5766,
        _5818,
        _5686,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="HypoidGearSetHarmonicAnalysis")


class HypoidGearSetHarmonicAnalysis(_5693.AGMAGleasonConicalGearSetHarmonicAnalysis):
    """HypoidGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetHarmonicAnalysis")

    class _Cast_HypoidGearSetHarmonicAnalysis:
        """Special nested class for casting HypoidGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
            parent: "HypoidGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_5693.AGMAGleasonConicalGearSetHarmonicAnalysis":
            return self._parent._cast(_5693.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_5722.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_5766.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5766,
            )

            return self._parent._cast(_5766.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_5818.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_5686.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
        ) -> "HypoidGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6916.HypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2772.HypoidGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_harmonic_analysis(self: Self) -> "List[_5779.HypoidGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_harmonic_analysis(
        self: Self,
    ) -> "List[_5779.HypoidGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5780.HypoidGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_harmonic_analysis(
        self: Self,
    ) -> "List[_5780.HypoidGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesHarmonicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetHarmonicAnalysis._Cast_HypoidGearSetHarmonicAnalysis":
        return self._Cast_HypoidGearSetHarmonicAnalysis(self)
