"""CustomSplineJointDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.detailed_rigid_connectors.splines import _1422
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CUSTOM_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "CustomSplineJointDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors import _1394


__docformat__ = "restructuredtext en"
__all__ = ("CustomSplineJointDesign",)


Self = TypeVar("Self", bound="CustomSplineJointDesign")


class CustomSplineJointDesign(_1422.SplineJointDesign):
    """CustomSplineJointDesign

    This is a mastapy class.
    """

    TYPE = _CUSTOM_SPLINE_JOINT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CustomSplineJointDesign")

    class _Cast_CustomSplineJointDesign:
        """Special nested class for casting CustomSplineJointDesign to subclasses."""

        def __init__(
            self: "CustomSplineJointDesign._Cast_CustomSplineJointDesign",
            parent: "CustomSplineJointDesign",
        ):
            self._parent = parent

        @property
        def spline_joint_design(
            self: "CustomSplineJointDesign._Cast_CustomSplineJointDesign",
        ) -> "_1422.SplineJointDesign":
            return self._parent._cast(_1422.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(
            self: "CustomSplineJointDesign._Cast_CustomSplineJointDesign",
        ) -> "_1394.DetailedRigidConnectorDesign":
            from mastapy.detailed_rigid_connectors import _1394

            return self._parent._cast(_1394.DetailedRigidConnectorDesign)

        @property
        def custom_spline_joint_design(
            self: "CustomSplineJointDesign._Cast_CustomSplineJointDesign",
        ) -> "CustomSplineJointDesign":
            return self._parent

        def __getattr__(
            self: "CustomSplineJointDesign._Cast_CustomSplineJointDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CustomSplineJointDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    @enforce_parameter_types
    def pressure_angle(self: Self, value: "float"):
        self.wrapped.PressureAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "CustomSplineJointDesign._Cast_CustomSplineJointDesign":
        return self._Cast_CustomSplineJointDesign(self)
