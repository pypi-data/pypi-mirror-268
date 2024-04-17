"""PartDetailConfiguration"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_DETAIL_CONFIGURATION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Configurations", "PartDetailConfiguration"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2475
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.part_model.configurations import _2620, _2622, _2623


__docformat__ = "restructuredtext en"
__all__ = ("PartDetailConfiguration",)


Self = TypeVar("Self", bound="PartDetailConfiguration")
TPartDetailSelection = TypeVar("TPartDetailSelection")
TPart = TypeVar("TPart", bound="_2475.Part")
TSelectableItem = TypeVar("TSelectableItem")


class PartDetailConfiguration(
    _0.APIBase, Generic[TPartDetailSelection, TPart, TSelectableItem]
):
    """PartDetailConfiguration

    This is a mastapy class.

    Generic Types:
        TPartDetailSelection
        TPart
        TSelectableItem
    """

    TYPE = _PART_DETAIL_CONFIGURATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartDetailConfiguration")

    class _Cast_PartDetailConfiguration:
        """Special nested class for casting PartDetailConfiguration to subclasses."""

        def __init__(
            self: "PartDetailConfiguration._Cast_PartDetailConfiguration",
            parent: "PartDetailConfiguration",
        ):
            self._parent = parent

        @property
        def active_gear_set_design_selection_group(
            self: "PartDetailConfiguration._Cast_PartDetailConfiguration",
        ) -> "_2519.ActiveGearSetDesignSelectionGroup":
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.ActiveGearSetDesignSelectionGroup)

        @property
        def active_fe_substructure_selection_group(
            self: "PartDetailConfiguration._Cast_PartDetailConfiguration",
        ) -> "_2620.ActiveFESubstructureSelectionGroup":
            from mastapy.system_model.part_model.configurations import _2620

            return self._parent._cast(_2620.ActiveFESubstructureSelectionGroup)

        @property
        def active_shaft_design_selection_group(
            self: "PartDetailConfiguration._Cast_PartDetailConfiguration",
        ) -> "_2622.ActiveShaftDesignSelectionGroup":
            from mastapy.system_model.part_model.configurations import _2622

            return self._parent._cast(_2622.ActiveShaftDesignSelectionGroup)

        @property
        def bearing_detail_configuration(
            self: "PartDetailConfiguration._Cast_PartDetailConfiguration",
        ) -> "_2623.BearingDetailConfiguration":
            from mastapy.system_model.part_model.configurations import _2623

            return self._parent._cast(_2623.BearingDetailConfiguration)

        @property
        def part_detail_configuration(
            self: "PartDetailConfiguration._Cast_PartDetailConfiguration",
        ) -> "PartDetailConfiguration":
            return self._parent

        def __getattr__(
            self: "PartDetailConfiguration._Cast_PartDetailConfiguration", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartDetailConfiguration.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_selected(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsSelected

        if temp is None:
            return False

        return temp

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def selections(self: Self) -> "List[TPartDetailSelection]":
        """List[TPartDetailSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Selections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def delete_configuration(self: Self):
        """Method does not return."""
        self.wrapped.DeleteConfiguration()

    def select_configuration(self: Self):
        """Method does not return."""
        self.wrapped.SelectConfiguration()

    @property
    def cast_to(self: Self) -> "PartDetailConfiguration._Cast_PartDetailConfiguration":
        return self._Cast_PartDetailConfiguration(self)
