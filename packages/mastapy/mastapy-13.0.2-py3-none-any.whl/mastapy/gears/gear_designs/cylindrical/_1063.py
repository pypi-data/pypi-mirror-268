"""LTCALoadCaseModifiableSettings"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LTCA_LOAD_CASE_MODIFIABLE_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "LTCALoadCaseModifiableSettings"
)


__docformat__ = "restructuredtext en"
__all__ = ("LTCALoadCaseModifiableSettings",)


Self = TypeVar("Self", bound="LTCALoadCaseModifiableSettings")


class LTCALoadCaseModifiableSettings(
    _1593.IndependentReportablePropertiesBase["LTCALoadCaseModifiableSettings"]
):
    """LTCALoadCaseModifiableSettings

    This is a mastapy class.
    """

    TYPE = _LTCA_LOAD_CASE_MODIFIABLE_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LTCALoadCaseModifiableSettings")

    class _Cast_LTCALoadCaseModifiableSettings:
        """Special nested class for casting LTCALoadCaseModifiableSettings to subclasses."""

        def __init__(
            self: "LTCALoadCaseModifiableSettings._Cast_LTCALoadCaseModifiableSettings",
            parent: "LTCALoadCaseModifiableSettings",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "LTCALoadCaseModifiableSettings._Cast_LTCALoadCaseModifiableSettings",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def ltca_load_case_modifiable_settings(
            self: "LTCALoadCaseModifiableSettings._Cast_LTCALoadCaseModifiableSettings",
        ) -> "LTCALoadCaseModifiableSettings":
            return self._parent

        def __getattr__(
            self: "LTCALoadCaseModifiableSettings._Cast_LTCALoadCaseModifiableSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LTCALoadCaseModifiableSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apply_application_and_dynamic_factor(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ApplyApplicationAndDynamicFactor

        if temp is None:
            return False

        return temp

    @apply_application_and_dynamic_factor.setter
    @enforce_parameter_types
    def apply_application_and_dynamic_factor(self: Self, value: "bool"):
        self.wrapped.ApplyApplicationAndDynamicFactor = (
            bool(value) if value is not None else False
        )

    @property
    def include_change_in_contact_point_due_to_micro_geometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeChangeInContactPointDueToMicroGeometry

        if temp is None:
            return False

        return temp

    @include_change_in_contact_point_due_to_micro_geometry.setter
    @enforce_parameter_types
    def include_change_in_contact_point_due_to_micro_geometry(
        self: Self, value: "bool"
    ):
        self.wrapped.IncludeChangeInContactPointDueToMicroGeometry = (
            bool(value) if value is not None else False
        )

    @property
    def use_jacobian_advanced_ltca_solver(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseJacobianAdvancedLTCASolver

        if temp is None:
            return False

        return temp

    @use_jacobian_advanced_ltca_solver.setter
    @enforce_parameter_types
    def use_jacobian_advanced_ltca_solver(self: Self, value: "bool"):
        self.wrapped.UseJacobianAdvancedLTCASolver = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "LTCALoadCaseModifiableSettings._Cast_LTCALoadCaseModifiableSettings":
        return self._Cast_LTCALoadCaseModifiableSettings(self)
