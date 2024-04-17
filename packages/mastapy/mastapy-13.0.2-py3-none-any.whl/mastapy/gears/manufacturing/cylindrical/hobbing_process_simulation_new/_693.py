"""RackMountingError"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _682
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RACK_MOUNTING_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "RackMountingError",
)


__docformat__ = "restructuredtext en"
__all__ = ("RackMountingError",)


Self = TypeVar("Self", bound="RackMountingError")


class RackMountingError(_682.MountingError):
    """RackMountingError

    This is a mastapy class.
    """

    TYPE = _RACK_MOUNTING_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RackMountingError")

    class _Cast_RackMountingError:
        """Special nested class for casting RackMountingError to subclasses."""

        def __init__(
            self: "RackMountingError._Cast_RackMountingError",
            parent: "RackMountingError",
        ):
            self._parent = parent

        @property
        def mounting_error(
            self: "RackMountingError._Cast_RackMountingError",
        ) -> "_682.MountingError":
            return self._parent._cast(_682.MountingError)

        @property
        def rack_mounting_error(
            self: "RackMountingError._Cast_RackMountingError",
        ) -> "RackMountingError":
            return self._parent

        def __getattr__(self: "RackMountingError._Cast_RackMountingError", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RackMountingError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_runout(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialRunout

        if temp is None:
            return 0.0

        return temp

    @axial_runout.setter
    @enforce_parameter_types
    def axial_runout(self: Self, value: "float"):
        self.wrapped.AxialRunout = float(value) if value is not None else 0.0

    @property
    def axial_runout_phase_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialRunoutPhaseAngle

        if temp is None:
            return 0.0

        return temp

    @axial_runout_phase_angle.setter
    @enforce_parameter_types
    def axial_runout_phase_angle(self: Self, value: "float"):
        self.wrapped.AxialRunoutPhaseAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "RackMountingError._Cast_RackMountingError":
        return self._Cast_RackMountingError(self)
