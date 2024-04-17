"""HobbingProcessCalculation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _683
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_CALCULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "HobbingProcessCalculation",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
        _670,
        _671,
        _672,
        _673,
        _674,
        _678,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HobbingProcessCalculation",)


Self = TypeVar("Self", bound="HobbingProcessCalculation")


class HobbingProcessCalculation(_683.ProcessCalculation):
    """HobbingProcessCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_CALCULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HobbingProcessCalculation")

    class _Cast_HobbingProcessCalculation:
        """Special nested class for casting HobbingProcessCalculation to subclasses."""

        def __init__(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
            parent: "HobbingProcessCalculation",
        ):
            self._parent = parent

        @property
        def process_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_683.ProcessCalculation":
            return self._parent._cast(_683.ProcessCalculation)

        @property
        def hobbing_process_gear_shape(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_670.HobbingProcessGearShape":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _670,
            )

            return self._parent._cast(_670.HobbingProcessGearShape)

        @property
        def hobbing_process_lead_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_671.HobbingProcessLeadCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _671,
            )

            return self._parent._cast(_671.HobbingProcessLeadCalculation)

        @property
        def hobbing_process_mark_on_shaft(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_672.HobbingProcessMarkOnShaft":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _672,
            )

            return self._parent._cast(_672.HobbingProcessMarkOnShaft)

        @property
        def hobbing_process_pitch_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_673.HobbingProcessPitchCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _673,
            )

            return self._parent._cast(_673.HobbingProcessPitchCalculation)

        @property
        def hobbing_process_profile_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_674.HobbingProcessProfileCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _674,
            )

            return self._parent._cast(_674.HobbingProcessProfileCalculation)

        @property
        def hobbing_process_total_modification_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "_678.HobbingProcessTotalModificationCalculation":
            from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
                _678,
            )

            return self._parent._cast(_678.HobbingProcessTotalModificationCalculation)

        @property
        def hobbing_process_calculation(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation",
        ) -> "HobbingProcessCalculation":
            return self._parent

        def __getattr__(
            self: "HobbingProcessCalculation._Cast_HobbingProcessCalculation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HobbingProcessCalculation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HobbingProcessCalculation._Cast_HobbingProcessCalculation":
        return self._Cast_HobbingProcessCalculation(self)
