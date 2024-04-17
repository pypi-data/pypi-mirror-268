"""GenericClutchEngagementStatus"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GENERIC_CLUTCH_ENGAGEMENT_STATUS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "GenericClutchEngagementStatus",
)

if TYPE_CHECKING:
    from mastapy.system_model import _2210
    from mastapy.system_model.analyses_and_results.load_case_groups import _5669, _5670


__docformat__ = "restructuredtext en"
__all__ = ("GenericClutchEngagementStatus",)


Self = TypeVar("Self", bound="GenericClutchEngagementStatus")
T = TypeVar("T", bound="_2210.DesignEntity")


class GenericClutchEngagementStatus(_0.APIBase, Generic[T]):
    """GenericClutchEngagementStatus

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _GENERIC_CLUTCH_ENGAGEMENT_STATUS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GenericClutchEngagementStatus")

    class _Cast_GenericClutchEngagementStatus:
        """Special nested class for casting GenericClutchEngagementStatus to subclasses."""

        def __init__(
            self: "GenericClutchEngagementStatus._Cast_GenericClutchEngagementStatus",
            parent: "GenericClutchEngagementStatus",
        ):
            self._parent = parent

        @property
        def clutch_engagement_status(
            self: "GenericClutchEngagementStatus._Cast_GenericClutchEngagementStatus",
        ) -> "_5669.ClutchEngagementStatus":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5669

            return self._parent._cast(_5669.ClutchEngagementStatus)

        @property
        def concept_synchro_gear_engagement_status(
            self: "GenericClutchEngagementStatus._Cast_GenericClutchEngagementStatus",
        ) -> "_5670.ConceptSynchroGearEngagementStatus":
            from mastapy.system_model.analyses_and_results.load_case_groups import _5670

            return self._parent._cast(_5670.ConceptSynchroGearEngagementStatus)

        @property
        def generic_clutch_engagement_status(
            self: "GenericClutchEngagementStatus._Cast_GenericClutchEngagementStatus",
        ) -> "GenericClutchEngagementStatus":
            return self._parent

        def __getattr__(
            self: "GenericClutchEngagementStatus._Cast_GenericClutchEngagementStatus",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GenericClutchEngagementStatus.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_engaged(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsEngaged

        if temp is None:
            return False

        return temp

    @is_engaged.setter
    @enforce_parameter_types
    def is_engaged(self: Self, value: "bool"):
        self.wrapped.IsEngaged = bool(value) if value is not None else False

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
    def unique_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UniqueName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GenericClutchEngagementStatus._Cast_GenericClutchEngagementStatus":
        return self._Cast_GenericClutchEngagementStatus(self)
