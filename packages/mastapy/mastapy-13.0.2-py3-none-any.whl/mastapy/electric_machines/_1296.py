"""PermanentMagnetAssistedSynchronousReluctanceMachine"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines import _1293
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERMANENT_MAGNET_ASSISTED_SYNCHRONOUS_RELUCTANCE_MACHINE = python_net_import(
    "SMT.MastaAPI.ElectricMachines",
    "PermanentMagnetAssistedSynchronousReluctanceMachine",
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1281, _1268


__docformat__ = "restructuredtext en"
__all__ = ("PermanentMagnetAssistedSynchronousReluctanceMachine",)


Self = TypeVar("Self", bound="PermanentMagnetAssistedSynchronousReluctanceMachine")


class PermanentMagnetAssistedSynchronousReluctanceMachine(
    _1293.NonCADElectricMachineDetail
):
    """PermanentMagnetAssistedSynchronousReluctanceMachine

    This is a mastapy class.
    """

    TYPE = _PERMANENT_MAGNET_ASSISTED_SYNCHRONOUS_RELUCTANCE_MACHINE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PermanentMagnetAssistedSynchronousReluctanceMachine"
    )

    class _Cast_PermanentMagnetAssistedSynchronousReluctanceMachine:
        """Special nested class for casting PermanentMagnetAssistedSynchronousReluctanceMachine to subclasses."""

        def __init__(
            self: "PermanentMagnetAssistedSynchronousReluctanceMachine._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine",
            parent: "PermanentMagnetAssistedSynchronousReluctanceMachine",
        ):
            self._parent = parent

        @property
        def non_cad_electric_machine_detail(
            self: "PermanentMagnetAssistedSynchronousReluctanceMachine._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine",
        ) -> "_1293.NonCADElectricMachineDetail":
            return self._parent._cast(_1293.NonCADElectricMachineDetail)

        @property
        def electric_machine_detail(
            self: "PermanentMagnetAssistedSynchronousReluctanceMachine._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine",
        ) -> "_1268.ElectricMachineDetail":
            from mastapy.electric_machines import _1268

            return self._parent._cast(_1268.ElectricMachineDetail)

        @property
        def permanent_magnet_assisted_synchronous_reluctance_machine(
            self: "PermanentMagnetAssistedSynchronousReluctanceMachine._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine",
        ) -> "PermanentMagnetAssistedSynchronousReluctanceMachine":
            return self._parent

        def __getattr__(
            self: "PermanentMagnetAssistedSynchronousReluctanceMachine._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine",
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
        self: Self,
        instance_to_wrap: "PermanentMagnetAssistedSynchronousReluctanceMachine.TYPE",
    ):
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
    ) -> "PermanentMagnetAssistedSynchronousReluctanceMachine._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine":
        return self._Cast_PermanentMagnetAssistedSynchronousReluctanceMachine(self)
