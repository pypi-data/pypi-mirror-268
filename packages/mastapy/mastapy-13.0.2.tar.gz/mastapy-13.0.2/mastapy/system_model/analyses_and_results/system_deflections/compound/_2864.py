"""AGMAGleasonConicalGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2892
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2697
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2871,
        _2876,
        _2923,
        _2961,
        _2967,
        _2970,
        _2988,
        _2919,
        _2925,
        _2894,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshCompoundSystemDeflection")


class AGMAGleasonConicalGearMeshCompoundSystemDeflection(
    _2892.ConicalGearMeshCompoundSystemDeflection
):
    """AGMAGleasonConicalGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
            parent: "AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2892.ConicalGearMeshCompoundSystemDeflection":
            return self._parent._cast(_2892.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2919.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(_2919.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2925.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(
                _2925.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2871.BevelDifferentialGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2871,
            )

            return self._parent._cast(
                _2871.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2876.BevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.BevelGearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2923.HypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(_2923.HypoidGearMeshCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2961.SpiralBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(_2961.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2967.StraightBevelDiffGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(
                _2967.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2970.StraightBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(
                _2970.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "_2988.ZerolBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2988,
            )

            return self._parent._cast(_2988.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
        ) -> "AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2697.AGMAGleasonConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection]

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
    ) -> "List[_2697.AGMAGleasonConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearMeshCompoundSystemDeflection._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearMeshCompoundSystemDeflection(self)
