"""UtilityMethods"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Callable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UTILITY_METHODS = python_net_import("SMT.MastaAPI", "UtilityMethods")

if TYPE_CHECKING:
    from mastapy import _0


__docformat__ = "restructuredtext en"
__all__ = ("UtilityMethods",)


Self = TypeVar("Self", bound="UtilityMethods")


class UtilityMethods:
    """UtilityMethods

    This is a mastapy class.
    """

    TYPE = _UTILITY_METHODS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UtilityMethods")

    class _Cast_UtilityMethods:
        """Special nested class for casting UtilityMethods to subclasses."""

        def __init__(
            self: "UtilityMethods._Cast_UtilityMethods", parent: "UtilityMethods"
        ):
            self._parent = parent

        @property
        def utility_methods(
            self: "UtilityMethods._Cast_UtilityMethods",
        ) -> "UtilityMethods":
            return self._parent

        def __getattr__(self: "UtilityMethods._Cast_UtilityMethods", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UtilityMethods.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    T_is_read_only = TypeVar("T_is_read_only", bound="_0.APIBase")

    @staticmethod
    @enforce_parameter_types
    def is_read_only(
        entity: "UtilityMethods.T_is_read_only",
        property_: "Callable[[UtilityMethods.T_is_read_only], object]",
    ) -> "bool":
        """bool

        Args:
            entity (T_is_read_only)
            property_ (Callable[[UtilityMethods.T_is_read_only], object])
        """
        method_result = UtilityMethods.TYPE.IsReadOnly(entity, property_)
        return method_result

    T_is_valid = TypeVar("T_is_valid", bound="_0.APIBase")

    @staticmethod
    @enforce_parameter_types
    def is_valid(
        entity: "UtilityMethods.T_is_valid",
        property_: "Callable[[UtilityMethods.T_is_valid], object]",
    ) -> "bool":
        """bool

        Args:
            entity (T_is_valid)
            property_ (Callable[[UtilityMethods.T_is_valid], object])
        """
        method_result = UtilityMethods.TYPE.IsValid(entity, property_)
        return method_result

    T_is_method_valid = TypeVar("T_is_method_valid", bound="_0.APIBase")

    @staticmethod
    @enforce_parameter_types
    def is_method_valid(
        entity: "UtilityMethods.T_is_method_valid",
        method: "Callable[[UtilityMethods.T_is_method_valid], Callable[..., None]]",
    ) -> "bool":
        """bool

        Args:
            entity (T_is_method_valid)
            method (Callable[[UtilityMethods.T_is_method_valid], Callable[..., None]])
        """
        method_result = UtilityMethods.TYPE.IsMethodValid(entity, method)
        return method_result

    T_is_method_read_only = TypeVar("T_is_method_read_only", bound="_0.APIBase")

    @staticmethod
    @enforce_parameter_types
    def is_method_read_only(
        entity: "UtilityMethods.T_is_method_read_only",
        method: "Callable[[UtilityMethods.T_is_method_read_only], Callable[..., None]]",
    ) -> "bool":
        """bool

        Args:
            entity (T_is_method_read_only)
            method (Callable[[UtilityMethods.T_is_method_read_only], Callable[..., None]])
        """
        method_result = UtilityMethods.TYPE.IsMethodReadOnly(entity, method)
        return method_result

    @staticmethod
    @enforce_parameter_types
    def initialise_api_access(installation_directory: "str"):
        """Method does not return.

        Args:
            installation_directory (str)
        """
        installation_directory = str(installation_directory)
        UtilityMethods.TYPE.InitialiseApiAccess(
            installation_directory if installation_directory else ""
        )

    @staticmethod
    def initialise_dot_net_program_access():
        """Method does not return."""
        UtilityMethods.TYPE.InitialiseDotNetProgramAccess()

    @property
    def cast_to(self: Self) -> "UtilityMethods._Cast_UtilityMethods":
        return self._Cast_UtilityMethods(self)
