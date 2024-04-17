"""ConicalGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.connections_and_sockets.gears import _2320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import (
        _2306,
        _2308,
        _2310,
        _2322,
        _2325,
        _2326,
        _2327,
        _2330,
        _2332,
        _2334,
        _2338,
    )
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMesh",)


Self = TypeVar("Self", bound="ConicalGearMesh")


class ConicalGearMesh(_2320.GearMesh):
    """ConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMesh")

    class _Cast_ConicalGearMesh:
        """Special nested class for casting ConicalGearMesh to subclasses."""

        def __init__(
            self: "ConicalGearMesh._Cast_ConicalGearMesh", parent: "ConicalGearMesh"
        ):
            self._parent = parent

        @property
        def gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2320.GearMesh":
            return self._parent._cast(_2320.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2306.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2308.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2310.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.BevelGearMesh)

        @property
        def hypoid_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2322.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2325.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2330.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2332.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2334.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "_2338.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.ZerolBevelGearMesh)

        @property
        def conical_gear_mesh(
            self: "ConicalGearMesh._Cast_ConicalGearMesh",
        ) -> "ConicalGearMesh":
            return self._parent

        def __getattr__(self: "ConicalGearMesh._Cast_ConicalGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return temp

    @crowning.setter
    @enforce_parameter_types
    def crowning(self: Self, value: "float"):
        self.wrapped.Crowning = float(value) if value is not None else 0.0

    @property
    def pinion_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PinionDropAngle

        if temp is None:
            return 0.0

        return temp

    @pinion_drop_angle.setter
    @enforce_parameter_types
    def pinion_drop_angle(self: Self, value: "float"):
        self.wrapped.PinionDropAngle = float(value) if value is not None else 0.0

    @property
    def wheel_drop_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelDropAngle

        if temp is None:
            return 0.0

        return temp

    @wheel_drop_angle.setter
    @enforce_parameter_types
    def wheel_drop_angle(self: Self, value: "float"):
        self.wrapped.WheelDropAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "ConicalGearMesh._Cast_ConicalGearMesh":
        return self._Cast_ConicalGearMesh(self)
