"""ElementPropertiesMass"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_MASS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementPropertiesMass",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1524


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesMass",)


Self = TypeVar("Self", bound="ElementPropertiesMass")


class ElementPropertiesMass(_211.ElementPropertiesBase):
    """ElementPropertiesMass

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_MASS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementPropertiesMass")

    class _Cast_ElementPropertiesMass:
        """Special nested class for casting ElementPropertiesMass to subclasses."""

        def __init__(
            self: "ElementPropertiesMass._Cast_ElementPropertiesMass",
            parent: "ElementPropertiesMass",
        ):
            self._parent = parent

        @property
        def element_properties_base(
            self: "ElementPropertiesMass._Cast_ElementPropertiesMass",
        ) -> "_211.ElementPropertiesBase":
            return self._parent._cast(_211.ElementPropertiesBase)

        @property
        def element_properties_mass(
            self: "ElementPropertiesMass._Cast_ElementPropertiesMass",
        ) -> "ElementPropertiesMass":
            return self._parent

        def __getattr__(
            self: "ElementPropertiesMass._Cast_ElementPropertiesMass", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementPropertiesMass.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inertia(self: Self) -> "_1524.InertiaTensor":
        """mastapy.math_utility.InertiaTensor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Inertia

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ElementPropertiesMass._Cast_ElementPropertiesMass":
        return self._Cast_ElementPropertiesMass(self)
