"""RealCMSResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.nodal_analysis.component_mode_synthesis import _232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REAL_CMS_RESULTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "RealCMSResults"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.states import _127
    from mastapy.nodal_analysis.component_mode_synthesis import _234, _238


__docformat__ = "restructuredtext en"
__all__ = ("RealCMSResults",)


Self = TypeVar("Self", bound="RealCMSResults")


class RealCMSResults(_232.CMSResults):
    """RealCMSResults

    This is a mastapy class.
    """

    TYPE = _REAL_CMS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RealCMSResults")

    class _Cast_RealCMSResults:
        """Special nested class for casting RealCMSResults to subclasses."""

        def __init__(
            self: "RealCMSResults._Cast_RealCMSResults", parent: "RealCMSResults"
        ):
            self._parent = parent

        @property
        def cms_results(
            self: "RealCMSResults._Cast_RealCMSResults",
        ) -> "_232.CMSResults":
            return self._parent._cast(_232.CMSResults)

        @property
        def modal_cms_results(
            self: "RealCMSResults._Cast_RealCMSResults",
        ) -> "_234.ModalCMSResults":
            from mastapy.nodal_analysis.component_mode_synthesis import _234

            return self._parent._cast(_234.ModalCMSResults)

        @property
        def static_cms_results(
            self: "RealCMSResults._Cast_RealCMSResults",
        ) -> "_238.StaticCMSResults":
            from mastapy.nodal_analysis.component_mode_synthesis import _238

            return self._parent._cast(_238.StaticCMSResults)

        @property
        def real_cms_results(
            self: "RealCMSResults._Cast_RealCMSResults",
        ) -> "RealCMSResults":
            return self._parent

        def __getattr__(self: "RealCMSResults._Cast_RealCMSResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RealCMSResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_displacements(self: Self) -> "_127.NodeVectorState":
        """mastapy.nodal_analysis.states.NodeVectorState

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeDisplacements

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RealCMSResults._Cast_RealCMSResults":
        return self._Cast_RealCMSResults(self)
