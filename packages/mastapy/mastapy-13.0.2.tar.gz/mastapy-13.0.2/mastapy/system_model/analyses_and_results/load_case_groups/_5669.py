"""ClutchEngagementStatus"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.load_case_groups import _5673
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_ENGAGEMENT_STATUS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "ClutchEngagementStatus",
)


__docformat__ = "restructuredtext en"
__all__ = ("ClutchEngagementStatus",)


Self = TypeVar("Self", bound="ClutchEngagementStatus")


class ClutchEngagementStatus(
    _5673.GenericClutchEngagementStatus["_2349.ClutchConnection"]
):
    """ClutchEngagementStatus

    This is a mastapy class.
    """

    TYPE = _CLUTCH_ENGAGEMENT_STATUS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchEngagementStatus")

    class _Cast_ClutchEngagementStatus:
        """Special nested class for casting ClutchEngagementStatus to subclasses."""

        def __init__(
            self: "ClutchEngagementStatus._Cast_ClutchEngagementStatus",
            parent: "ClutchEngagementStatus",
        ):
            self._parent = parent

        @property
        def generic_clutch_engagement_status(
            self: "ClutchEngagementStatus._Cast_ClutchEngagementStatus",
        ) -> "_5673.GenericClutchEngagementStatus":
            return self._parent._cast(_5673.GenericClutchEngagementStatus)

        @property
        def clutch_engagement_status(
            self: "ClutchEngagementStatus._Cast_ClutchEngagementStatus",
        ) -> "ClutchEngagementStatus":
            return self._parent

        def __getattr__(
            self: "ClutchEngagementStatus._Cast_ClutchEngagementStatus", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchEngagementStatus.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ClutchEngagementStatus._Cast_ClutchEngagementStatus":
        return self._Cast_ClutchEngagementStatus(self)
