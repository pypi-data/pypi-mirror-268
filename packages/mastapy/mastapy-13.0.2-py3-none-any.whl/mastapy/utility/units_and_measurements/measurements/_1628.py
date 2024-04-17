"""AngularVelocity"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_VELOCITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "AngularVelocity"
)


__docformat__ = "restructuredtext en"
__all__ = ("AngularVelocity",)


Self = TypeVar("Self", bound="AngularVelocity")


class AngularVelocity(_1612.MeasurementBase):
    """AngularVelocity

    This is a mastapy class.
    """

    TYPE = _ANGULAR_VELOCITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularVelocity")

    class _Cast_AngularVelocity:
        """Special nested class for casting AngularVelocity to subclasses."""

        def __init__(
            self: "AngularVelocity._Cast_AngularVelocity", parent: "AngularVelocity"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "AngularVelocity._Cast_AngularVelocity",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def angular_velocity(
            self: "AngularVelocity._Cast_AngularVelocity",
        ) -> "AngularVelocity":
            return self._parent

        def __getattr__(self: "AngularVelocity._Cast_AngularVelocity", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularVelocity.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AngularVelocity._Cast_AngularVelocity":
        return self._Cast_AngularVelocity(self)
