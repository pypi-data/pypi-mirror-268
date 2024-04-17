"""AGMAGleasonConicalGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6855
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2306
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6832,
        _6837,
        _6915,
        _6963,
        _6969,
        _6972,
        _6995,
        _6901,
        _6920,
        _6858,
    )
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshLoadCase",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshLoadCase")


class AGMAGleasonConicalGearMeshLoadCase(_6855.ConicalGearMeshLoadCase):
    """AGMAGleasonConicalGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshLoadCase")

    class _Cast_AGMAGleasonConicalGearMeshLoadCase:
        """Special nested class for casting AGMAGleasonConicalGearMeshLoadCase to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
            parent: "AGMAGleasonConicalGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6855.ConicalGearMeshLoadCase":
            return self._parent._cast(_6855.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6901.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6901

            return self._parent._cast(_6901.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6920.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(_6920.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6858.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6832.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6837.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.BevelGearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6915.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.HypoidGearMeshLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6963.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6969.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6972.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.StraightBevelGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "_6995.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6995

            return self._parent._cast(_6995.ZerolBevelGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
        ) -> "AGMAGleasonConicalGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearMeshLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2306.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshLoadCase._Cast_AGMAGleasonConicalGearMeshLoadCase":
        return self._Cast_AGMAGleasonConicalGearMeshLoadCase(self)
