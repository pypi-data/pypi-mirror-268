"""SKFModuleResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SKF_MODULE_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule", "SKFModuleResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling.skf_module import (
        _2083,
        _2085,
        _2086,
        _2087,
        _2088,
        _2090,
        _2094,
        _2098,
        _2106,
        _2107,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SKFModuleResults",)


Self = TypeVar("Self", bound="SKFModuleResults")


class SKFModuleResults(_0.APIBase):
    """SKFModuleResults

    This is a mastapy class.
    """

    TYPE = _SKF_MODULE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SKFModuleResults")

    class _Cast_SKFModuleResults:
        """Special nested class for casting SKFModuleResults to subclasses."""

        def __init__(
            self: "SKFModuleResults._Cast_SKFModuleResults", parent: "SKFModuleResults"
        ):
            self._parent = parent

        @property
        def skf_module_results(
            self: "SKFModuleResults._Cast_SKFModuleResults",
        ) -> "SKFModuleResults":
            return self._parent

        def __getattr__(self: "SKFModuleResults._Cast_SKFModuleResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SKFModuleResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjusted_speed(self: Self) -> "_2083.AdjustedSpeed":
        """mastapy.bearings.bearing_results.rolling.skf_module.AdjustedSpeed

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdjustedSpeed

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_loads(self: Self) -> "_2085.BearingLoads":
        """mastapy.bearings.bearing_results.rolling.skf_module.BearingLoads

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingLoads

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bearing_rating_life(self: Self) -> "_2086.BearingRatingLife":
        """mastapy.bearings.bearing_results.rolling.skf_module.BearingRatingLife

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BearingRatingLife

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def dynamic_axial_load_carrying_capacity(
        self: Self,
    ) -> "_2087.DynamicAxialLoadCarryingCapacity":
        """mastapy.bearings.bearing_results.rolling.skf_module.DynamicAxialLoadCarryingCapacity

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicAxialLoadCarryingCapacity

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def frequencies(self: Self) -> "_2088.Frequencies":
        """mastapy.bearings.bearing_results.rolling.skf_module.Frequencies

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Frequencies

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def friction(self: Self) -> "_2090.Friction":
        """mastapy.bearings.bearing_results.rolling.skf_module.Friction

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Friction

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def grease_life_and_relubrication_interval(
        self: Self,
    ) -> "_2094.GreaseLifeAndRelubricationInterval":
        """mastapy.bearings.bearing_results.rolling.skf_module.GreaseLifeAndRelubricationInterval

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GreaseLifeAndRelubricationInterval

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_load(self: Self) -> "_2098.MinimumLoad":
        """mastapy.bearings.bearing_results.rolling.skf_module.MinimumLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_safety_factors(self: Self) -> "_2106.StaticSafetyFactors":
        """mastapy.bearings.bearing_results.rolling.skf_module.StaticSafetyFactors

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticSafetyFactors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def viscosities(self: Self) -> "_2107.Viscosities":
        """mastapy.bearings.bearing_results.rolling.skf_module.Viscosities

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Viscosities

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "SKFModuleResults._Cast_SKFModuleResults":
        return self._Cast_SKFModuleResults(self)
