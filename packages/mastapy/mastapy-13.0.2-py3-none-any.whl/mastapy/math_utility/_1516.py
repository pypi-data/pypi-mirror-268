"""EulerParameters"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility import _1533
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EULER_PARAMETERS = python_net_import("SMT.MastaAPI.MathUtility", "EulerParameters")

if TYPE_CHECKING:
    from mastapy.math_utility import _1532, _1521


__docformat__ = "restructuredtext en"
__all__ = ("EulerParameters",)


Self = TypeVar("Self", bound="EulerParameters")


class EulerParameters(_1533.RealVector):
    """EulerParameters

    This is a mastapy class.
    """

    TYPE = _EULER_PARAMETERS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_EulerParameters")

    class _Cast_EulerParameters:
        """Special nested class for casting EulerParameters to subclasses."""

        def __init__(
            self: "EulerParameters._Cast_EulerParameters", parent: "EulerParameters"
        ):
            self._parent = parent

        @property
        def real_vector(
            self: "EulerParameters._Cast_EulerParameters",
        ) -> "_1533.RealVector":
            return self._parent._cast(_1533.RealVector)

        @property
        def real_matrix(
            self: "EulerParameters._Cast_EulerParameters",
        ) -> "_1532.RealMatrix":
            from mastapy.math_utility import _1532

            return self._parent._cast(_1532.RealMatrix)

        @property
        def generic_matrix(
            self: "EulerParameters._Cast_EulerParameters",
        ) -> "_1521.GenericMatrix":
            from mastapy.math_utility import _1521

            return self._parent._cast(_1521.GenericMatrix)

        @property
        def euler_parameters(
            self: "EulerParameters._Cast_EulerParameters",
        ) -> "EulerParameters":
            return self._parent

        def __getattr__(self: "EulerParameters._Cast_EulerParameters", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "EulerParameters.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "EulerParameters._Cast_EulerParameters":
        return self._Cast_EulerParameters(self)
