"""MaterialPropertiesWithSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL_PROPERTIES_WITH_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "MaterialPropertiesWithSelection"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _220


__docformat__ = "restructuredtext en"
__all__ = ("MaterialPropertiesWithSelection",)


Self = TypeVar("Self", bound="MaterialPropertiesWithSelection")


class MaterialPropertiesWithSelection(_0.APIBase):
    """MaterialPropertiesWithSelection

    This is a mastapy class.
    """

    TYPE = _MATERIAL_PROPERTIES_WITH_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaterialPropertiesWithSelection")

    class _Cast_MaterialPropertiesWithSelection:
        """Special nested class for casting MaterialPropertiesWithSelection to subclasses."""

        def __init__(
            self: "MaterialPropertiesWithSelection._Cast_MaterialPropertiesWithSelection",
            parent: "MaterialPropertiesWithSelection",
        ):
            self._parent = parent

        @property
        def material_properties_with_selection(
            self: "MaterialPropertiesWithSelection._Cast_MaterialPropertiesWithSelection",
        ) -> "MaterialPropertiesWithSelection":
            return self._parent

        def __getattr__(
            self: "MaterialPropertiesWithSelection._Cast_MaterialPropertiesWithSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaterialPropertiesWithSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def material_properties(self: Self) -> "_220.MaterialPropertiesReporting":
        """mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.MaterialPropertiesReporting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialProperties

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def select_nodes(self: Self):
        """Method does not return."""
        self.wrapped.SelectNodes()

    @property
    def cast_to(
        self: Self,
    ) -> "MaterialPropertiesWithSelection._Cast_MaterialPropertiesWithSelection":
        return self._Cast_MaterialPropertiesWithSelection(self)
