"""CADStator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.electric_machines import _1249
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_STATOR = python_net_import("SMT.MastaAPI.ElectricMachines", "CADStator")

if TYPE_CHECKING:
    from mastapy.electric_machines import _1258


__docformat__ = "restructuredtext en"
__all__ = ("CADStator",)


Self = TypeVar("Self", bound="CADStator")


class CADStator(_1249.AbstractStator):
    """CADStator

    This is a mastapy class.
    """

    TYPE = _CAD_STATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADStator")

    class _Cast_CADStator:
        """Special nested class for casting CADStator to subclasses."""

        def __init__(self: "CADStator._Cast_CADStator", parent: "CADStator"):
            self._parent = parent

        @property
        def abstract_stator(
            self: "CADStator._Cast_CADStator",
        ) -> "_1249.AbstractStator":
            return self._parent._cast(_1249.AbstractStator)

        @property
        def cad_stator(self: "CADStator._Cast_CADStator") -> "CADStator":
            return self._parent

        def __getattr__(self: "CADStator._Cast_CADStator", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADStator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_has_unequal_notches_between_adjacent_teeth(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.DesignHasUnequalNotchesBetweenAdjacentTeeth

        if temp is None:
            return False

        return temp

    @design_has_unequal_notches_between_adjacent_teeth.setter
    @enforce_parameter_types
    def design_has_unequal_notches_between_adjacent_teeth(self: Self, value: "bool"):
        self.wrapped.DesignHasUnequalNotchesBetweenAdjacentTeeth = (
            bool(value) if value is not None else False
        )

    @property
    def importing_full_stator(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ImportingFullStator

        if temp is None:
            return False

        return temp

    @importing_full_stator.setter
    @enforce_parameter_types
    def importing_full_stator(self: Self, value: "bool"):
        self.wrapped.ImportingFullStator = bool(value) if value is not None else False

    @property
    def number_of_slots_for_imported_sector(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfSlotsForImportedSector

        if temp is None:
            return 0

        return temp

    @number_of_slots_for_imported_sector.setter
    @enforce_parameter_types
    def number_of_slots_for_imported_sector(self: Self, value: "int"):
        self.wrapped.NumberOfSlotsForImportedSector = (
            int(value) if value is not None else 0
        )

    @property
    def tooth_and_slot(self: Self) -> "_1258.CADToothAndSlot":
        """mastapy.electric_machines.CADToothAndSlot

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CADStator._Cast_CADStator":
        return self._Cast_CADStator(self)
