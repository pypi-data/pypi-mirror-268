"""CVTHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5697
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CVTHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.system_deflections import _2742
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5818,
        _5686,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("CVTHarmonicAnalysis",)


Self = TypeVar("Self", bound="CVTHarmonicAnalysis")


class CVTHarmonicAnalysis(_5697.BeltDriveHarmonicAnalysis):
    """CVTHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTHarmonicAnalysis")

    class _Cast_CVTHarmonicAnalysis:
        """Special nested class for casting CVTHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
            parent: "CVTHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_5697.BeltDriveHarmonicAnalysis":
            return self._parent._cast(_5697.BeltDriveHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_5818.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_5686.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis",
        ) -> "CVTHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2742.CVTSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTHarmonicAnalysis._Cast_CVTHarmonicAnalysis":
        return self._Cast_CVTHarmonicAnalysis(self)
