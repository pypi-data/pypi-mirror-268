"""ElementPropertiesSolid"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_SOLID = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementPropertiesSolid",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesSolid",)


Self = TypeVar("Self", bound="ElementPropertiesSolid")


class ElementPropertiesSolid(_219.ElementPropertiesWithMaterial):
    """ElementPropertiesSolid

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_SOLID
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementPropertiesSolid")

    class _Cast_ElementPropertiesSolid:
        """Special nested class for casting ElementPropertiesSolid to subclasses."""

        def __init__(
            self: "ElementPropertiesSolid._Cast_ElementPropertiesSolid",
            parent: "ElementPropertiesSolid",
        ):
            self._parent = parent

        @property
        def element_properties_with_material(
            self: "ElementPropertiesSolid._Cast_ElementPropertiesSolid",
        ) -> "_219.ElementPropertiesWithMaterial":
            return self._parent._cast(_219.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(
            self: "ElementPropertiesSolid._Cast_ElementPropertiesSolid",
        ) -> "_211.ElementPropertiesBase":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211

            return self._parent._cast(_211.ElementPropertiesBase)

        @property
        def element_properties_solid(
            self: "ElementPropertiesSolid._Cast_ElementPropertiesSolid",
        ) -> "ElementPropertiesSolid":
            return self._parent

        def __getattr__(
            self: "ElementPropertiesSolid._Cast_ElementPropertiesSolid", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementPropertiesSolid.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ElementPropertiesSolid._Cast_ElementPropertiesSolid":
        return self._Cast_ElementPropertiesSolid(self)
