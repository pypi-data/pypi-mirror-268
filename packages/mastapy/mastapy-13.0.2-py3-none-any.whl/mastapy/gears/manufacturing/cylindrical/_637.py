"""MicroGeometryInputsLead"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical import _636
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS_LEAD = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical", "MicroGeometryInputsLead"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1496


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryInputsLead",)


Self = TypeVar("Self", bound="MicroGeometryInputsLead")


class MicroGeometryInputsLead(_636.MicroGeometryInputs["_635.LeadModificationSegment"]):
    """MicroGeometryInputsLead

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_INPUTS_LEAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MicroGeometryInputsLead")

    class _Cast_MicroGeometryInputsLead:
        """Special nested class for casting MicroGeometryInputsLead to subclasses."""

        def __init__(
            self: "MicroGeometryInputsLead._Cast_MicroGeometryInputsLead",
            parent: "MicroGeometryInputsLead",
        ):
            self._parent = parent

        @property
        def micro_geometry_inputs(
            self: "MicroGeometryInputsLead._Cast_MicroGeometryInputsLead",
        ) -> "_636.MicroGeometryInputs":
            return self._parent._cast(_636.MicroGeometryInputs)

        @property
        def micro_geometry_inputs_lead(
            self: "MicroGeometryInputsLead._Cast_MicroGeometryInputsLead",
        ) -> "MicroGeometryInputsLead":
            return self._parent

        def __getattr__(
            self: "MicroGeometryInputsLead._Cast_MicroGeometryInputsLead", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MicroGeometryInputsLead.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_micro_geometry_range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadMicroGeometryRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def number_of_lead_segments(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfLeadSegments

        if temp is None:
            return 0

        return temp

    @number_of_lead_segments.setter
    @enforce_parameter_types
    def number_of_lead_segments(self: Self, value: "int"):
        self.wrapped.NumberOfLeadSegments = int(value) if value is not None else 0

    @property
    def cast_to(self: Self) -> "MicroGeometryInputsLead._Cast_MicroGeometryInputsLead":
        return self._Cast_MicroGeometryInputsLead(self)
