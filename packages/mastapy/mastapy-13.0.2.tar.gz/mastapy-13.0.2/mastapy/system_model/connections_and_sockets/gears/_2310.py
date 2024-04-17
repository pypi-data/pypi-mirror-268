"""BevelGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2306
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1187
    from mastapy.system_model.connections_and_sockets.gears import (
        _2308,
        _2330,
        _2332,
        _2334,
        _2338,
        _2314,
        _2320,
    )
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMesh",)


Self = TypeVar("Self", bound="BevelGearMesh")


class BevelGearMesh(_2306.AGMAGleasonConicalGearMesh):
    """BevelGearMesh

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMesh")

    class _Cast_BevelGearMesh:
        """Special nested class for casting BevelGearMesh to subclasses."""

        def __init__(
            self: "BevelGearMesh._Cast_BevelGearMesh", parent: "BevelGearMesh"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2306.AGMAGleasonConicalGearMesh":
            return self._parent._cast(_2306.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2314.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.ConicalGearMesh)

        @property
        def gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh") -> "_2320.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(self: "BevelGearMesh._Cast_BevelGearMesh") -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bevel_differential_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2308.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.BevelDifferentialGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2330.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2332.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2334.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "_2338.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.ZerolBevelGearMesh)

        @property
        def bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "BevelGearMesh":
            return self._parent

        def __getattr__(self: "BevelGearMesh._Cast_BevelGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(self: Self) -> "_1187.BevelGearMeshDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_mesh_design(self: Self) -> "_1187.BevelGearMeshDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearMesh._Cast_BevelGearMesh":
        return self._Cast_BevelGearMesh(self)
