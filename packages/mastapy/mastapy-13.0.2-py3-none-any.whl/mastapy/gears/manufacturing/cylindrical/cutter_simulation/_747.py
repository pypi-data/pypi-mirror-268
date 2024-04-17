"""RoughCutterSimulation"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _742
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROUGH_CUTTER_SIMULATION = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "RoughCutterSimulation",
)


__docformat__ = "restructuredtext en"
__all__ = ("RoughCutterSimulation",)


Self = TypeVar("Self", bound="RoughCutterSimulation")


class RoughCutterSimulation(_742.GearCutterSimulation):
    """RoughCutterSimulation

    This is a mastapy class.
    """

    TYPE = _ROUGH_CUTTER_SIMULATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RoughCutterSimulation")

    class _Cast_RoughCutterSimulation:
        """Special nested class for casting RoughCutterSimulation to subclasses."""

        def __init__(
            self: "RoughCutterSimulation._Cast_RoughCutterSimulation",
            parent: "RoughCutterSimulation",
        ):
            self._parent = parent

        @property
        def gear_cutter_simulation(
            self: "RoughCutterSimulation._Cast_RoughCutterSimulation",
        ) -> "_742.GearCutterSimulation":
            return self._parent._cast(_742.GearCutterSimulation)

        @property
        def rough_cutter_simulation(
            self: "RoughCutterSimulation._Cast_RoughCutterSimulation",
        ) -> "RoughCutterSimulation":
            return self._parent

        def __getattr__(
            self: "RoughCutterSimulation._Cast_RoughCutterSimulation", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RoughCutterSimulation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "RoughCutterSimulation._Cast_RoughCutterSimulation":
        return self._Cast_RoughCutterSimulation(self)
