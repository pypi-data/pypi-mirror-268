"""WormGrindingProcessSimulationInput"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _688
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_INPUT = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessSimulationInput",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _694,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessSimulationInput",)


Self = TypeVar("Self", bound="WormGrindingProcessSimulationInput")


class WormGrindingProcessSimulationInput(_688.ProcessSimulationInput):
    """WormGrindingProcessSimulationInput

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_INPUT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrindingProcessSimulationInput")

    class _Cast_WormGrindingProcessSimulationInput:
        """Special nested class for casting WormGrindingProcessSimulationInput to subclasses."""

        def __init__(
            self: "WormGrindingProcessSimulationInput._Cast_WormGrindingProcessSimulationInput",
            parent: "WormGrindingProcessSimulationInput",
        ):
            self._parent = parent

        @property
        def process_simulation_input(
            self: "WormGrindingProcessSimulationInput._Cast_WormGrindingProcessSimulationInput",
        ) -> "_688.ProcessSimulationInput":
            return self._parent._cast(_688.ProcessSimulationInput)

        @property
        def worm_grinding_process_simulation_input(
            self: "WormGrindingProcessSimulationInput._Cast_WormGrindingProcessSimulationInput",
        ) -> "WormGrindingProcessSimulationInput":
            return self._parent

        def __getattr__(
            self: "WormGrindingProcessSimulationInput._Cast_WormGrindingProcessSimulationInput",
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
        self: Self, instance_to_wrap: "WormGrindingProcessSimulationInput.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinder_manufacture_error(
        self: Self,
    ) -> "_694.WormGrinderManufactureError":
        """mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new.WormGrinderManufactureError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WormGrinderManufactureError

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingProcessSimulationInput._Cast_WormGrindingProcessSimulationInput":
        return self._Cast_WormGrindingProcessSimulationInput(self)
