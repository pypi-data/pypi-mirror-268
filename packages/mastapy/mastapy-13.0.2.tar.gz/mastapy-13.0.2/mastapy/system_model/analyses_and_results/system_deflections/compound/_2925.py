"""InterMountableComponentConnectionCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2894
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "InterMountableComponentConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2775
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2864,
        _2868,
        _2871,
        _2876,
        _2881,
        _2886,
        _2889,
        _2892,
        _2897,
        _2899,
        _2907,
        _2914,
        _2919,
        _2923,
        _2927,
        _2930,
        _2933,
        _2941,
        _2950,
        _2953,
        _2961,
        _2964,
        _2967,
        _2970,
        _2979,
        _2985,
        _2988,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundSystemDeflection"
)


class InterMountableComponentConnectionCompoundSystemDeflection(
    _2894.ConnectionCompoundSystemDeflection
):
    """InterMountableComponentConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundSystemDeflection",
    )

    class _Cast_InterMountableComponentConnectionCompoundSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
            parent: "InterMountableComponentConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2864.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(
                _2864.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def belt_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2868.BeltConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2868,
            )

            return self._parent._cast(_2868.BeltConnectionCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2871.BevelDifferentialGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2871,
            )

            return self._parent._cast(
                _2871.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2876.BevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.BevelGearMeshCompoundSystemDeflection)

        @property
        def clutch_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2881.ClutchConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.ClutchConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2886.ConceptCouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(
                _2886.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2889.ConceptGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2892.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.ConicalGearMeshCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2897.CouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2897,
            )

            return self._parent._cast(_2897.CouplingConnectionCompoundSystemDeflection)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2899.CVTBeltConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2907.CylindricalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2914.FaceGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(_2914.FaceGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2919.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(_2919.GearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2923.HypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(_2923.HypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2927.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2927,
            )

            return self._parent._cast(
                _2927.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2930.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(
                _2930.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> (
            "_2933.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(
                _2933.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2941.PartToPartShearCouplingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(
                _2941.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2950.RingPinsToDiscConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(
                _2950.RingPinsToDiscConnectionCompoundSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2953.RollingRingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2953,
            )

            return self._parent._cast(
                _2953.RollingRingConnectionCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2961.SpiralBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(_2961.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2964.SpringDamperConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2964,
            )

            return self._parent._cast(
                _2964.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2967.StraightBevelDiffGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(
                _2967.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2970.StraightBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(
                _2970.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2979.TorqueConverterConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2979,
            )

            return self._parent._cast(
                _2979.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2985.WormGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2985,
            )

            return self._parent._cast(_2985.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "_2988.ZerolBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2988,
            )

            return self._parent._cast(_2988.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
        ) -> "InterMountableComponentConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2775.InterMountableComponentConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2775.InterMountableComponentConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionCompoundSystemDeflection._Cast_InterMountableComponentConnectionCompoundSystemDeflection":
        return self._Cast_InterMountableComponentConnectionCompoundSystemDeflection(
            self
        )
