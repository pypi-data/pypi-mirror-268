"""WormGrinderManufactureError"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _692
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GRINDER_MANUFACTURE_ERROR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew",
    "WormGrinderManufactureError",
)


__docformat__ = "restructuredtext en"
__all__ = ("WormGrinderManufactureError",)


Self = TypeVar("Self", bound="WormGrinderManufactureError")


class WormGrinderManufactureError(_692.RackManufactureError):
    """WormGrinderManufactureError

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDER_MANUFACTURE_ERROR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_WormGrinderManufactureError")

    class _Cast_WormGrinderManufactureError:
        """Special nested class for casting WormGrinderManufactureError to subclasses."""

        def __init__(
            self: "WormGrinderManufactureError._Cast_WormGrinderManufactureError",
            parent: "WormGrinderManufactureError",
        ):
            self._parent = parent

        @property
        def rack_manufacture_error(
            self: "WormGrinderManufactureError._Cast_WormGrinderManufactureError",
        ) -> "_692.RackManufactureError":
            return self._parent._cast(_692.RackManufactureError)

        @property
        def worm_grinder_manufacture_error(
            self: "WormGrinderManufactureError._Cast_WormGrinderManufactureError",
        ) -> "WormGrinderManufactureError":
            return self._parent

        def __getattr__(
            self: "WormGrinderManufactureError._Cast_WormGrinderManufactureError",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "WormGrinderManufactureError.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "WormGrinderManufactureError._Cast_WormGrinderManufactureError":
        return self._Cast_WormGrinderManufactureError(self)
