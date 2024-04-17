"""OptimisationHistory"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OPTIMISATION_HISTORY = python_net_import(
    "SMT.MastaAPI.MathUtility.Optimisation", "OptimisationHistory"
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1552


__docformat__ = "restructuredtext en"
__all__ = ("OptimisationHistory",)


Self = TypeVar("Self", bound="OptimisationHistory")


class OptimisationHistory(_0.APIBase):
    """OptimisationHistory

    This is a mastapy class.
    """

    TYPE = _OPTIMISATION_HISTORY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OptimisationHistory")

    class _Cast_OptimisationHistory:
        """Special nested class for casting OptimisationHistory to subclasses."""

        def __init__(
            self: "OptimisationHistory._Cast_OptimisationHistory",
            parent: "OptimisationHistory",
        ):
            self._parent = parent

        @property
        def optimisation_history(
            self: "OptimisationHistory._Cast_OptimisationHistory",
        ) -> "OptimisationHistory":
            return self._parent

        def __getattr__(
            self: "OptimisationHistory._Cast_OptimisationHistory", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OptimisationHistory.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def input_history(self: Self) -> "List[_1552.OptimizationVariable]":
        """List[mastapy.math_utility.optimisation.OptimizationVariable]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputHistory

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def input_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InputNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @property
    def target_history(self: Self) -> "List[_1552.OptimizationVariable]":
        """List[mastapy.math_utility.optimisation.OptimizationVariable]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TargetHistory

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def target_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TargetNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def add_input_history(self: Self, value: "_1552.OptimizationVariable"):
        """Method does not return.

        Args:
            value (mastapy.math_utility.optimisation.OptimizationVariable)
        """
        self.wrapped.AddInputHistory(value.wrapped if value else None)

    @enforce_parameter_types
    def add_target_history(self: Self, value: "_1552.OptimizationVariable"):
        """Method does not return.

        Args:
            value (mastapy.math_utility.optimisation.OptimizationVariable)
        """
        self.wrapped.AddTargetHistory(value.wrapped if value else None)

    @property
    def cast_to(self: Self) -> "OptimisationHistory._Cast_OptimisationHistory":
        return self._Cast_OptimisationHistory(self)
