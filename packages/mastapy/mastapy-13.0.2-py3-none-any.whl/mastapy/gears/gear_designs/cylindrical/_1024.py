"""CylindricalGearMicroGeometrySettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility import _1593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearMicroGeometrySettings"
)

if TYPE_CHECKING:
    from mastapy.gears.micro_geometry import _574
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1128
    from mastapy.gears.gear_designs.cylindrical import _1049


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMicroGeometrySettings",)


Self = TypeVar("Self", bound="CylindricalGearMicroGeometrySettings")


class CylindricalGearMicroGeometrySettings(
    _1593.IndependentReportablePropertiesBase["CylindricalGearMicroGeometrySettings"]
):
    """CylindricalGearMicroGeometrySettings

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMicroGeometrySettings")

    class _Cast_CylindricalGearMicroGeometrySettings:
        """Special nested class for casting CylindricalGearMicroGeometrySettings to subclasses."""

        def __init__(
            self: "CylindricalGearMicroGeometrySettings._Cast_CylindricalGearMicroGeometrySettings",
            parent: "CylindricalGearMicroGeometrySettings",
        ):
            self._parent = parent

        @property
        def independent_reportable_properties_base(
            self: "CylindricalGearMicroGeometrySettings._Cast_CylindricalGearMicroGeometrySettings",
        ) -> "_1593.IndependentReportablePropertiesBase":
            pass

            return self._parent._cast(_1593.IndependentReportablePropertiesBase)

        @property
        def cylindrical_gear_micro_geometry_settings(
            self: "CylindricalGearMicroGeometrySettings._Cast_CylindricalGearMicroGeometrySettings",
        ) -> "CylindricalGearMicroGeometrySettings":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMicroGeometrySettings._Cast_CylindricalGearMicroGeometrySettings",
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
        self: Self, instance_to_wrap: "CylindricalGearMicroGeometrySettings.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_side_with_zero_face_width(self: Self) -> "_574.FlankSide":
        """mastapy.gears.micro_geometry.FlankSide"""
        temp = self.wrapped.FlankSideWithZeroFaceWidth

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.MicroGeometry.FlankSide"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.micro_geometry._574", "FlankSide"
        )(value)

    @flank_side_with_zero_face_width.setter
    @enforce_parameter_types
    def flank_side_with_zero_face_width(self: Self, value: "_574.FlankSide"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.MicroGeometry.FlankSide"
        )
        self.wrapped.FlankSideWithZeroFaceWidth = value

    @property
    def micro_geometry_lead_tolerance_chart_view(
        self: Self,
    ) -> "_1128.MicroGeometryLeadToleranceChartView":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.MicroGeometryLeadToleranceChartView"""
        temp = self.wrapped.MicroGeometryLeadToleranceChartView

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry.MicroGeometryLeadToleranceChartView",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical.micro_geometry._1128",
            "MicroGeometryLeadToleranceChartView",
        )(value)

    @micro_geometry_lead_tolerance_chart_view.setter
    @enforce_parameter_types
    def micro_geometry_lead_tolerance_chart_view(
        self: Self, value: "_1128.MicroGeometryLeadToleranceChartView"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry.MicroGeometryLeadToleranceChartView",
        )
        self.wrapped.MicroGeometryLeadToleranceChartView = value

    @property
    def scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts(
        self: Self,
    ) -> "_1049.DoubleAxisScaleAndRange":
        """mastapy.gears.gear_designs.cylindrical.DoubleAxisScaleAndRange"""
        temp = (
            self.wrapped.ScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.DoubleAxisScaleAndRange"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1049", "DoubleAxisScaleAndRange"
        )(value)

    @scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts.setter
    @enforce_parameter_types
    def scale_and_range_of_flank_relief_axes_for_micro_geometry_tolerance_charts(
        self: Self, value: "_1049.DoubleAxisScaleAndRange"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.DoubleAxisScaleAndRange"
        )
        self.wrapped.ScaleAndRangeOfFlankReliefAxesForMicroGeometryToleranceCharts = (
            value
        )

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMicroGeometrySettings._Cast_CylindricalGearMicroGeometrySettings":
        return self._Cast_CylindricalGearMicroGeometrySettings(self)
