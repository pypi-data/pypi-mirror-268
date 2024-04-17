"""StraightBevelGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "StraightBevelGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.straight_bevel import _398
    from mastapy.system_model.connections_and_sockets.gears import _2334
    from mastapy.system_model.analyses_and_results.static_loads import _6972
    from mastapy.system_model.analyses_and_results.system_deflections import _2824
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7286,
        _7314,
        _7342,
        _7348,
        _7316,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7549, _7546
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelGearMeshAdvancedSystemDeflection")


class StraightBevelGearMeshAdvancedSystemDeflection(
    _7298.BevelGearMeshAdvancedSystemDeflection
):
    """StraightBevelGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearMeshAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelGearMeshAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
            parent: "StraightBevelGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7298.BevelGearMeshAdvancedSystemDeflection":
            return self._parent._cast(_7298.BevelGearMeshAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7286.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(
                _7286.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7314.ConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7314,
            )

            return self._parent._cast(_7314.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7342.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7342,
            )

            return self._parent._cast(_7342.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7348.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(
                _7348.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7316.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7549.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_7546.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
        ) -> "StraightBevelGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelGearMeshAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self: Self) -> "_398.StraightBevelGearMeshRating":
        """mastapy.gears.rating.straight_bevel.StraightBevelGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2334.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6972.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

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
    ) -> "List[_2824.StraightBevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection]

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
    ) -> "StraightBevelGearMeshAdvancedSystemDeflection._Cast_StraightBevelGearMeshAdvancedSystemDeflection":
        return self._Cast_StraightBevelGearMeshAdvancedSystemDeflection(self)
