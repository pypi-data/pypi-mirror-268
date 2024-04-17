"""LinearAngularDamping"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_ANGULAR_DAMPING = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "LinearAngularDamping"
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearAngularDamping",)


Self = TypeVar("Self", bound="LinearAngularDamping")


class LinearAngularDamping(_1612.MeasurementBase):
    """LinearAngularDamping

    This is a mastapy class.
    """

    TYPE = _LINEAR_ANGULAR_DAMPING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearAngularDamping")

    class _Cast_LinearAngularDamping:
        """Special nested class for casting LinearAngularDamping to subclasses."""

        def __init__(
            self: "LinearAngularDamping._Cast_LinearAngularDamping",
            parent: "LinearAngularDamping",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LinearAngularDamping._Cast_LinearAngularDamping",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def linear_angular_damping(
            self: "LinearAngularDamping._Cast_LinearAngularDamping",
        ) -> "LinearAngularDamping":
            return self._parent

        def __getattr__(
            self: "LinearAngularDamping._Cast_LinearAngularDamping", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearAngularDamping.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "LinearAngularDamping._Cast_LinearAngularDamping":
        return self._Cast_LinearAngularDamping(self)
