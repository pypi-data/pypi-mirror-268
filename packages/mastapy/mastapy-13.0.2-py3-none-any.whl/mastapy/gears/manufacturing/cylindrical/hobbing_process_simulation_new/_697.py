"""WormGrindingProcessCalculation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _683
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrindingProcessCalculation",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _695,
        _696,
        _698,
        _699,
        _700,
        _701,
        _705,
    )


__docformat__ = "restructuredtext en"
__all__ = ("WormGrindingProcessCalculation",)


Self = TypeVar("Self", bound="WormGrindingProcessCalculation")


class WormGrindingProcessCalculation(_683.ProcessCalculation):
    """WormGrindingProcessCalculation

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrindingProcessCalculation")

    class _Cast_WormGrindingProcessCalculation:
        """Special nested class for casting WormGrindingProcessCalculation to subclasses."""

        def __init__(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
            parent: "WormGrindingProcessCalculation",
        ):
            self._parent = parent

        @property
        def process_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "_683.ProcessCalculation":
            return self._parent._cast(_683.ProcessCalculation)

        @property
        def worm_grinding_cutter_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "_695.WormGrindingCutterCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _695,
            )

            return self._parent._cast(_695.WormGrindingCutterCalculation)

        @property
        def worm_grinding_lead_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "_696.WormGrindingLeadCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _696,
            )

            return self._parent._cast(_696.WormGrindingLeadCalculation)

        @property
        def worm_grinding_process_gear_shape(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "_698.WormGrindingProcessGearShape":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _698,
            )

            return self._parent._cast(_698.WormGrindingProcessGearShape)

        @property
        def worm_grinding_process_mark_on_shaft(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "_699.WormGrindingProcessMarkOnShaft":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _699,
            )

            return self._parent._cast(_699.WormGrindingProcessMarkOnShaft)

        @property
        def worm_grinding_process_pitch_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "_700.WormGrindingProcessPitchCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _700,
            )

            return self._parent._cast(_700.WormGrindingProcessPitchCalculation)

        @property
        def worm_grinding_process_profile_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "_701.WormGrindingProcessProfileCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _701,
            )

            return self._parent._cast(_701.WormGrindingProcessProfileCalculation)

        @property
        def worm_grinding_process_total_modification_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "_705.WormGrindingProcessTotalModificationCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _705,
            )

            return self._parent._cast(
                _705.WormGrindingProcessTotalModificationCalculation
            )

        @property
        def worm_grinding_process_calculation(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
        ) -> "WormGrindingProcessCalculation":
            return self._parent

        def __getattr__(
            self: "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGrindingProcessCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrindingProcessCalculation._Cast_WormGrindingProcessCalculation":
        return self._Cast_WormGrindingProcessCalculation(self)
