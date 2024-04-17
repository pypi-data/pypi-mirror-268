"""ShaftDamageResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_DAMAGE_RESULTS = python_net_import("SMT.MastaAPI.Shafts", "ShaftDamageResults")

if TYPE_CHECKING:
    from mastapy.math_utility import _1533
    from mastapy.nodal_analysis import _85
    from mastapy.shafts import _37, _40, _36
    from mastapy.utility.report import _1793


__docformat__ = "restructuredtext en"
__all__ = ("ShaftDamageResults",)


Self = TypeVar("Self", bound="ShaftDamageResults")


class ShaftDamageResults(_0.APIBase):
    """ShaftDamageResults

    This is a mastapy class.
    """

    TYPE = _SHAFT_DAMAGE_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftDamageResults")

    class _Cast_ShaftDamageResults:
        """Special nested class for casting ShaftDamageResults to subclasses."""

        def __init__(
            self: "ShaftDamageResults._Cast_ShaftDamageResults",
            parent: "ShaftDamageResults",
        ):
            self._parent = parent

        @property
        def shaft_damage_results(
            self: "ShaftDamageResults._Cast_ShaftDamageResults",
        ) -> "ShaftDamageResults":
            return self._parent

        def __getattr__(self: "ShaftDamageResults._Cast_ShaftDamageResults", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftDamageResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cyclic_degrees_of_utilisation(self: Self) -> "List[_1533.RealVector]":
        """List[mastapy.math_utility.RealVector]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CyclicDegreesOfUtilisation

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def displacement_angular(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def displacement_linear(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementLinear

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def displacement_maximum_radial_magnitude(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementMaximumRadialMagnitude

        if temp is None:
            return 0.0

        return temp

    @property
    def force_angular(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceAngular

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def force_linear(self: Self) -> "List[Vector3D]":
        """List[Vector3D]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceLinear

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector3D)

        if value is None:
            return None

        return value

    @property
    def rating_type_for_shaft_reliability(
        self: Self,
    ) -> "_85.RatingTypeForShaftReliability":
        """mastapy.nodal_analysis.RatingTypeForShaftReliability

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingTypeForShaftReliability

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.RatingTypeForShaftReliability"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._85", "RatingTypeForShaftReliability"
        )(value)

    @property
    def stress_highest_equivalent_fully_reversed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressHighestEquivalentFullyReversed

        if temp is None:
            return 0.0

        return temp

    @property
    def using_fkm_shaft_rating_method(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UsingFKMShaftRatingMethod

        if temp is None:
            return False

        return temp

    @property
    def worst_fatigue_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstFatigueDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_fatigue_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstFatigueSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_fatigue_safety_factor_for_infinite_life(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstFatigueSafetyFactorForInfiniteLife

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_reliability_for_finite_life(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstReliabilityForFiniteLife

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_reliability_for_infinite_life(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstReliabilityForInfiniteLife

        if temp is None:
            return 0.0

        return temp

    @property
    def worst_static_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorstStaticSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor(
        self: Self,
    ) -> "_37.ShaftSectionEndDamageResults":
        """mastapy.shafts.ShaftSectionEndDamageResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor_for_infinite_life(
        self: Self,
    ) -> "_37.ShaftSectionEndDamageResults":
        """mastapy.shafts.ShaftSectionEndDamageResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_section_end_with_worst_static_safety_factor(
        self: Self,
    ) -> "_37.ShaftSectionEndDamageResults":
        """mastapy.shafts.ShaftSectionEndDamageResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionEndWithWorstStaticSafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_settings(self: Self) -> "_40.ShaftSettingsItem":
        """mastapy.shafts.ShaftSettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_section_damage_results(
        self: Self,
    ) -> "List[_36.ShaftSectionDamageResults]":
        """List[mastapy.shafts.ShaftSectionDamageResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionDamageResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_section_end_results_by_offset_with_worst_safety_factor(
        self: Self,
    ) -> "List[_37.ShaftSectionEndDamageResults]":
        """List[mastapy.shafts.ShaftSectionEndDamageResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftSectionEndResultsByOffsetWithWorstSafetyFactor

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_damage_chart_items(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftDamageChartItems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

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
    def shaft_damage_chart(
        self: Self, item: "str", title: "str"
    ) -> "_1793.SimpleChartDefinition":
        """mastapy.utility.report.SimpleChartDefinition

        Args:
            item (str)
            title (str)
        """
        item = str(item)
        title = str(title)
        method_result = self.wrapped.ShaftDamageChart(
            item if item else "", title if title else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

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
    def cast_to(self: Self) -> "ShaftDamageResults._Cast_ShaftDamageResults":
        return self._Cast_ShaftDamageResults(self)
