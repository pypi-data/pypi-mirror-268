"""ElectricMachineHarmonicLoadImportOptionsBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_IMPORT_OPTIONS_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadImportOptionsBase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6887,
        _6888,
        _6890,
        _6891,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadImportOptionsBase",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadImportOptionsBase")


class ElectricMachineHarmonicLoadImportOptionsBase(_0.APIBase):
    """ElectricMachineHarmonicLoadImportOptionsBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_IMPORT_OPTIONS_BASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadImportOptionsBase"
    )

    class _Cast_ElectricMachineHarmonicLoadImportOptionsBase:
        """Special nested class for casting ElectricMachineHarmonicLoadImportOptionsBase to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase",
            parent: "ElectricMachineHarmonicLoadImportOptionsBase",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_excel_import_options(
            self: "ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase",
        ) -> "_6887.ElectricMachineHarmonicLoadExcelImportOptions":
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(
                _6887.ElectricMachineHarmonicLoadExcelImportOptions
            )

        @property
        def electric_machine_harmonic_load_flux_import_options(
            self: "ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase",
        ) -> "_6888.ElectricMachineHarmonicLoadFluxImportOptions":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(
                _6888.ElectricMachineHarmonicLoadFluxImportOptions
            )

        @property
        def electric_machine_harmonic_load_jmag_import_options(
            self: "ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase",
        ) -> "_6890.ElectricMachineHarmonicLoadJMAGImportOptions":
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(
                _6890.ElectricMachineHarmonicLoadJMAGImportOptions
            )

        @property
        def electric_machine_harmonic_load_motor_cad_import_options(
            self: "ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase",
        ) -> "_6891.ElectricMachineHarmonicLoadMotorCADImportOptions":
            from mastapy.system_model.analyses_and_results.static_loads import _6891

            return self._parent._cast(
                _6891.ElectricMachineHarmonicLoadMotorCADImportOptions
            )

        @property
        def electric_machine_harmonic_load_import_options_base(
            self: "ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase",
        ) -> "ElectricMachineHarmonicLoadImportOptionsBase":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase",
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
        instance_to_wrap: "ElectricMachineHarmonicLoadImportOptionsBase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadImportOptionsBase._Cast_ElectricMachineHarmonicLoadImportOptionsBase":
        return self._Cast_ElectricMachineHarmonicLoadImportOptionsBase(self)
