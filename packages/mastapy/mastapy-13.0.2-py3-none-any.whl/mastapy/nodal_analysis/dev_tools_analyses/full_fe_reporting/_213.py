"""ElementPropertiesInterface"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_INTERFACE = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementPropertiesInterface",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesInterface",)


Self = TypeVar("Self", bound="ElementPropertiesInterface")


class ElementPropertiesInterface(_211.ElementPropertiesBase):
    """ElementPropertiesInterface

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_INTERFACE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementPropertiesInterface")

    class _Cast_ElementPropertiesInterface:
        """Special nested class for casting ElementPropertiesInterface to subclasses."""

        def __init__(
            self: "ElementPropertiesInterface._Cast_ElementPropertiesInterface",
            parent: "ElementPropertiesInterface",
        ):
            self._parent = parent

        @property
        def element_properties_base(
            self: "ElementPropertiesInterface._Cast_ElementPropertiesInterface",
        ) -> "_211.ElementPropertiesBase":
            return self._parent._cast(_211.ElementPropertiesBase)

        @property
        def element_properties_interface(
            self: "ElementPropertiesInterface._Cast_ElementPropertiesInterface",
        ) -> "ElementPropertiesInterface":
            return self._parent

        def __getattr__(
            self: "ElementPropertiesInterface._Cast_ElementPropertiesInterface",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementPropertiesInterface.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElementPropertiesInterface._Cast_ElementPropertiesInterface":
        return self._Cast_ElementPropertiesInterface(self)
