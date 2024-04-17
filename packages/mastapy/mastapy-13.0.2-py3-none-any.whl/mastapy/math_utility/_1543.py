"""Vector6D"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility import _1533
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VECTOR_6D = python_net_import("SMT.MastaAPI.MathUtility", "Vector6D")

if TYPE_CHECKING:
    from mastapy.math_utility import _1532, _1521


__docformat__ = "restructuredtext en"
__all__ = ("Vector6D",)


Self = TypeVar("Self", bound="Vector6D")


class Vector6D(_1533.RealVector):
    """Vector6D

    This is a mastapy class.
    """

    TYPE = _VECTOR_6D
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Vector6D")

    class _Cast_Vector6D:
        """Special nested class for casting Vector6D to subclasses."""

        def __init__(self: "Vector6D._Cast_Vector6D", parent: "Vector6D"):
            self._parent = parent

        @property
        def real_vector(self: "Vector6D._Cast_Vector6D") -> "_1533.RealVector":
            return self._parent._cast(_1533.RealVector)

        @property
        def real_matrix(self: "Vector6D._Cast_Vector6D") -> "_1532.RealMatrix":
            from mastapy.math_utility import _1532

            return self._parent._cast(_1532.RealMatrix)

        @property
        def generic_matrix(self: "Vector6D._Cast_Vector6D") -> "_1521.GenericMatrix":
            from mastapy.math_utility import _1521

            return self._parent._cast(_1521.GenericMatrix)

        @property
        def vector_6d(self: "Vector6D._Cast_Vector6D") -> "Vector6D":
            return self._parent

        def __getattr__(self: "Vector6D._Cast_Vector6D", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Vector6D.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Vector6D._Cast_Vector6D":
        return self._Cast_Vector6D(self)
