"""LoadedSphericalThrustRollerBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2046
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_THRUST_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalThrustRollerBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2035, _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalThrustRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedSphericalThrustRollerBearingElement")


class LoadedSphericalThrustRollerBearingElement(
    _2046.LoadedSphericalRollerBearingElement
):
    """LoadedSphericalThrustRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_THRUST_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedSphericalThrustRollerBearingElement"
    )

    class _Cast_LoadedSphericalThrustRollerBearingElement:
        """Special nested class for casting LoadedSphericalThrustRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedSphericalThrustRollerBearingElement._Cast_LoadedSphericalThrustRollerBearingElement",
            parent: "LoadedSphericalThrustRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_spherical_roller_bearing_element(
            self: "LoadedSphericalThrustRollerBearingElement._Cast_LoadedSphericalThrustRollerBearingElement",
        ) -> "_2046.LoadedSphericalRollerBearingElement":
            return self._parent._cast(_2046.LoadedSphericalRollerBearingElement)

        @property
        def loaded_roller_bearing_element(
            self: "LoadedSphericalThrustRollerBearingElement._Cast_LoadedSphericalThrustRollerBearingElement",
        ) -> "_2035.LoadedRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedSphericalThrustRollerBearingElement._Cast_LoadedSphericalThrustRollerBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(
            self: "LoadedSphericalThrustRollerBearingElement._Cast_LoadedSphericalThrustRollerBearingElement",
        ) -> "LoadedSphericalThrustRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalThrustRollerBearingElement._Cast_LoadedSphericalThrustRollerBearingElement",
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
        self: Self, instance_to_wrap: "LoadedSphericalThrustRollerBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedSphericalThrustRollerBearingElement._Cast_LoadedSphericalThrustRollerBearingElement":
        return self._Cast_LoadedSphericalThrustRollerBearingElement(self)
