"""ISO14179SettingsPerBearingType"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, conversion
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ISO14179_SETTINGS_PER_BEARING_TYPE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "ISO14179SettingsPerBearingType"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1903
    from mastapy.bearings.bearing_results.rolling import _1981


__docformat__ = "restructuredtext en"
__all__ = ("ISO14179SettingsPerBearingType",)


Self = TypeVar("Self", bound="ISO14179SettingsPerBearingType")


class ISO14179SettingsPerBearingType(
    _1593.IndependentReportablePropertiesBase["ISO14179SettingsPerBearingType"]
):
    """ISO14179SettingsPerBearingType

    This is a mastapy class.
    """

    TYPE = _ISO14179_SETTINGS_PER_BEARING_TYPE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO14179SettingsPerBearingType")

    class _Cast_ISO14179SettingsPerBearingType:
        """Special nested class for casting ISO14179SettingsPerBearingType to subclasses."""

        def __init__(
            self: "ISO14179SettingsPerBearingType._Cast_ISO14179SettingsPerBearingType",
            parent: "ISO14179SettingsPerBearingType",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "ISO14179SettingsPerBearingType._Cast_ISO14179SettingsPerBearingType",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def iso14179_settings_per_bearing_type(
            self: "ISO14179SettingsPerBearingType._Cast_ISO14179SettingsPerBearingType",
        ) -> "ISO14179SettingsPerBearingType":
            return self._parent

        def __getattr__(
            self: "ISO14179SettingsPerBearingType._Cast_ISO14179SettingsPerBearingType",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO14179SettingsPerBearingType.TYPE"):
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
    def rolling_bearing_type(self: Self) -> "_1903.RollingBearingType":
        """mastapy.bearings.RollingBearingType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RollingBearingType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.RollingBearingType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.bearings._1903", "RollingBearingType"
        )(value)

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
    def cast_to(
        self: Self,
    ) -> "ISO14179SettingsPerBearingType._Cast_ISO14179SettingsPerBearingType":
        return self._Cast_ISO14179SettingsPerBearingType(self)
