"""StraightBevelDiffGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2310
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelDiffGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _970
    from mastapy.system_model.connections_and_sockets.gears import _2306, _2314, _2320
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMesh",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMesh")


class StraightBevelDiffGearMesh(_2310.BevelGearMesh):
    """StraightBevelDiffGearMesh

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearMesh")

    class _Cast_StraightBevelDiffGearMesh:
        """Special nested class for casting StraightBevelDiffGearMesh to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
            parent: "StraightBevelDiffGearMesh",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2310.BevelGearMesh":
            return self._parent._cast(_2310.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2306.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2314.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2320.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh",
        ) -> "StraightBevelDiffGearMesh":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self: Self) -> "_970.StraightBevelDiffGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gear_mesh_design(
        self: Self,
    ) -> "_970.StraightBevelDiffGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMesh._Cast_StraightBevelDiffGearMesh":
        return self._Cast_StraightBevelDiffGearMesh(self)
