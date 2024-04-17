"""AngularAcceleration"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_ACCELERATION = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "AngularAcceleration"
)


__docformat__ = "restructuredtext en"
__all__ = ("AngularAcceleration",)


Self = TypeVar("Self", bound="AngularAcceleration")


class AngularAcceleration(_1612.MeasurementBase):
    """AngularAcceleration

    This is a mastapy class.
    """

    TYPE = _ANGULAR_ACCELERATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularAcceleration")

    class _Cast_AngularAcceleration:
        """Special nested class for casting AngularAcceleration to subclasses."""

        def __init__(
            self: "AngularAcceleration._Cast_AngularAcceleration",
            parent: "AngularAcceleration",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "AngularAcceleration._Cast_AngularAcceleration",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def angular_acceleration(
            self: "AngularAcceleration._Cast_AngularAcceleration",
        ) -> "AngularAcceleration":
            return self._parent

        def __getattr__(
            self: "AngularAcceleration._Cast_AngularAcceleration", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularAcceleration.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AngularAcceleration._Cast_AngularAcceleration":
        return self._Cast_AngularAcceleration(self)
