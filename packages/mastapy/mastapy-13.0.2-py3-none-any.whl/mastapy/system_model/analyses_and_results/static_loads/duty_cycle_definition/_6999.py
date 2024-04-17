"""DesignStateOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.analyses_and_results.load_case_groups import _5671
from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DESIGN_STATE_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "DesignStateOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model import _2214


__docformat__ = "restructuredtext en"
__all__ = ("DesignStateOptions",)


Self = TypeVar("Self", bound="DesignStateOptions")


class DesignStateOptions(_1854.ColumnInputOptions):
    """DesignStateOptions

    This is a mastapy class.
    """

    TYPE = _DESIGN_STATE_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DesignStateOptions")

    class _Cast_DesignStateOptions:
        """Special nested class for casting DesignStateOptions to subclasses."""

        def __init__(
            self: "DesignStateOptions._Cast_DesignStateOptions",
            parent: "DesignStateOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "DesignStateOptions._Cast_DesignStateOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def design_state_options(
            self: "DesignStateOptions._Cast_DesignStateOptions",
        ) -> "DesignStateOptions":
            return self._parent

        def __getattr__(self: "DesignStateOptions._Cast_DesignStateOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DesignStateOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def create_new_design_state(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CreateNewDesignState

        if temp is None:
            return False

        return temp

    @create_new_design_state.setter
    @enforce_parameter_types
    def create_new_design_state(self: Self, value: "bool"):
        self.wrapped.CreateNewDesignState = bool(value) if value is not None else False

    @property
    def design_state(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_DesignState":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.load_case_groups.DesignState]"""
        temp = self.wrapped.DesignState

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_DesignState",
        )(temp)

    @design_state.setter
    @enforce_parameter_types
    def design_state(self: Self, value: "_5671.DesignState"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_DesignState.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_DesignState.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.DesignState = value

    @property
    def design_state_destinations(
        self: Self,
    ) -> "List[_2214.DutyCycleImporterDesignEntityMatch[_5671.DesignState]]":
        """List[mastapy.system_model.DutyCycleImporterDesignEntityMatch[mastapy.system_model.analyses_and_results.load_case_groups.DesignState]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignStateDestinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "DesignStateOptions._Cast_DesignStateOptions":
        return self._Cast_DesignStateOptions(self)
