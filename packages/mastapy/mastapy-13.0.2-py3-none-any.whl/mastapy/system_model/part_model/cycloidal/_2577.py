"""RingPins"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model import _2471
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_RING_PINS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "RingPins"
)

if TYPE_CHECKING:
    from mastapy.cycloidal import _1469, _1470
    from mastapy.system_model.part_model import _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("RingPins",)


Self = TypeVar("Self", bound="RingPins")


class RingPins(_2471.MountableComponent):
    """RingPins

    This is a mastapy class.
    """

    TYPE = _RING_PINS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPins")

    class _Cast_RingPins:
        """Special nested class for casting RingPins to subclasses."""

        def __init__(self: "RingPins._Cast_RingPins", parent: "RingPins"):
            self._parent = parent

        @property
        def mountable_component(
            self: "RingPins._Cast_RingPins",
        ) -> "_2471.MountableComponent":
            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(self: "RingPins._Cast_RingPins") -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "RingPins._Cast_RingPins") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "RingPins._Cast_RingPins") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def ring_pins(self: "RingPins._Cast_RingPins") -> "RingPins":
            return self._parent

        def __getattr__(self: "RingPins._Cast_RingPins", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPins.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def ring_pins_material_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.RingPinsMaterialDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @ring_pins_material_database.setter
    @enforce_parameter_types
    def ring_pins_material_database(self: Self, value: "str"):
        self.wrapped.RingPinsMaterialDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def ring_pins_design(self: Self) -> "_1469.RingPinsDesign":
        """mastapy.cycloidal.RingPinsDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPinsDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_pins_material(self: Self) -> "_1470.RingPinsMaterial":
        """mastapy.cycloidal.RingPinsMaterial

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingPinsMaterial

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RingPins._Cast_RingPins":
        return self._Cast_RingPins(self)
