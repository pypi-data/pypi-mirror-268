"""LoadedSphericalRollerBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2035
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_SPHERICAL_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSphericalRollerBearingElement",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2045, _2052, _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSphericalRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedSphericalRollerBearingElement")


class LoadedSphericalRollerBearingElement(_2035.LoadedRollerBearingElement):
    """LoadedSphericalRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_SPHERICAL_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedSphericalRollerBearingElement")

    class _Cast_LoadedSphericalRollerBearingElement:
        """Special nested class for casting LoadedSphericalRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
            parent: "LoadedSphericalRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "_2035.LoadedRollerBearingElement":
            return self._parent._cast(_2035.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_spherical_radial_roller_bearing_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "_2045.LoadedSphericalRadialRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2045

            return self._parent._cast(_2045.LoadedSphericalRadialRollerBearingElement)

        @property
        def loaded_spherical_thrust_roller_bearing_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "_2052.LoadedSphericalThrustRollerBearingElement":
            from mastapy.bearings.bearing_results.rolling import _2052

            return self._parent._cast(_2052.LoadedSphericalThrustRollerBearingElement)

        @property
        def loaded_spherical_roller_bearing_element(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
        ) -> "LoadedSphericalRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement",
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
        self: Self, instance_to_wrap: "LoadedSphericalRollerBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "LoadedSphericalRollerBearingElement._Cast_LoadedSphericalRollerBearingElement"
    ):
        return self._Cast_LoadedSphericalRollerBearingElement(self)
