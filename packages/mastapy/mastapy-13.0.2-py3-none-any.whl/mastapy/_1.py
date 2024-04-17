"""Initialiser"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INITIALISER = python_net_import("SMT.MastaAPI", "Initialiser")


__docformat__ = "restructuredtext en"
__all__ = ("Initialiser",)


Self = TypeVar("Self", bound="Initialiser")


class Initialiser:
    """Initialiser

    This is a mastapy class.
    """

    TYPE = _INITIALISER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Initialiser")

    class _Cast_Initialiser:
        """Special nested class for casting Initialiser to subclasses."""

        def __init__(self: "Initialiser._Cast_Initialiser", parent: "Initialiser"):
            self._parent = parent

        @property
        def initialiser(self: "Initialiser._Cast_Initialiser") -> "Initialiser":
            return self._parent

        def __getattr__(self: "Initialiser._Cast_Initialiser", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Initialiser.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1
        self._freeze()

    __frozen = False

    def __setattr__(self: Self, attr, value):
        prop = getattr(self.__class__, attr, None)
        if isinstance(prop, property):
            prop.fset(self, value)
        else:
            if self.__frozen and attr not in self.__dict__:
                raise AttributeError(
                    ("Attempted to set unknown " "attribute: '{}'".format(attr))
                ) from None

            super().__setattr__(attr, value)

    def __delattr__(self: Self, name: str):
        raise AttributeError(
            "Cannot delete the attributes of a mastapy object."
        ) from None

    def _freeze(self: Self):
        self.__frozen = True

    @enforce_parameter_types
    def initialise_api_access(self: Self, installation_directory: "str"):
        """Method does not return.

        Args:
            installation_directory (str)
        """
        installation_directory = str(installation_directory)
        self.wrapped.InitialiseApiAccess(
            installation_directory if installation_directory else ""
        )

    @property
    def cast_to(self: Self) -> "Initialiser._Cast_Initialiser":
        return self._Cast_Initialiser(self)
