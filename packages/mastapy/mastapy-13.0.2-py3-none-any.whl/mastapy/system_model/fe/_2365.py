"""AlignmentUsingAxialNodePositions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1498
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ALIGNMENT_USING_AXIAL_NODE_POSITIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "AlignmentUsingAxialNodePositions"
)


__docformat__ = "restructuredtext en"
__all__ = ("AlignmentUsingAxialNodePositions",)


Self = TypeVar("Self", bound="AlignmentUsingAxialNodePositions")


class AlignmentUsingAxialNodePositions(_0.APIBase):
    """AlignmentUsingAxialNodePositions

    This is a mastapy class.
    """

    TYPE = _ALIGNMENT_USING_AXIAL_NODE_POSITIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AlignmentUsingAxialNodePositions")

    class _Cast_AlignmentUsingAxialNodePositions:
        """Special nested class for casting AlignmentUsingAxialNodePositions to subclasses."""

        def __init__(
            self: "AlignmentUsingAxialNodePositions._Cast_AlignmentUsingAxialNodePositions",
            parent: "AlignmentUsingAxialNodePositions",
        ):
            self._parent = parent

        @property
        def alignment_using_axial_node_positions(
            self: "AlignmentUsingAxialNodePositions._Cast_AlignmentUsingAxialNodePositions",
        ) -> "AlignmentUsingAxialNodePositions":
            return self._parent

        def __getattr__(
            self: "AlignmentUsingAxialNodePositions._Cast_AlignmentUsingAxialNodePositions",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AlignmentUsingAxialNodePositions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fe_axis_for_angle_alignment(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_AlignmentAxis":
        """EnumWithSelectedValue[mastapy.math_utility.AlignmentAxis]"""
        temp = self.wrapped.FEAxisForAngleAlignment

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_AlignmentAxis.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @fe_axis_for_angle_alignment.setter
    @enforce_parameter_types
    def fe_axis_for_angle_alignment(self: Self, value: "_1498.AlignmentAxis"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_AlignmentAxis.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FEAxisForAngleAlignment = value

    @property
    def rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    @enforce_parameter_types
    def rotation_angle(self: Self, value: "float"):
        self.wrapped.RotationAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "AlignmentUsingAxialNodePositions._Cast_AlignmentUsingAxialNodePositions":
        return self._Cast_AlignmentUsingAxialNodePositions(self)
