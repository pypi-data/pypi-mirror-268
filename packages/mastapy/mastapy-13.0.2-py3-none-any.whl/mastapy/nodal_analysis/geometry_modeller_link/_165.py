"""MeshRequest"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Dict

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.nodal_analysis.geometry_modeller_link import _159
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_REQUEST = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "MeshRequest"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.geometry_modeller_link import _158


__docformat__ = "restructuredtext en"
__all__ = ("MeshRequest",)


Self = TypeVar("Self", bound="MeshRequest")


class MeshRequest(_0.APIBase):
    """MeshRequest

    This is a mastapy class.
    """

    TYPE = _MESH_REQUEST
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshRequest")

    class _Cast_MeshRequest:
        """Special nested class for casting MeshRequest to subclasses."""

        def __init__(self: "MeshRequest._Cast_MeshRequest", parent: "MeshRequest"):
            self._parent = parent

        @property
        def mesh_request(self: "MeshRequest._Cast_MeshRequest") -> "MeshRequest":
            return self._parent

        def __getattr__(self: "MeshRequest._Cast_MeshRequest", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshRequest.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cad_face_group(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CADFaceGroup

        if temp is None:
            return False

        return temp

    @cad_face_group.setter
    @enforce_parameter_types
    def cad_face_group(self: Self, value: "bool"):
        self.wrapped.CADFaceGroup = bool(value) if value is not None else False

    @property
    def geometry_modeller_design_information(
        self: Self,
    ) -> "_158.GeometryModellerDesignInformation":
        """mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation"""
        temp = self.wrapped.GeometryModellerDesignInformation

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @geometry_modeller_design_information.setter
    @enforce_parameter_types
    def geometry_modeller_design_information(
        self: Self, value: "_158.GeometryModellerDesignInformation"
    ):
        self.wrapped.GeometryModellerDesignInformation = value.wrapped

    @property
    def moniker(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Moniker

        if temp is None:
            return ""

        return temp

    @moniker.setter
    @enforce_parameter_types
    def moniker(self: Self, value: "str"):
        self.wrapped.Moniker = str(value) if value is not None else ""

    def geometry_modeller_dimensions(
        self: Self,
    ) -> "Dict[str, _159.GeometryModellerDimension]":
        """Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension]"""
        method_result = self.wrapped.GeometryModellerDimensions()
        return method_result

    @property
    def cast_to(self: Self) -> "MeshRequest._Cast_MeshRequest":
        return self._Cast_MeshRequest(self)
