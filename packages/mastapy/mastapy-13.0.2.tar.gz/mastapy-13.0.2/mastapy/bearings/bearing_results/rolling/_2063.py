"""LoadedToroidalRollerBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.bearings.bearing_results.rolling import _2035
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TOROIDAL_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedToroidalRollerBearingElement"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedToroidalRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedToroidalRollerBearingElement")


class LoadedToroidalRollerBearingElement(_2035.LoadedRollerBearingElement):
    """LoadedToroidalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_TOROIDAL_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedToroidalRollerBearingElement")

    class _Cast_LoadedToroidalRollerBearingElement:
        """Special nested class for casting LoadedToroidalRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedToroidalRollerBearingElement._Cast_LoadedToroidalRollerBearingElement",
            parent: "LoadedToroidalRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(
            self: "LoadedToroidalRollerBearingElement._Cast_LoadedToroidalRollerBearingElement",
        ) -> "_2035.LoadedRollerBearingElement":
            return self._parent._cast(_2035.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedToroidalRollerBearingElement._Cast_LoadedToroidalRollerBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_toroidal_roller_bearing_element(
            self: "LoadedToroidalRollerBearingElement._Cast_LoadedToroidalRollerBearingElement",
        ) -> "LoadedToroidalRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedToroidalRollerBearingElement._Cast_LoadedToroidalRollerBearingElement",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "LoadedToroidalRollerBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ContactAngle

        if temp is None:
            return 0.0

        return temp

    @contact_angle.setter
    @enforce_parameter_types
    def contact_angle(self: Self, value: "float"):
        self.wrapped.ContactAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedToroidalRollerBearingElement._Cast_LoadedToroidalRollerBearingElement":
        return self._Cast_LoadedToroidalRollerBearingElement(self)
