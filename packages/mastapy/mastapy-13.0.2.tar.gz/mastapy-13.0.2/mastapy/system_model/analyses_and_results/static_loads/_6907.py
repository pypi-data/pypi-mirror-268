"""HarmonicLoadDataCSVImport"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CSV_IMPORT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "HarmonicLoadDataCSVImport",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6877,
        _6889,
        _6909,
        _6912,
        _6910,
    )


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataCSVImport",)


Self = TypeVar("Self", bound="HarmonicLoadDataCSVImport")
T = TypeVar("T", bound="_6889.ElectricMachineHarmonicLoadImportOptionsBase")


class HarmonicLoadDataCSVImport(_6911.HarmonicLoadDataImportFromMotorPackages[T]):
    """HarmonicLoadDataCSVImport

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _HARMONIC_LOAD_DATA_CSV_IMPORT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HarmonicLoadDataCSVImport")

    class _Cast_HarmonicLoadDataCSVImport:
        """Special nested class for casting HarmonicLoadDataCSVImport to subclasses."""

        def __init__(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
            parent: "HarmonicLoadDataCSVImport",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_import_from_motor_packages(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "_6911.HarmonicLoadDataImportFromMotorPackages":
            return self._parent._cast(_6911.HarmonicLoadDataImportFromMotorPackages)

        @property
        def harmonic_load_data_import_base(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "_6910.HarmonicLoadDataImportBase":
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.HarmonicLoadDataImportBase)

        @property
        def harmonic_load_data_flux_import(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "_6909.HarmonicLoadDataFluxImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.HarmonicLoadDataFluxImport)

        @property
        def harmonic_load_data_jmag_import(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "_6912.HarmonicLoadDataJMAGImport":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.HarmonicLoadDataJMAGImport)

        @property
        def harmonic_load_data_csv_import(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport",
        ) -> "HarmonicLoadDataCSVImport":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HarmonicLoadDataCSVImport.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_data_per_speed(
        self: Self,
    ) -> "List[_6877.DataFromMotorPackagePerSpeed]":
        """List[mastapy.system_model.analyses_and_results.static_loads.DataFromMotorPackagePerSpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectricMachineDataPerSpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicLoadDataCSVImport._Cast_HarmonicLoadDataCSVImport":
        return self._Cast_HarmonicLoadDataCSVImport(self)
