"""BevelGearMeshAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7023,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2310
    from mastapy.system_model.analyses_and_results.system_deflections import _2714
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7031,
        _7120,
        _7126,
        _7129,
        _7147,
        _7052,
        _7078,
        _7085,
        _7054,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="BevelGearMeshAdvancedTimeSteppingAnalysisForModulation")


class BevelGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """BevelGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            return self._parent._cast(
                _7023.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7078.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7078,
            )

            return self._parent._cast(
                _7078.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7085,
            )

            return self._parent._cast(
                _7085.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7054.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7054,
            )

            return self._parent._cast(
                _7054.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7031.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7031,
            )

            return self._parent._cast(
                _7031.BevelDifferentialGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7120.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7120,
            )

            return self._parent._cast(
                _7120.SpiralBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7126.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.StraightBevelDiffGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7129.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7147.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7147,
            )

            return self._parent._cast(
                _7147.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2310.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2714.BevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection

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
    ) -> "BevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelGearMeshAdvancedTimeSteppingAnalysisForModulation(self)
