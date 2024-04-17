"""StraightBevelGearMeshHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5704
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "StraightBevelGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2334
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.system_deflections import _2824
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5692,
        _5721,
        _5763,
        _5782,
        _5723,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearMeshHarmonicAnalysis")


class StraightBevelGearMeshHarmonicAnalysis(_5704.BevelGearMeshHarmonicAnalysis):
    """StraightBevelGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshHarmonicAnalysis"
    )

    class _Cast_StraightBevelGearMeshHarmonicAnalysis:
        """Special nested class for casting StraightBevelGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
            parent: "StraightBevelGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_5704.BevelGearMeshHarmonicAnalysis":
            return self._parent._cast(_5704.BevelGearMeshHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_5692.AGMAGleasonConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_5721.ConicalGearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_5763.GearMeshHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5763,
            )

            return self._parent._cast(_5763.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_5782.InterMountableComponentConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(
                _5782.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_5723.ConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
        ) -> "StraightBevelGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearMeshHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2334.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6972.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2824.StraightBevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection

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
    ) -> "StraightBevelGearMeshHarmonicAnalysis._Cast_StraightBevelGearMeshHarmonicAnalysis":
        return self._Cast_StraightBevelGearMeshHarmonicAnalysis(self)
