"""ShaftSectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _129
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_SECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ShaftSectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2810
    from mastapy.nodal_analysis.nodal_entities import _145, _147


__docformat__ = "restructuredtext en"
__all__ = ("ShaftSectionSystemDeflection",)


Self = TypeVar("Self", bound="ShaftSectionSystemDeflection")


class ShaftSectionSystemDeflection(_129.Bar):
    """ShaftSectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_SECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftSectionSystemDeflection")

    class _Cast_ShaftSectionSystemDeflection:
        """Special nested class for casting ShaftSectionSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
            parent: "ShaftSectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def bar(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
        ) -> "_129.Bar":
            return self._parent._cast(_129.Bar)

        @property
        def nodal_component(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
        ) -> "_145.NodalComponent":
            from mastapy.nodal_analysis.nodal_entities import _145

            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
        ) -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def shaft_section_system_deflection(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
        ) -> "ShaftSectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftSectionSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_end(self: Self) -> "_2810.ShaftSectionEndResultsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionEndResultsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftEnd

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_end(self: Self) -> "_2810.ShaftSectionEndResultsSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftSectionEndResultsSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightEnd

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftSectionSystemDeflection._Cast_ShaftSectionSystemDeflection":
        return self._Cast_ShaftSectionSystemDeflection(self)
