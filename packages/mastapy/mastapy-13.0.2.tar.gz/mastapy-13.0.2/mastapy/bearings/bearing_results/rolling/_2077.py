"""RollingBearingFrictionCoefficients"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ROLLING_BEARING_FRICTION_COEFFICIENTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "RollingBearingFrictionCoefficients"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results import _1952
    from mastapy.bearings.bearing_results.rolling import _1981


__docformat__ = "restructuredtext en"
__all__ = ("RollingBearingFrictionCoefficients",)


Self = TypeVar("Self", bound="RollingBearingFrictionCoefficients")


class RollingBearingFrictionCoefficients(
    _1593.IndependentReportablePropertiesBase["RollingBearingFrictionCoefficients"]
):
    """RollingBearingFrictionCoefficients

    This is a mastapy class.
    """

    TYPE = _ROLLING_BEARING_FRICTION_COEFFICIENTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingBearingFrictionCoefficients")

    class _Cast_RollingBearingFrictionCoefficients:
        """Special nested class for casting RollingBearingFrictionCoefficients to subclasses."""

        def __init__(
            self: "RollingBearingFrictionCoefficients._Cast_RollingBearingFrictionCoefficients",
            parent: "RollingBearingFrictionCoefficients",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "RollingBearingFrictionCoefficients._Cast_RollingBearingFrictionCoefficients",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def rolling_bearing_friction_coefficients(
            self: "RollingBearingFrictionCoefficients._Cast_RollingBearingFrictionCoefficients",
        ) -> "RollingBearingFrictionCoefficients":
            return self._parent

        def __getattr__(
            self: "RollingBearingFrictionCoefficients._Cast_RollingBearingFrictionCoefficients",
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
        self: Self, instance_to_wrap: "RollingBearingFrictionCoefficients.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def iso14179_settings_database(self: Self) -> "str":
        """str"""
        temp = self.wrapped.ISO14179SettingsDatabase.SelectedItemName

        if temp is None:
            return ""

        return temp

    @iso14179_settings_database.setter
    @enforce_parameter_types
    def iso14179_settings_database(self: Self, value: "str"):
        self.wrapped.ISO14179SettingsDatabase.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def use_user_specified_f0(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseUserSpecifiedF0

        if temp is None:
            return False

        return temp

    @use_user_specified_f0.setter
    @enforce_parameter_types
    def use_user_specified_f0(self: Self, value: "bool"):
        self.wrapped.UseUserSpecifiedF0 = bool(value) if value is not None else False

    @property
    def use_user_specified_f0r(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseUserSpecifiedF0r

        if temp is None:
            return False

        return temp

    @use_user_specified_f0r.setter
    @enforce_parameter_types
    def use_user_specified_f0r(self: Self, value: "bool"):
        self.wrapped.UseUserSpecifiedF0r = bool(value) if value is not None else False

    @property
    def use_user_specified_f1_for_din7322010(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseUserSpecifiedF1ForDIN7322010

        if temp is None:
            return False

        return temp

    @use_user_specified_f1_for_din7322010.setter
    @enforce_parameter_types
    def use_user_specified_f1_for_din7322010(self: Self, value: "bool"):
        self.wrapped.UseUserSpecifiedF1ForDIN7322010 = (
            bool(value) if value is not None else False
        )

    @property
    def use_user_specified_f1r(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseUserSpecifiedF1r

        if temp is None:
            return False

        return temp

    @use_user_specified_f1r.setter
    @enforce_parameter_types
    def use_user_specified_f1r(self: Self, value: "bool"):
        self.wrapped.UseUserSpecifiedF1r = bool(value) if value is not None else False

    @property
    def user_specified_f0(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedF0

        if temp is None:
            return 0.0

        return temp

    @user_specified_f0.setter
    @enforce_parameter_types
    def user_specified_f0(self: Self, value: "float"):
        self.wrapped.UserSpecifiedF0 = float(value) if value is not None else 0.0

    @property
    def user_specified_f0r(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedF0r

        if temp is None:
            return 0.0

        return temp

    @user_specified_f0r.setter
    @enforce_parameter_types
    def user_specified_f0r(self: Self, value: "float"):
        self.wrapped.UserSpecifiedF0r = float(value) if value is not None else 0.0

    @property
    def user_specified_f1_for_din7322010(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedF1ForDIN7322010

        if temp is None:
            return 0.0

        return temp

    @user_specified_f1_for_din7322010.setter
    @enforce_parameter_types
    def user_specified_f1_for_din7322010(self: Self, value: "float"):
        self.wrapped.UserSpecifiedF1ForDIN7322010 = (
            float(value) if value is not None else 0.0
        )

    @property
    def user_specified_f1r(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UserSpecifiedF1r

        if temp is None:
            return 0.0

        return temp

    @user_specified_f1r.setter
    @enforce_parameter_types
    def user_specified_f1r(self: Self, value: "float"):
        self.wrapped.UserSpecifiedF1r = float(value) if value is not None else 0.0

    @property
    def iso14179_dynamic_equivalent_load_factors(
        self: Self,
    ) -> "_1952.EquivalentLoadFactors":
        """mastapy.bearings.bearing_results.EquivalentLoadFactors

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO14179DynamicEquivalentLoadFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso14179_settings(self: Self) -> "_1981.ISO14179Settings":
        """mastapy.bearings.bearing_results.rolling.ISO14179Settings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO14179Settings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def iso14179_static_equivalent_load_factors(
        self: Self,
    ) -> "_1952.EquivalentLoadFactors":
        """mastapy.bearings.bearing_results.EquivalentLoadFactors

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ISO14179StaticEquivalentLoadFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RollingBearingFrictionCoefficients._Cast_RollingBearingFrictionCoefficients":
        return self._Cast_RollingBearingFrictionCoefficients(self)
