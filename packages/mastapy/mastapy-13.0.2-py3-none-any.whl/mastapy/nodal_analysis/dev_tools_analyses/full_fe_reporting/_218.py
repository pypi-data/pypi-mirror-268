"""ElementPropertiesSpringDashpot"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _211
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_SPRING_DASHPOT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementPropertiesSpringDashpot",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElementPropertiesSpringDashpot",)


Self = TypeVar("Self", bound="ElementPropertiesSpringDashpot")


class ElementPropertiesSpringDashpot(_211.ElementPropertiesBase):
    """ElementPropertiesSpringDashpot

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_SPRING_DASHPOT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementPropertiesSpringDashpot")

    class _Cast_ElementPropertiesSpringDashpot:
        """Special nested class for casting ElementPropertiesSpringDashpot to subclasses."""

        def __init__(
            self: "ElementPropertiesSpringDashpot._Cast_ElementPropertiesSpringDashpot",
            parent: "ElementPropertiesSpringDashpot",
        ):
            self._parent = parent

        @property
        def element_properties_base(
            self: "ElementPropertiesSpringDashpot._Cast_ElementPropertiesSpringDashpot",
        ) -> "_211.ElementPropertiesBase":
            return self._parent._cast(_211.ElementPropertiesBase)

        @property
        def element_properties_spring_dashpot(
            self: "ElementPropertiesSpringDashpot._Cast_ElementPropertiesSpringDashpot",
        ) -> "ElementPropertiesSpringDashpot":
            return self._parent

        def __getattr__(
            self: "ElementPropertiesSpringDashpot._Cast_ElementPropertiesSpringDashpot",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementPropertiesSpringDashpot.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_freedom_1(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DegreeOfFreedom1

        if temp is None:
            return 0

        return temp

    @property
    def degree_of_freedom_2(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DegreeOfFreedom2

        if temp is None:
            return 0

        return temp

    @property
    def stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Stiffness

        if temp is None:
            return 0.0

        return temp

    @stiffness.setter
    @enforce_parameter_types
    def stiffness(self: Self, value: "float"):
        self.wrapped.Stiffness = float(value) if value is not None else 0.0

    @property
    def stiffness_matrix_lower_triangle(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessMatrixLowerTriangle

        if temp is None:
            return ""

        return temp

    @property
    def stiffness_rotation(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessRotation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def stiffness_translation(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessTranslation

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ElementPropertiesSpringDashpot._Cast_ElementPropertiesSpringDashpot":
        return self._Cast_ElementPropertiesSpringDashpot(self)
