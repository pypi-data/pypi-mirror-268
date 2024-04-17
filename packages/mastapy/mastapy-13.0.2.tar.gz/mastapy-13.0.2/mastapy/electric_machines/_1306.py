"""Stator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1249
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATOR = python_net_import("SMT.MastaAPI.ElectricMachines", "Stator")

if TYPE_CHECKING:
    from mastapy.electric_machines import _1307, _1313


__docformat__ = "restructuredtext en"
__all__ = ("Stator",)


Self = TypeVar("Self", bound="Stator")


class Stator(_1249.AbstractStator):
    """Stator

    This is a mastapy class.
    """

    TYPE = _STATOR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Stator")

    class _Cast_Stator:
        """Special nested class for casting Stator to subclasses."""

        def __init__(self: "Stator._Cast_Stator", parent: "Stator"):
            self._parent = parent

        @property
        def abstract_stator(self: "Stator._Cast_Stator") -> "_1249.AbstractStator":
            return self._parent._cast(_1249.AbstractStator)

        @property
        def stator(self: "Stator._Cast_Stator") -> "Stator":
            return self._parent

        def __getattr__(self: "Stator._Cast_Stator", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Stator.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_stator_cut_out_specifications(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfStatorCutOutSpecifications

        if temp is None:
            return 0

        return temp

    @number_of_stator_cut_out_specifications.setter
    @enforce_parameter_types
    def number_of_stator_cut_out_specifications(self: Self, value: "int"):
        self.wrapped.NumberOfStatorCutOutSpecifications = (
            int(value) if value is not None else 0
        )

    @property
    def radius_at_mid_coil_height(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusAtMidCoilHeight

        if temp is None:
            return 0.0

        return temp

    @property
    def stator_cut_out_specifications(
        self: Self,
    ) -> "List[_1307.StatorCutOutSpecification]":
        """List[mastapy.electric_machines.StatorCutOutSpecification]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StatorCutOutSpecifications

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def tooth_and_slot(self: Self) -> "_1313.ToothAndSlot":
        """mastapy.electric_machines.ToothAndSlot

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothAndSlot

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Stator._Cast_Stator":
        return self._Cast_Stator(self)
