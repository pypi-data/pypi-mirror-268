"""ContactPairWithSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTACT_PAIR_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "ContactPairWithSelection"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _206


__docformat__ = "restructuredtext en"
__all__ = ("ContactPairWithSelection",)


Self = TypeVar("Self", bound="ContactPairWithSelection")


class ContactPairWithSelection(_0.APIBase):
    """ContactPairWithSelection

    This is a mastapy class.
    """

    TYPE = _CONTACT_PAIR_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ContactPairWithSelection")

    class _Cast_ContactPairWithSelection:
        """Special nested class for casting ContactPairWithSelection to subclasses."""

        def __init__(
            self: "ContactPairWithSelection._Cast_ContactPairWithSelection",
            parent: "ContactPairWithSelection",
        ):
            self._parent = parent

        @property
        def contact_pair_with_selection(
            self: "ContactPairWithSelection._Cast_ContactPairWithSelection",
        ) -> "ContactPairWithSelection":
            return self._parent

        def __getattr__(
            self: "ContactPairWithSelection._Cast_ContactPairWithSelection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ContactPairWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_pair(self: Self) -> "_206.ContactPairReporting":
        """mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ContactPairReporting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPair

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def select_constrained_surface(self: Self):
        """Method does not return."""
        self.wrapped.SelectConstrainedSurface()

    def select_contacting_constrained_surface(self: Self):
        """Method does not return."""
        self.wrapped.SelectContactingConstrainedSurface()

    def select_contacting_reference_surface(self: Self):
        """Method does not return."""
        self.wrapped.SelectContactingReferenceSurface()

    def select_reference_surface(self: Self):
        """Method does not return."""
        self.wrapped.SelectReferenceSurface()

    @property
    def cast_to(
        self: Self,
    ) -> "ContactPairWithSelection._Cast_ContactPairWithSelection":
        return self._Cast_ContactPairWithSelection(self)
