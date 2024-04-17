"""AngleVerySmall"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGLE_VERY_SMALL = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "AngleVerySmall"
)


__docformat__ = "restructuredtext en"
__all__ = ("AngleVerySmall",)


Self = TypeVar("Self", bound="AngleVerySmall")


class AngleVerySmall(_1612.MeasurementBase):
    """AngleVerySmall

    This is a mastapy class.
    """

    TYPE = _ANGLE_VERY_SMALL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngleVerySmall")

    class _Cast_AngleVerySmall:
        """Special nested class for casting AngleVerySmall to subclasses."""

        def __init__(
            self: "AngleVerySmall._Cast_AngleVerySmall", parent: "AngleVerySmall"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "AngleVerySmall._Cast_AngleVerySmall",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def angle_very_small(
            self: "AngleVerySmall._Cast_AngleVerySmall",
        ) -> "AngleVerySmall":
            return self._parent

        def __getattr__(self: "AngleVerySmall._Cast_AngleVerySmall", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngleVerySmall.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AngleVerySmall._Cast_AngleVerySmall":
        return self._Cast_AngleVerySmall(self)
