"""PythonUtility"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.class_property import classproperty
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PYTHON_UTILITY = python_net_import("SMT.MastaAPI", "PythonUtility")


__docformat__ = "restructuredtext en"
__all__ = ("PythonUtility",)


Self = TypeVar("Self", bound="PythonUtility")


class PythonUtility:
    """PythonUtility

    This is a mastapy class.
    """

    TYPE = _PYTHON_UTILITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PythonUtility")

    class _Cast_PythonUtility:
        """Special nested class for casting PythonUtility to subclasses."""

        def __init__(
            self: "PythonUtility._Cast_PythonUtility", parent: "PythonUtility"
        ):
            self._parent = parent

        @property
        def python_utility(
            self: "PythonUtility._Cast_PythonUtility",
        ) -> "PythonUtility":
            return self._parent

        def __getattr__(self: "PythonUtility._Cast_PythonUtility", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PythonUtility.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @classproperty
    def python_install_directory(cls) -> "str":
        """str"""
        temp = PythonUtility.TYPE.PythonInstallDirectory

        if temp is None:
            return ""

        return temp

    @python_install_directory.setter
    @enforce_parameter_types
    def python_install_directory(cls, value: "str"):
        PythonUtility.TYPE.PythonInstallDirectory = (
            str(value) if value is not None else ""
        )

    @property
    def cast_to(self: Self) -> "PythonUtility._Cast_PythonUtility":
        return self._Cast_PythonUtility(self)
