"""ComplexVector6D"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility import _1503
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPLEX_VECTOR_6D = python_net_import("SMT.MastaAPI.MathUtility", "ComplexVector6D")

if TYPE_CHECKING:
    from mastapy.math_utility import _1501, _1521


__docformat__ = "restructuredtext en"
__all__ = ("ComplexVector6D",)


Self = TypeVar("Self", bound="ComplexVector6D")


class ComplexVector6D(_1503.ComplexVector):
    """ComplexVector6D

    This is a mastapy class.
    """

    TYPE = _COMPLEX_VECTOR_6D
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComplexVector6D")

    class _Cast_ComplexVector6D:
        """Special nested class for casting ComplexVector6D to subclasses."""

        def __init__(
            self: "ComplexVector6D._Cast_ComplexVector6D", parent: "ComplexVector6D"
        ):
            self._parent = parent

        @property
        def complex_vector(
            self: "ComplexVector6D._Cast_ComplexVector6D",
        ) -> "_1503.ComplexVector":
            return self._parent._cast(_1503.ComplexVector)

        @property
        def complex_matrix(
            self: "ComplexVector6D._Cast_ComplexVector6D",
        ) -> "_1501.ComplexMatrix":
            from mastapy.math_utility import _1501

            return self._parent._cast(_1501.ComplexMatrix)

        @property
        def generic_matrix(
            self: "ComplexVector6D._Cast_ComplexVector6D",
        ) -> "_1521.GenericMatrix":
            from mastapy.math_utility import _1521

            return self._parent._cast(_1521.GenericMatrix)

        @property
        def complex_vector_6d(
            self: "ComplexVector6D._Cast_ComplexVector6D",
        ) -> "ComplexVector6D":
            return self._parent

        def __getattr__(self: "ComplexVector6D._Cast_ComplexVector6D", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComplexVector6D.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ComplexVector6D._Cast_ComplexVector6D":
        return self._Cast_ComplexVector6D(self)
