"""QuadraticAngularDamping"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_QUADRATIC_ANGULAR_DAMPING = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements", "QuadraticAngularDamping"
)


__docformat__ = "restructuredtext en"
__all__ = ("QuadraticAngularDamping",)


Self = TypeVar("Self", bound="QuadraticAngularDamping")


class QuadraticAngularDamping(_1612.MeasurementBase):
    """QuadraticAngularDamping

    This is a mastapy class.
    """

    TYPE = _QUADRATIC_ANGULAR_DAMPING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_QuadraticAngularDamping")

    class _Cast_QuadraticAngularDamping:
        """Special nested class for casting QuadraticAngularDamping to subclasses."""

        def __init__(
            self: "QuadraticAngularDamping._Cast_QuadraticAngularDamping",
            parent: "QuadraticAngularDamping",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "QuadraticAngularDamping._Cast_QuadraticAngularDamping",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def quadratic_angular_damping(
            self: "QuadraticAngularDamping._Cast_QuadraticAngularDamping",
        ) -> "QuadraticAngularDamping":
            return self._parent

        def __getattr__(
            self: "QuadraticAngularDamping._Cast_QuadraticAngularDamping", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "QuadraticAngularDamping.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "QuadraticAngularDamping._Cast_QuadraticAngularDamping":
        return self._Cast_QuadraticAngularDamping(self)
