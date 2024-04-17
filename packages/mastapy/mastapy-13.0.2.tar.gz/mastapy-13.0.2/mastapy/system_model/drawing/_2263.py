"""ShaftDeflectionDrawingNodeItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_DEFLECTION_DRAWING_NODE_ITEM = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "ShaftDeflectionDrawingNodeItem"
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_vectors import _1567
    from mastapy.system_model.analyses_and_results.system_deflections import _2811


__docformat__ = "restructuredtext en"
__all__ = ("ShaftDeflectionDrawingNodeItem",)


Self = TypeVar("Self", bound="ShaftDeflectionDrawingNodeItem")


class ShaftDeflectionDrawingNodeItem(_0.APIBase):
    """ShaftDeflectionDrawingNodeItem

    This is a mastapy class.
    """

    TYPE = _SHAFT_DEFLECTION_DRAWING_NODE_ITEM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftDeflectionDrawingNodeItem")

    class _Cast_ShaftDeflectionDrawingNodeItem:
        """Special nested class for casting ShaftDeflectionDrawingNodeItem to subclasses."""

        def __init__(
            self: "ShaftDeflectionDrawingNodeItem._Cast_ShaftDeflectionDrawingNodeItem",
            parent: "ShaftDeflectionDrawingNodeItem",
        ):
            self._parent = parent

        @property
        def shaft_deflection_drawing_node_item(
            self: "ShaftDeflectionDrawingNodeItem._Cast_ShaftDeflectionDrawingNodeItem",
        ) -> "ShaftDeflectionDrawingNodeItem":
            return self._parent

        def __getattr__(
            self: "ShaftDeflectionDrawingNodeItem._Cast_ShaftDeflectionDrawingNodeItem",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftDeflectionDrawingNodeItem.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def offset(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Offset

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def node_detail(self: Self) -> "_1567.ForceAndDisplacementResults":
        """mastapy.math_utility.measured_vectors.ForceAndDisplacementResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def section_to_the_left_side(self: Self) -> "_2811.ShaftSectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SectionToTheLeftSide

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def section_to_the_right_side(self: Self) -> "_2811.ShaftSectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SectionToTheRightSide

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftDeflectionDrawingNodeItem._Cast_ShaftDeflectionDrawingNodeItem":
        return self._Cast_ShaftDeflectionDrawingNodeItem(self)
