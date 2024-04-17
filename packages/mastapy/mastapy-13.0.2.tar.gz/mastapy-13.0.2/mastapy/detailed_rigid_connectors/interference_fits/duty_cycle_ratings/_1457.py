"""InterferenceFitDutyCycleRating"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_FIT_DUTY_CYCLE_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits.DutyCycleRatings",
    "InterferenceFitDutyCycleRating",
)


__docformat__ = "restructuredtext en"
__all__ = ("InterferenceFitDutyCycleRating",)


Self = TypeVar("Self", bound="InterferenceFitDutyCycleRating")


class InterferenceFitDutyCycleRating(_0.APIBase):
    """InterferenceFitDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_FIT_DUTY_CYCLE_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InterferenceFitDutyCycleRating")

    class _Cast_InterferenceFitDutyCycleRating:
        """Special nested class for casting InterferenceFitDutyCycleRating to subclasses."""

        def __init__(
            self: "InterferenceFitDutyCycleRating._Cast_InterferenceFitDutyCycleRating",
            parent: "InterferenceFitDutyCycleRating",
        ):
            self._parent = parent

        @property
        def interference_fit_duty_cycle_rating(
            self: "InterferenceFitDutyCycleRating._Cast_InterferenceFitDutyCycleRating",
        ) -> "InterferenceFitDutyCycleRating":
            return self._parent

        def __getattr__(
            self: "InterferenceFitDutyCycleRating._Cast_InterferenceFitDutyCycleRating",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InterferenceFitDutyCycleRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def safety_factor_for_axial_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForAxialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def safety_factor_for_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactorForTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "InterferenceFitDutyCycleRating._Cast_InterferenceFitDutyCycleRating":
        return self._Cast_InterferenceFitDutyCycleRating(self)
