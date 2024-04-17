"""ClampedSection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CLAMPED_SECTION = python_net_import("SMT.MastaAPI.Bolts", "ClampedSection")

if TYPE_CHECKING:
    from mastapy.bolts import _1473


__docformat__ = "restructuredtext en"
__all__ = ("ClampedSection",)


Self = TypeVar("Self", bound="ClampedSection")


class ClampedSection(_0.APIBase):
    """ClampedSection

    This is a mastapy class.
    """

    TYPE = _CLAMPED_SECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClampedSection")

    class _Cast_ClampedSection:
        """Special nested class for casting ClampedSection to subclasses."""

        def __init__(
            self: "ClampedSection._Cast_ClampedSection", parent: "ClampedSection"
        ):
            self._parent = parent

        @property
        def clamped_section(
            self: "ClampedSection._Cast_ClampedSection",
        ) -> "ClampedSection":
            return self._parent

        def __getattr__(self: "ClampedSection._Cast_ClampedSection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClampedSection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def edit_material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.EditMaterial.SelectedItemName

        if temp is None:
            return ""

        return temp

    @edit_material.setter
    @enforce_parameter_types
    def edit_material(self: Self, value: "str"):
        self.wrapped.EditMaterial.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def part_thickness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PartThickness

        if temp is None:
            return 0.0

        return temp

    @part_thickness.setter
    @enforce_parameter_types
    def part_thickness(self: Self, value: "float"):
        self.wrapped.PartThickness = float(value) if value is not None else 0.0

    @property
    def material(self: Self) -> "_1473.BoltedJointMaterial":
        """mastapy.bolts.BoltedJointMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Material

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClampedSection._Cast_ClampedSection":
        return self._Cast_ClampedSection(self)
