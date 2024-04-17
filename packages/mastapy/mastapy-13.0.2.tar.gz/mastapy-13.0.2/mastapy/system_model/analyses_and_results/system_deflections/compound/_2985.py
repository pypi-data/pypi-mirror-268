"""WormGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2919
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "WormGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2336
    from mastapy.system_model.analyses_and_results.system_deflections import _2844
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2925,
        _2894,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="WormGearMeshCompoundSystemDeflection")


class WormGearMeshCompoundSystemDeflection(_2919.GearMeshCompoundSystemDeflection):
    """WormGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMeshCompoundSystemDeflection")

    class _Cast_WormGearMeshCompoundSystemDeflection:
        """Special nested class for casting WormGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
            parent: "WormGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_system_deflection(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
        ) -> "_2919.GearMeshCompoundSystemDeflection":
            return self._parent._cast(_2919.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
        ) -> "_2925.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(
                _2925.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
        ) -> "WormGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "WormGearMeshCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2336.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2336.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

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
    ) -> "List[_2844.WormGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection]

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
    ) -> "List[_2844.WormGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection]

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
    ) -> "WormGearMeshCompoundSystemDeflection._Cast_WormGearMeshCompoundSystemDeflection":
        return self._Cast_WormGearMeshCompoundSystemDeflection(self)
