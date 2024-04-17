"""ConceptGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7342
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConceptGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.concept import _553
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6851
    from mastapy.system_model.analyses_and_results.system_deflections import _2728
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7348,
        _7316,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptGearMeshAdvancedSystemDeflection")


class ConceptGearMeshAdvancedSystemDeflection(_7342.GearMeshAdvancedSystemDeflection):
    """ConceptGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearMeshAdvancedSystemDeflection"
    )

    class _Cast_ConceptGearMeshAdvancedSystemDeflection:
        """Special nested class for casting ConceptGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
            parent: "ConceptGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_advanced_system_deflection(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "_7342.GearMeshAdvancedSystemDeflection":
            return self._parent._cast(_7342.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "_7348.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(
                _7348.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "_7316.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
        ) -> "ConceptGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConceptGearMeshAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self: Self) -> "_553.ConceptGearMeshRating":
        """mastapy.gears.rating.concept.ConceptGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

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
    def connection_load_case(self: Self) -> "_6851.ConceptGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2728.ConceptGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearMeshAdvancedSystemDeflection._Cast_ConceptGearMeshAdvancedSystemDeflection":
        return self._Cast_ConceptGearMeshAdvancedSystemDeflection(self)
