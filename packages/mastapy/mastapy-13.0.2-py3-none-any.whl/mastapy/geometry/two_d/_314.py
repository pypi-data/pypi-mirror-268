"""CADFaceGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_FACE_GROUP = python_net_import("SMT.MastaAPI.Geometry.TwoD", "CADFaceGroup")

if TYPE_CHECKING:
    from mastapy.geometry.two_d import _313


__docformat__ = "restructuredtext en"
__all__ = ("CADFaceGroup",)


Self = TypeVar("Self", bound="CADFaceGroup")


class CADFaceGroup(_0.APIBase):
    """CADFaceGroup

    This is a mastapy class.
    """

    TYPE = _CAD_FACE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADFaceGroup")

    class _Cast_CADFaceGroup:
        """Special nested class for casting CADFaceGroup to subclasses."""

        def __init__(self: "CADFaceGroup._Cast_CADFaceGroup", parent: "CADFaceGroup"):
            self._parent = parent

        @property
        def cad_face_group(self: "CADFaceGroup._Cast_CADFaceGroup") -> "CADFaceGroup":
            return self._parent

        def __getattr__(self: "CADFaceGroup._Cast_CADFaceGroup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADFaceGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @enforce_parameter_types
    def add_face(self: Self, moniker: "str") -> "_313.CADFace":
        """mastapy.geometry.two_d.CADFace

        Args:
            moniker (str)
        """
        moniker = str(moniker)
        method_result = self.wrapped.AddFace(moniker if moniker else "")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "CADFaceGroup._Cast_CADFaceGroup":
        return self._Cast_CADFaceGroup(self)
