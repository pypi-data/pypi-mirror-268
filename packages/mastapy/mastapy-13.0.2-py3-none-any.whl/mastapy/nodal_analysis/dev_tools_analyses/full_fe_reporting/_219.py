"""ElementPropertiesWithMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_WITH_MATERIAL = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementPropertiesWithMaterial",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
        _212,
        _216,
        _217,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesWithMaterial",)


Self = TypeVar("Self", bound="ElementPropertiesWithMaterial")


class ElementPropertiesWithMaterial(_211.ElementPropertiesBase):
    """ElementPropertiesWithMaterial

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_WITH_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementPropertiesWithMaterial")

    class _Cast_ElementPropertiesWithMaterial:
        """Special nested class for casting ElementPropertiesWithMaterial to subclasses."""

        def __init__(
            self: "ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial",
            parent: "ElementPropertiesWithMaterial",
        ):
            self._parent = parent

        @property
        def element_properties_base(
            self: "ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial",
        ) -> "_211.ElementPropertiesBase":
            return self._parent._cast(_211.ElementPropertiesBase)

        @property
        def element_properties_beam(
            self: "ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial",
        ) -> "_212.ElementPropertiesBeam":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _212

            return self._parent._cast(_212.ElementPropertiesBeam)

        @property
        def element_properties_shell(
            self: "ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial",
        ) -> "_216.ElementPropertiesShell":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _216

            return self._parent._cast(_216.ElementPropertiesShell)

        @property
        def element_properties_solid(
            self: "ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial",
        ) -> "_217.ElementPropertiesSolid":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _217

            return self._parent._cast(_217.ElementPropertiesSolid)

        @property
        def element_properties_with_material(
            self: "ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial",
        ) -> "ElementPropertiesWithMaterial":
            return self._parent

        def __getattr__(
            self: "ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementPropertiesWithMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def material_coordinate_system_id(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.MaterialCoordinateSystemID

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @material_coordinate_system_id.setter
    @enforce_parameter_types
    def material_coordinate_system_id(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.MaterialCoordinateSystemID = value

    @property
    def material_id(self: Self) -> "list_with_selected_item.ListWithSelectedItem_int":
        """ListWithSelectedItem[int]"""
        temp = self.wrapped.MaterialID

        if temp is None:
            return 0

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_int",
        )(temp)

    @material_id.setter
    @enforce_parameter_types
    def material_id(self: Self, value: "int"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_int.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_int.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0
        )
        self.wrapped.MaterialID = value

    @property
    def cast_to(
        self: Self,
    ) -> "ElementPropertiesWithMaterial._Cast_ElementPropertiesWithMaterial":
        return self._Cast_ElementPropertiesWithMaterial(self)
