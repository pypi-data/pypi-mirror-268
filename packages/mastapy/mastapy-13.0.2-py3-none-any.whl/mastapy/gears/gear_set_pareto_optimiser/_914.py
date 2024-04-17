"""GearSetOptimiserCandidate"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_set_pareto_optimiser import _910
from mastapy.gears.rating import _358
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISER_CANDIDATE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser", "GearSetOptimiserCandidate"
)


__docformat__ = "restructuredtext en"
__all__ = ("GearSetOptimiserCandidate",)


Self = TypeVar("Self", bound="GearSetOptimiserCandidate")


class GearSetOptimiserCandidate(
    _910.DesignSpaceSearchCandidateBase[
        "_358.AbstractGearSetRating", "GearSetOptimiserCandidate"
    ]
):
    """GearSetOptimiserCandidate

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISER_CANDIDATE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetOptimiserCandidate")

    class _Cast_GearSetOptimiserCandidate:
        """Special nested class for casting GearSetOptimiserCandidate to subclasses."""

        def __init__(
            self: "GearSetOptimiserCandidate._Cast_GearSetOptimiserCandidate",
            parent: "GearSetOptimiserCandidate",
        ):
            self._parent = parent

        @property
        def design_space_search_candidate_base(
            self: "GearSetOptimiserCandidate._Cast_GearSetOptimiserCandidate",
        ) -> "_910.DesignSpaceSearchCandidateBase":
            pass

            return self._parent._cast(_910.DesignSpaceSearchCandidateBase)

        @property
        def gear_set_optimiser_candidate(
            self: "GearSetOptimiserCandidate._Cast_GearSetOptimiserCandidate",
        ) -> "GearSetOptimiserCandidate":
            return self._parent

        def __getattr__(
            self: "GearSetOptimiserCandidate._Cast_GearSetOptimiserCandidate", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetOptimiserCandidate.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def candidate(self: Self) -> "_358.AbstractGearSetRating":
        """mastapy.gears.rating.AbstractGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Candidate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def add_design(self: Self):
        """Method does not return."""
        self.wrapped.AddDesign()

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetOptimiserCandidate._Cast_GearSetOptimiserCandidate":
        return self._Cast_GearSetOptimiserCandidate(self)
