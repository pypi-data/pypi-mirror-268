"""PlanetCarrier"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2471
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrier"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468, _2451, _2475
    from mastapy.system_model.connections_and_sockets import _2295
    from mastapy.system_model.part_model.shaft_model import _2489
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrier",)


Self = TypeVar("Self", bound="PlanetCarrier")


class PlanetCarrier(_2471.MountableComponent):
    """PlanetCarrier

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrier")

    class _Cast_PlanetCarrier:
        """Special nested class for casting PlanetCarrier to subclasses."""

        def __init__(
            self: "PlanetCarrier._Cast_PlanetCarrier", parent: "PlanetCarrier"
        ):
            self._parent = parent

        @property
        def mountable_component(
            self: "PlanetCarrier._Cast_PlanetCarrier",
        ) -> "_2471.MountableComponent":
            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "PlanetCarrier._Cast_PlanetCarrier") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "PlanetCarrier._Cast_PlanetCarrier") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "PlanetCarrier._Cast_PlanetCarrier",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def planet_carrier(
            self: "PlanetCarrier._Cast_PlanetCarrier",
        ) -> "PlanetCarrier":
            return self._parent

        def __getattr__(self: "PlanetCarrier._Cast_PlanetCarrier", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrier.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def number_of_planetary_sockets(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfPlanetarySockets

        if temp is None:
            return 0

        return temp

    @number_of_planetary_sockets.setter
    @enforce_parameter_types
    def number_of_planetary_sockets(self: Self, value: "int"):
        self.wrapped.NumberOfPlanetarySockets = int(value) if value is not None else 0

    @property
    def load_sharing_settings(self: Self) -> "_2468.LoadSharingSettings":
        """mastapy.system_model.part_model.LoadSharingSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadSharingSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetary_sockets(self: Self) -> "List[_2295.PlanetarySocket]":
        """List[mastapy.system_model.connections_and_sockets.PlanetarySocket]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetarySockets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def attach_carrier_shaft(
        self: Self, shaft: "_2489.Shaft", offset: "float" = float("nan")
    ):
        """Method does not return.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)
        """
        offset = float(offset)
        self.wrapped.AttachCarrierShaft(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )

    @enforce_parameter_types
    def attach_pin_shaft(
        self: Self, shaft: "_2489.Shaft", offset: "float" = float("nan")
    ):
        """Method does not return.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)
        """
        offset = float(offset)
        self.wrapped.AttachPinShaft(
            shaft.wrapped if shaft else None, offset if offset else 0.0
        )

    @property
    def cast_to(self: Self) -> "PlanetCarrier._Cast_PlanetCarrier":
        return self._Cast_PlanetCarrier(self)
