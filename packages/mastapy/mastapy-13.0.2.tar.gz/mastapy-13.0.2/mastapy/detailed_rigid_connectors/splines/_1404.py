"""GBT3478SplineJointDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.bearings.tolerances import _1917
from mastapy.detailed_rigid_connectors.splines import _1407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GBT3478_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "GBT3478SplineJointDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1427, _1422
    from mastapy.detailed_rigid_connectors import _1394


__docformat__ = "restructuredtext en"
__all__ = ("GBT3478SplineJointDesign",)


Self = TypeVar("Self", bound="GBT3478SplineJointDesign")


class GBT3478SplineJointDesign(_1407.ISO4156SplineJointDesign):
    """GBT3478SplineJointDesign

    This is a mastapy class.
    """

    TYPE = _GBT3478_SPLINE_JOINT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GBT3478SplineJointDesign")

    class _Cast_GBT3478SplineJointDesign:
        """Special nested class for casting GBT3478SplineJointDesign to subclasses."""

        def __init__(
            self: "GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign",
            parent: "GBT3478SplineJointDesign",
        ):
            self._parent = parent

        @property
        def iso4156_spline_joint_design(
            self: "GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign",
        ) -> "_1407.ISO4156SplineJointDesign":
            return self._parent._cast(_1407.ISO4156SplineJointDesign)

        @property
        def standard_spline_joint_design(
            self: "GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign",
        ) -> "_1427.StandardSplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1427

            return self._parent._cast(_1427.StandardSplineJointDesign)

        @property
        def spline_joint_design(
            self: "GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign",
        ) -> "_1422.SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1422

            return self._parent._cast(_1422.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(
            self: "GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign",
        ) -> "_1394.DetailedRigidConnectorDesign":
            from mastapy.detailed_rigid_connectors import _1394

            return self._parent._cast(_1394.DetailedRigidConnectorDesign)

        @property
        def gbt3478_spline_joint_design(
            self: "GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign",
        ) -> "GBT3478SplineJointDesign":
            return self._parent

        def __getattr__(
            self: "GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GBT3478SplineJointDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def external_minimum_major_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExternalMinimumMajorDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def major_diameter_standard_tolerance_grade(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ITDesignation":
        """EnumWithSelectedValue[mastapy.bearings.tolerances.ITDesignation]"""
        temp = self.wrapped.MajorDiameterStandardToleranceGrade

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @major_diameter_standard_tolerance_grade.setter
    @enforce_parameter_types
    def major_diameter_standard_tolerance_grade(
        self: Self, value: "_1917.ITDesignation"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MajorDiameterStandardToleranceGrade = value

    @property
    def minor_diameter_standard_tolerance_grade(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_ITDesignation":
        """EnumWithSelectedValue[mastapy.bearings.tolerances.ITDesignation]"""
        temp = self.wrapped.MinorDiameterStandardToleranceGrade

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @minor_diameter_standard_tolerance_grade.setter
    @enforce_parameter_types
    def minor_diameter_standard_tolerance_grade(
        self: Self, value: "_1917.ITDesignation"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_ITDesignation.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MinorDiameterStandardToleranceGrade = value

    @property
    def cast_to(
        self: Self,
    ) -> "GBT3478SplineJointDesign._Cast_GBT3478SplineJointDesign":
        return self._Cast_GBT3478SplineJointDesign(self)
