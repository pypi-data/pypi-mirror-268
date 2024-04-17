"""ActiveCylindricalGearSetDesignSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2518
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ACTIVE_CYLINDRICAL_GEAR_SET_DESIGN_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "ActiveCylindricalGearSetDesignSelection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.configurations import _2626


__docformat__ = "restructuredtext en"
__all__ = ("ActiveCylindricalGearSetDesignSelection",)


Self = TypeVar("Self", bound="ActiveCylindricalGearSetDesignSelection")


class ActiveCylindricalGearSetDesignSelection(_2518.ActiveGearSetDesignSelection):
    """ActiveCylindricalGearSetDesignSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_CYLINDRICAL_GEAR_SET_DESIGN_SELECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ActiveCylindricalGearSetDesignSelection"
    )

    class _Cast_ActiveCylindricalGearSetDesignSelection:
        """Special nested class for casting ActiveCylindricalGearSetDesignSelection to subclasses."""

        def __init__(
            self: "ActiveCylindricalGearSetDesignSelection._Cast_ActiveCylindricalGearSetDesignSelection",
            parent: "ActiveCylindricalGearSetDesignSelection",
        ):
            self._parent = parent

        @property
        def active_gear_set_design_selection(
            self: "ActiveCylindricalGearSetDesignSelection._Cast_ActiveCylindricalGearSetDesignSelection",
        ) -> "_2518.ActiveGearSetDesignSelection":
            return self._parent._cast(_2518.ActiveGearSetDesignSelection)

        @property
        def part_detail_selection(
            self: "ActiveCylindricalGearSetDesignSelection._Cast_ActiveCylindricalGearSetDesignSelection",
        ) -> "_2626.PartDetailSelection":
            pass

            from mastapy.system_model.part_model.configurations import _2626

            return self._parent._cast(_2626.PartDetailSelection)

        @property
        def active_cylindrical_gear_set_design_selection(
            self: "ActiveCylindricalGearSetDesignSelection._Cast_ActiveCylindricalGearSetDesignSelection",
        ) -> "ActiveCylindricalGearSetDesignSelection":
            return self._parent

        def __getattr__(
            self: "ActiveCylindricalGearSetDesignSelection._Cast_ActiveCylindricalGearSetDesignSelection",
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
        self: Self, instance_to_wrap: "ActiveCylindricalGearSetDesignSelection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_selection(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.MicroGeometrySelection

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @micro_geometry_selection.setter
    @enforce_parameter_types
    def micro_geometry_selection(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.MicroGeometrySelection = value

    @property
    def cast_to(
        self: Self,
    ) -> "ActiveCylindricalGearSetDesignSelection._Cast_ActiveCylindricalGearSetDesignSelection":
        return self._Cast_ActiveCylindricalGearSetDesignSelection(self)
