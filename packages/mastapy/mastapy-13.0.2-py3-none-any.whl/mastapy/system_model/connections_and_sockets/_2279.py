"""Connection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.python_net import python_net_import
from mastapy.system_model import _2210
from mastapy._internal.cast_exception import CastException

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2451
    from mastapy.system_model.connections_and_sockets import (
        _2303,
        _2272,
        _2275,
        _2276,
        _2280,
        _2288,
        _2294,
        _2299,
        _2302,
    )
    from mastapy.system_model.connections_and_sockets.gears import (
        _2306,
        _2308,
        _2310,
        _2312,
        _2314,
        _2316,
        _2318,
        _2320,
        _2322,
        _2325,
        _2326,
        _2327,
        _2330,
        _2332,
        _2334,
        _2336,
        _2338,
    )
    from mastapy.system_model.connections_and_sockets.cycloidal import (
        _2342,
        _2345,
        _2348,
    )
    from mastapy.system_model.connections_and_sockets.couplings import (
        _2349,
        _2351,
        _2353,
        _2355,
        _2357,
        _2359,
    )


__docformat__ = "restructuredtext en"
__all__ = ("Connection",)


Self = TypeVar("Self", bound="Connection")


class Connection(_2210.DesignEntity):
    """Connection

    This is a mastapy class.
    """

    TYPE = _CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Connection")

    class _Cast_Connection:
        """Special nested class for casting Connection to subclasses."""

        def __init__(self: "Connection._Cast_Connection", parent: "Connection"):
            self._parent = parent

        @property
        def design_entity(self: "Connection._Cast_Connection") -> "_2210.DesignEntity":
            return self._parent._cast(_2210.DesignEntity)

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2272.AbstractShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2272

            return self._parent._cast(_2272.AbstractShaftToMountableComponentConnection)

        @property
        def belt_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2275.BeltConnection":
            from mastapy.system_model.connections_and_sockets import _2275

            return self._parent._cast(_2275.BeltConnection)

        @property
        def coaxial_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2276.CoaxialConnection":
            from mastapy.system_model.connections_and_sockets import _2276

            return self._parent._cast(_2276.CoaxialConnection)

        @property
        def cvt_belt_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2280.CVTBeltConnection":
            from mastapy.system_model.connections_and_sockets import _2280

            return self._parent._cast(_2280.CVTBeltConnection)

        @property
        def inter_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def planetary_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2294.PlanetaryConnection":
            from mastapy.system_model.connections_and_sockets import _2294

            return self._parent._cast(_2294.PlanetaryConnection)

        @property
        def rolling_ring_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2299.RollingRingConnection":
            from mastapy.system_model.connections_and_sockets import _2299

            return self._parent._cast(_2299.RollingRingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2302.ShaftToMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2302

            return self._parent._cast(_2302.ShaftToMountableComponentConnection)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2306.AGMAGleasonConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2306

            return self._parent._cast(_2306.AGMAGleasonConicalGearMesh)

        @property
        def bevel_differential_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2308.BevelDifferentialGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2308

            return self._parent._cast(_2308.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2310.BevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.BevelGearMesh)

        @property
        def concept_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2312.ConceptGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2312

            return self._parent._cast(_2312.ConceptGearMesh)

        @property
        def conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2314.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.ConicalGearMesh)

        @property
        def cylindrical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2316.CylindricalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2316

            return self._parent._cast(_2316.CylindricalGearMesh)

        @property
        def face_gear_mesh(self: "Connection._Cast_Connection") -> "_2318.FaceGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.FaceGearMesh)

        @property
        def gear_mesh(self: "Connection._Cast_Connection") -> "_2320.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.GearMesh)

        @property
        def hypoid_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2322.HypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.HypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2325.KlingelnbergCycloPalloidConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2326.KlingelnbergCycloPalloidHypoidGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2326

            return self._parent._cast(_2326.KlingelnbergCycloPalloidHypoidGearMesh)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2327

            return self._parent._cast(_2327.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2330.SpiralBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2330

            return self._parent._cast(_2330.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2332.StraightBevelDiffGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2332

            return self._parent._cast(_2332.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2334.StraightBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2334

            return self._parent._cast(_2334.StraightBevelGearMesh)

        @property
        def worm_gear_mesh(self: "Connection._Cast_Connection") -> "_2336.WormGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2336

            return self._parent._cast(_2336.WormGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "Connection._Cast_Connection",
        ) -> "_2338.ZerolBevelGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2338

            return self._parent._cast(_2338.ZerolBevelGearMesh)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2342.CycloidalDiscCentralBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2342

            return self._parent._cast(_2342.CycloidalDiscCentralBearingConnection)

        @property
        def cycloidal_disc_planetary_bearing_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2345.CycloidalDiscPlanetaryBearingConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2345

            return self._parent._cast(_2345.CycloidalDiscPlanetaryBearingConnection)

        @property
        def ring_pins_to_disc_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2348.RingPinsToDiscConnection":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2348

            return self._parent._cast(_2348.RingPinsToDiscConnection)

        @property
        def clutch_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2349.ClutchConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2349

            return self._parent._cast(_2349.ClutchConnection)

        @property
        def concept_coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2351.ConceptCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2351

            return self._parent._cast(_2351.ConceptCouplingConnection)

        @property
        def coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2353.CouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2353

            return self._parent._cast(_2353.CouplingConnection)

        @property
        def part_to_part_shear_coupling_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2355.PartToPartShearCouplingConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2355

            return self._parent._cast(_2355.PartToPartShearCouplingConnection)

        @property
        def spring_damper_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2357.SpringDamperConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2357

            return self._parent._cast(_2357.SpringDamperConnection)

        @property
        def torque_converter_connection(
            self: "Connection._Cast_Connection",
        ) -> "_2359.TorqueConverterConnection":
            from mastapy.system_model.connections_and_sockets.couplings import _2359

            return self._parent._cast(_2359.TorqueConverterConnection)

        @property
        def connection(self: "Connection._Cast_Connection") -> "Connection":
            return self._parent

        def __getattr__(self: "Connection._Cast_Connection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Connection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionID

        if temp is None:
            return ""

        return temp

    @property
    def drawing_position(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.DrawingPosition

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @drawing_position.setter
    @enforce_parameter_types
    def drawing_position(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.DrawingPosition = value

    @property
    def speed_ratio_from_a_to_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpeedRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ratio_from_a_to_b(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueRatioFromAToB

        if temp is None:
            return 0.0

        return temp

    @property
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def owner_a(self: Self) -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OwnerA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def owner_b(self: Self) -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OwnerB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_a(self: Self) -> "_2303.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def socket_b(self: Self) -> "_2303.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SocketB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def other_owner(self: Self, component: "_2451.Component") -> "_2451.Component":
        """mastapy.system_model.part_model.Component

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherOwner(
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_socket_for_component(
        self: Self, component: "_2451.Component"
    ) -> "_2303.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherSocket.Overloads[_COMPONENT](
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_socket(self: Self, socket: "_2303.Socket") -> "_2303.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = self.wrapped.OtherSocket.Overloads[_SOCKET](
            socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def socket_for(self: Self, component: "_2451.Component") -> "_2303.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.SocketFor(component.wrapped if component else None)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "Connection._Cast_Connection":
        return self._Cast_Connection(self)
