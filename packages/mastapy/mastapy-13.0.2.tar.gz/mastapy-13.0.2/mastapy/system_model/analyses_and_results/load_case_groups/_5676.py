"""SystemOptimisationGearSet"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_OPTIMISATION_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "SystemOptimisationGearSet",
)


__docformat__ = "restructuredtext en"
__all__ = ("SystemOptimisationGearSet",)


Self = TypeVar("Self", bound="SystemOptimisationGearSet")


class SystemOptimisationGearSet(_0.APIBase):
    """SystemOptimisationGearSet

    This is a mastapy class.
    """

    TYPE = _SYSTEM_OPTIMISATION_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemOptimisationGearSet")

    class _Cast_SystemOptimisationGearSet:
        """Special nested class for casting SystemOptimisationGearSet to subclasses."""

        def __init__(
            self: "SystemOptimisationGearSet._Cast_SystemOptimisationGearSet",
            parent: "SystemOptimisationGearSet",
        ):
            self._parent = parent

        @property
        def system_optimisation_gear_set(
            self: "SystemOptimisationGearSet._Cast_SystemOptimisationGearSet",
        ) -> "SystemOptimisationGearSet":
            return self._parent

        def __getattr__(
            self: "SystemOptimisationGearSet._Cast_SystemOptimisationGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemOptimisationGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def highest_teeth_numbers(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestTeethNumbers

        if temp is None:
            return ""

        return temp

    @property
    def lowest_teeth_numbers(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowestTeethNumbers

        if temp is None:
            return ""

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def number_of_candidate_designs(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCandidateDesigns

        if temp is None:
            return 0

        return temp

    def create_designs(self: Self):
        """Method does not return."""
        self.wrapped.CreateDesigns()

    def create_designs_dont_attempt_to_fix(self: Self):
        """Method does not return."""
        self.wrapped.CreateDesignsDontAttemptToFix()

    @property
    def cast_to(
        self: Self,
    ) -> "SystemOptimisationGearSet._Cast_SystemOptimisationGearSet":
        return self._Cast_SystemOptimisationGearSet(self)
