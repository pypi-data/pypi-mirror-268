"""AngularJerk"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ANGULAR_JERK = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "AngularJerk"
)


__docformat__ = "restructuredtext en"
__all__ = ("AngularJerk",)


Self = TypeVar("Self", bound="AngularJerk")


class AngularJerk(_1612.MeasurementBase):
    """AngularJerk

    This is a mastapy class.
    """

    TYPE = _ANGULAR_JERK
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AngularJerk")

    class _Cast_AngularJerk:
        """Special nested class for casting AngularJerk to subclasses."""

        def __init__(self: "AngularJerk._Cast_AngularJerk", parent: "AngularJerk"):
            self._parent = parent

        @property
        def measurement_base(
            self: "AngularJerk._Cast_AngularJerk",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def angular_jerk(self: "AngularJerk._Cast_AngularJerk") -> "AngularJerk":
            return self._parent

        def __getattr__(self: "AngularJerk._Cast_AngularJerk", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AngularJerk.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AngularJerk._Cast_AngularJerk":
        return self._Cast_AngularJerk(self)
