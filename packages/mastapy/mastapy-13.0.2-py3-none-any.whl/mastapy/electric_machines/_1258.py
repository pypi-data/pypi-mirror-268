"""CADToothAndSlot"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1250
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_TOOTH_AND_SLOT = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CADToothAndSlot"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1280, _1319


__docformat__ = "restructuredtext en"
__all__ = ("CADToothAndSlot",)


Self = TypeVar("Self", bound="CADToothAndSlot")


class CADToothAndSlot(_1250.AbstractToothAndSlot):
    """CADToothAndSlot

    This is a mastapy class.
    """

    TYPE = _CAD_TOOTH_AND_SLOT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADToothAndSlot")

    class _Cast_CADToothAndSlot:
        """Special nested class for casting CADToothAndSlot to subclasses."""

        def __init__(
            self: "CADToothAndSlot._Cast_CADToothAndSlot", parent: "CADToothAndSlot"
        ):
            self._parent = parent

        @property
        def abstract_tooth_and_slot(
            self: "CADToothAndSlot._Cast_CADToothAndSlot",
        ) -> "_1250.AbstractToothAndSlot":
            return self._parent._cast(_1250.AbstractToothAndSlot)

        @property
        def cad_tooth_and_slot(
            self: "CADToothAndSlot._Cast_CADToothAndSlot",
        ) -> "CADToothAndSlot":
            return self._parent

        def __getattr__(self: "CADToothAndSlot._Cast_CADToothAndSlot", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADToothAndSlot.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def individual_conductor_specification_source(
        self: Self,
    ) -> "_1280.IndividualConductorSpecificationSource":
        """mastapy.electric_machines.IndividualConductorSpecificationSource"""
        temp = self.wrapped.IndividualConductorSpecificationSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.ElectricMachines.IndividualConductorSpecificationSource"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.electric_machines._1280", "IndividualConductorSpecificationSource"
        )(value)

    @individual_conductor_specification_source.setter
    @enforce_parameter_types
    def individual_conductor_specification_source(
        self: Self, value: "_1280.IndividualConductorSpecificationSource"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.ElectricMachines.IndividualConductorSpecificationSource",
        )
        self.wrapped.IndividualConductorSpecificationSource = value

    @property
    def conductors(self: Self) -> "List[_1319.WindingConductor]":
        """List[mastapy.electric_machines.WindingConductor]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Conductors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "CADToothAndSlot._Cast_CADToothAndSlot":
        return self._Cast_CADToothAndSlot(self)
