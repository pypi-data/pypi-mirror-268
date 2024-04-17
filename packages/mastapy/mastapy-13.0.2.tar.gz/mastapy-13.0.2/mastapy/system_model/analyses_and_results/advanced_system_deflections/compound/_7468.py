"""FaceGearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7473,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "FaceGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2318
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7337,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7479,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="FaceGearMeshCompoundAdvancedSystemDeflection")


class FaceGearMeshCompoundAdvancedSystemDeflection(
    _7473.GearMeshCompoundAdvancedSystemDeflection
):
    """FaceGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_FaceGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting FaceGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
            parent: "FaceGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7473.GearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7473.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def face_gear_mesh_compound_advanced_system_deflection(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
        ) -> "FaceGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "FaceGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2318.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2318.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

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
    ) -> "List[_7337.FaceGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FaceGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7337.FaceGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FaceGearMeshAdvancedSystemDeflection]

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
    ) -> "FaceGearMeshCompoundAdvancedSystemDeflection._Cast_FaceGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_FaceGearMeshCompoundAdvancedSystemDeflection(self)
