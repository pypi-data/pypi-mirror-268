"""Remoting"""

from __future__ import annotations

from typing import TypeVar, Iterable

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._internal.class_property import classproperty
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REMOTING = python_net_import("SMT.MastaAPIUtility", "Remoting")


__docformat__ = "restructuredtext en"
__all__ = ("Remoting",)


Self = TypeVar("Self", bound="Remoting")


class Remoting:
    """Remoting

    This is a mastapy class.
    """

    TYPE = _REMOTING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Remoting")

    class _Cast_Remoting:
        """Special nested class for casting Remoting to subclasses."""

        def __init__(self: "Remoting._Cast_Remoting", parent: "Remoting"):
            self._parent = parent

        @property
        def remoting(self: "Remoting._Cast_Remoting") -> "Remoting":
            return self._parent

        def __getattr__(self: "Remoting._Cast_Remoting", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Remoting.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @classproperty
    def masta_processes(cls) -> "Iterable[int]":
        """Iterable[int]"""
        temp = Remoting.TYPE.MastaProcesses

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_iterable(temp, int)

        if value is None:
            return None

        return value

    @classproperty
    def remote_identifier(cls) -> "str":
        """str"""
        temp = Remoting.TYPE.RemoteIdentifier

        if temp is None:
            return ""

        return temp

    @staticmethod
    @enforce_parameter_types
    def initialise(process_id: "int"):
        """Method does not return.

        Args:
            process_id (int)
        """
        process_id = int(process_id)
        Remoting.TYPE.Initialise(process_id if process_id else 0)

    @staticmethod
    def stop():
        """Method does not return."""
        Remoting.TYPE.Stop()

    @staticmethod
    @enforce_parameter_types
    def url_for_process_id(process_id: "int") -> "str":
        """str

        Args:
            process_id (int)
        """
        process_id = int(process_id)
        method_result = Remoting.TYPE.UrlForProcessId(process_id if process_id else 0)
        return method_result

    @staticmethod
    @enforce_parameter_types
    def is_remoting(process_id: "int" = 0) -> "bool":
        """bool

        Args:
            process_id (int, optional)
        """
        process_id = int(process_id)
        method_result = Remoting.TYPE.IsRemoting(process_id if process_id else 0)
        return method_result

    @staticmethod
    @enforce_parameter_types
    def is_masta_or_runna_process(process_id: "int") -> "bool":
        """bool

        Args:
            process_id (int)
        """
        process_id = int(process_id)
        method_result = Remoting.TYPE.IsMastaOrRunnaProcess(
            process_id if process_id else 0
        )
        return method_result

    @staticmethod
    @enforce_parameter_types
    def remoting_port_name(process_id: "int") -> "str":
        """str

        Args:
            process_id (int)
        """
        process_id = int(process_id)
        method_result = Remoting.TYPE.RemotingPortName(process_id if process_id else 0)
        return method_result

    @staticmethod
    def remoting_port_name_for_current_process() -> "str":
        """str"""
        method_result = Remoting.TYPE.RemotingPortNameForCurrentProcess()
        return method_result

    @property
    def cast_to(self: Self) -> "Remoting._Cast_Remoting":
        return self._Cast_Remoting(self)
