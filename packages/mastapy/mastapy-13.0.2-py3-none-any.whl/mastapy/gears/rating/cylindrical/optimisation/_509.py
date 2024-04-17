"""SafetyFactorOptimisationStepResultNumber"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.cylindrical.optimisation import _507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_NUMBER = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation",
    "SafetyFactorOptimisationStepResultNumber",
)


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorOptimisationStepResultNumber",)


Self = TypeVar("Self", bound="SafetyFactorOptimisationStepResultNumber")


class SafetyFactorOptimisationStepResultNumber(_507.SafetyFactorOptimisationStepResult):
    """SafetyFactorOptimisationStepResultNumber

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_NUMBER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SafetyFactorOptimisationStepResultNumber"
    )

    class _Cast_SafetyFactorOptimisationStepResultNumber:
        """Special nested class for casting SafetyFactorOptimisationStepResultNumber to subclasses."""

        def __init__(
            self: "SafetyFactorOptimisationStepResultNumber._Cast_SafetyFactorOptimisationStepResultNumber",
            parent: "SafetyFactorOptimisationStepResultNumber",
        ):
            self._parent = parent

        @property
        def safety_factor_optimisation_step_result(
            self: "SafetyFactorOptimisationStepResultNumber._Cast_SafetyFactorOptimisationStepResultNumber",
        ) -> "_507.SafetyFactorOptimisationStepResult":
            return self._parent._cast(_507.SafetyFactorOptimisationStepResult)

        @property
        def safety_factor_optimisation_step_result_number(
            self: "SafetyFactorOptimisationStepResultNumber._Cast_SafetyFactorOptimisationStepResultNumber",
        ) -> "SafetyFactorOptimisationStepResultNumber":
            return self._parent

        def __getattr__(
            self: "SafetyFactorOptimisationStepResultNumber._Cast_SafetyFactorOptimisationStepResultNumber",
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
        self: Self, instance_to_wrap: "SafetyFactorOptimisationStepResultNumber.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def value(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Value

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "SafetyFactorOptimisationStepResultNumber._Cast_SafetyFactorOptimisationStepResultNumber":
        return self._Cast_SafetyFactorOptimisationStepResultNumber(self)
