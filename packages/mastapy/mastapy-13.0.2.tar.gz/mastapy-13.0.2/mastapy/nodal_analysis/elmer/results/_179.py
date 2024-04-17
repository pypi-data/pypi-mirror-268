"""Data1D"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy.nodal_analysis.elmer.results import _178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_1D = python_net_import("SMT.MastaAPI.NodalAnalysis.Elmer.Results", "Data1D")


__docformat__ = "restructuredtext en"
__all__ = ("Data1D",)


Self = TypeVar("Self", bound="Data1D")


class Data1D(_178.Data):
    """Data1D

    This is a mastapy class.
    """

    TYPE = _DATA_1D
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Data1D")

    class _Cast_Data1D:
        """Special nested class for casting Data1D to subclasses."""

        def __init__(self: "Data1D._Cast_Data1D", parent: "Data1D"):
            self._parent = parent

        @property
        def data(self: "Data1D._Cast_Data1D") -> "_178.Data":
            return self._parent._cast(_178.Data)

        @property
        def data_1d(self: "Data1D._Cast_Data1D") -> "Data1D":
            return self._parent

        def __getattr__(self: "Data1D._Cast_Data1D", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Data1D.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Data

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "Data1D._Cast_Data1D":
        return self._Cast_Data1D(self)
