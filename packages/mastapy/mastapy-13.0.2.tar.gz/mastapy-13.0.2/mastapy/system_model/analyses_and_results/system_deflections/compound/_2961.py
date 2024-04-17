"""SpiralBevelGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "SpiralBevelGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2330
    from mastapy.system_model.analyses_and_results.system_deflections import _2815
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2864,
        _2892,
        _2919,
        _2925,
        _2894,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundSystemDeflection")


class SpiralBevelGearMeshCompoundSystemDeflection(
    _2876.BevelGearMeshCompoundSystemDeflection
):
    """SpiralBevelGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundSystemDeflection"
    )

    class _Cast_SpiralBevelGearMeshCompoundSystemDeflection:
        """Special nested class for casting SpiralBevelGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
            parent: "SpiralBevelGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_2876.BevelGearMeshCompoundSystemDeflection":
            return self._parent._cast(_2876.BevelGearMeshCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_2864.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(
                _2864.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_2892.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_2919.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(_2919.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_2925.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(
                _2925.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
        ) -> "SpiralBevelGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2330.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2815.SpiralBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2815.SpiralBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshCompoundSystemDeflection._Cast_SpiralBevelGearMeshCompoundSystemDeflection":
        return self._Cast_SpiralBevelGearMeshCompoundSystemDeflection(self)
