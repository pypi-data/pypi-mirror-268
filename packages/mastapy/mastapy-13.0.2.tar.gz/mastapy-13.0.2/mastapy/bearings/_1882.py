"""BearingLoadCaseResultsLightweight"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_LOAD_CASE_RESULTS_LIGHTWEIGHT = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingLoadCaseResultsLightweight"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1881
    from mastapy.bearings.bearing_results import (
        _1956,
        _1958,
        _1959,
        _1960,
        _1961,
        _1962,
        _1964,
    )
    from mastapy.bearings.bearing_results.rolling import (
        _1990,
        _1993,
        _1996,
        _2001,
        _2004,
        _2009,
        _2012,
        _2016,
        _2019,
        _2024,
        _2028,
        _2031,
        _2036,
        _2040,
        _2043,
        _2047,
        _2050,
        _2055,
        _2058,
        _2061,
        _2064,
    )
    from mastapy.bearings.bearing_results.fluid_film import (
        _2126,
        _2127,
        _2128,
        _2129,
        _2131,
        _2134,
        _2135,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BearingLoadCaseResultsLightweight",)


Self = TypeVar("Self", bound="BearingLoadCaseResultsLightweight")


class BearingLoadCaseResultsLightweight(_0.APIBase):
    """BearingLoadCaseResultsLightweight

    This is a mastapy class.
    """

    TYPE = _BEARING_LOAD_CASE_RESULTS_LIGHTWEIGHT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingLoadCaseResultsLightweight")

    class _Cast_BearingLoadCaseResultsLightweight:
        """Special nested class for casting BearingLoadCaseResultsLightweight to subclasses."""

        def __init__(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
            parent: "BearingLoadCaseResultsLightweight",
        ):
            self._parent = parent

        @property
        def bearing_load_case_results_for_pst(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1881.BearingLoadCaseResultsForPST":
            from mastapy.bearings import _1881

            return self._parent._cast(_1881.BearingLoadCaseResultsForPST)

        @property
        def loaded_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1956.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedBearingResults)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1958.LoadedConceptAxialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1958

            return self._parent._cast(_1958.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1959.LoadedConceptClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1959

            return self._parent._cast(_1959.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1960.LoadedConceptRadialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1960

            return self._parent._cast(_1960.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1961.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1961

            return self._parent._cast(_1961.LoadedDetailedBearingResults)

        @property
        def loaded_linear_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1962.LoadedLinearBearingResults":
            from mastapy.bearings.bearing_results import _1962

            return self._parent._cast(_1962.LoadedLinearBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1964.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1964

            return self._parent._cast(_1964.LoadedNonLinearBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1990.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1990

            return self._parent._cast(_1990.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1993.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1993

            return self._parent._cast(
                _1993.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1996.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _1996

            return self._parent._cast(
                _1996.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2001.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2001

            return self._parent._cast(
                _2001.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2004.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(_2004.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2009.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(_2009.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2012.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(_2012.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2016.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2016

            return self._parent._cast(_2016.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2019.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2019

            return self._parent._cast(_2019.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2024.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2024

            return self._parent._cast(_2024.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2028.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2031.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2031

            return self._parent._cast(_2031.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2036.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2036

            return self._parent._cast(_2036.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2040.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2043.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2043

            return self._parent._cast(_2043.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2047.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2047

            return self._parent._cast(_2047.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2050.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2050

            return self._parent._cast(_2050.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2055.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2055

            return self._parent._cast(_2055.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2058.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2058

            return self._parent._cast(_2058.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2061.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2061

            return self._parent._cast(_2061.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2064.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2064

            return self._parent._cast(_2064.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2126.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2126

            return self._parent._cast(_2126.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2127.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2127

            return self._parent._cast(_2127.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2128.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2128

            return self._parent._cast(_2128.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2129.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2129

            return self._parent._cast(_2129.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2131.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2131

            return self._parent._cast(_2131.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2134.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2134

            return self._parent._cast(_2134.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2135.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2135

            return self._parent._cast(_2135.LoadedTiltingPadThrustBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "BearingLoadCaseResultsLightweight":
            return self._parent

        def __getattr__(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
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
        self: Self, instance_to_wrap: "BearingLoadCaseResultsLightweight.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

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
    def cast_to(
        self: Self,
    ) -> "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight":
        return self._Cast_BearingLoadCaseResultsLightweight(self)
