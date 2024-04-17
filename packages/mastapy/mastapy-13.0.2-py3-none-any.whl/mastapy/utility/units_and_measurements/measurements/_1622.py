"""AngleSmall"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE_SMALL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "AngleSmall"
)


__docformat__ = "restructuredtext en"
__all__ = ("AngleSmall",)


Self = TypeVar("Self", bound="AngleSmall")


class AngleSmall(_1612.MeasurementBase):
    """AngleSmall

    This is a mastapy class.
    """

    TYPE = _ANGLE_SMALL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngleSmall")

    class _Cast_AngleSmall:
        """Special nested class for casting AngleSmall to subclasses."""

        def __init__(self: "AngleSmall._Cast_AngleSmall", parent: "AngleSmall"):
            self._parent = parent

        @property
        def measurement_base(
            self: "AngleSmall._Cast_AngleSmall",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def angle_small(self: "AngleSmall._Cast_AngleSmall") -> "AngleSmall":
            return self._parent

        def __getattr__(self: "AngleSmall._Cast_AngleSmall", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngleSmall.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AngleSmall._Cast_AngleSmall":
        return self._Cast_AngleSmall(self)
