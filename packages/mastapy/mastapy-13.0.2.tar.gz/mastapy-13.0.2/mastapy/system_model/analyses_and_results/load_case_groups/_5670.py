"""ConceptSynchroGearEngagementStatus"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.load_case_groups import _5673
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_SYNCHRO_GEAR_ENGAGEMENT_STATUS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "ConceptSynchroGearEngagementStatus",
)


__docformat__ = "restructuredtext en"
__all__ = ("ConceptSynchroGearEngagementStatus",)


Self = TypeVar("Self", bound="ConceptSynchroGearEngagementStatus")


class ConceptSynchroGearEngagementStatus(
    _5673.GenericClutchEngagementStatus["_2532.CylindricalGear"]
):
    """ConceptSynchroGearEngagementStatus

    This is a mastapy class.
    """

    TYPE = _CONCEPT_SYNCHRO_GEAR_ENGAGEMENT_STATUS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptSynchroGearEngagementStatus")

    class _Cast_ConceptSynchroGearEngagementStatus:
        """Special nested class for casting ConceptSynchroGearEngagementStatus to subclasses."""

        def __init__(
            self: "ConceptSynchroGearEngagementStatus._Cast_ConceptSynchroGearEngagementStatus",
            parent: "ConceptSynchroGearEngagementStatus",
        ):
            self._parent = parent

        @property
        def generic_clutch_engagement_status(
            self: "ConceptSynchroGearEngagementStatus._Cast_ConceptSynchroGearEngagementStatus",
        ) -> "_5673.GenericClutchEngagementStatus":
            return self._parent._cast(_5673.GenericClutchEngagementStatus)

        @property
        def concept_synchro_gear_engagement_status(
            self: "ConceptSynchroGearEngagementStatus._Cast_ConceptSynchroGearEngagementStatus",
        ) -> "ConceptSynchroGearEngagementStatus":
            return self._parent

        def __getattr__(
            self: "ConceptSynchroGearEngagementStatus._Cast_ConceptSynchroGearEngagementStatus",
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
        self: Self, instance_to_wrap: "ConceptSynchroGearEngagementStatus.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptSynchroGearEngagementStatus._Cast_ConceptSynchroGearEngagementStatus":
        return self._Cast_ConceptSynchroGearEngagementStatus(self)
