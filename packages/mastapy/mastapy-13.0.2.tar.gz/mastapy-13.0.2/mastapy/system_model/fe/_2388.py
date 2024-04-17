"""FEStiffnessGeometry"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_STIFFNESS_GEOMETRY = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FEStiffnessGeometry"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEStiffnessGeometry",)


Self = TypeVar("Self", bound="FEStiffnessGeometry")


class FEStiffnessGeometry(_0.APIBase):
    """FEStiffnessGeometry

    This is a mastapy class.
    """

    TYPE = _FE_STIFFNESS_GEOMETRY
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEStiffnessGeometry")

    class _Cast_FEStiffnessGeometry:
        """Special nested class for casting FEStiffnessGeometry to subclasses."""

        def __init__(
            self: "FEStiffnessGeometry._Cast_FEStiffnessGeometry",
            parent: "FEStiffnessGeometry",
        ):
            self._parent = parent

        @property
        def fe_stiffness_geometry(
            self: "FEStiffnessGeometry._Cast_FEStiffnessGeometry",
        ) -> "FEStiffnessGeometry":
            return self._parent

        def __getattr__(
            self: "FEStiffnessGeometry._Cast_FEStiffnessGeometry", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEStiffnessGeometry.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    def delete_geometry(self: Self):
        """Method does not return."""
        self.wrapped.DeleteGeometry()

    def reduce_file_size(self: Self):
        """Method does not return."""
        self.wrapped.ReduceFileSize()

    @property
    def cast_to(self: Self) -> "FEStiffnessGeometry._Cast_FEStiffnessGeometry":
        return self._Cast_FEStiffnessGeometry(self)
