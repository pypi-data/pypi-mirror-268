"""SpiralBevelGearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SpiralBevelGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2330
    from mastapy.system_model.analyses_and_results.stability_analyses import _3872
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3910,
        _3938,
        _3964,
        _3970,
        _3940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundStabilityAnalysis")


class SpiralBevelGearMeshCompoundStabilityAnalysis(
    _3922.BevelGearMeshCompoundStabilityAnalysis
):
    """SpiralBevelGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
            parent: "SpiralBevelGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3922.BevelGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(_3922.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3910.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(
                _3910.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3938.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3964.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(_3964.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3970.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3940.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
        ) -> "SpiralBevelGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis",
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
        instance_to_wrap: "SpiralBevelGearMeshCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2330.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2330.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3872.SpiralBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpiralBevelGearMeshStabilityAnalysis]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3872.SpiralBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpiralBevelGearMeshStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshCompoundStabilityAnalysis._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis":
        return self._Cast_SpiralBevelGearMeshCompoundStabilityAnalysis(self)
