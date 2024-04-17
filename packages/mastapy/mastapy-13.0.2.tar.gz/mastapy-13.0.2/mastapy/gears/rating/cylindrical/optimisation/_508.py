"""SafetyFactorOptimisationStepResultAngle"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.cylindrical.optimisation import _507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_ANGLE = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation",
    "SafetyFactorOptimisationStepResultAngle",
)


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorOptimisationStepResultAngle",)


Self = TypeVar("Self", bound="SafetyFactorOptimisationStepResultAngle")


class SafetyFactorOptimisationStepResultAngle(_507.SafetyFactorOptimisationStepResult):
    """SafetyFactorOptimisationStepResultAngle

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_ANGLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SafetyFactorOptimisationStepResultAngle"
    )

    class _Cast_SafetyFactorOptimisationStepResultAngle:
        """Special nested class for casting SafetyFactorOptimisationStepResultAngle to subclasses."""

        def __init__(
            self: "SafetyFactorOptimisationStepResultAngle._Cast_SafetyFactorOptimisationStepResultAngle",
            parent: "SafetyFactorOptimisationStepResultAngle",
        ):
            self._parent = parent

        @property
        def safety_factor_optimisation_step_result(
            self: "SafetyFactorOptimisationStepResultAngle._Cast_SafetyFactorOptimisationStepResultAngle",
        ) -> "_507.SafetyFactorOptimisationStepResult":
            return self._parent._cast(_507.SafetyFactorOptimisationStepResult)

        @property
        def safety_factor_optimisation_step_result_angle(
            self: "SafetyFactorOptimisationStepResultAngle._Cast_SafetyFactorOptimisationStepResultAngle",
        ) -> "SafetyFactorOptimisationStepResultAngle":
            return self._parent

        def __getattr__(
            self: "SafetyFactorOptimisationStepResultAngle._Cast_SafetyFactorOptimisationStepResultAngle",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "SafetyFactorOptimisationStepResultAngle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "SafetyFactorOptimisationStepResultAngle._Cast_SafetyFactorOptimisationStepResultAngle":
        return self._Cast_SafetyFactorOptimisationStepResultAngle(self)
