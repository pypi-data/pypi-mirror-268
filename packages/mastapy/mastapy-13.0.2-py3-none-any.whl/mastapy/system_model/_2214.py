"""DutyCycleImporterDesignEntityMatch"""

from __future__ import annotations

from typing import TypeVar, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_IMPORTER_DESIGN_ENTITY_MATCH = python_net_import(
    "SMT.MastaAPI.SystemModel", "DutyCycleImporterDesignEntityMatch"
)


__docformat__ = "restructuredtext en"
__all__ = ("DutyCycleImporterDesignEntityMatch",)


Self = TypeVar("Self", bound="DutyCycleImporterDesignEntityMatch")
T = TypeVar("T")


class DutyCycleImporterDesignEntityMatch(_0.APIBase, Generic[T]):
    """DutyCycleImporterDesignEntityMatch

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DUTY_CYCLE_IMPORTER_DESIGN_ENTITY_MATCH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DutyCycleImporterDesignEntityMatch")

    class _Cast_DutyCycleImporterDesignEntityMatch:
        """Special nested class for casting DutyCycleImporterDesignEntityMatch to subclasses."""

        def __init__(
            self: "DutyCycleImporterDesignEntityMatch._Cast_DutyCycleImporterDesignEntityMatch",
            parent: "DutyCycleImporterDesignEntityMatch",
        ):
            self._parent = parent

        @property
        def duty_cycle_importer_design_entity_match(
            self: "DutyCycleImporterDesignEntityMatch._Cast_DutyCycleImporterDesignEntityMatch",
        ) -> "DutyCycleImporterDesignEntityMatch":
            return self._parent

        def __getattr__(
            self: "DutyCycleImporterDesignEntityMatch._Cast_DutyCycleImporterDesignEntityMatch",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "DutyCycleImporterDesignEntityMatch.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def destination(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.Destination

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @destination.setter
    @enforce_parameter_types
    def destination(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.Destination = value

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
    def cast_to(
        self: Self,
    ) -> "DutyCycleImporterDesignEntityMatch._Cast_DutyCycleImporterDesignEntityMatch":
        return self._Cast_DutyCycleImporterDesignEntityMatch(self)
