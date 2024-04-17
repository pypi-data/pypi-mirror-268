"""LinearDamping"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_DAMPING = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LinearDamping"
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearDamping",)


Self = TypeVar("Self", bound="LinearDamping")


class LinearDamping(_1612.MeasurementBase):
    """LinearDamping

    This is a mastapy class.
    """

    TYPE = _LINEAR_DAMPING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearDamping")

    class _Cast_LinearDamping:
        """Special nested class for casting LinearDamping to subclasses."""

        def __init__(
            self: "LinearDamping._Cast_LinearDamping", parent: "LinearDamping"
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LinearDamping._Cast_LinearDamping",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def linear_damping(
            self: "LinearDamping._Cast_LinearDamping",
        ) -> "LinearDamping":
            return self._parent

        def __getattr__(self: "LinearDamping._Cast_LinearDamping", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearDamping.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LinearDamping._Cast_LinearDamping":
        return self._Cast_LinearDamping(self)
