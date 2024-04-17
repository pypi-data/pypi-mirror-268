"""ZerolBevelGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ZerolBevelGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2338
    from mastapy.system_model.analyses_and_results.system_deflections import _2847
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
__all__ = ("ZerolBevelGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshCompoundSystemDeflection")


class ZerolBevelGearMeshCompoundSystemDeflection(
    _2876.BevelGearMeshCompoundSystemDeflection
):
    """ZerolBevelGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshCompoundSystemDeflection"
    )

    class _Cast_ZerolBevelGearMeshCompoundSystemDeflection:
        """Special nested class for casting ZerolBevelGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
            parent: "ZerolBevelGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2876.BevelGearMeshCompoundSystemDeflection":
            return self._parent._cast(_2876.BevelGearMeshCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2864.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(
                _2864.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2892.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2919.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(_2919.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2925.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2925,
            )

            return self._parent._cast(
                _2925.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2894.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(_2894.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
        ) -> "ZerolBevelGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2338.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2338.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

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
    ) -> "List[_2847.ZerolBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection]

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
    ) -> "List[_2847.ZerolBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection]

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
    ) -> "ZerolBevelGearMeshCompoundSystemDeflection._Cast_ZerolBevelGearMeshCompoundSystemDeflection":
        return self._Cast_ZerolBevelGearMeshCompoundSystemDeflection(self)
