"""InterMountableComponentConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2735
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "InterMountableComponentConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2288
    from mastapy.system_model.analyses_and_results.power_flows import _4108
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2697,
        _2707,
        _2709,
        _2714,
        _2719,
        _2725,
        _2728,
        _2732,
        _2737,
        _2740,
        _2747,
        _2748,
        _2749,
        _2762,
        _2767,
        _2771,
        _2776,
        _2779,
        _2782,
        _2794,
        _2803,
        _2806,
        _2815,
        _2818,
        _2821,
        _2824,
        _2836,
        _2844,
        _2847,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7548,
        _7549,
        _7546,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionSystemDeflection",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionSystemDeflection")


class InterMountableComponentConnectionSystemDeflection(
    _2735.ConnectionSystemDeflection
):
    """InterMountableComponentConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionSystemDeflection"
    )

    class _Cast_InterMountableComponentConnectionSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
            parent: "InterMountableComponentConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2735.ConnectionSystemDeflection":
            return self._parent._cast(_2735.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_7548.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2697.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2697,
            )

            return self._parent._cast(_2697.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2707.BeltConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BeltConnectionSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2709.BevelDifferentialGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2714.BevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.BevelGearMeshSystemDeflection)

        @property
        def clutch_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2719.ClutchConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ClutchConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2725.ConceptCouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2728.ConceptGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2732.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.ConicalGearMeshSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2737.CouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(_2737.CouplingConnectionSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2740.CVTBeltConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CVTBeltConnectionSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2747.CylindricalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2748.CylindricalGearMeshSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2749.CylindricalGearMeshSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(
                _2749.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2762.FaceGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.FaceGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2767.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(_2767.GearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2771.HypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(_2771.HypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2776.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2776,
            )

            return self._parent._cast(
                _2776.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2779.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2779,
            )

            return self._parent._cast(
                _2779.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2782.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(
                _2782.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2794.PartToPartShearCouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(
                _2794.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2803.RingPinsToDiscConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2806.RollingRingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.RollingRingConnectionSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2815.SpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.SpiralBevelGearMeshSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2818.SpringDamperConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.SpringDamperConnectionSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2821.StraightBevelDiffGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2824.StraightBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.StraightBevelGearMeshSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2836.TorqueConverterConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.TorqueConverterConnectionSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2844.WormGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2844,
            )

            return self._parent._cast(_2844.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2847.ZerolBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2847,
            )

            return self._parent._cast(_2847.ZerolBevelGearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "InterMountableComponentConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2288.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4108.InterMountableComponentConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.InterMountableComponentConnectionPowerFlow

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
    ) -> "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection":
        return self._Cast_InterMountableComponentConnectionSystemDeflection(self)
