"""GearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets import _2303
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2307,
        _2309,
        _2311,
        _2313,
        _2315,
        _2319,
        _2323,
        _2324,
        _2328,
        _2329,
        _2331,
        _2333,
        _2335,
        _2337,
        _2339,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearTeethSocket",)


Self = TypeVar("Self", bound="GearTeethSocket")


class GearTeethSocket(_2303.Socket):
    """GearTeethSocket

    This is a mastapy class.
    """

    TYPE = _GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearTeethSocket")

    class _Cast_GearTeethSocket:
        """Special nested class for casting GearTeethSocket to subclasses."""

        def __init__(
            self: "GearTeethSocket._Cast_GearTeethSocket", parent: "GearTeethSocket"
        ):
            self._parent = parent

        @property
        def socket(self: "GearTeethSocket._Cast_GearTeethSocket") -> "_2303.Socket":
            return self._parent._cast(_2303.Socket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2307.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2309.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2309

            return self._parent._cast(_2309.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2311.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.BevelGearTeethSocket)

        @property
        def concept_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2313.ConceptGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.ConceptGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2315.ConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.ConicalGearTeethSocket)

        @property
        def face_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2319.FaceGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.FaceGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2323.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2324.KlingelnbergConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2328.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2329.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2331.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2333.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2335.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.StraightBevelGearTeethSocket)

        @property
        def worm_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2337.WormGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2337

            return self._parent._cast(_2337.WormGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "_2339.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.ZerolBevelGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "GearTeethSocket._Cast_GearTeethSocket",
        ) -> "GearTeethSocket":
            return self._parent

        def __getattr__(self: "GearTeethSocket._Cast_GearTeethSocket", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearTeethSocket._Cast_GearTeethSocket":
        return self._Cast_GearTeethSocket(self)
