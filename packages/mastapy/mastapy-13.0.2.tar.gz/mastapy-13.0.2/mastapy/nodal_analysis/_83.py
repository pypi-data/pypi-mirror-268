"""NodalMatrixRow"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODAL_MATRIX_ROW = python_net_import("SMT.MastaAPI.NodalAnalysis", "NodalMatrixRow")


__docformat__ = "restructuredtext en"
__all__ = ("NodalMatrixRow",)


Self = TypeVar("Self", bound="NodalMatrixRow")


class NodalMatrixRow(_0.APIBase):
    """NodalMatrixRow

    This is a mastapy class.
    """

    TYPE = _NODAL_MATRIX_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodalMatrixRow")

    class _Cast_NodalMatrixRow:
        """Special nested class for casting NodalMatrixRow to subclasses."""

        def __init__(
            self: "NodalMatrixRow._Cast_NodalMatrixRow", parent: "NodalMatrixRow"
        ):
            self._parent = parent

        @property
        def nodal_matrix_row(
            self: "NodalMatrixRow._Cast_NodalMatrixRow",
        ) -> "NodalMatrixRow":
            return self._parent

        def __getattr__(self: "NodalMatrixRow._Cast_NodalMatrixRow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodalMatrixRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comma_separated_values(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CommaSeparatedValues

        if temp is None:
            return ""

        return temp

    @property
    def degree_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def node_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeIndex

        if temp is None:
            return 0

        return temp

    @property
    def values(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Values

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "NodalMatrixRow._Cast_NodalMatrixRow":
        return self._Cast_NodalMatrixRow(self)
