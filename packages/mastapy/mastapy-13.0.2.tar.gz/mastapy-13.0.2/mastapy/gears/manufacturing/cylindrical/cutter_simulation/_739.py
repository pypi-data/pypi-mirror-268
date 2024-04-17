"""FinishCutterSimulation"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _742
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FINISH_CUTTER_SIMULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "FinishCutterSimulation",
)


__docformat__ = "restructuredtext en"
__all__ = ("FinishCutterSimulation",)


Self = TypeVar("Self", bound="FinishCutterSimulation")


class FinishCutterSimulation(_742.GearCutterSimulation):
    """FinishCutterSimulation

    This is a mastapy class.
    """

    TYPE = _FINISH_CUTTER_SIMULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FinishCutterSimulation")

    class _Cast_FinishCutterSimulation:
        """Special nested class for casting FinishCutterSimulation to subclasses."""

        def __init__(
            self: "FinishCutterSimulation._Cast_FinishCutterSimulation",
            parent: "FinishCutterSimulation",
        ):
            self._parent = parent

        @property
        def gear_cutter_simulation(
            self: "FinishCutterSimulation._Cast_FinishCutterSimulation",
        ) -> "_742.GearCutterSimulation":
            return self._parent._cast(_742.GearCutterSimulation)

        @property
        def finish_cutter_simulation(
            self: "FinishCutterSimulation._Cast_FinishCutterSimulation",
        ) -> "FinishCutterSimulation":
            return self._parent

        def __getattr__(
            self: "FinishCutterSimulation._Cast_FinishCutterSimulation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FinishCutterSimulation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "FinishCutterSimulation._Cast_FinishCutterSimulation":
        return self._Cast_FinishCutterSimulation(self)
