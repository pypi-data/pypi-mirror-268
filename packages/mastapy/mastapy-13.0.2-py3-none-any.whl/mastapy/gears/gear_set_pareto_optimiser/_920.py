"""MicroGeometryDesignSpaceSearchCandidate"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.gear_set_pareto_optimiser import _910
from mastapy.gears.ltca.cylindrical import _863
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CANDIDATE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "MicroGeometryDesignSpaceSearchCandidate",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1113


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryDesignSpaceSearchCandidate",)


Self = TypeVar("Self", bound="MicroGeometryDesignSpaceSearchCandidate")


class MicroGeometryDesignSpaceSearchCandidate(
    _910.DesignSpaceSearchCandidateBase[
        "_863.CylindricalGearSetLoadDistributionAnalysis",
        "MicroGeometryDesignSpaceSearchCandidate",
    ]
):
    """MicroGeometryDesignSpaceSearchCandidate

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CANDIDATE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MicroGeometryDesignSpaceSearchCandidate"
    )

    class _Cast_MicroGeometryDesignSpaceSearchCandidate:
        """Special nested class for casting MicroGeometryDesignSpaceSearchCandidate to subclasses."""

        def __init__(
            self: "MicroGeometryDesignSpaceSearchCandidate._Cast_MicroGeometryDesignSpaceSearchCandidate",
            parent: "MicroGeometryDesignSpaceSearchCandidate",
        ):
            self._parent = parent

        @property
        def design_space_search_candidate_base(
            self: "MicroGeometryDesignSpaceSearchCandidate._Cast_MicroGeometryDesignSpaceSearchCandidate",
        ) -> "_910.DesignSpaceSearchCandidateBase":
            pass

            return self._parent._cast(_910.DesignSpaceSearchCandidateBase)

        @property
        def micro_geometry_design_space_search_candidate(
            self: "MicroGeometryDesignSpaceSearchCandidate._Cast_MicroGeometryDesignSpaceSearchCandidate",
        ) -> "MicroGeometryDesignSpaceSearchCandidate":
            return self._parent

        def __getattr__(
            self: "MicroGeometryDesignSpaceSearchCandidate._Cast_MicroGeometryDesignSpaceSearchCandidate",
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
        self: Self, instance_to_wrap: "MicroGeometryDesignSpaceSearchCandidate.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def candidate(self: Self) -> "_863.CylindricalGearSetLoadDistributionAnalysis":
        """mastapy.gears.ltca.cylindrical.CylindricalGearSetLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Candidate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def candidate_for_slider(self: Self) -> "_1113.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CandidateForSlider

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
    ) -> "MicroGeometryDesignSpaceSearchCandidate._Cast_MicroGeometryDesignSpaceSearchCandidate":
        return self._Cast_MicroGeometryDesignSpaceSearchCandidate(self)
