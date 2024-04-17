"""SplineFlankContactReporting"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_FLANK_CONTACT_REPORTING = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting",
    "SplineFlankContactReporting",
)

if TYPE_CHECKING:
    from mastapy.math_utility.measured_vectors import _1571


__docformat__ = "restructuredtext en"
__all__ = ("SplineFlankContactReporting",)


Self = TypeVar("Self", bound="SplineFlankContactReporting")


class SplineFlankContactReporting(_0.APIBase):
    """SplineFlankContactReporting

    This is a mastapy class.
    """

    TYPE = _SPLINE_FLANK_CONTACT_REPORTING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SplineFlankContactReporting")

    class _Cast_SplineFlankContactReporting:
        """Special nested class for casting SplineFlankContactReporting to subclasses."""

        def __init__(
            self: "SplineFlankContactReporting._Cast_SplineFlankContactReporting",
            parent: "SplineFlankContactReporting",
        ):
            self._parent = parent

        @property
        def spline_flank_contact_reporting(
            self: "SplineFlankContactReporting._Cast_SplineFlankContactReporting",
        ) -> "SplineFlankContactReporting":
            return self._parent

        def __getattr__(
            self: "SplineFlankContactReporting._Cast_SplineFlankContactReporting",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SplineFlankContactReporting.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return temp

    @property
    def entity_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EntityName

        if temp is None:
            return ""

        return temp

    @property
    def normal_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalForce

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_deflection_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeDeflectionMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_penetration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfacePenetration

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialForce

        if temp is None:
            return 0.0

        return temp

    @property
    def tangential_stiffness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TangentialStiffness

        if temp is None:
            return 0.0

        return temp

    @property
    def tilt_moment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TiltMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_position_lcs(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPositionLCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def contact_position_wcs(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPositionWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def force_on_inner_contact_coordinate_system(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnInnerContactCoordinateSystem

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_on_inner_wcs(self: Self) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnInnerWCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def normal_direction_lcs(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDirectionLCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def normal_direction_wcs(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalDirectionWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def relative_deflection_lcs(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeDeflectionLCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def relative_deflection_wcs(
        self: Self,
    ) -> "_1571.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeDeflectionWCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SplineFlankContactReporting._Cast_SplineFlankContactReporting":
        return self._Cast_SplineFlankContactReporting(self)
