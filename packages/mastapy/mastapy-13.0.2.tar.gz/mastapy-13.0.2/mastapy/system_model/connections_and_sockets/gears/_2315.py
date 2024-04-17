"""ConicalGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2321
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearTeethSocket"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2307,
        _2309,
        _2311,
        _2323,
        _2324,
        _2328,
        _2329,
        _2331,
        _2333,
        _2335,
        _2339,
    )
    from mastapy.system_model.connections_and_sockets import _2303


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearTeethSocket",)


Self = TypeVar("Self", bound="ConicalGearTeethSocket")


class ConicalGearTeethSocket(_2321.GearTeethSocket):
    """ConicalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearTeethSocket")

    class _Cast_ConicalGearTeethSocket:
        """Special nested class for casting ConicalGearTeethSocket to subclasses."""

        def __init__(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
            parent: "ConicalGearTeethSocket",
        ):
            self._parent = parent

        @property
        def gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2321.GearTeethSocket":
            return self._parent._cast(_2321.GearTeethSocket)

        @property
        def socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2307.AGMAGleasonConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2307

            return self._parent._cast(_2307.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2309.BevelDifferentialGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2309

            return self._parent._cast(_2309.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2311.BevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.BevelGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2323.HypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2324.KlingelnbergConicalGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2328.KlingelnbergHypoidGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2329.KlingelnbergSpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2331.SpiralBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2331

            return self._parent._cast(_2331.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2333.StraightBevelDiffGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2333

            return self._parent._cast(_2333.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2335.StraightBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2335

            return self._parent._cast(_2335.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "_2339.ZerolBevelGearTeethSocket":
            from mastapy.system_model.connections_and_sockets.gears import _2339

            return self._parent._cast(_2339.ZerolBevelGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "ConicalGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket":
        return self._Cast_ConicalGearTeethSocket(self)
