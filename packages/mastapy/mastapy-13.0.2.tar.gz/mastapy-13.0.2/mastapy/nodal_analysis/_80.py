"""NodalMatrixEditorWrapper"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.utility.units_and_measurements import _1617
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_MATRIX_EDITOR_WRAPPER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "NodalMatrixEditorWrapper"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _81, _82


__docformat__ = "restructuredtext en"
__all__ = ("NodalMatrixEditorWrapper",)


Self = TypeVar("Self", bound="NodalMatrixEditorWrapper")


class NodalMatrixEditorWrapper(_0.APIBase):
    """NodalMatrixEditorWrapper

    This is a mastapy class.
    """

    TYPE = _NODAL_MATRIX_EDITOR_WRAPPER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalMatrixEditorWrapper")

    class _Cast_NodalMatrixEditorWrapper:
        """Special nested class for casting NodalMatrixEditorWrapper to subclasses."""

        def __init__(
            self: "NodalMatrixEditorWrapper._Cast_NodalMatrixEditorWrapper",
            parent: "NodalMatrixEditorWrapper",
        ):
            self._parent = parent

        @property
        def nodal_matrix_editor_wrapper_concept_coupling_stiffness(
            self: "NodalMatrixEditorWrapper._Cast_NodalMatrixEditorWrapper",
        ) -> "_82.NodalMatrixEditorWrapperConceptCouplingStiffness":
            from mastapy.nodal_analysis import _82

            return self._parent._cast(
                _82.NodalMatrixEditorWrapperConceptCouplingStiffness
            )

        @property
        def nodal_matrix_editor_wrapper(
            self: "NodalMatrixEditorWrapper._Cast_NodalMatrixEditorWrapper",
        ) -> "NodalMatrixEditorWrapper":
            return self._parent

        def __getattr__(
            self: "NodalMatrixEditorWrapper._Cast_NodalMatrixEditorWrapper", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalMatrixEditorWrapper.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_units(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.DistanceUnits

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @distance_units.setter
    @enforce_parameter_types
    def distance_units(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.DistanceUnits = value

    @property
    def force_units(self: Self) -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = self.wrapped.ForceUnits

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @force_units.setter
    @enforce_parameter_types
    def force_units(self: Self, value: "_1617.Unit"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.ForceUnits = value

    @property
    def columns(self: Self) -> "List[_81.NodalMatrixEditorWrapperColumn]":
        """List[mastapy.nodal_analysis.NodalMatrixEditorWrapperColumn]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Columns

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "NodalMatrixEditorWrapper._Cast_NodalMatrixEditorWrapper":
        return self._Cast_NodalMatrixEditorWrapper(self)
