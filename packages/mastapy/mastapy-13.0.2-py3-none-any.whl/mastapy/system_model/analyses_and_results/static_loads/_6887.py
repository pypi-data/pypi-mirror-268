"""ElectricMachineHarmonicLoadExcelImportOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6889
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_EXCEL_IMPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadExcelImportOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadExcelImportOptions",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadExcelImportOptions")


class ElectricMachineHarmonicLoadExcelImportOptions(
    _6889.ElectricMachineHarmonicLoadImportOptionsBase
):
    """ElectricMachineHarmonicLoadExcelImportOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_EXCEL_IMPORT_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadExcelImportOptions"
    )

    class _Cast_ElectricMachineHarmonicLoadExcelImportOptions:
        """Special nested class for casting ElectricMachineHarmonicLoadExcelImportOptions to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadExcelImportOptions._Cast_ElectricMachineHarmonicLoadExcelImportOptions",
            parent: "ElectricMachineHarmonicLoadExcelImportOptions",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_import_options_base(
            self: "ElectricMachineHarmonicLoadExcelImportOptions._Cast_ElectricMachineHarmonicLoadExcelImportOptions",
        ) -> "_6889.ElectricMachineHarmonicLoadImportOptionsBase":
            return self._parent._cast(
                _6889.ElectricMachineHarmonicLoadImportOptionsBase
            )

        @property
        def electric_machine_harmonic_load_excel_import_options(
            self: "ElectricMachineHarmonicLoadExcelImportOptions._Cast_ElectricMachineHarmonicLoadExcelImportOptions",
        ) -> "ElectricMachineHarmonicLoadExcelImportOptions":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadExcelImportOptions._Cast_ElectricMachineHarmonicLoadExcelImportOptions",
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
        self: Self,
        instance_to_wrap: "ElectricMachineHarmonicLoadExcelImportOptions.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadExcelImportOptions._Cast_ElectricMachineHarmonicLoadExcelImportOptions":
        return self._Cast_ElectricMachineHarmonicLoadExcelImportOptions(self)
