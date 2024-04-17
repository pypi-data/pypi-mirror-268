"""CMSNodeGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis.dev_tools_analyses import _203
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_NODE_GROUP = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "CMSNodeGroup"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _186, _185


__docformat__ = "restructuredtext en"
__all__ = ("CMSNodeGroup",)


Self = TypeVar("Self", bound="CMSNodeGroup")


class CMSNodeGroup(_203.NodeGroup):
    """CMSNodeGroup

    This is a mastapy class.
    """

    TYPE = _CMS_NODE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CMSNodeGroup")

    class _Cast_CMSNodeGroup:
        """Special nested class for casting CMSNodeGroup to subclasses."""

        def __init__(self: "CMSNodeGroup._Cast_CMSNodeGroup", parent: "CMSNodeGroup"):
            self._parent = parent

        @property
        def node_group(self: "CMSNodeGroup._Cast_CMSNodeGroup") -> "_203.NodeGroup":
            return self._parent._cast(_203.NodeGroup)

        @property
        def fe_entity_group_integer(
            self: "CMSNodeGroup._Cast_CMSNodeGroup",
        ) -> "_186.FEEntityGroupInteger":
            from mastapy.nodal_analysis.dev_tools_analyses import _186

            return self._parent._cast(_186.FEEntityGroupInteger)

        @property
        def fe_entity_group(
            self: "CMSNodeGroup._Cast_CMSNodeGroup",
        ) -> "_185.FEEntityGroup":
            from mastapy.nodal_analysis.dev_tools_analyses import _185

            return self._parent._cast(_185.FEEntityGroup)

        @property
        def cms_node_group(self: "CMSNodeGroup._Cast_CMSNodeGroup") -> "CMSNodeGroup":
            return self._parent

        def __getattr__(self: "CMSNodeGroup._Cast_CMSNodeGroup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CMSNodeGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_nvh_results_at_these_nodes(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowNVHResultsAtTheseNodes

        if temp is None:
            return False

        return temp

    @show_nvh_results_at_these_nodes.setter
    @enforce_parameter_types
    def show_nvh_results_at_these_nodes(self: Self, value: "bool"):
        self.wrapped.ShowNVHResultsAtTheseNodes = (
            bool(value) if value is not None else False
        )

    def create_element_face_group(self: Self):
        """Method does not return."""
        self.wrapped.CreateElementFaceGroup()

    @property
    def cast_to(self: Self) -> "CMSNodeGroup._Cast_CMSNodeGroup":
        return self._Cast_CMSNodeGroup(self)
