"""BevelGearSetHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5693
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelGearSetHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.system_deflections import _2715
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5700,
        _5822,
        _5829,
        _5832,
        _5851,
        _5722,
        _5766,
        _5818,
        _5686,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetHarmonicAnalysis")


class BevelGearSetHarmonicAnalysis(_5693.AGMAGleasonConicalGearSetHarmonicAnalysis):
    """BevelGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetHarmonicAnalysis")

    class _Cast_BevelGearSetHarmonicAnalysis:
        """Special nested class for casting BevelGearSetHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
            parent: "BevelGearSetHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5693.AGMAGleasonConicalGearSetHarmonicAnalysis":
            return self._parent._cast(_5693.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5722.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5722,
            )

            return self._parent._cast(_5722.ConicalGearSetHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5766.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5766,
            )

            return self._parent._cast(_5766.GearSetHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5818.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5686.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5686,
            )

            return self._parent._cast(_5686.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5700.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5822.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5822,
            )

            return self._parent._cast(_5822.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5829.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5832.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.StraightBevelGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "_5851.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5851,
            )

            return self._parent._cast(_5851.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
        ) -> "BevelGearSetHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2527.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2715.BevelGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection

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
    ) -> "BevelGearSetHarmonicAnalysis._Cast_BevelGearSetHarmonicAnalysis":
        return self._Cast_BevelGearSetHarmonicAnalysis(self)
