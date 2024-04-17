"""SAESplineJointDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.detailed_rigid_connectors.splines import _1427
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "SAESplineJointDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1402, _1422
    from mastapy.detailed_rigid_connectors import _1394


__docformat__ = "restructuredtext en"
__all__ = ("SAESplineJointDesign",)


Self = TypeVar("Self", bound="SAESplineJointDesign")


class SAESplineJointDesign(_1427.StandardSplineJointDesign):
    """SAESplineJointDesign

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_JOINT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SAESplineJointDesign")

    class _Cast_SAESplineJointDesign:
        """Special nested class for casting SAESplineJointDesign to subclasses."""

        def __init__(
            self: "SAESplineJointDesign._Cast_SAESplineJointDesign",
            parent: "SAESplineJointDesign",
        ):
            self._parent = parent

        @property
        def standard_spline_joint_design(
            self: "SAESplineJointDesign._Cast_SAESplineJointDesign",
        ) -> "_1427.StandardSplineJointDesign":
            return self._parent._cast(_1427.StandardSplineJointDesign)

        @property
        def spline_joint_design(
            self: "SAESplineJointDesign._Cast_SAESplineJointDesign",
        ) -> "_1422.SplineJointDesign":
            from mastapy.detailed_rigid_connectors.splines import _1422

            return self._parent._cast(_1422.SplineJointDesign)

        @property
        def detailed_rigid_connector_design(
            self: "SAESplineJointDesign._Cast_SAESplineJointDesign",
        ) -> "_1394.DetailedRigidConnectorDesign":
            from mastapy.detailed_rigid_connectors import _1394

            return self._parent._cast(_1394.DetailedRigidConnectorDesign)

        @property
        def sae_spline_joint_design(
            self: "SAESplineJointDesign._Cast_SAESplineJointDesign",
        ) -> "SAESplineJointDesign":
            return self._parent

        def __getattr__(
            self: "SAESplineJointDesign._Cast_SAESplineJointDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SAESplineJointDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fit_type(self: Self) -> "_1402.FitTypes":
        """mastapy.detailed_rigid_connectors.splines.FitTypes"""
        temp = self.wrapped.FitType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.FitTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.splines._1402", "FitTypes"
        )(value)

    @fit_type.setter
    @enforce_parameter_types
    def fit_type(self: Self, value: "_1402.FitTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.FitTypes"
        )
        self.wrapped.FitType = value

    @property
    def form_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FormClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_effective_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tip_chamfer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTipChamfer

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_effective_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumEffectiveClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_tip_chamfer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumTipChamfer

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "int"):
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def use_internal_half_minimum_minor_diameter_for_external_half_form_diameter_calculation(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.UseInternalHalfMinimumMinorDiameterForExternalHalfFormDiameterCalculation
        )

        if temp is None:
            return False

        return temp

    @use_internal_half_minimum_minor_diameter_for_external_half_form_diameter_calculation.setter
    @enforce_parameter_types
    def use_internal_half_minimum_minor_diameter_for_external_half_form_diameter_calculation(
        self: Self, value: "bool"
    ):
        self.wrapped.UseInternalHalfMinimumMinorDiameterForExternalHalfFormDiameterCalculation = (
            bool(value) if value is not None else False
        )

    @property
    def use_saeb921b_1996(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseSAEB921b1996

        if temp is None:
            return False

        return temp

    @use_saeb921b_1996.setter
    @enforce_parameter_types
    def use_saeb921b_1996(self: Self, value: "bool"):
        self.wrapped.UseSAEB921b1996 = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "SAESplineJointDesign._Cast_SAESplineJointDesign":
        return self._Cast_SAESplineJointDesign(self)
