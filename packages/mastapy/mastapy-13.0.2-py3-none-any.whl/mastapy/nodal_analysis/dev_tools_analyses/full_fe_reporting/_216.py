"""ElementPropertiesShell"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _219
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_SHELL = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementPropertiesShell",
)

if TYPE_CHECKING:
    from mastapy.fe_tools.vis_tools_global.vis_tools_global_enums import _1243
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesShell",)


Self = TypeVar("Self", bound="ElementPropertiesShell")


class ElementPropertiesShell(_219.ElementPropertiesWithMaterial):
    """ElementPropertiesShell

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_SHELL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementPropertiesShell")

    class _Cast_ElementPropertiesShell:
        """Special nested class for casting ElementPropertiesShell to subclasses."""

        def __init__(
            self: "ElementPropertiesShell._Cast_ElementPropertiesShell",
            parent: "ElementPropertiesShell",
        ):
            self._parent = parent

        @property
        def element_properties_with_material(
            self: "ElementPropertiesShell._Cast_ElementPropertiesShell",
        ) -> "_219.ElementPropertiesWithMaterial":
            return self._parent._cast(_219.ElementPropertiesWithMaterial)

        @property
        def element_properties_base(
            self: "ElementPropertiesShell._Cast_ElementPropertiesShell",
        ) -> "_211.ElementPropertiesBase":
            from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211

            return self._parent._cast(_211.ElementPropertiesBase)

        @property
        def element_properties_shell(
            self: "ElementPropertiesShell._Cast_ElementPropertiesShell",
        ) -> "ElementPropertiesShell":
            return self._parent

        def __getattr__(
            self: "ElementPropertiesShell._Cast_ElementPropertiesShell", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementPropertiesShell.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_shear_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveShearRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def layer_thicknesses(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LayerThicknesses

        if temp is None:
            return ""

        return temp

    @property
    def number_of_layers(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfLayers

        if temp is None:
            return 0

        return temp

    @property
    def thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Thickness

        if temp is None:
            return 0.0

        return temp

    @property
    def wall_type(self: Self) -> "_1243.ElementPropertiesShellWallType":
        """mastapy.fe_tools.vis_tools_global.vis_tools_global_enums.ElementPropertiesShellWallType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WallType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.FETools.VisToolsGlobal.VisToolsGlobalEnums.ElementPropertiesShellWallType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.fe_tools.vis_tools_global.vis_tools_global_enums._1243",
            "ElementPropertiesShellWallType",
        )(value)

    @property
    def cast_to(self: Self) -> "ElementPropertiesShell._Cast_ElementPropertiesShell":
        return self._Cast_ElementPropertiesShell(self)
