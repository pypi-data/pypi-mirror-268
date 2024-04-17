"""BevelGearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7419,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7298,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7426,
        _7514,
        _7520,
        _7523,
        _7541,
        _7447,
        _7473,
        _7479,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundAdvancedSystemDeflection")


class BevelGearMeshCompoundAdvancedSystemDeflection(
    _7419.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
):
    """BevelGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_BevelGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
            parent: "BevelGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7419.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7419.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7447.ConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7447,
            )

            return self._parent._cast(
                _7447.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7473.GearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(_7473.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7426.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7514.SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7514,
            )

            return self._parent._cast(
                _7514.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7520.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7523.StraightBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7541.ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7541,
            )

            return self._parent._cast(
                _7541.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
        ) -> "BevelGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "BevelGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7298.BevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7298.BevelGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelGearMeshAdvancedSystemDeflection]

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
    ) -> "BevelGearMeshCompoundAdvancedSystemDeflection._Cast_BevelGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_BevelGearMeshCompoundAdvancedSystemDeflection(self)
