"""AGMAGleasonConicalGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2314
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2308,
        _2310,
        _2322,
        _2330,
        _2332,
        _2334,
        _2338,
        _2320,
    )
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMesh",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMesh")


class AGMAGleasonConicalGearMesh(_2314.ConicalGearMesh):
    """AGMAGleasonConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMesh")

    class _Cast_AGMAGleasonConicalGearMesh:
        """Special nested class for casting AGMAGleasonConicalGearMesh to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
            parent: "AGMAGleasonConicalGearMesh",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2314.ConicalGearMesh":
            return self._parent._cast(_2314.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2320.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bevel_differential_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2308.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2310.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.BevelGearMesh)

        @property
        def hypoid_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2322.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.HypoidGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2330.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2332.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2334.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "_2338.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.ZerolBevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "AGMAGleasonConicalGearMesh":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh":
        return self._Cast_AGMAGleasonConicalGearMesh(self)
