"""MarshalByRefObjects"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MARSHAL_BY_REF_OBJECTS = python_net_import(
    "SMT.MastaAPIUtility", "MarshalByRefObjects"
)


__docformat__ = "restructuredtext en"
__all__ = ("MarshalByRefObjects",)


Self = TypeVar("Self", bound="MarshalByRefObjects")


class MarshalByRefObjects:
    """MarshalByRefObjects

    This is a mastapy class.
    """

    TYPE = _MARSHAL_BY_REF_OBJECTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MarshalByRefObjects")

    class _Cast_MarshalByRefObjects:
        """Special nested class for casting MarshalByRefObjects to subclasses."""

        def __init__(
            self: "MarshalByRefObjects._Cast_MarshalByRefObjects",
            parent: "MarshalByRefObjects",
        ):
            self._parent = parent

        @property
        def marshal_by_ref_objects(
            self: "MarshalByRefObjects._Cast_MarshalByRefObjects",
        ) -> "MarshalByRefObjects":
            return self._parent

        def __getattr__(
            self: "MarshalByRefObjects._Cast_MarshalByRefObjects", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MarshalByRefObjects.TYPE"):
        self.wrapped = instance_to_wrap
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0
        self.wrapped.reference_count += 1

    @staticmethod
    @enforce_parameter_types
    def add(item: "object"):
        """Method does not return.

        Args:
            item (object)
        """
        MarshalByRefObjects.TYPE.Add(item)

    @staticmethod
    @enforce_parameter_types
    def remove(item: "object"):
        """Method does not return.

        Args:
            item (object)
        """
        MarshalByRefObjects.TYPE.Remove(item)

    @staticmethod
    @enforce_parameter_types
    def disconnect(item: "object"):
        """Method does not return.

        Args:
            item (object)
        """
        MarshalByRefObjects.TYPE.Disconnect(item)

    @staticmethod
    def clear():
        """Method does not return."""
        MarshalByRefObjects.TYPE.Clear()

    @property
    def cast_to(self: Self) -> "MarshalByRefObjects._Cast_MarshalByRefObjects":
        return self._Cast_MarshalByRefObjects(self)
