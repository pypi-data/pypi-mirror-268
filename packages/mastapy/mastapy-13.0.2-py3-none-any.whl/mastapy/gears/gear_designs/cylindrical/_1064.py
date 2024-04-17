"""LTCASettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LTCA_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "LTCASettings"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1063


__docformat__ = "restructuredtext en"
__all__ = ("LTCASettings",)


Self = TypeVar("Self", bound="LTCASettings")


class LTCASettings(_1593.IndependentReportablePropertiesBase["LTCASettings"]):
    """LTCASettings

    This is a mastapy class.
    """

    TYPE = _LTCA_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LTCASettings")

    class _Cast_LTCASettings:
        """Special nested class for casting LTCASettings to subclasses."""

        def __init__(self: "LTCASettings._Cast_LTCASettings", parent: "LTCASettings"):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "LTCASettings._Cast_LTCASettings",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def ltca_settings(self: "LTCASettings._Cast_LTCASettings") -> "LTCASettings":
            return self._parent

        def __getattr__(self: "LTCASettings._Cast_LTCASettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LTCASettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_utilization_load_cutoff_parameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceUtilizationLoadCutoffParameter

        if temp is None:
            return 0.0

        return temp

    @face_utilization_load_cutoff_parameter.setter
    @enforce_parameter_types
    def face_utilization_load_cutoff_parameter(self: Self, value: "float"):
        self.wrapped.FaceUtilizationLoadCutoffParameter = (
            float(value) if value is not None else 0.0
        )

    @property
    def include_extended_tip_contact(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IncludeExtendedTipContact

        if temp is None:
            return False

        return temp

    @include_extended_tip_contact.setter
    @enforce_parameter_types
    def include_extended_tip_contact(self: Self, value: "bool"):
        self.wrapped.IncludeExtendedTipContact = (
            bool(value) if value is not None else False
        )

    @property
    def load_case_modifiable_settings(
        self: Self,
    ) -> "_1063.LTCALoadCaseModifiableSettings":
        """mastapy.gears.gear_designs.cylindrical.LTCALoadCaseModifiableSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseModifiableSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "LTCASettings._Cast_LTCASettings":
        return self._Cast_LTCASettings(self)
