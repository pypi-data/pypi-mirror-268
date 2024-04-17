"""BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5554
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2308
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5397
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5542,
        _5570,
        _5596,
        _5602,
        _5572,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis"
)


class BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis(
    _5554.BevelGearMeshCompoundMultibodyDynamicsAnalysis
):
    """BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
            parent: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5554.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5542.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5570.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5596.GearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(_5596.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5602.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5602,
            )

            return self._parent._cast(
                _5602.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(_5572.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2308.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2308.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

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
    ) -> "List[_5397.BevelDifferentialGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "List[_5397.BevelDifferentialGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BevelDifferentialGearMeshMultibodyDynamicsAnalysis]

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
    ) -> "BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis(
            self
        )
