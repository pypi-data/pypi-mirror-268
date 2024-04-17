"""SurfacePermanentMagnetMachine"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines import _1293
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SURFACE_PERMANENT_MAGNET_MACHINE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "SurfacePermanentMagnetMachine"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1311, _1268


__docformat__ = "restructuredtext en"
__all__ = ("SurfacePermanentMagnetMachine",)


Self = TypeVar("Self", bound="SurfacePermanentMagnetMachine")


class SurfacePermanentMagnetMachine(_1293.NonCADElectricMachineDetail):
    """SurfacePermanentMagnetMachine

    This is a mastapy class.
    """

    TYPE = _SURFACE_PERMANENT_MAGNET_MACHINE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SurfacePermanentMagnetMachine")

    class _Cast_SurfacePermanentMagnetMachine:
        """Special nested class for casting SurfacePermanentMagnetMachine to subclasses."""

        def __init__(
            self: "SurfacePermanentMagnetMachine._Cast_SurfacePermanentMagnetMachine",
            parent: "SurfacePermanentMagnetMachine",
        ):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(
            self: "SurfacePermanentMagnetMachine._Cast_SurfacePermanentMagnetMachine",
        ) -> "_1293.NonCADElectricMachineDetail":
            return self._parent._cast(_1293.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(
            self: "SurfacePermanentMagnetMachine._Cast_SurfacePermanentMagnetMachine",
        ) -> "_1268.ElectricMachineDetail":
            from mastapy.electric_machines import _1268

            return self._parent._cast(_1268.ElectricMachineDetail)

        @property
        def surface_permanent_magnet_machine(
            self: "SurfacePermanentMagnetMachine._Cast_SurfacePermanentMagnetMachine",
        ) -> "SurfacePermanentMagnetMachine":
            return self._parent

        def __getattr__(
            self: "SurfacePermanentMagnetMachine._Cast_SurfacePermanentMagnetMachine",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SurfacePermanentMagnetMachine.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor(self: Self) -> "_1311.SurfacePermanentMagnetRotor":
        """mastapy.electric_machines.SurfacePermanentMagnetRotor

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
    ) -> "SurfacePermanentMagnetMachine._Cast_SurfacePermanentMagnetMachine":
        return self._Cast_SurfacePermanentMagnetMachine(self)
