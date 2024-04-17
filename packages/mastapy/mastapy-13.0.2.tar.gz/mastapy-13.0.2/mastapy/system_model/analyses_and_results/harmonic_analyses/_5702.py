"""BevelDifferentialSunGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5698
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelDifferentialSunGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.system_deflections import _2713
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5703,
        _5691,
        _5720,
        _5761,
        _5794,
        _5713,
        _5796,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7556, _7553
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialSunGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearHarmonicAnalysis")


class BevelDifferentialSunGearHarmonicAnalysis(
    _5698.BevelDifferentialGearHarmonicAnalysis
):
    """BevelDifferentialSunGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialSunGearHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialSunGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
            parent: "BevelDifferentialSunGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5698.BevelDifferentialGearHarmonicAnalysis":
            return self._parent._cast(_5698.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5703.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5691.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5720.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5761.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(_5761.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5794.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5794,
            )

            return self._parent._cast(_5794.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5713.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_5796.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_7556.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7556

            return self._parent._cast(_7556.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_7553.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7553

            return self._parent._cast(_7553.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
        ) -> "BevelDifferentialSunGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialSunGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.BevelDifferentialSunGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2713.BevelDifferentialSunGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection

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
    ) -> "BevelDifferentialSunGearHarmonicAnalysis._Cast_BevelDifferentialSunGearHarmonicAnalysis":
        return self._Cast_BevelDifferentialSunGearHarmonicAnalysis(self)
