"""BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7036,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2308
    from mastapy.system_model.analyses_and_results.static_loads import _6832
    from mastapy.system_model.analyses_and_results.system_deflections import _2709
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7023,
        _7052,
        _7078,
        _7085,
        _7054,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation"
)


class BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7036.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7036.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7036.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7023,
            )

            return self._parent._cast(
                _7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7078.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7078,
            )

            return self._parent._cast(
                _7078.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7054.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6832.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

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
    ) -> "_2709.BevelDifferentialGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection

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
    ) -> "BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation(
            self
        )
