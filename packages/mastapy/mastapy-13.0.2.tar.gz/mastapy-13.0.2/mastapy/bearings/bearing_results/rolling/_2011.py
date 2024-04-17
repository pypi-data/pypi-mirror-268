"""LoadedCrossedRollerBearingElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results.rolling import _2035
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_CROSSED_ROLLER_BEARING_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedCrossedRollerBearingElement"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _2021


__docformat__ = "restructuredtext en"
__all__ = ("LoadedCrossedRollerBearingElement",)


Self = TypeVar("Self", bound="LoadedCrossedRollerBearingElement")


class LoadedCrossedRollerBearingElement(_2035.LoadedRollerBearingElement):
    """LoadedCrossedRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_CROSSED_ROLLER_BEARING_ELEMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedCrossedRollerBearingElement")

    class _Cast_LoadedCrossedRollerBearingElement:
        """Special nested class for casting LoadedCrossedRollerBearingElement to subclasses."""

        def __init__(
            self: "LoadedCrossedRollerBearingElement._Cast_LoadedCrossedRollerBearingElement",
            parent: "LoadedCrossedRollerBearingElement",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_element(
            self: "LoadedCrossedRollerBearingElement._Cast_LoadedCrossedRollerBearingElement",
        ) -> "_2035.LoadedRollerBearingElement":
            return self._parent._cast(_2035.LoadedRollerBearingElement)

        @property
        def loaded_element(
            self: "LoadedCrossedRollerBearingElement._Cast_LoadedCrossedRollerBearingElement",
        ) -> "_2021.LoadedElement":
            from mastapy.bearings.bearing_results.rolling import _2021

            return self._parent._cast(_2021.LoadedElement)

        @property
        def loaded_crossed_roller_bearing_element(
            self: "LoadedCrossedRollerBearingElement._Cast_LoadedCrossedRollerBearingElement",
        ) -> "LoadedCrossedRollerBearingElement":
            return self._parent

        def __getattr__(
            self: "LoadedCrossedRollerBearingElement._Cast_LoadedCrossedRollerBearingElement",
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
        self: Self, instance_to_wrap: "LoadedCrossedRollerBearingElement.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedCrossedRollerBearingElement._Cast_LoadedCrossedRollerBearingElement":
        return self._Cast_LoadedCrossedRollerBearingElement(self)
