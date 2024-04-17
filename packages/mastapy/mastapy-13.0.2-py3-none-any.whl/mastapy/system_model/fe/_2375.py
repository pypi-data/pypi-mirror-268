"""CoordinateSystemWithSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COORDINATE_SYSTEM_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "CoordinateSystemWithSelection"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _207


__docformat__ = "restructuredtext en"
__all__ = ("CoordinateSystemWithSelection",)


Self = TypeVar("Self", bound="CoordinateSystemWithSelection")


class CoordinateSystemWithSelection(_0.APIBase):
    """CoordinateSystemWithSelection

    This is a mastapy class.
    """

    TYPE = _COORDINATE_SYSTEM_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CoordinateSystemWithSelection")

    class _Cast_CoordinateSystemWithSelection:
        """Special nested class for casting CoordinateSystemWithSelection to subclasses."""

        def __init__(
            self: "CoordinateSystemWithSelection._Cast_CoordinateSystemWithSelection",
            parent: "CoordinateSystemWithSelection",
        ):
            self._parent = parent

        @property
        def coordinate_system_with_selection(
            self: "CoordinateSystemWithSelection._Cast_CoordinateSystemWithSelection",
        ) -> "CoordinateSystemWithSelection":
            return self._parent

        def __getattr__(
            self: "CoordinateSystemWithSelection._Cast_CoordinateSystemWithSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CoordinateSystemWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coordinate_system(self: Self) -> "_207.CoordinateSystemReporting":
        """mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.CoordinateSystemReporting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def select_nodes_using_this_for_material_orientation(self: Self):
        """Method does not return."""
        self.wrapped.SelectNodesUsingThisForMaterialOrientation()

    @property
    def cast_to(
        self: Self,
    ) -> "CoordinateSystemWithSelection._Cast_CoordinateSystemWithSelection":
        return self._Cast_CoordinateSystemWithSelection(self)
