"""FEModelPart"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_MODEL_PART = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEModelPart"
)


__docformat__ = "restructuredtext en"
__all__ = ("FEModelPart",)


Self = TypeVar("Self", bound="FEModelPart")


class FEModelPart(_0.APIBase):
    """FEModelPart

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_PART
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEModelPart")

    class _Cast_FEModelPart:
        """Special nested class for casting FEModelPart to subclasses."""

        def __init__(self: "FEModelPart._Cast_FEModelPart", parent: "FEModelPart"):
            self._parent = parent

        @property
        def fe_model_part(self: "FEModelPart._Cast_FEModelPart") -> "FEModelPart":
            return self._parent

        def __getattr__(self: "FEModelPart._Cast_FEModelPart", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEModelPart.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ID

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self: Self) -> "FEModelPart._Cast_FEModelPart":
        return self._Cast_FEModelPart(self)
