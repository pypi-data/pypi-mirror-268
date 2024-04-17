"""GearMountingError"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _682
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MOUNTING_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "GearMountingError",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearMountingError",)


Self = TypeVar("Self", bound="GearMountingError")


class GearMountingError(_682.MountingError):
    """GearMountingError

    This is a mastapy class.
    """

    TYPE = _GEAR_MOUNTING_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMountingError")

    class _Cast_GearMountingError:
        """Special nested class for casting GearMountingError to subclasses."""

        def __init__(
            self: "GearMountingError._Cast_GearMountingError",
            parent: "GearMountingError",
        ):
            self._parent = parent

        @property
        def mounting_error(
            self: "GearMountingError._Cast_GearMountingError",
        ) -> "_682.MountingError":
            return self._parent._cast(_682.MountingError)

        @property
        def gear_mounting_error(
            self: "GearMountingError._Cast_GearMountingError",
        ) -> "GearMountingError":
            return self._parent

        def __getattr__(self: "GearMountingError._Cast_GearMountingError", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMountingError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearMountingError._Cast_GearMountingError":
        return self._Cast_GearMountingError(self)
