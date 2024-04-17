"""FEPartWithBatchOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_WITH_BATCH_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FEPartWithBatchOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.fe import _2396


__docformat__ = "restructuredtext en"
__all__ = ("FEPartWithBatchOptions",)


Self = TypeVar("Self", bound="FEPartWithBatchOptions")


class FEPartWithBatchOptions(_0.APIBase):
    """FEPartWithBatchOptions

    This is a mastapy class.
    """

    TYPE = _FE_PART_WITH_BATCH_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartWithBatchOptions")

    class _Cast_FEPartWithBatchOptions:
        """Special nested class for casting FEPartWithBatchOptions to subclasses."""

        def __init__(
            self: "FEPartWithBatchOptions._Cast_FEPartWithBatchOptions",
            parent: "FEPartWithBatchOptions",
        ):
            self._parent = parent

        @property
        def fe_part_with_batch_options(
            self: "FEPartWithBatchOptions._Cast_FEPartWithBatchOptions",
        ) -> "FEPartWithBatchOptions":
            return self._parent

        def __getattr__(
            self: "FEPartWithBatchOptions._Cast_FEPartWithBatchOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartWithBatchOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def all_selected(self: Self) -> "Optional[bool]":
        """Optional[bool]"""
        temp = self.wrapped.AllSelected

        if temp is None:
            return None

        return temp

    @all_selected.setter
    @enforce_parameter_types
    def all_selected(self: Self, value: "Optional[bool]"):
        self.wrapped.AllSelected = value

    @property
    def fe_part(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEPart

        if temp is None:
            return ""

        return temp

    @property
    def f_es(self: Self) -> "List[_2396.FESubstructureWithBatchOptions]":
        """List[mastapy.system_model.fe.FESubstructureWithBatchOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def f_es_with_external_files(
        self: Self,
    ) -> "List[_2396.FESubstructureWithBatchOptions]":
        """List[mastapy.system_model.fe.FESubstructureWithBatchOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FEsWithExternalFiles

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "FEPartWithBatchOptions._Cast_FEPartWithBatchOptions":
        return self._Cast_FEPartWithBatchOptions(self)
