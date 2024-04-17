"""BearingDynamicElementContactPropertyWrapper"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DYNAMIC_ELEMENT_CONTACT_PROPERTY_WRAPPER = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BearingDynamicElementContactPropertyWrapper",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2704


__docformat__ = "restructuredtext en"
__all__ = ("BearingDynamicElementContactPropertyWrapper",)


Self = TypeVar("Self", bound="BearingDynamicElementContactPropertyWrapper")


class BearingDynamicElementContactPropertyWrapper(_0.APIBase):
    """BearingDynamicElementContactPropertyWrapper

    This is a mastapy class.
    """

    TYPE = _BEARING_DYNAMIC_ELEMENT_CONTACT_PROPERTY_WRAPPER
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BearingDynamicElementContactPropertyWrapper"
    )

    class _Cast_BearingDynamicElementContactPropertyWrapper:
        """Special nested class for casting BearingDynamicElementContactPropertyWrapper to subclasses."""

        def __init__(
            self: "BearingDynamicElementContactPropertyWrapper._Cast_BearingDynamicElementContactPropertyWrapper",
            parent: "BearingDynamicElementContactPropertyWrapper",
        ):
            self._parent = parent

        @property
        def bearing_dynamic_element_contact_property_wrapper(
            self: "BearingDynamicElementContactPropertyWrapper._Cast_BearingDynamicElementContactPropertyWrapper",
        ) -> "BearingDynamicElementContactPropertyWrapper":
            return self._parent

        def __getattr__(
            self: "BearingDynamicElementContactPropertyWrapper._Cast_BearingDynamicElementContactPropertyWrapper",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "BearingDynamicElementContactPropertyWrapper.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def contact_results(
        self: Self,
    ) -> "List[_2704.BearingDynamicResultsPropertyWrapper]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BearingDynamicResultsPropertyWrapper]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BearingDynamicElementContactPropertyWrapper._Cast_BearingDynamicElementContactPropertyWrapper":
        return self._Cast_BearingDynamicElementContactPropertyWrapper(self)
