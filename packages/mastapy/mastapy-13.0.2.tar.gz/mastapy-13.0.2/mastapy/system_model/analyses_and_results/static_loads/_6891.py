"""ElectricMachineHarmonicLoadMotorCADImportOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6889
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_MOTOR_CAD_IMPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadMotorCADImportOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadMotorCADImportOptions",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadMotorCADImportOptions")


class ElectricMachineHarmonicLoadMotorCADImportOptions(
    _6889.ElectricMachineHarmonicLoadImportOptionsBase
):
    """ElectricMachineHarmonicLoadMotorCADImportOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_MOTOR_CAD_IMPORT_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadMotorCADImportOptions"
    )

    class _Cast_ElectricMachineHarmonicLoadMotorCADImportOptions:
        """Special nested class for casting ElectricMachineHarmonicLoadMotorCADImportOptions to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadMotorCADImportOptions._Cast_ElectricMachineHarmonicLoadMotorCADImportOptions",
            parent: "ElectricMachineHarmonicLoadMotorCADImportOptions",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_import_options_base(
            self: "ElectricMachineHarmonicLoadMotorCADImportOptions._Cast_ElectricMachineHarmonicLoadMotorCADImportOptions",
        ) -> "_6889.ElectricMachineHarmonicLoadImportOptionsBase":
            return self._parent._cast(
                _6889.ElectricMachineHarmonicLoadImportOptionsBase
            )

        @property
        def electric_machine_harmonic_load_motor_cad_import_options(
            self: "ElectricMachineHarmonicLoadMotorCADImportOptions._Cast_ElectricMachineHarmonicLoadMotorCADImportOptions",
        ) -> "ElectricMachineHarmonicLoadMotorCADImportOptions":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadMotorCADImportOptions._Cast_ElectricMachineHarmonicLoadMotorCADImportOptions",
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
        instance_to_wrap: "ElectricMachineHarmonicLoadMotorCADImportOptions.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadMotorCADImportOptions._Cast_ElectricMachineHarmonicLoadMotorCADImportOptions":
        return self._Cast_ElectricMachineHarmonicLoadMotorCADImportOptions(self)
