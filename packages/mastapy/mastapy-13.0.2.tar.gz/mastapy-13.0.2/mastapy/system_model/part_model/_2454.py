"""Connector"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2471
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2442, _2451, _2452, _2446, _2473, _2475
    from mastapy.system_model.connections_and_sockets import _2279, _2283
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("Connector",)


Self = TypeVar("Self", bound="Connector")


class Connector(_2471.MountableComponent):
    """Connector

    This is a mastapy class.
    """

    TYPE = _CONNECTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Connector")

    class _Cast_Connector:
        """Special nested class for casting Connector to subclasses."""

        def __init__(self: "Connector._Cast_Connector", parent: "Connector"):
            self._parent = parent

        @property
        def mountable_component(
            self: "Connector._Cast_Connector",
        ) -> "_2471.MountableComponent":
            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "Connector._Cast_Connector") -> "_2451.Component":
            return self._parent._cast(_2451.Component)

        @property
        def part(self: "Connector._Cast_Connector") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "Connector._Cast_Connector") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def bearing(self: "Connector._Cast_Connector") -> "_2446.Bearing":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Bearing)

        @property
        def oil_seal(self: "Connector._Cast_Connector") -> "_2473.OilSeal":
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.OilSeal)

        @property
        def shaft_hub_connection(
            self: "Connector._Cast_Connector",
        ) -> "_2606.ShaftHubConnection":
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.ShaftHubConnection)

        @property
        def connector(self: "Connector._Cast_Connector") -> "Connector":
            return self._parent

        def __getattr__(self: "Connector._Cast_Connector", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Connector.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def outer_component(self: Self) -> "_2442.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterComponent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_connection(self: Self) -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterConnection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def outer_socket(self: Self) -> "_2283.CylindricalSocket":
        """mastapy.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OuterSocket

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def house_in(
        self: Self, shaft: "_2442.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2279.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.HouseIn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def other_component(
        self: Self, component: "_2451.Component"
    ) -> "_2442.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = self.wrapped.OtherComponent(
            component.wrapped if component else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_house_in(
        self: Self, shaft: "_2442.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2452.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = self.wrapped.TryHouseIn(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "Connector._Cast_Connector":
        return self._Cast_Connector(self)
