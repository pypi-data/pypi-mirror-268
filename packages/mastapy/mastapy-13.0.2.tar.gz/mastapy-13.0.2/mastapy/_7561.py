"""MarshalByRefObjectPermanent"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MARSHAL_BY_REF_OBJECT_PERMANENT = python_net_import(
    "SMT.MastaAPIUtility", "MarshalByRefObjectPermanent"
)


__docformat__ = "restructuredtext en"
__all__ = ("MarshalByRefObjectPermanent",)


Self = TypeVar("Self", bound="MarshalByRefObjectPermanent")


class MarshalByRefObjectPermanent:
    """MarshalByRefObjectPermanent

    This is a mastapy class.
    """

    TYPE = _MARSHAL_BY_REF_OBJECT_PERMANENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MarshalByRefObjectPermanent")

    class _Cast_MarshalByRefObjectPermanent:
        """Special nested class for casting MarshalByRefObjectPermanent to subclasses."""

        def __init__(
            self: "MarshalByRefObjectPermanent._Cast_MarshalByRefObjectPermanent",
            parent: "MarshalByRefObjectPermanent",
        ):
            self._parent = parent

        @property
        def marshal_by_ref_object_permanent(
            self: "MarshalByRefObjectPermanent._Cast_MarshalByRefObjectPermanent",
        ) -> "MarshalByRefObjectPermanent":
            return self._parent

        def __getattr__(
            self: "MarshalByRefObjectPermanent._Cast_MarshalByRefObjectPermanent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MarshalByRefObjectPermanent.TYPE"):
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

    def initialize_lifetime_service(self: Self) -> "object":
        """object"""
        method_result = self.wrapped.InitializeLifetimeService()
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "MarshalByRefObjectPermanent._Cast_MarshalByRefObjectPermanent":
        return self._Cast_MarshalByRefObjectPermanent(self)
