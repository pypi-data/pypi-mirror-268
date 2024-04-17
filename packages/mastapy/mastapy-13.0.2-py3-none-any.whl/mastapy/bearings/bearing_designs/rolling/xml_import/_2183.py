"""AbstractXmlVariableAssignment"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_XML_VARIABLE_ASSIGNMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling.XmlImport",
    "AbstractXmlVariableAssignment",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling.xml_import import _2187


__docformat__ = "restructuredtext en"
__all__ = ("AbstractXmlVariableAssignment",)


Self = TypeVar("Self", bound="AbstractXmlVariableAssignment")


class AbstractXmlVariableAssignment(_0.APIBase):
    """AbstractXmlVariableAssignment

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_XML_VARIABLE_ASSIGNMENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractXmlVariableAssignment")

    class _Cast_AbstractXmlVariableAssignment:
        """Special nested class for casting AbstractXmlVariableAssignment to subclasses."""

        def __init__(
            self: "AbstractXmlVariableAssignment._Cast_AbstractXmlVariableAssignment",
            parent: "AbstractXmlVariableAssignment",
        ):
            self._parent = parent

        @property
        def xml_variable_assignment(
            self: "AbstractXmlVariableAssignment._Cast_AbstractXmlVariableAssignment",
        ) -> "_2187.XMLVariableAssignment":
            from mastapy.bearings.bearing_designs.rolling.xml_import import _2187

            return self._parent._cast(_2187.XMLVariableAssignment)

        @property
        def abstract_xml_variable_assignment(
            self: "AbstractXmlVariableAssignment._Cast_AbstractXmlVariableAssignment",
        ) -> "AbstractXmlVariableAssignment":
            return self._parent

        def __getattr__(
            self: "AbstractXmlVariableAssignment._Cast_AbstractXmlVariableAssignment",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractXmlVariableAssignment.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def definitions(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.Definitions

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @definitions.setter
    @enforce_parameter_types
    def definitions(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.Definitions = value

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
    def variable_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VariableName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractXmlVariableAssignment._Cast_AbstractXmlVariableAssignment":
        return self._Cast_AbstractXmlVariableAssignment(self)
