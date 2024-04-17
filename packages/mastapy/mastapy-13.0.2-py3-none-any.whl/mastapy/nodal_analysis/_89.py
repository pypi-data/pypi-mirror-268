"""SparseNodalMatrix"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis import _47
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPARSE_NODAL_MATRIX = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "SparseNodalMatrix"
)


__docformat__ = "restructuredtext en"
__all__ = ("SparseNodalMatrix",)


Self = TypeVar("Self", bound="SparseNodalMatrix")


class SparseNodalMatrix(_47.AbstractNodalMatrix):
    """SparseNodalMatrix

    This is a mastapy class.
    """

    TYPE = _SPARSE_NODAL_MATRIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SparseNodalMatrix")

    class _Cast_SparseNodalMatrix:
        """Special nested class for casting SparseNodalMatrix to subclasses."""

        def __init__(
            self: "SparseNodalMatrix._Cast_SparseNodalMatrix",
            parent: "SparseNodalMatrix",
        ):
            self._parent = parent

        @property
        def abstract_nodal_matrix(
            self: "SparseNodalMatrix._Cast_SparseNodalMatrix",
        ) -> "_47.AbstractNodalMatrix":
            return self._parent._cast(_47.AbstractNodalMatrix)

        @property
        def sparse_nodal_matrix(
            self: "SparseNodalMatrix._Cast_SparseNodalMatrix",
        ) -> "SparseNodalMatrix":
            return self._parent

        def __getattr__(self: "SparseNodalMatrix._Cast_SparseNodalMatrix", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SparseNodalMatrix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "SparseNodalMatrix._Cast_SparseNodalMatrix":
        return self._Cast_SparseNodalMatrix(self)
