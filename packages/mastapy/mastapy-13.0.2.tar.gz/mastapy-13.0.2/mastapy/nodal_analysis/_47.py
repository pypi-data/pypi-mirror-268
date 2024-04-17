"""AbstractNodalMatrix"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_NODAL_MATRIX = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "AbstractNodalMatrix"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _79, _89


__docformat__ = "restructuredtext en"
__all__ = ("AbstractNodalMatrix",)


Self = TypeVar("Self", bound="AbstractNodalMatrix")


class AbstractNodalMatrix(_0.APIBase):
    """AbstractNodalMatrix

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_NODAL_MATRIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractNodalMatrix")

    class _Cast_AbstractNodalMatrix:
        """Special nested class for casting AbstractNodalMatrix to subclasses."""

        def __init__(
            self: "AbstractNodalMatrix._Cast_AbstractNodalMatrix",
            parent: "AbstractNodalMatrix",
        ):
            self._parent = parent

        @property
        def nodal_matrix(
            self: "AbstractNodalMatrix._Cast_AbstractNodalMatrix",
        ) -> "_79.NodalMatrix":
            from mastapy.nodal_analysis import _79

            return self._parent._cast(_79.NodalMatrix)

        @property
        def sparse_nodal_matrix(
            self: "AbstractNodalMatrix._Cast_AbstractNodalMatrix",
        ) -> "_89.SparseNodalMatrix":
            from mastapy.nodal_analysis import _89

            return self._parent._cast(_89.SparseNodalMatrix)

        @property
        def abstract_nodal_matrix(
            self: "AbstractNodalMatrix._Cast_AbstractNodalMatrix",
        ) -> "AbstractNodalMatrix":
            return self._parent

        def __getattr__(
            self: "AbstractNodalMatrix._Cast_AbstractNodalMatrix", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractNodalMatrix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AbstractNodalMatrix._Cast_AbstractNodalMatrix":
        return self._Cast_AbstractNodalMatrix(self)
