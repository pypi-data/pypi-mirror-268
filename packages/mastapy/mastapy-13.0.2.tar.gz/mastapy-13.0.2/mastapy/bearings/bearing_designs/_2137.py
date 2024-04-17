"""BearingDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_DESIGN = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "BearingDesign"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1525
    from mastapy.bearings.bearing_designs import _2138, _2139, _2140, _2141
    from mastapy.bearings.bearing_designs.rolling import (
        _2142,
        _2143,
        _2144,
        _2145,
        _2146,
        _2147,
        _2149,
        _2155,
        _2156,
        _2157,
        _2161,
        _2166,
        _2167,
        _2168,
        _2169,
        _2172,
        _2173,
        _2176,
        _2177,
        _2178,
        _2179,
        _2180,
        _2181,
    )
    from mastapy.bearings.bearing_designs.fluid_film import (
        _2194,
        _2196,
        _2198,
        _2200,
        _2201,
        _2202,
    )
    from mastapy.bearings.bearing_designs.concept import _2204, _2205, _2206


__docformat__ = "restructuredtext en"
__all__ = ("BearingDesign",)


Self = TypeVar("Self", bound="BearingDesign")


class BearingDesign(_0.APIBase):
    """BearingDesign

    This is a mastapy class.
    """

    TYPE = _BEARING_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingDesign")

    class _Cast_BearingDesign:
        """Special nested class for casting BearingDesign to subclasses."""

        def __init__(
            self: "BearingDesign._Cast_BearingDesign", parent: "BearingDesign"
        ):
            self._parent = parent

        @property
        def detailed_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2138.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2138

            return self._parent._cast(_2138.DetailedBearing)

        @property
        def dummy_rolling_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2139.DummyRollingBearing":
            from mastapy.bearings.bearing_designs import _2139

            return self._parent._cast(_2139.DummyRollingBearing)

        @property
        def linear_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2140.LinearBearing":
            from mastapy.bearings.bearing_designs import _2140

            return self._parent._cast(_2140.LinearBearing)

        @property
        def non_linear_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2141.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2141

            return self._parent._cast(_2141.NonLinearBearing)

        @property
        def angular_contact_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2142.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2142

            return self._parent._cast(_2142.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2143.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2143

            return self._parent._cast(_2143.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2144.AsymmetricSphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2144

            return self._parent._cast(_2144.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2145.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2145

            return self._parent._cast(_2145.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2146.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2146

            return self._parent._cast(_2146.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2147.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2147

            return self._parent._cast(_2147.BallBearing)

        @property
        def barrel_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2149.BarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2149

            return self._parent._cast(_2149.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2155.CrossedRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2155

            return self._parent._cast(_2155.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2156.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2157.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2161.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2161

            return self._parent._cast(_2161.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2166.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2166

            return self._parent._cast(_2166.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2167.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2168.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2169.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.RollerBearing)

        @property
        def rolling_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2172.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.RollingBearing)

        @property
        def self_aligning_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2173.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2173

            return self._parent._cast(_2173.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2176.SphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2176

            return self._parent._cast(_2176.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2177.SphericalRollerThrustBearing":
            from mastapy.bearings.bearing_designs.rolling import _2177

            return self._parent._cast(_2177.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2178.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2178

            return self._parent._cast(_2178.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2179.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2179

            return self._parent._cast(_2179.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2180.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2180

            return self._parent._cast(_2180.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2181.ToroidalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2181

            return self._parent._cast(_2181.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2194.PadFluidFilmBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2194

            return self._parent._cast(_2194.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2196.PlainGreaseFilledJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2196

            return self._parent._cast(_2196.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2198.PlainJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2198

            return self._parent._cast(_2198.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2200.PlainOilFedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2200

            return self._parent._cast(_2200.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2201.TiltingPadJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2201

            return self._parent._cast(_2201.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2202.TiltingPadThrustBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2202

            return self._parent._cast(_2202.TiltingPadThrustBearing)

        @property
        def concept_axial_clearance_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2204.ConceptAxialClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2204

            return self._parent._cast(_2204.ConceptAxialClearanceBearing)

        @property
        def concept_clearance_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2205.ConceptClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2205

            return self._parent._cast(_2205.ConceptClearanceBearing)

        @property
        def concept_radial_clearance_bearing(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "_2206.ConceptRadialClearanceBearing":
            from mastapy.bearings.bearing_designs.concept import _2206

            return self._parent._cast(_2206.ConceptRadialClearanceBearing)

        @property
        def bearing_design(
            self: "BearingDesign._Cast_BearingDesign",
        ) -> "BearingDesign":
            return self._parent

        def __getattr__(self: "BearingDesign._Cast_BearingDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return temp

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "float"):
        self.wrapped.Bore = float(value) if value is not None else 0.0

    @property
    def mass(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Mass = value

    @property
    def outer_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return temp

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "float"):
        self.wrapped.OuterDiameter = float(value) if value is not None else 0.0

    @property
    def type_(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Type

        if temp is None:
            return ""

        return temp

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def mass_properties_of_elements_from_geometry(self: Self) -> "_1525.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfElementsFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_of_inner_ring_from_geometry(
        self: Self,
    ) -> "_1525.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfInnerRingFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_of_outer_ring_from_geometry(
        self: Self,
    ) -> "_1525.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesOfOuterRingFromGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def total_mass_properties(self: Self) -> "_1525.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalMassProperties

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
    def cast_to(self: Self) -> "BearingDesign._Cast_BearingDesign":
        return self._Cast_BearingDesign(self)
