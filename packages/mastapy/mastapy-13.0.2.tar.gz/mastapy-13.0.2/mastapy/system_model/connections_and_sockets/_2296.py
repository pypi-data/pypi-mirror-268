"""PlanetarySocketBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2283
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_SOCKET_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetarySocketBase"
)

if TYPE_CHECKING:
    from mastapy.gears import _343
    from mastapy.system_model.connections_and_sockets import _2295, _2303
    from mastapy.system_model.connections_and_sockets.cycloidal import _2346


__docformat__ = "restructuredtext en"
__all__ = ("PlanetarySocketBase",)


Self = TypeVar("Self", bound="PlanetarySocketBase")


class PlanetarySocketBase(_2283.CylindricalSocket):
    """PlanetarySocketBase

    This is a mastapy class.
    """

    TYPE = _PLANETARY_SOCKET_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetarySocketBase")

    class _Cast_PlanetarySocketBase:
        """Special nested class for casting PlanetarySocketBase to subclasses."""

        def __init__(
            self: "PlanetarySocketBase._Cast_PlanetarySocketBase",
            parent: "PlanetarySocketBase",
        ):
            self._parent = parent

        @property
        def cylindrical_socket(
            self: "PlanetarySocketBase._Cast_PlanetarySocketBase",
        ) -> "_2283.CylindricalSocket":
            return self._parent._cast(_2283.CylindricalSocket)

        @property
        def socket(
            self: "PlanetarySocketBase._Cast_PlanetarySocketBase",
        ) -> "_2303.Socket":
            from mastapy.system_model.connections_and_sockets import _2303

            return self._parent._cast(_2303.Socket)

        @property
        def planetary_socket(
            self: "PlanetarySocketBase._Cast_PlanetarySocketBase",
        ) -> "_2295.PlanetarySocket":
            from mastapy.system_model.connections_and_sockets import _2295

            return self._parent._cast(_2295.PlanetarySocket)

        @property
        def cycloidal_disc_planetary_bearing_socket(
            self: "PlanetarySocketBase._Cast_PlanetarySocketBase",
        ) -> "_2346.CycloidalDiscPlanetaryBearingSocket":
            from mastapy.system_model.connections_and_sockets.cycloidal import _2346

            return self._parent._cast(_2346.CycloidalDiscPlanetaryBearingSocket)

        @property
        def planetary_socket_base(
            self: "PlanetarySocketBase._Cast_PlanetarySocketBase",
        ) -> "PlanetarySocketBase":
            return self._parent

        def __getattr__(
            self: "PlanetarySocketBase._Cast_PlanetarySocketBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetarySocketBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def draw_on_lower_half_of_2d(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DrawOnLowerHalfOf2D

        if temp is None:
            return False

        return temp

    @draw_on_lower_half_of_2d.setter
    @enforce_parameter_types
    def draw_on_lower_half_of_2d(self: Self, value: "bool"):
        self.wrapped.DrawOnLowerHalfOf2D = bool(value) if value is not None else False

    @property
    def draw_on_upper_half_of_2d(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DrawOnUpperHalfOf2D

        if temp is None:
            return False

        return temp

    @draw_on_upper_half_of_2d.setter
    @enforce_parameter_types
    def draw_on_upper_half_of_2d(self: Self, value: "bool"):
        self.wrapped.DrawOnUpperHalfOf2D = bool(value) if value is not None else False

    @property
    def editable_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.EditableName

        if temp is None:
            return ""

        return temp

    @editable_name.setter
    @enforce_parameter_types
    def editable_name(self: Self, value: "str"):
        self.wrapped.EditableName = str(value) if value is not None else ""

    @property
    def planetary_load_sharing_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PlanetaryLoadSharingFactor

        if temp is None:
            return 0.0

        return temp

    @planetary_load_sharing_factor.setter
    @enforce_parameter_types
    def planetary_load_sharing_factor(self: Self, value: "float"):
        self.wrapped.PlanetaryLoadSharingFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def planetary_details(self: Self) -> "_343.PlanetaryDetail":
        """mastapy.gears.PlanetaryDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PlanetarySocketBase._Cast_PlanetarySocketBase":
        return self._Cast_PlanetarySocketBase(self)
