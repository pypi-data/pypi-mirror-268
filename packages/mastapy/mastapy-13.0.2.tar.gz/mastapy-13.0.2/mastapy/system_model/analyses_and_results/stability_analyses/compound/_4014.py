"""StraightBevelGearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "StraightBevelGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2334
    from mastapy.system_model.analyses_and_results.stability_analyses import _3884
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
__all__ = ("StraightBevelGearMeshCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearMeshCompoundStabilityAnalysis")


class StraightBevelGearMeshCompoundStabilityAnalysis(
    _3922.BevelGearMeshCompoundStabilityAnalysis
):
    """StraightBevelGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshCompoundStabilityAnalysis"
    )

    class _Cast_StraightBevelGearMeshCompoundStabilityAnalysis:
        """Special nested class for casting StraightBevelGearMeshCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
            parent: "StraightBevelGearMeshCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3922.BevelGearMeshCompoundStabilityAnalysis":
            return self._parent._cast(_3922.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3910.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3910,
            )

            return self._parent._cast(
                _3910.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3938.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3964.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(_3964.GearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3970.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_3940.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3940,
            )

            return self._parent._cast(_3940.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
        ) -> "StraightBevelGearMeshCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis",
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
        instance_to_wrap: "StraightBevelGearMeshCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2334.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3884.StraightBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelGearMeshStabilityAnalysis]

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
    ) -> "List[_3884.StraightBevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.StraightBevelGearMeshStabilityAnalysis]

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
    ) -> "StraightBevelGearMeshCompoundStabilityAnalysis._Cast_StraightBevelGearMeshCompoundStabilityAnalysis":
        return self._Cast_StraightBevelGearMeshCompoundStabilityAnalysis(self)
