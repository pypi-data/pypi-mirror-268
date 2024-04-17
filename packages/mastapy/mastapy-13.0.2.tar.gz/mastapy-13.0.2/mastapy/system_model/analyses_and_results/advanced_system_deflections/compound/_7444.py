"""ConceptGearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7473,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConceptGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7311,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7479,
        _7449,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptGearMeshCompoundAdvancedSystemDeflection")


class ConceptGearMeshCompoundAdvancedSystemDeflection(
    _7473.GearMeshCompoundAdvancedSystemDeflection
):
    """ConceptGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConceptGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
            parent: "ConceptGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7473.GearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7473.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7449.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7547.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
        ) -> "ConceptGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConceptGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2312.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2312.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

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
    ) -> "List[_7311.ConceptGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7311.ConceptGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearMeshAdvancedSystemDeflection]

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
    ) -> "ConceptGearMeshCompoundAdvancedSystemDeflection._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_ConceptGearMeshCompoundAdvancedSystemDeflection(self)
