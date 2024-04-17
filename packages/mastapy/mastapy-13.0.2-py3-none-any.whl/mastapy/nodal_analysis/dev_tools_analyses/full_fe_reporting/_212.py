"""ElementPropertiesBeam"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_BEAM = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementPropertiesBeam",
)

if TYPE_CHECKING:
    from mastapy.fe_tools.vis_tools_global.vis_tools_global_enums import _1240
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesBeam",)


Self = TypeVar("Self", bound="ElementPropertiesBeam")


class ElementPropertiesBeam(_219.ElementPropertiesWithMaterial):
    """ElementPropertiesBeam

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_BEAM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementPropertiesBeam")

    class _Cast_ElementPropertiesBeam:
        """Special nested class for casting ElementPropertiesBeam to subclasses."""

        def __init__(
            self: "ElementPropertiesBeam._Cast_ElementPropertiesBeam",
            parent: "ElementPropertiesBeam",
        ):
            self._parent = parent

        @property
        def element_properties_with_material(
            self: "ElementPropertiesBeam._Cast_ElementPropertiesBeam",
        ) -> "_219.ElementPropertiesWithMaterial":
            return self._parent._cast(_219.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(
            self: "ElementPropertiesBeam._Cast_ElementPropertiesBeam",
        ) -> "_211.ElementPropertiesBase":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211

            return self._parent._cast(_211.ElementPropertiesBase)

        @property
        def element_properties_beam(
            self: "ElementPropertiesBeam._Cast_ElementPropertiesBeam",
        ) -> "ElementPropertiesBeam":
            return self._parent

        def __getattr__(
            self: "ElementPropertiesBeam._Cast_ElementPropertiesBeam", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementPropertiesBeam.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def section_dimensions(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SectionDimensions

        if temp is None:
            return ""

        return temp

    @property
    def section_type(self: Self) -> "_1240.BeamSectionType":
        """mastapy.fe_tools.vis_tools_global.vis_tools_global_enums.BeamSectionType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SectionType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.FETools.VisToolsGlobal.VisToolsGlobalEnums.BeamSectionType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.fe_tools.vis_tools_global.vis_tools_global_enums._1240",
            "BeamSectionType",
        )(value)

    @property
    def cast_to(self: Self) -> "ElementPropertiesBeam._Cast_ElementPropertiesBeam":
        return self._Cast_ElementPropertiesBeam(self)
