"""MeshRequestResult"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Dict

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.nodal_analysis.geometry_modeller_link import _159
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_REQUEST_RESULT = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.GeometryModellerLink", "MeshRequestResult"
)

if TYPE_CHECKING:
    from mastapy.geometry.two_d import _314
    from mastapy.math_utility import _1518
    from mastapy.nodal_analysis.geometry_modeller_link import _158


__docformat__ = "restructuredtext en"
__all__ = ("MeshRequestResult",)


Self = TypeVar("Self", bound="MeshRequestResult")


class MeshRequestResult(_0.APIBase):
    """MeshRequestResult

    This is a mastapy class.
    """

    TYPE = _MESH_REQUEST_RESULT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshRequestResult")

    class _Cast_MeshRequestResult:
        """Special nested class for casting MeshRequestResult to subclasses."""

        def __init__(
            self: "MeshRequestResult._Cast_MeshRequestResult",
            parent: "MeshRequestResult",
        ):
            self._parent = parent

        @property
        def mesh_request_result(
            self: "MeshRequestResult._Cast_MeshRequestResult",
        ) -> "MeshRequestResult":
            return self._parent

        def __getattr__(self: "MeshRequestResult._Cast_MeshRequestResult", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshRequestResult.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def aborted(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Aborted

        if temp is None:
            return False

        return temp

    @aborted.setter
    @enforce_parameter_types
    def aborted(self: Self, value: "bool"):
        self.wrapped.Aborted = bool(value) if value is not None else False

    @property
    def body_moniker(self: Self) -> "str":
        """str"""
        temp = self.wrapped.BodyMoniker

        if temp is None:
            return ""

        return temp

    @body_moniker.setter
    @enforce_parameter_types
    def body_moniker(self: Self, value: "str"):
        self.wrapped.BodyMoniker = str(value) if value is not None else ""

    @property
    def cad_face_group(self: Self) -> "_314.CADFaceGroup":
        """mastapy.geometry.two_d.CADFaceGroup"""
        temp = self.wrapped.CADFaceGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @cad_face_group.setter
    @enforce_parameter_types
    def cad_face_group(self: Self, value: "_314.CADFaceGroup"):
        self.wrapped.CADFaceGroup = value.wrapped

    @property
    def data_file_name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.DataFileName

        if temp is None:
            return ""

        return temp

    @data_file_name.setter
    @enforce_parameter_types
    def data_file_name(self: Self, value: "str"):
        self.wrapped.DataFileName = str(value) if value is not None else ""

    @property
    def error_message(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ErrorMessage

        if temp is None:
            return ""

        return temp

    @error_message.setter
    @enforce_parameter_types
    def error_message(self: Self, value: "str"):
        self.wrapped.ErrorMessage = str(value) if value is not None else ""

    @property
    def faceted_body(self: Self) -> "_1518.FacetedBody":
        """mastapy.math_utility.FacetedBody"""
        temp = self.wrapped.FacetedBody

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @faceted_body.setter
    @enforce_parameter_types
    def faceted_body(self: Self, value: "_1518.FacetedBody"):
        self.wrapped.FacetedBody = value.wrapped

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

    @enforce_parameter_types
    def set_geometry_modeller_dimensions(
        self: Self, dimensions: "Dict[str, _159.GeometryModellerDimension]"
    ):
        """Method does not return.

        Args:
            dimensions (Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension])
        """
        self.wrapped.SetGeometryModellerDimensions(dimensions)

    @property
    def cast_to(self: Self) -> "MeshRequestResult._Cast_MeshRequestResult":
        return self._Cast_MeshRequestResult(self)
