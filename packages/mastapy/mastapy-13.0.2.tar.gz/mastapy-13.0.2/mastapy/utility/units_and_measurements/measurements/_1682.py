"""LinearFlexibility"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_FLEXIBILITY = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LinearFlexibility"
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearFlexibility",)


Self = TypeVar("Self", bound="LinearFlexibility")


class LinearFlexibility(_1612.MeasurementBase):
    """LinearFlexibility

    This is a mastapy class.
    """

    TYPE = _LINEAR_FLEXIBILITY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearFlexibility")

    class _Cast_LinearFlexibility:
        """Special nested class for casting LinearFlexibility to subclasses."""

        def __init__(
            self: "LinearFlexibility._Cast_LinearFlexibility",
            parent: "LinearFlexibility",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LinearFlexibility._Cast_LinearFlexibility",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def linear_flexibility(
            self: "LinearFlexibility._Cast_LinearFlexibility",
        ) -> "LinearFlexibility":
            return self._parent

        def __getattr__(self: "LinearFlexibility._Cast_LinearFlexibility", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearFlexibility.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LinearFlexibility._Cast_LinearFlexibility":
        return self._Cast_LinearFlexibility(self)
