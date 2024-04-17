"""ExcelSheetDesignStateSelector"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXCEL_SHEET_DESIGN_STATE_SELECTOR = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DutyCycles.ExcelBatchDutyCycles",
    "ExcelSheetDesignStateSelector",
)


__docformat__ = "restructuredtext en"
__all__ = ("ExcelSheetDesignStateSelector",)


Self = TypeVar("Self", bound="ExcelSheetDesignStateSelector")


class ExcelSheetDesignStateSelector(_0.APIBase):
    """ExcelSheetDesignStateSelector

    This is a mastapy class.
    """

    TYPE = _EXCEL_SHEET_DESIGN_STATE_SELECTOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExcelSheetDesignStateSelector")

    class _Cast_ExcelSheetDesignStateSelector:
        """Special nested class for casting ExcelSheetDesignStateSelector to subclasses."""

        def __init__(
            self: "ExcelSheetDesignStateSelector._Cast_ExcelSheetDesignStateSelector",
            parent: "ExcelSheetDesignStateSelector",
        ):
            self._parent = parent

        @property
        def excel_sheet_design_state_selector(
            self: "ExcelSheetDesignStateSelector._Cast_ExcelSheetDesignStateSelector",
        ) -> "ExcelSheetDesignStateSelector":
            return self._parent

        def __getattr__(
            self: "ExcelSheetDesignStateSelector._Cast_ExcelSheetDesignStateSelector",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExcelSheetDesignStateSelector.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_state(self: Self) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.DesignState

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @design_state.setter
    @enforce_parameter_types
    def design_state(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.DesignState = value

    @property
    def sheet_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SheetName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ExcelSheetDesignStateSelector._Cast_ExcelSheetDesignStateSelector":
        return self._Cast_ExcelSheetDesignStateSelector(self)
