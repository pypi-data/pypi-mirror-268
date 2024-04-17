"""ComplexVector3D"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility import _1503
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPLEX_VECTOR_3D = python_net_import("SMT.MastaAPI.MathUtility", "ComplexVector3D")

if TYPE_CHECKING:
    from mastapy.math_utility import _1501, _1521


__docformat__ = "restructuredtext en"
__all__ = ("ComplexVector3D",)


Self = TypeVar("Self", bound="ComplexVector3D")


class ComplexVector3D(_1503.ComplexVector):
    """ComplexVector3D

    This is a mastapy class.
    """

    TYPE = _COMPLEX_VECTOR_3D
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComplexVector3D")

    class _Cast_ComplexVector3D:
        """Special nested class for casting ComplexVector3D to subclasses."""

        def __init__(
            self: "ComplexVector3D._Cast_ComplexVector3D", parent: "ComplexVector3D"
        ):
            self._parent = parent

        @property
        def complex_vector(
            self: "ComplexVector3D._Cast_ComplexVector3D",
        ) -> "_1503.ComplexVector":
            return self._parent._cast(_1503.ComplexVector)

        @property
        def complex_matrix(
            self: "ComplexVector3D._Cast_ComplexVector3D",
        ) -> "_1501.ComplexMatrix":
            from mastapy.math_utility import _1501

            return self._parent._cast(_1501.ComplexMatrix)

        @property
        def generic_matrix(
            self: "ComplexVector3D._Cast_ComplexVector3D",
        ) -> "_1521.GenericMatrix":
            from mastapy.math_utility import _1521

            return self._parent._cast(_1521.GenericMatrix)

        @property
        def complex_vector_3d(
            self: "ComplexVector3D._Cast_ComplexVector3D",
        ) -> "ComplexVector3D":
            return self._parent

        def __getattr__(self: "ComplexVector3D._Cast_ComplexVector3D", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComplexVector3D.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ComplexVector3D._Cast_ComplexVector3D":
        return self._Cast_ComplexVector3D(self)
