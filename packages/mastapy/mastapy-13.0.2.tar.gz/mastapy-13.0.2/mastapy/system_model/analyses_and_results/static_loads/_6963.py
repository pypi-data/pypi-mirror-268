"""SpiralBevelGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6837
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2330
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6823,
        _6855,
        _6901,
        _6920,
        _6858,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshLoadCase",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshLoadCase")


class SpiralBevelGearMeshLoadCase(_6837.BevelGearMeshLoadCase):
    """SpiralBevelGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearMeshLoadCase")

    class _Cast_SpiralBevelGearMeshLoadCase:
        """Special nested class for casting SpiralBevelGearMeshLoadCase to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
            parent: "SpiralBevelGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_6837.BevelGearMeshLoadCase":
            return self._parent._cast(_6837.BevelGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_6823.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_6855.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_6901.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6901

            return self._parent._cast(_6901.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_6920.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_6858.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
        ) -> "SpiralBevelGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshLoadCase._Cast_SpiralBevelGearMeshLoadCase":
        return self._Cast_SpiralBevelGearMeshLoadCase(self)
