"""WormGearMeshAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7078,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2336
    from mastapy.system_model.analyses_and_results.static_loads import _6992
    from mastapy.system_model.analyses_and_results.system_deflections import _2844
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7085,
        _7054,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="WormGearMeshAdvancedTimeSteppingAnalysisForModulation")


class WormGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7078.GearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """WormGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation"
    )

    class _Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting WormGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7078.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7078.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7054.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "WormGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "WormGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2336.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6992.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2844.WormGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection

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
    ) -> "WormGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_WormGearMeshAdvancedTimeSteppingAnalysisForModulation(self)
