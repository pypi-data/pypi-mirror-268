"""NodalMatrix"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.nodal_analysis import _47
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_MATRIX = python_net_import("SMT.MastaAPI.NodalAnalysis", "NodalMatrix")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _83


__docformat__ = "restructuredtext en"
__all__ = ("NodalMatrix",)


Self = TypeVar("Self", bound="NodalMatrix")


class NodalMatrix(_47.AbstractNodalMatrix):
    """NodalMatrix

    This is a mastapy class.
    """

    TYPE = _NODAL_MATRIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalMatrix")

    class _Cast_NodalMatrix:
        """Special nested class for casting NodalMatrix to subclasses."""

        def __init__(self: "NodalMatrix._Cast_NodalMatrix", parent: "NodalMatrix"):
            self._parent = parent

        @property
        def abstract_nodal_matrix(
            self: "NodalMatrix._Cast_NodalMatrix",
        ) -> "_47.AbstractNodalMatrix":
            return self._parent._cast(_47.AbstractNodalMatrix)

        @property
        def nodal_matrix(self: "NodalMatrix._Cast_NodalMatrix") -> "NodalMatrix":
            return self._parent

        def __getattr__(self: "NodalMatrix._Cast_NodalMatrix", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalMatrix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rows(self: Self) -> "List[_83.NodalMatrixRow]":
        """List[mastapy.nodal_analysis.NodalMatrixRow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "NodalMatrix._Cast_NodalMatrix":
        return self._Cast_NodalMatrix(self)
