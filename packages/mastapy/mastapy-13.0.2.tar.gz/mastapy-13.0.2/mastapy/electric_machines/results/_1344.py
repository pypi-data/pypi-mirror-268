"""ElectricMachineResultsViewable"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.electric_machines.results import _1333
from mastapy.electric_machines import _1302, _1299
from mastapy.nodal_analysis.elmer import _175
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_VIEWABLE = python_net_import(
    "SMT.MastaAPI.ElectricMachines.Results", "ElectricMachineResultsViewable"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.results import _1345
    from mastapy.utility.property import _1850


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineResultsViewable",)


Self = TypeVar("Self", bound="ElectricMachineResultsViewable")


class ElectricMachineResultsViewable(_175.ElmerResultsViewable):
    """ElectricMachineResultsViewable

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_VIEWABLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineResultsViewable")

    class _Cast_ElectricMachineResultsViewable:
        """Special nested class for casting ElectricMachineResultsViewable to subclasses."""

        def __init__(
            self: "ElectricMachineResultsViewable._Cast_ElectricMachineResultsViewable",
            parent: "ElectricMachineResultsViewable",
        ):
            self._parent = parent

        @property
        def elmer_results_viewable(
            self: "ElectricMachineResultsViewable._Cast_ElectricMachineResultsViewable",
        ) -> "_175.ElmerResultsViewable":
            return self._parent._cast(_175.ElmerResultsViewable)

        @property
        def electric_machine_results_viewable(
            self: "ElectricMachineResultsViewable._Cast_ElectricMachineResultsViewable",
        ) -> "ElectricMachineResultsViewable":
            return self._parent

        def __getattr__(
            self: "ElectricMachineResultsViewable._Cast_ElectricMachineResultsViewable",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineResultsViewable.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_view_options(self: Self) -> "_1345.ElectricMachineForceViewOptions":
        """mastapy.electric_machines.results.ElectricMachineForceViewOptions"""
        temp = self.wrapped.ForceViewOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.ElectricMachines.Results.ElectricMachineForceViewOptions",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines.results._1345", "ElectricMachineForceViewOptions"
        )(value)

    @force_view_options.setter
    @enforce_parameter_types
    def force_view_options(self: Self, value: "_1345.ElectricMachineForceViewOptions"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.Results.ElectricMachineForceViewOptions",
        )
        self.wrapped.ForceViewOptions = value

    @property
    def number_of_lines(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfLines

        if temp is None:
            return 0

        return temp

    @number_of_lines.setter
    @enforce_parameter_types
    def number_of_lines(self: Self, value: "int"):
        self.wrapped.NumberOfLines = int(value) if value is not None else 0

    @property
    def results(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ElectricMachineResults":
        """ListWithSelectedItem[mastapy.electric_machines.results.ElectricMachineResults]"""
        temp = self.wrapped.Results

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ElectricMachineResults",
        )(temp)

    @results.setter
    @enforce_parameter_types
    def results(self: Self, value: "_1333.ElectricMachineResults"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineResults.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ElectricMachineResults.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Results = value

    @property
    def show_field_lines(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowFieldLines

        if temp is None:
            return False

        return temp

    @show_field_lines.setter
    @enforce_parameter_types
    def show_field_lines(self: Self, value: "bool"):
        self.wrapped.ShowFieldLines = bool(value) if value is not None else False

    @property
    def slice(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_RotorSkewSlice":
        """ListWithSelectedItem[mastapy.electric_machines.RotorSkewSlice]"""
        temp = self.wrapped.Slice

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_RotorSkewSlice",
        )(temp)

    @slice.setter
    @enforce_parameter_types
    def slice(self: Self, value: "_1302.RotorSkewSlice"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.Slice = value

    @property
    def parts_to_view(self: Self) -> "List[_1850.EnumWithBoolean[_1299.RegionID]]":
        """List[mastapy.utility.property.EnumWithBoolean[mastapy.electric_machines.RegionID]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartsToView

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def deselect_all(self: Self):
        """Method does not return."""
        self.wrapped.DeselectAll()

    def select_all(self: Self):
        """Method does not return."""
        self.wrapped.SelectAll()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineResultsViewable._Cast_ElectricMachineResultsViewable":
        return self._Cast_ElectricMachineResultsViewable(self)
