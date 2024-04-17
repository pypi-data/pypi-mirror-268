"""SpiralBevelGearMeshDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "SpiralBevelGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2330
    from mastapy.system_model.analyses_and_results.static_loads import _6963
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6290,
        _6318,
        _6346,
        _6352,
        _6320,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshDynamicAnalysis")


class SpiralBevelGearMeshDynamicAnalysis(_6302.BevelGearMeshDynamicAnalysis):
    """SpiralBevelGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshDynamicAnalysis")

    class _Cast_SpiralBevelGearMeshDynamicAnalysis:
        """Special nested class for casting SpiralBevelGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
            parent: "SpiralBevelGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_6302.BevelGearMeshDynamicAnalysis":
            return self._parent._cast(_6302.BevelGearMeshDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_6290.AGMAGleasonConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_6318.ConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.ConicalGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_6346.GearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(_6346.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_6352.InterMountableComponentConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_6320.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
        ) -> "SpiralBevelGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6963.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshDynamicAnalysis._Cast_SpiralBevelGearMeshDynamicAnalysis":
        return self._Cast_SpiralBevelGearMeshDynamicAnalysis(self)
