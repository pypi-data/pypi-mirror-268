"""EnvironmentVariableUtility"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ENVIRONMENT_VARIABLE_UTILITY = python_net_import(
    "SMT.MastaAPIUtility", "EnvironmentVariableUtility"
)


__docformat__ = "restructuredtext en"
__all__ = ("EnvironmentVariableUtility",)


Self = TypeVar("Self", bound="EnvironmentVariableUtility")


class EnvironmentVariableUtility:
    """EnvironmentVariableUtility

    This is a mastapy class.
    """

    TYPE = _ENVIRONMENT_VARIABLE_UTILITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EnvironmentVariableUtility")

    class _Cast_EnvironmentVariableUtility:
        """Special nested class for casting EnvironmentVariableUtility to subclasses."""

        def __init__(
            self: "EnvironmentVariableUtility._Cast_EnvironmentVariableUtility",
            parent: "EnvironmentVariableUtility",
        ):
            self._parent = parent

        @property
        def environment_variable_utility(
            self: "EnvironmentVariableUtility._Cast_EnvironmentVariableUtility",
        ) -> "EnvironmentVariableUtility":
            return self._parent

        def __getattr__(
            self: "EnvironmentVariableUtility._Cast_EnvironmentVariableUtility",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EnvironmentVariableUtility.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    @enforce_parameter_types
    def add_to_path_if_necessary(directory: "str"):
        """Method does not return.

        Args:
            directory (str)
        """
        directory = str(directory)
        EnvironmentVariableUtility.TYPE.AddToPathIfNecessary(
            directory if directory else ""
        )

    @property
    def cast_to(
        self: Self,
    ) -> "EnvironmentVariableUtility._Cast_EnvironmentVariableUtility":
        return self._Cast_EnvironmentVariableUtility(self)
