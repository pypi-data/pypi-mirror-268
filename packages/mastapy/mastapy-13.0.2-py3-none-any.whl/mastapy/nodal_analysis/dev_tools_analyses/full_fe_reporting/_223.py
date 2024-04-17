"""RigidElementNodeDegreesOfFreedom"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RIGID_ELEMENT_NODE_DEGREES_OF_FREEDOM = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "RigidElementNodeDegreesOfFreedom",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _208


__docformat__ = "restructuredtext en"
__all__ = ("RigidElementNodeDegreesOfFreedom",)


Self = TypeVar("Self", bound="RigidElementNodeDegreesOfFreedom")


class RigidElementNodeDegreesOfFreedom(_0.APIBase):
    """RigidElementNodeDegreesOfFreedom

    This is a mastapy class.
    """

    TYPE = _RIGID_ELEMENT_NODE_DEGREES_OF_FREEDOM
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RigidElementNodeDegreesOfFreedom")

    class _Cast_RigidElementNodeDegreesOfFreedom:
        """Special nested class for casting RigidElementNodeDegreesOfFreedom to subclasses."""

        def __init__(
            self: "RigidElementNodeDegreesOfFreedom._Cast_RigidElementNodeDegreesOfFreedom",
            parent: "RigidElementNodeDegreesOfFreedom",
        ):
            self._parent = parent

        @property
        def rigid_element_node_degrees_of_freedom(
            self: "RigidElementNodeDegreesOfFreedom._Cast_RigidElementNodeDegreesOfFreedom",
        ) -> "RigidElementNodeDegreesOfFreedom":
            return self._parent

        def __getattr__(
            self: "RigidElementNodeDegreesOfFreedom._Cast_RigidElementNodeDegreesOfFreedom",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RigidElementNodeDegreesOfFreedom.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Index

        if temp is None:
            return 0

        return temp

    @property
    def type_(self: Self) -> "_208.DegreeOfFreedomType":
        """mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.DegreeOfFreedomType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Type

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting.DegreeOfFreedomType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting._208",
            "DegreeOfFreedomType",
        )(value)

    @property
    def x(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.X

        if temp is None:
            return False

        return temp

    @x.setter
    @enforce_parameter_types
    def x(self: Self, value: "bool"):
        self.wrapped.X = bool(value) if value is not None else False

    @property
    def y(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Y

        if temp is None:
            return False

        return temp

    @y.setter
    @enforce_parameter_types
    def y(self: Self, value: "bool"):
        self.wrapped.Y = bool(value) if value is not None else False

    @property
    def z(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Z

        if temp is None:
            return False

        return temp

    @z.setter
    @enforce_parameter_types
    def z(self: Self, value: "bool"):
        self.wrapped.Z = bool(value) if value is not None else False

    @property
    def theta_x(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ThetaX

        if temp is None:
            return False

        return temp

    @theta_x.setter
    @enforce_parameter_types
    def theta_x(self: Self, value: "bool"):
        self.wrapped.ThetaX = bool(value) if value is not None else False

    @property
    def theta_y(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ThetaY

        if temp is None:
            return False

        return temp

    @theta_y.setter
    @enforce_parameter_types
    def theta_y(self: Self, value: "bool"):
        self.wrapped.ThetaY = bool(value) if value is not None else False

    @property
    def theta_z(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ThetaZ

        if temp is None:
            return False

        return temp

    @theta_z.setter
    @enforce_parameter_types
    def theta_z(self: Self, value: "bool"):
        self.wrapped.ThetaZ = bool(value) if value is not None else False

    @property
    def cast_to(
        self: Self,
    ) -> "RigidElementNodeDegreesOfFreedom._Cast_RigidElementNodeDegreesOfFreedom":
        return self._Cast_RigidElementNodeDegreesOfFreedom(self)
