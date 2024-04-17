"""XMLVariableAssignment"""

from __future__ import annotations

from typing import TypeVar, Generic

from mastapy.bearings.bearing_designs.rolling.xml_import import _2183
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_XML_VARIABLE_ASSIGNMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.XmlImport", "XMLVariableAssignment"
)


__docformat__ = "restructuredtext en"
__all__ = ("XMLVariableAssignment",)


Self = TypeVar("Self", bound="XMLVariableAssignment")
T = TypeVar("T")


class XMLVariableAssignment(_2183.AbstractXmlVariableAssignment, Generic[T]):
    """XMLVariableAssignment

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _XML_VARIABLE_ASSIGNMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_XMLVariableAssignment")

    class _Cast_XMLVariableAssignment:
        """Special nested class for casting XMLVariableAssignment to subclasses."""

        def __init__(
            self: "XMLVariableAssignment._Cast_XMLVariableAssignment",
            parent: "XMLVariableAssignment",
        ):
            self._parent = parent

        @property
        def abstract_xml_variable_assignment(
            self: "XMLVariableAssignment._Cast_XMLVariableAssignment",
        ) -> "_2183.AbstractXmlVariableAssignment":
            return self._parent._cast(_2183.AbstractXmlVariableAssignment)

        @property
        def xml_variable_assignment(
            self: "XMLVariableAssignment._Cast_XMLVariableAssignment",
        ) -> "XMLVariableAssignment":
            return self._parent

        def __getattr__(
            self: "XMLVariableAssignment._Cast_XMLVariableAssignment", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "XMLVariableAssignment.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "XMLVariableAssignment._Cast_XMLVariableAssignment":
        return self._Cast_XMLVariableAssignment(self)
