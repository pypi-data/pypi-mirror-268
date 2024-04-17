"""WormGrindingProcessSimulationViewModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _690
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessSimulationViewModel",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _631


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessSimulationViewModel",)


Self = TypeVar("Self", bound="WormGrindingProcessSimulationViewModel")


class WormGrindingProcessSimulationViewModel(
    _690.ProcessSimulationViewModel["_703.WormGrindingProcessSimulationNew"]
):
    """WormGrindingProcessSimulationViewModel

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_VIEW_MODEL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGrindingProcessSimulationViewModel"
    )

    class _Cast_WormGrindingProcessSimulationViewModel:
        """Special nested class for casting WormGrindingProcessSimulationViewModel to subclasses."""

        def __init__(
            self: "WormGrindingProcessSimulationViewModel._Cast_WormGrindingProcessSimulationViewModel",
            parent: "WormGrindingProcessSimulationViewModel",
        ):
            self._parent = parent

        @property
        def process_simulation_view_model(
            self: "WormGrindingProcessSimulationViewModel._Cast_WormGrindingProcessSimulationViewModel",
        ) -> "_690.ProcessSimulationViewModel":
            return self._parent._cast(_690.ProcessSimulationViewModel)

        @property
        def gear_manufacturing_configuration_view_model(
            self: "WormGrindingProcessSimulationViewModel._Cast_WormGrindingProcessSimulationViewModel",
        ) -> "_631.GearManufacturingConfigurationViewModel":
            from mastapy.gears.manufacturing.cylindrical import _631

            return self._parent._cast(_631.GearManufacturingConfigurationViewModel)

        @property
        def worm_grinding_process_simulation_view_model(
            self: "WormGrindingProcessSimulationViewModel._Cast_WormGrindingProcessSimulationViewModel",
        ) -> "WormGrindingProcessSimulationViewModel":
            return self._parent

        def __getattr__(
            self: "WormGrindingProcessSimulationViewModel._Cast_WormGrindingProcessSimulationViewModel",
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
        self: Self, instance_to_wrap: "WormGrindingProcessSimulationViewModel.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingProcessSimulationViewModel._Cast_WormGrindingProcessSimulationViewModel":
        return self._Cast_WormGrindingProcessSimulationViewModel(self)
