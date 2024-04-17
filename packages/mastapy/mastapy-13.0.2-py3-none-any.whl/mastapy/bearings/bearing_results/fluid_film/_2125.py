"""LoadedFluidFilmBearingPad"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FLUID_FILM_BEARING_PAD = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedFluidFilmBearingPad"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import _2133, _2136


__docformat__ = "restructuredtext en"
__all__ = ("LoadedFluidFilmBearingPad",)


Self = TypeVar("Self", bound="LoadedFluidFilmBearingPad")


class LoadedFluidFilmBearingPad(_0.APIBase):
    """LoadedFluidFilmBearingPad

    This is a mastapy class.
    """

    TYPE = _LOADED_FLUID_FILM_BEARING_PAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedFluidFilmBearingPad")

    class _Cast_LoadedFluidFilmBearingPad:
        """Special nested class for casting LoadedFluidFilmBearingPad to subclasses."""

        def __init__(
            self: "LoadedFluidFilmBearingPad._Cast_LoadedFluidFilmBearingPad",
            parent: "LoadedFluidFilmBearingPad",
        ):
            self._parent = parent

        @property
        def loaded_tilting_journal_pad(
            self: "LoadedFluidFilmBearingPad._Cast_LoadedFluidFilmBearingPad",
        ) -> "_2133.LoadedTiltingJournalPad":
            from mastapy.bearings.bearing_results.fluid_film import _2133

            return self._parent._cast(_2133.LoadedTiltingJournalPad)

        @property
        def loaded_tilting_thrust_pad(
            self: "LoadedFluidFilmBearingPad._Cast_LoadedFluidFilmBearingPad",
        ) -> "_2136.LoadedTiltingThrustPad":
            from mastapy.bearings.bearing_results.fluid_film import _2136

            return self._parent._cast(_2136.LoadedTiltingThrustPad)

        @property
        def loaded_fluid_film_bearing_pad(
            self: "LoadedFluidFilmBearingPad._Cast_LoadedFluidFilmBearingPad",
        ) -> "LoadedFluidFilmBearingPad":
            return self._parent

        def __getattr__(
            self: "LoadedFluidFilmBearingPad._Cast_LoadedFluidFilmBearingPad", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedFluidFilmBearingPad.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Misalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def pad_id(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PadID

        if temp is None:
            return ""

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
    ) -> "LoadedFluidFilmBearingPad._Cast_LoadedFluidFilmBearingPad":
        return self._Cast_LoadedFluidFilmBearingPad(self)
