"""InteriorPermanentMagnetMachine"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines import _1293
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_MACHINE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "InteriorPermanentMagnetMachine"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1281, _1268


__docformat__ = "restructuredtext en"
__all__ = ("InteriorPermanentMagnetMachine",)


Self = TypeVar("Self", bound="InteriorPermanentMagnetMachine")


class InteriorPermanentMagnetMachine(_1293.NonCADElectricMachineDetail):
    """InteriorPermanentMagnetMachine

    This is a mastapy class.
    """

    TYPE = _INTERIOR_PERMANENT_MAGNET_MACHINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InteriorPermanentMagnetMachine")

    class _Cast_InteriorPermanentMagnetMachine:
        """Special nested class for casting InteriorPermanentMagnetMachine to subclasses."""

        def __init__(
            self: "InteriorPermanentMagnetMachine._Cast_InteriorPermanentMagnetMachine",
            parent: "InteriorPermanentMagnetMachine",
        ):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(
            self: "InteriorPermanentMagnetMachine._Cast_InteriorPermanentMagnetMachine",
        ) -> "_1293.NonCADElectricMachineDetail":
            return self._parent._cast(_1293.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(
            self: "InteriorPermanentMagnetMachine._Cast_InteriorPermanentMagnetMachine",
        ) -> "_1268.ElectricMachineDetail":
            from mastapy.electric_machines import _1268

            return self._parent._cast(_1268.ElectricMachineDetail)

        @property
        def interior_permanent_magnet_machine(
            self: "InteriorPermanentMagnetMachine._Cast_InteriorPermanentMagnetMachine",
        ) -> "InteriorPermanentMagnetMachine":
            return self._parent

        def __getattr__(
            self: "InteriorPermanentMagnetMachine._Cast_InteriorPermanentMagnetMachine",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InteriorPermanentMagnetMachine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor(
        self: Self,
    ) -> "_1281.InteriorPermanentMagnetAndSynchronousReluctanceRotor":
        """mastapy.electric_machines.InteriorPermanentMagnetAndSynchronousReluctanceRotor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InteriorPermanentMagnetMachine._Cast_InteriorPermanentMagnetMachine":
        return self._Cast_InteriorPermanentMagnetMachine(self)
