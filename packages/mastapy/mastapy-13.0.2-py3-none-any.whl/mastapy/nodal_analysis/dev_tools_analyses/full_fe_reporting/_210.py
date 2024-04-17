"""ElementDetailsForFEModel"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELEMENT_DETAILS_FOR_FE_MODEL = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting",
    "ElementDetailsForFEModel",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElementDetailsForFEModel",)


Self = TypeVar("Self", bound="ElementDetailsForFEModel")


class ElementDetailsForFEModel(_0.APIBase):
    """ElementDetailsForFEModel

    This is a mastapy class.
    """

    TYPE = _ELEMENT_DETAILS_FOR_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElementDetailsForFEModel")

    class _Cast_ElementDetailsForFEModel:
        """Special nested class for casting ElementDetailsForFEModel to subclasses."""

        def __init__(
            self: "ElementDetailsForFEModel._Cast_ElementDetailsForFEModel",
            parent: "ElementDetailsForFEModel",
        ):
            self._parent = parent

        @property
        def element_details_for_fe_model(
            self: "ElementDetailsForFEModel._Cast_ElementDetailsForFEModel",
        ) -> "ElementDetailsForFEModel":
            return self._parent

        def __getattr__(
            self: "ElementDetailsForFEModel._Cast_ElementDetailsForFEModel", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElementDetailsForFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_areas(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementAreas

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def element_ids_with_negative_jacobian(self: Self) -> "List[int]":
        """List[int]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementIdsWithNegativeJacobian

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value

    @property
    def element_ids_with_negative_size(self: Self) -> "List[int]":
        """List[int]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementIdsWithNegativeSize

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value

    @property
    def element_ids_with_no_material(self: Self) -> "List[int]":
        """List[int]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementIdsWithNoMaterial

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value

    @property
    def element_volumes(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementVolumes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def external_ids(self: Self) -> "List[int]":
        """List[int]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalIDs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, int)

        if value is None:
            return None

        return value

    @property
    def node_ids_for_elements(self: Self) -> "List[List[int]]":
        """List[List[int]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeIDsForElements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list_of_lists(temp, int)

        if value is None:
            return None

        return value

    @property
    def total_element_area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementArea

        if temp is None:
            return 0.0

        return temp

    @property
    def total_element_volume(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalElementVolume

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "ElementDetailsForFEModel._Cast_ElementDetailsForFEModel":
        return self._Cast_ElementDetailsForFEModel(self)
