"""ConicalMeshedWheelFlankManufacturingConfig"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears import _323
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESHED_WHEEL_FLANK_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel",
    "ConicalMeshedWheelFlankManufacturingConfig",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshedWheelFlankManufacturingConfig",)


Self = TypeVar("Self", bound="ConicalMeshedWheelFlankManufacturingConfig")


class ConicalMeshedWheelFlankManufacturingConfig(_323.ConicalGearToothSurface):
    """ConicalMeshedWheelFlankManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESHED_WHEEL_FLANK_MANUFACTURING_CONFIG
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalMeshedWheelFlankManufacturingConfig"
    )

    class _Cast_ConicalMeshedWheelFlankManufacturingConfig:
        """Special nested class for casting ConicalMeshedWheelFlankManufacturingConfig to subclasses."""

        def __init__(
            self: "ConicalMeshedWheelFlankManufacturingConfig._Cast_ConicalMeshedWheelFlankManufacturingConfig",
            parent: "ConicalMeshedWheelFlankManufacturingConfig",
        ):
            self._parent = parent

        @property
        def conical_gear_tooth_surface(
            self: "ConicalMeshedWheelFlankManufacturingConfig._Cast_ConicalMeshedWheelFlankManufacturingConfig",
        ) -> "_323.ConicalGearToothSurface":
            return self._parent._cast(_323.ConicalGearToothSurface)

        @property
        def conical_meshed_wheel_flank_manufacturing_config(
            self: "ConicalMeshedWheelFlankManufacturingConfig._Cast_ConicalMeshedWheelFlankManufacturingConfig",
        ) -> "ConicalMeshedWheelFlankManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "ConicalMeshedWheelFlankManufacturingConfig._Cast_ConicalMeshedWheelFlankManufacturingConfig",
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
        self: Self, instance_to_wrap: "ConicalMeshedWheelFlankManufacturingConfig.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshedWheelFlankManufacturingConfig._Cast_ConicalMeshedWheelFlankManufacturingConfig":
        return self._Cast_ConicalMeshedWheelFlankManufacturingConfig(self)
