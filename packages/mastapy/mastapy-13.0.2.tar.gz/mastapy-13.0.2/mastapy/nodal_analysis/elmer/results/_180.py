"""Data3D"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy.nodal_analysis.elmer.results import _178
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_3D = python_net_import("SMT.MastaAPI.NodalAnalysis.Elmer.Results", "Data3D")


__docformat__ = "restructuredtext en"
__all__ = ("Data3D",)


Self = TypeVar("Self", bound="Data3D")


class Data3D(_178.Data):
    """Data3D

    This is a mastapy class.
    """

    TYPE = _DATA_3D
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Data3D")

    class _Cast_Data3D:
        """Special nested class for casting Data3D to subclasses."""

        def __init__(self: "Data3D._Cast_Data3D", parent: "Data3D"):
            self._parent = parent

        @property
        def data(self: "Data3D._Cast_Data3D") -> "_178.Data":
            return self._parent._cast(_178.Data)

        @property
        def data_3d(self: "Data3D._Cast_Data3D") -> "Data3D":
            return self._parent

        def __getattr__(self: "Data3D._Cast_Data3D", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Data3D.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_data(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def y_data(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def z_data(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZData

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "Data3D._Cast_Data3D":
        return self._Cast_Data3D(self)
