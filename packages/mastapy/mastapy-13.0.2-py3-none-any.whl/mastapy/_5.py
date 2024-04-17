"""Versioning"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.class_property import classproperty
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VERSIONING = python_net_import("SMT.MastaAPI", "Versioning")


__docformat__ = "restructuredtext en"
__all__ = ("Versioning",)


Self = TypeVar("Self", bound="Versioning")


class Versioning:
    """Versioning

    This is a mastapy class.
    """

    TYPE = _VERSIONING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Versioning")

    class _Cast_Versioning:
        """Special nested class for casting Versioning to subclasses."""

        def __init__(self: "Versioning._Cast_Versioning", parent: "Versioning"):
            self._parent = parent

        @property
        def versioning(self: "Versioning._Cast_Versioning") -> "Versioning":
            return self._parent

        def __getattr__(self: "Versioning._Cast_Versioning", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Versioning.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @classproperty
    def api_release_version_string(cls) -> "str":
        """str"""
        temp = Versioning.TYPE.APIReleaseVersionString

        if temp is None:
            return ""

        return temp

    @classproperty
    def masta_version_string(cls) -> "str":
        """str"""
        temp = Versioning.TYPE.MastaVersionString

        if temp is None:
            return ""

        return temp

    @classproperty
    def is_backwards_compatible_case(cls) -> "bool":
        """bool"""
        temp = Versioning.TYPE.IsBackwardsCompatibleCase

        if temp is None:
            return False

        return temp

    @property
    def cast_to(self: Self) -> "Versioning._Cast_Versioning":
        return self._Cast_Versioning(self)
