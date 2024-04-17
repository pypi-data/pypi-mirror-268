"""StaticCMSResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.nodal_analysis.component_mode_synthesis import _235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STATIC_CMS_RESULTS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "StaticCMSResults"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.states import _127
    from mastapy.nodal_analysis.component_mode_synthesis import _232


__docformat__ = "restructuredtext en"
__all__ = ("StaticCMSResults",)


Self = TypeVar("Self", bound="StaticCMSResults")


class StaticCMSResults(_235.RealCMSResults):
    """StaticCMSResults

    This is a mastapy class.
    """

    TYPE = _STATIC_CMS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StaticCMSResults")

    class _Cast_StaticCMSResults:
        """Special nested class for casting StaticCMSResults to subclasses."""

        def __init__(
            self: "StaticCMSResults._Cast_StaticCMSResults", parent: "StaticCMSResults"
        ):
            self._parent = parent

        @property
        def real_cms_results(
            self: "StaticCMSResults._Cast_StaticCMSResults",
        ) -> "_235.RealCMSResults":
            return self._parent._cast(_235.RealCMSResults)

        @property
        def cms_results(
            self: "StaticCMSResults._Cast_StaticCMSResults",
        ) -> "_232.CMSResults":
            from mastapy.nodal_analysis.component_mode_synthesis import _232

            return self._parent._cast(_232.CMSResults)

        @property
        def static_cms_results(
            self: "StaticCMSResults._Cast_StaticCMSResults",
        ) -> "StaticCMSResults":
            return self._parent

        def __getattr__(self: "StaticCMSResults._Cast_StaticCMSResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StaticCMSResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_stress_tensors(self: Self) -> "_127.NodeVectorState":
        """mastapy.nodal_analysis.states.NodeVectorState

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeStressTensors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def calculate_stress(self: Self):
        """Method does not return."""
        self.wrapped.CalculateStress()

    @property
    def cast_to(self: Self) -> "StaticCMSResults._Cast_StaticCMSResults":
        return self._Cast_StaticCMSResults(self)
