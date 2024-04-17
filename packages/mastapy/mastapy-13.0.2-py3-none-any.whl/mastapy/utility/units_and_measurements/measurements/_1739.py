"""VelocitySmall"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VELOCITY_SMALL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "VelocitySmall"
)


__docformat__ = "restructuredtext en"
__all__ = ("VelocitySmall",)


Self = TypeVar("Self", bound="VelocitySmall")


class VelocitySmall(_1612.MeasurementBase):
    """VelocitySmall

    This is a mastapy class.
    """

    TYPE = _VELOCITY_SMALL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VelocitySmall")

    class _Cast_VelocitySmall:
        """Special nested class for casting VelocitySmall to subclasses."""

        def __init__(
            self: "VelocitySmall._Cast_VelocitySmall", parent: "VelocitySmall"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "VelocitySmall._Cast_VelocitySmall",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def velocity_small(
            self: "VelocitySmall._Cast_VelocitySmall",
        ) -> "VelocitySmall":
            return self._parent

        def __getattr__(self: "VelocitySmall._Cast_VelocitySmall", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VelocitySmall.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "VelocitySmall._Cast_VelocitySmall":
        return self._Cast_VelocitySmall(self)
