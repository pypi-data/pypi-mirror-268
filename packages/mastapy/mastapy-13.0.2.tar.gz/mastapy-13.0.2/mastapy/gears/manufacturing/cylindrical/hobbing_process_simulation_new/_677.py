"""HobbingProcessSimulationViewModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _690
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_SIMULATION_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobbingProcessSimulationViewModel",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _631


__docformat__ = "restructuredtext en"
__all__ = ("HobbingProcessSimulationViewModel",)


Self = TypeVar("Self", bound="HobbingProcessSimulationViewModel")


class HobbingProcessSimulationViewModel(
    _690.ProcessSimulationViewModel["_676.HobbingProcessSimulationNew"]
):
    """HobbingProcessSimulationViewModel

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_SIMULATION_VIEW_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobbingProcessSimulationViewModel")

    class _Cast_HobbingProcessSimulationViewModel:
        """Special nested class for casting HobbingProcessSimulationViewModel to subclasses."""

        def __init__(
            self: "HobbingProcessSimulationViewModel._Cast_HobbingProcessSimulationViewModel",
            parent: "HobbingProcessSimulationViewModel",
        ):
            self._parent = parent

        @property
        def process_simulation_view_model(
            self: "HobbingProcessSimulationViewModel._Cast_HobbingProcessSimulationViewModel",
        ) -> "_690.ProcessSimulationViewModel":
            return self._parent._cast(_690.ProcessSimulationViewModel)

        @property
        def gear_manufacturing_configuration_view_model(
            self: "HobbingProcessSimulationViewModel._Cast_HobbingProcessSimulationViewModel",
        ) -> "_631.GearManufacturingConfigurationViewModel":
            from mastapy.gears.manufacturing.cylindrical import _631

            return self._parent._cast(_631.GearManufacturingConfigurationViewModel)

        @property
        def hobbing_process_simulation_view_model(
            self: "HobbingProcessSimulationViewModel._Cast_HobbingProcessSimulationViewModel",
        ) -> "HobbingProcessSimulationViewModel":
            return self._parent

        def __getattr__(
            self: "HobbingProcessSimulationViewModel._Cast_HobbingProcessSimulationViewModel",
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
        self: Self, instance_to_wrap: "HobbingProcessSimulationViewModel.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HobbingProcessSimulationViewModel._Cast_HobbingProcessSimulationViewModel":
        return self._Cast_HobbingProcessSimulationViewModel(self)
