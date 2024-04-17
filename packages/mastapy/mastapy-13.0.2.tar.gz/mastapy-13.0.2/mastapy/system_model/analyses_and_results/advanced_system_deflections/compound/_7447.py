"""ConicalGearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7473,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConicalGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7314,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7419,
        _7426,
        _7431,
        _7477,
        _7481,
        _7484,
        _7487,
        _7514,
        _7520,
        _7523,
        _7541,
        _7479,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundAdvancedSystemDeflection")


class ConicalGearMeshCompoundAdvancedSystemDeflection(
    _7473.GearMeshCompoundAdvancedSystemDeflection
):
    """ConicalGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConicalGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
            parent: "ConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7473.GearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7473.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7419.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7419,
            )

            return self._parent._cast(
                _7419.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7426.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7431.BevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(
                _7431.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7477.HypoidGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(
                _7477.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7481.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(
                _7481.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7484.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(
                _7484.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7487.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(
                _7487.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7514.SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(
                _7514.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7520.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7523.StraightBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7541.ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7541,
            )

            return self._parent._cast(
                _7541.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "ConicalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConicalGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7314.ConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7314.ConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearMeshAdvancedSystemDeflection]

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
    ) -> "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection(self)
