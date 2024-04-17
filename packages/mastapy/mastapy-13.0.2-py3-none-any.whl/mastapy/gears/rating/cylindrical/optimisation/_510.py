"""SafetyFactorOptimisationStepResultShortLength"""

from __future__ import annotations

from typing import TypeVar

from mastapy.gears.rating.cylindrical.optimisation import _507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_SHORT_LENGTH = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.Optimisation",
    "SafetyFactorOptimisationStepResultShortLength",
)


__docformat__ = "restructuredtext en"
__all__ = ("SafetyFactorOptimisationStepResultShortLength",)


Self = TypeVar("Self", bound="SafetyFactorOptimisationStepResultShortLength")


class SafetyFactorOptimisationStepResultShortLength(
    _507.SafetyFactorOptimisationStepResult
):
    """SafetyFactorOptimisationStepResultShortLength

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_OPTIMISATION_STEP_RESULT_SHORT_LENGTH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SafetyFactorOptimisationStepResultShortLength"
    )

    class _Cast_SafetyFactorOptimisationStepResultShortLength:
        """Special nested class for casting SafetyFactorOptimisationStepResultShortLength to subclasses."""

        def __init__(
            self: "SafetyFactorOptimisationStepResultShortLength._Cast_SafetyFactorOptimisationStepResultShortLength",
            parent: "SafetyFactorOptimisationStepResultShortLength",
        ):
            self._parent = parent

        @property
        def safety_factor_optimisation_step_result(
            self: "SafetyFactorOptimisationStepResultShortLength._Cast_SafetyFactorOptimisationStepResultShortLength",
        ) -> "_507.SafetyFactorOptimisationStepResult":
            return self._parent._cast(_507.SafetyFactorOptimisationStepResult)

        @property
        def safety_factor_optimisation_step_result_short_length(
            self: "SafetyFactorOptimisationStepResultShortLength._Cast_SafetyFactorOptimisationStepResultShortLength",
        ) -> "SafetyFactorOptimisationStepResultShortLength":
            return self._parent

        def __getattr__(
            self: "SafetyFactorOptimisationStepResultShortLength._Cast_SafetyFactorOptimisationStepResultShortLength",
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
        self: Self,
        instance_to_wrap: "SafetyFactorOptimisationStepResultShortLength.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "SafetyFactorOptimisationStepResultShortLength._Cast_SafetyFactorOptimisationStepResultShortLength":
        return self._Cast_SafetyFactorOptimisationStepResultShortLength(self)
