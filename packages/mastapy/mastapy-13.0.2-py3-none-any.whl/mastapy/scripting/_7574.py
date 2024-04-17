"""MastaPropertyAttribute"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASTA_PROPERTY_ATTRIBUTE = python_net_import(
    "SMT.MastaAPIUtility.Scripting", "MastaPropertyAttribute"
)

if TYPE_CHECKING:
    from mastapy.units_and_measurements import _7568


__docformat__ = "restructuredtext en"
__all__ = ("MastaPropertyAttribute",)


Self = TypeVar("Self", bound="MastaPropertyAttribute")


class MastaPropertyAttribute:
    """MastaPropertyAttribute

    This is a mastapy class.
    """

    TYPE = _MASTA_PROPERTY_ATTRIBUTE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MastaPropertyAttribute")

    class _Cast_MastaPropertyAttribute:
        """Special nested class for casting MastaPropertyAttribute to subclasses."""

        def __init__(
            self: "MastaPropertyAttribute._Cast_MastaPropertyAttribute",
            parent: "MastaPropertyAttribute",
        ):
            self._parent = parent

        @property
        def masta_property_attribute(
            self: "MastaPropertyAttribute._Cast_MastaPropertyAttribute",
        ) -> "MastaPropertyAttribute":
            return self._parent

        def __getattr__(
            self: "MastaPropertyAttribute._Cast_MastaPropertyAttribute", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MastaPropertyAttribute.TYPE"):
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

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def description(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Description

        if temp is None:
            return ""

        return temp

    @property
    def symbol(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Symbol

        if temp is None:
            return ""

        return temp

    @property
    def measurement(self: Self) -> "_7568.MeasurementType":
        """mastapy.units_and_measurements.MeasurementType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Measurement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPIUtility.UnitsAndMeasurements.MeasurementType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.units_and_measurements._7568", "MeasurementType"
        )(value)

    @property
    def cast_to(self: Self) -> "MastaPropertyAttribute._Cast_MastaPropertyAttribute":
        return self._Cast_MastaPropertyAttribute(self)
