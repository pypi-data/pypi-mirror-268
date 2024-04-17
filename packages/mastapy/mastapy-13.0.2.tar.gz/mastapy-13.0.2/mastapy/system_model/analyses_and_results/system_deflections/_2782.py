"""KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2776
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
        "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _408
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6928
    from mastapy.system_model.analyses_and_results.power_flows import _4115
    from mastapy.system_model.analyses_and_results.system_deflections import (
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
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection"
)


class KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection(
    _2776.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
):
    """KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_2776.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection":
            return self._parent._cast(
                _2776.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def conical_gear_mesh_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_2732.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_2767.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(_2767.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_2775.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_2735.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_408.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_408.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
        """mastapy.gears.rating.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(
        self: Self,
    ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6928.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4115.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection(
            self
        )
