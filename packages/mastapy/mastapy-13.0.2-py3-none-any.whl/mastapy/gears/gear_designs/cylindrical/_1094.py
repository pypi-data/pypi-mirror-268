"""Usage"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_USAGE = python_net_import("SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "Usage")

if TYPE_CHECKING:
    from mastapy.gears import _348
    from mastapy.gears.gear_designs.cylindrical import _1081


__docformat__ = "restructuredtext en"
__all__ = ("Usage",)


Self = TypeVar("Self", bound="Usage")


class Usage(_1593.IndependentReportablePropertiesBase["Usage"]):
    """Usage

    This is a mastapy class.
    """

    TYPE = _USAGE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Usage")

    class _Cast_Usage:
        """Special nested class for casting Usage to subclasses."""

        def __init__(self: "Usage._Cast_Usage", parent: "Usage"):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "Usage._Cast_Usage",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def usage(self: "Usage._Cast_Usage") -> "Usage":
            return self._parent

        def __getattr__(self: "Usage._Cast_Usage", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Usage.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gearing_is_runin(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.GearingIsRunin

        if temp is None:
            return False

        return temp

    @gearing_is_runin.setter
    @enforce_parameter_types
    def gearing_is_runin(self: Self, value: "bool"):
        self.wrapped.GearingIsRunin = bool(value) if value is not None else False

    @property
    def improved_gearing(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ImprovedGearing

        if temp is None:
            return False

        return temp

    @improved_gearing.setter
    @enforce_parameter_types
    def improved_gearing(self: Self, value: "bool"):
        self.wrapped.ImprovedGearing = bool(value) if value is not None else False

    @property
    def leads_modified(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.LeadsModified

        if temp is None:
            return False

        return temp

    @leads_modified.setter
    @enforce_parameter_types
    def leads_modified(self: Self, value: "bool"):
        self.wrapped.LeadsModified = bool(value) if value is not None else False

    @property
    def safety_requirement(self: Self) -> "_348.SafetyRequirementsAGMA":
        """mastapy.gears.SafetyRequirementsAGMA"""
        temp = self.wrapped.SafetyRequirement

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.SafetyRequirementsAGMA"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._348", "SafetyRequirementsAGMA"
        )(value)

    @safety_requirement.setter
    @enforce_parameter_types
    def safety_requirement(self: Self, value: "_348.SafetyRequirementsAGMA"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.SafetyRequirementsAGMA"
        )
        self.wrapped.SafetyRequirement = value

    @property
    def spur_gear_load_sharing_code(self: Self) -> "_1081.SpurGearLoadSharingCodes":
        """mastapy.gears.gear_designs.cylindrical.SpurGearLoadSharingCodes"""
        temp = self.wrapped.SpurGearLoadSharingCode

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.SpurGearLoadSharingCodes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1081", "SpurGearLoadSharingCodes"
        )(value)

    @spur_gear_load_sharing_code.setter
    @enforce_parameter_types
    def spur_gear_load_sharing_code(
        self: Self, value: "_1081.SpurGearLoadSharingCodes"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.SpurGearLoadSharingCodes"
        )
        self.wrapped.SpurGearLoadSharingCode = value

    @property
    def cast_to(self: Self) -> "Usage._Cast_Usage":
        return self._Cast_Usage(self)
