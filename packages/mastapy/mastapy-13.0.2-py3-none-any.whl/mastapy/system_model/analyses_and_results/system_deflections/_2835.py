"""SystemDeflectionOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.system_model.analyses_and_results.analysis_cases import _7544
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SystemDeflectionOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("SystemDeflectionOptions",)


Self = TypeVar("Self", bound="SystemDeflectionOptions")


class SystemDeflectionOptions(_7544.AbstractAnalysisOptions["_6813.StaticLoadCase"]):
    """SystemDeflectionOptions

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SystemDeflectionOptions")

    class _Cast_SystemDeflectionOptions:
        """Special nested class for casting SystemDeflectionOptions to subclasses."""

        def __init__(
            self: "SystemDeflectionOptions._Cast_SystemDeflectionOptions",
            parent: "SystemDeflectionOptions",
        ):
            self._parent = parent

        @property
        def abstract_analysis_options(
            self: "SystemDeflectionOptions._Cast_SystemDeflectionOptions",
        ) -> "_7544.AbstractAnalysisOptions":
            return self._parent._cast(_7544.AbstractAnalysisOptions)

        @property
        def system_deflection_options(
            self: "SystemDeflectionOptions._Cast_SystemDeflectionOptions",
        ) -> "SystemDeflectionOptions":
            return self._parent

        def __getattr__(
            self: "SystemDeflectionOptions._Cast_SystemDeflectionOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SystemDeflectionOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ground_shaft_if_rigid_body_rotation_is_large(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.GroundShaftIfRigidBodyRotationIsLarge

        if temp is None:
            return False

        return temp

    @ground_shaft_if_rigid_body_rotation_is_large.setter
    @enforce_parameter_types
    def ground_shaft_if_rigid_body_rotation_is_large(self: Self, value: "bool"):
        self.wrapped.GroundShaftIfRigidBodyRotationIsLarge = (
            bool(value) if value is not None else False
        )

    @property
    def maximum_number_of_unstable_rigid_body_rotation_iterations(self: Self) -> "int":
        """int"""
        temp = self.wrapped.MaximumNumberOfUnstableRigidBodyRotationIterations

        if temp is None:
            return 0

        return temp

    @maximum_number_of_unstable_rigid_body_rotation_iterations.setter
    @enforce_parameter_types
    def maximum_number_of_unstable_rigid_body_rotation_iterations(
        self: Self, value: "int"
    ):
        self.wrapped.MaximumNumberOfUnstableRigidBodyRotationIterations = (
            int(value) if value is not None else 0
        )

    @property
    def maximum_rigid_body_rotation_change_in_system_deflection(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumRigidBodyRotationChangeInSystemDeflection

        if temp is None:
            return 0.0

        return temp

    @maximum_rigid_body_rotation_change_in_system_deflection.setter
    @enforce_parameter_types
    def maximum_rigid_body_rotation_change_in_system_deflection(
        self: Self, value: "float"
    ):
        self.wrapped.MaximumRigidBodyRotationChangeInSystemDeflection = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "SystemDeflectionOptions._Cast_SystemDeflectionOptions":
        return self._Cast_SystemDeflectionOptions(self)
