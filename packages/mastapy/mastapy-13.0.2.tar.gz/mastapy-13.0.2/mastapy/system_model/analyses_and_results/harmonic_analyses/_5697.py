"""BeltDriveHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BeltDriveHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.static_loads import _6830
    from mastapy.system_model.analyses_and_results.system_deflections import _2708
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5729,
        _5686,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveHarmonicAnalysis",)


Self = TypeVar("Self", bound="BeltDriveHarmonicAnalysis")


class BeltDriveHarmonicAnalysis(_5818.SpecialisedAssemblyHarmonicAnalysis):
    """BeltDriveHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveHarmonicAnalysis")

    class _Cast_BeltDriveHarmonicAnalysis:
        """Special nested class for casting BeltDriveHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
            parent: "BeltDriveHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_5818.SpecialisedAssemblyHarmonicAnalysis":
            return self._parent._cast(_5818.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_5686.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "_5729.CVTHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.CVTHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis",
        ) -> "BeltDriveHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6830.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2708.BeltDriveSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection

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
    ) -> "BeltDriveHarmonicAnalysis._Cast_BeltDriveHarmonicAnalysis":
        return self._Cast_BeltDriveHarmonicAnalysis(self)
