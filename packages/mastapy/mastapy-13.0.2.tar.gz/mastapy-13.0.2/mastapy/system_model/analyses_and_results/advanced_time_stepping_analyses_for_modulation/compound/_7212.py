"""HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7154,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7083,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7182,
        _7208,
        _7214,
        _7184,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7154.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7154.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7154.AGMAGleasonConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7182.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.ConicalGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7208.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7208,
            )

            return self._parent._cast(
                _7208.GearMeshCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7214.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7214,
            )

            return self._parent._cast(
                _7214.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7184,
            )

            return self._parent._cast(
                _7184.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2322.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2322.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

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
    ) -> "List[_7083.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7083.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_HypoidGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
