"""WormGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "WormGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.worm import _962
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMesh",)


Self = TypeVar("Self", bound="WormGearMesh")


class WormGearMesh(_2320.GearMesh):
    """WormGearMesh

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGearMesh")

    class _Cast_WormGearMesh:
        """Special nested class for casting WormGearMesh to subclasses."""

        def __init__(self: "WormGearMesh._Cast_WormGearMesh", parent: "WormGearMesh"):
            self._parent = parent

        @property
        def gear_mesh(self: "WormGearMesh._Cast_WormGearMesh") -> "_2320.GearMesh":
            return self._parent._cast(_2320.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "WormGearMesh._Cast_WormGearMesh",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(self: "WormGearMesh._Cast_WormGearMesh") -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "WormGearMesh._Cast_WormGearMesh",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def worm_gear_mesh(self: "WormGearMesh._Cast_WormGearMesh") -> "WormGearMesh":
            return self._parent

        def __getattr__(self: "WormGearMesh._Cast_WormGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def meshing_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeshingAngle

        if temp is None:
            return 0.0

        return temp

    @meshing_angle.setter
    @enforce_parameter_types
    def meshing_angle(self: Self, value: "float"):
        self.wrapped.MeshingAngle = float(value) if value is not None else 0.0

    @property
    def active_gear_mesh_design(self: Self) -> "_962.WormGearMeshDesign":
        """mastapy.gears.gear_designs.worm.WormGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def worm_gear_mesh_design(self: Self) -> "_962.WormGearMeshDesign":
        """mastapy.gears.gear_designs.worm.WormGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "WormGearMesh._Cast_WormGearMesh":
        return self._Cast_WormGearMesh(self)
