"""LinearAngularStiffnessCrossTerm"""

from __future__ import annotations

from typing import TypeVar

from mastapy.utility.units_and_measurements import _1612
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LINEAR_ANGULAR_STIFFNESS_CROSS_TERM = python_net_import(
    "SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements",
    "LinearAngularStiffnessCrossTerm",
)


__docformat__ = "restructuredtext en"
__all__ = ("LinearAngularStiffnessCrossTerm",)


Self = TypeVar("Self", bound="LinearAngularStiffnessCrossTerm")


class LinearAngularStiffnessCrossTerm(_1612.MeasurementBase):
    """LinearAngularStiffnessCrossTerm

    This is a mastapy class.
    """

    TYPE = _LINEAR_ANGULAR_STIFFNESS_CROSS_TERM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LinearAngularStiffnessCrossTerm")

    class _Cast_LinearAngularStiffnessCrossTerm:
        """Special nested class for casting LinearAngularStiffnessCrossTerm to subclasses."""

        def __init__(
            self: "LinearAngularStiffnessCrossTerm._Cast_LinearAngularStiffnessCrossTerm",
            parent: "LinearAngularStiffnessCrossTerm",
        ):
            self._parent = parent

        @property
        def measurement_base(
            self: "LinearAngularStiffnessCrossTerm._Cast_LinearAngularStiffnessCrossTerm",
        ) -> "_1612.MeasurementBase":
            return self._parent._cast(_1612.MeasurementBase)

        @property
        def linear_angular_stiffness_cross_term(
            self: "LinearAngularStiffnessCrossTerm._Cast_LinearAngularStiffnessCrossTerm",
        ) -> "LinearAngularStiffnessCrossTerm":
            return self._parent

        def __getattr__(
            self: "LinearAngularStiffnessCrossTerm._Cast_LinearAngularStiffnessCrossTerm",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LinearAngularStiffnessCrossTerm.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LinearAngularStiffnessCrossTerm._Cast_LinearAngularStiffnessCrossTerm":
        return self._Cast_LinearAngularStiffnessCrossTerm(self)
