"""Data"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA = python_net_import("SMT.MastaAPI.NodalAnalysis.Elmer.Results", "Data")

if TYPE_CHECKING:
    from mastapy.nodal_analysis.elmer.results import _179, _180


__docformat__ = "restructuredtext en"
__all__ = ("Data",)


Self = TypeVar("Self", bound="Data")


class Data(_0.APIBase):
    """Data

    This is a mastapy class.
    """

    TYPE = _DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Data")

    class _Cast_Data:
        """Special nested class for casting Data to subclasses."""

        def __init__(self: "Data._Cast_Data", parent: "Data"):
            self._parent = parent

        @property
        def data_1d(self: "Data._Cast_Data") -> "_179.Data1D":
            from mastapy.nodal_analysis.elmer.results import _179

            return self._parent._cast(_179.Data1D)

        @property
        def data_3d(self: "Data._Cast_Data") -> "_180.Data3D":
            from mastapy.nodal_analysis.elmer.results import _180

            return self._parent._cast(_180.Data3D)

        @property
        def data(self: "Data._Cast_Data") -> "Data":
            return self._parent

        def __getattr__(self: "Data._Cast_Data", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Data.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def quantity_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.QuantityName

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "Data._Cast_Data":
        return self._Cast_Data(self)
