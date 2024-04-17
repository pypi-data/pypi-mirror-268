"""AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5920
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5692
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5899,
        _5904,
        _5950,
        _5987,
        _5993,
        _5996,
        _6014,
        _5946,
        _5952,
        _5922,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis")


class AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis(
    _5920.ConicalGearMeshCompoundHarmonicAnalysis
):
    """AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5920.ConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(_5920.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5946.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(_5946.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5952.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5952,
            )

            return self._parent._cast(
                _5952.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5922.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5922,
            )

            return self._parent._cast(_5922.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5899.BevelDifferentialGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5899,
            )

            return self._parent._cast(
                _5899.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5904.BevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5904,
            )

            return self._parent._cast(_5904.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5950.HypoidGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5950,
            )

            return self._parent._cast(_5950.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5987.SpiralBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(_5987.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5993.StraightBevelDiffGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(
                _5993.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_5996.StraightBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5996,
            )

            return self._parent._cast(
                _5996.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "_6014.ZerolBevelGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6014,
            )

            return self._parent._cast(_6014.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5692.AGMAGleasonConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5692.AGMAGleasonConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis(self)
