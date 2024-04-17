"""LoadedRollingBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollingBearingRow"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874
    from mastapy.bearings.bearing_results.rolling import (
        _2040,
        _1980,
        _2021,
        _2039,
        _2075,
        _2080,
        _1991,
        _1994,
        _1997,
        _2002,
        _2005,
        _2010,
        _2013,
        _2017,
        _2020,
        _2025,
        _2029,
        _2032,
        _2037,
        _2044,
        _2048,
        _2051,
        _2056,
        _2059,
        _2062,
        _2065,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollingBearingRow",)


Self = TypeVar("Self", bound="LoadedRollingBearingRow")


class LoadedRollingBearingRow(_0.APIBase):
    """LoadedRollingBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollingBearingRow")

    class _Cast_LoadedRollingBearingRow:
        """Special nested class for casting LoadedRollingBearingRow to subclasses."""

        def __init__(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
            parent: "LoadedRollingBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_angular_contact_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_1991.LoadedAngularContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _1991

            return self._parent._cast(_1991.LoadedAngularContactBallBearingRow)

        @property
        def loaded_angular_contact_thrust_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_1994.LoadedAngularContactThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(_1994.LoadedAngularContactThrustBallBearingRow)

        @property
        def loaded_asymmetric_spherical_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_1997.LoadedAsymmetricSphericalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _1997

            return self._parent._cast(_1997.LoadedAsymmetricSphericalRollerBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2002.LoadedAxialThrustCylindricalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2002

            return self._parent._cast(
                _2002.LoadedAxialThrustCylindricalRollerBearingRow
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2005.LoadedAxialThrustNeedleRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2005

            return self._parent._cast(_2005.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2010.LoadedBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2010

            return self._parent._cast(_2010.LoadedBallBearingRow)

        @property
        def loaded_crossed_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2013.LoadedCrossedRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2013

            return self._parent._cast(_2013.LoadedCrossedRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2017.LoadedCylindricalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2017

            return self._parent._cast(_2017.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_deep_groove_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2020.LoadedDeepGrooveBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2020

            return self._parent._cast(_2020.LoadedDeepGrooveBallBearingRow)

        @property
        def loaded_four_point_contact_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2025.LoadedFourPointContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2025

            return self._parent._cast(_2025.LoadedFourPointContactBallBearingRow)

        @property
        def loaded_needle_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2029.LoadedNeedleRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2029

            return self._parent._cast(_2029.LoadedNeedleRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2032.LoadedNonBarrelRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2032

            return self._parent._cast(_2032.LoadedNonBarrelRollerBearingRow)

        @property
        def loaded_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2037.LoadedRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2037

            return self._parent._cast(_2037.LoadedRollerBearingRow)

        @property
        def loaded_self_aligning_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2044.LoadedSelfAligningBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2044

            return self._parent._cast(_2044.LoadedSelfAligningBallBearingRow)

        @property
        def loaded_spherical_roller_radial_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2048.LoadedSphericalRollerRadialBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2048

            return self._parent._cast(_2048.LoadedSphericalRollerRadialBearingRow)

        @property
        def loaded_spherical_roller_thrust_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2051.LoadedSphericalRollerThrustBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedSphericalRollerThrustBearingRow)

        @property
        def loaded_taper_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2056.LoadedTaperRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2056

            return self._parent._cast(_2056.LoadedTaperRollerBearingRow)

        @property
        def loaded_three_point_contact_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2059.LoadedThreePointContactBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2059

            return self._parent._cast(_2059.LoadedThreePointContactBallBearingRow)

        @property
        def loaded_thrust_ball_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2062.LoadedThrustBallBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2062

            return self._parent._cast(_2062.LoadedThrustBallBearingRow)

        @property
        def loaded_toroidal_roller_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "_2065.LoadedToroidalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2065

            return self._parent._cast(_2065.LoadedToroidalRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow",
        ) -> "LoadedRollingBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollingBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_equivalent_reference_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicEquivalentReferenceLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def life_modification_factor_for_systems_approach(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LifeModificationFactorForSystemsApproach

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_element_normal_stress_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumElementNormalStressOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadInner

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_normal_load_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumNormalLoadOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_contact_stress_chart_inner(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_left(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_outer(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def normal_contact_stress_chart_right(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalContactStressChartRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def row_id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RowID

        if temp is None:
            return ""

        return temp

    @property
    def subsurface_shear_stress_chart_inner(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressChartInner

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def subsurface_shear_stress_chart_outer(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressChartOuter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def loaded_bearing(self: Self) -> "_2040.LoadedRollingBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedRollingBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_operating_internal_clearance(self: Self) -> "_1980.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def minimum_operating_internal_clearance(self: Self) -> "_1980.InternalClearance":
        """mastapy.bearings.bearing_results.rolling.InternalClearance

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingInternalClearance

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def elements(self: Self) -> "List[_2021.LoadedElement]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedElement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Elements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def race_results(self: Self) -> "List[_2039.LoadedRollingBearingRaceResults]":
        """List[mastapy.bearings.bearing_results.rolling.LoadedRollingBearingRaceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RaceResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ring_force_and_displacement_results(
        self: Self,
    ) -> "List[_2075.RingForceAndDisplacement]":
        """List[mastapy.bearings.bearing_results.rolling.RingForceAndDisplacement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RingForceAndDisplacementResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def subsurface_shear_stress_for_most_heavily_loaded_element_inner(
        self: Self,
    ) -> "List[_2080.StressAtPosition]":
        """List[mastapy.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressForMostHeavilyLoadedElementInner

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def subsurface_shear_stress_for_most_heavily_loaded_element_outer(
        self: Self,
    ) -> "List[_2080.StressAtPosition]":
        """List[mastapy.bearings.bearing_results.rolling.StressAtPosition]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SubsurfaceShearStressForMostHeavilyLoadedElementOuter

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

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
    def cast_to(self: Self) -> "LoadedRollingBearingRow._Cast_LoadedRollingBearingRow":
        return self._Cast_LoadedRollingBearingRow(self)
