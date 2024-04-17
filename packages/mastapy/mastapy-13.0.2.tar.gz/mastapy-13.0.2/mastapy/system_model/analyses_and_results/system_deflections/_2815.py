"""SpiralBevelGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2714
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpiralBevelGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.spiral_bevel import _405
    from mastapy.system_model.connections_and_sockets.gears import _2330
    from mastapy.system_model.analyses_and_results.static_loads import _6963
    from mastapy.system_model.analyses_and_results.power_flows import _4144
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2697,
        _2732,
        _2767,
        _2775,
        _2735,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshSystemDeflection")


class SpiralBevelGearMeshSystemDeflection(_2714.BevelGearMeshSystemDeflection):
    """SpiralBevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshSystemDeflection")

    class _Cast_SpiralBevelGearMeshSystemDeflection:
        """Special nested class for casting SpiralBevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
            parent: "SpiralBevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2714.BevelGearMeshSystemDeflection":
            return self._parent._cast(_2714.BevelGearMeshSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2697.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2697,
            )

            return self._parent._cast(_2697.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2732.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2767.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(_2767.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2775.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2735.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
        ) -> "SpiralBevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_405.SpiralBevelGearMeshRating":
        """mastapy.gears.rating.spiral_bevel.SpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_405.SpiralBevelGearMeshRating":
        """mastapy.gears.rating.spiral_bevel.SpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

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
    def power_flow_results(self: Self) -> "_4144.SpiralBevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "SpiralBevelGearMeshSystemDeflection._Cast_SpiralBevelGearMeshSystemDeflection"
    ):
        return self._Cast_SpiralBevelGearMeshSystemDeflection(self)
