"""LinearStiffness"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_STIFFNESS = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LinearStiffness"
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearStiffness",)


Self = TypeVar("Self", bound="LinearStiffness")


class LinearStiffness(_1612.MeasurementBase):
    """LinearStiffness

    This is a mastapy class.
    """

    TYPE = _LINEAR_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearStiffness")

    class _Cast_LinearStiffness:
        """Special nested class for casting LinearStiffness to subclasses."""

        def __init__(
            self: "LinearStiffness._Cast_LinearStiffness", parent: "LinearStiffness"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LinearStiffness._Cast_LinearStiffness",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def linear_stiffness(
            self: "LinearStiffness._Cast_LinearStiffness",
        ) -> "LinearStiffness":
            return self._parent

        def __getattr__(self: "LinearStiffness._Cast_LinearStiffness", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LinearStiffness._Cast_LinearStiffness":
        return self._Cast_LinearStiffness(self)
