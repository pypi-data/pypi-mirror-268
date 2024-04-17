"""ElectricMachineHarmonicLoadFluxImportOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6889
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_FLUX_IMPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadFluxImportOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadFluxImportOptions",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadFluxImportOptions")


class ElectricMachineHarmonicLoadFluxImportOptions(
    _6889.ElectricMachineHarmonicLoadImportOptionsBase
):
    """ElectricMachineHarmonicLoadFluxImportOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_FLUX_IMPORT_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadFluxImportOptions"
    )

    class _Cast_ElectricMachineHarmonicLoadFluxImportOptions:
        """Special nested class for casting ElectricMachineHarmonicLoadFluxImportOptions to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadFluxImportOptions._Cast_ElectricMachineHarmonicLoadFluxImportOptions",
            parent: "ElectricMachineHarmonicLoadFluxImportOptions",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_import_options_base(
            self: "ElectricMachineHarmonicLoadFluxImportOptions._Cast_ElectricMachineHarmonicLoadFluxImportOptions",
        ) -> "_6889.ElectricMachineHarmonicLoadImportOptionsBase":
            return self._parent._cast(
                _6889.ElectricMachineHarmonicLoadImportOptionsBase
            )

        @property
        def electric_machine_harmonic_load_flux_import_options(
            self: "ElectricMachineHarmonicLoadFluxImportOptions._Cast_ElectricMachineHarmonicLoadFluxImportOptions",
        ) -> "ElectricMachineHarmonicLoadFluxImportOptions":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadFluxImportOptions._Cast_ElectricMachineHarmonicLoadFluxImportOptions",
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
        instance_to_wrap: "ElectricMachineHarmonicLoadFluxImportOptions.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadFluxImportOptions._Cast_ElectricMachineHarmonicLoadFluxImportOptions":
        return self._Cast_ElectricMachineHarmonicLoadFluxImportOptions(self)
