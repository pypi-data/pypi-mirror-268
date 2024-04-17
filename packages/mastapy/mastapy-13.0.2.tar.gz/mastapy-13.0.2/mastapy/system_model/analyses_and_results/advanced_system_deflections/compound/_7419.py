"""AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7447,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7286,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7426,
        _7431,
        _7477,
        _7514,
        _7520,
        _7523,
        _7541,
        _7473,
        _7479,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection"
)


class AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection(
    _7447.ConicalGearMeshCompoundAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7447.ConicalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7447.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7473.GearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(_7473.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7426.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7431.BevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(
                _7431.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7477.HypoidGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(
                _7477.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7514.SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(
                _7514.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7520.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7523.StraightBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7541.ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7541,
            )

            return self._parent._cast(
                _7541.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7286.AGMAGleasonConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7286.AGMAGleasonConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearMeshAdvancedSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection(
            self
        )
