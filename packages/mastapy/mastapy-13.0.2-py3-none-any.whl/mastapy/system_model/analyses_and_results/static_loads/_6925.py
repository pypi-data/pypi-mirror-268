"""KlingelnbergCycloPalloidHypoidGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6922
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2326
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6855,
        _6901,
        _6920,
        _6858,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshLoadCase")


class KlingelnbergCycloPalloidHypoidGearMeshLoadCase(
    _6922.KlingelnbergCycloPalloidConicalGearMeshLoadCase
):
    """KlingelnbergCycloPalloidHypoidGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6922.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            return self._parent._cast(
                _6922.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def conical_gear_mesh_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6855.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6901.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6901

            return self._parent._cast(_6901.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6920.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_6858.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshLoadCase(self)
