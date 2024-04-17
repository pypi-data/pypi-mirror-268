"""ElectricMachineHarmonicLoadJMAGImportOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6889
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_JMAG_IMPORT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadJMAGImportOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadJMAGImportOptions",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadJMAGImportOptions")


class ElectricMachineHarmonicLoadJMAGImportOptions(
    _6889.ElectricMachineHarmonicLoadImportOptionsBase
):
    """ElectricMachineHarmonicLoadJMAGImportOptions

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_JMAG_IMPORT_OPTIONS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadJMAGImportOptions"
    )

    class _Cast_ElectricMachineHarmonicLoadJMAGImportOptions:
        """Special nested class for casting ElectricMachineHarmonicLoadJMAGImportOptions to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadJMAGImportOptions._Cast_ElectricMachineHarmonicLoadJMAGImportOptions",
            parent: "ElectricMachineHarmonicLoadJMAGImportOptions",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_import_options_base(
            self: "ElectricMachineHarmonicLoadJMAGImportOptions._Cast_ElectricMachineHarmonicLoadJMAGImportOptions",
        ) -> "_6889.ElectricMachineHarmonicLoadImportOptionsBase":
            return self._parent._cast(
                _6889.ElectricMachineHarmonicLoadImportOptionsBase
            )

        @property
        def electric_machine_harmonic_load_jmag_import_options(
            self: "ElectricMachineHarmonicLoadJMAGImportOptions._Cast_ElectricMachineHarmonicLoadJMAGImportOptions",
        ) -> "ElectricMachineHarmonicLoadJMAGImportOptions":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadJMAGImportOptions._Cast_ElectricMachineHarmonicLoadJMAGImportOptions",
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
        instance_to_wrap: "ElectricMachineHarmonicLoadJMAGImportOptions.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadJMAGImportOptions._Cast_ElectricMachineHarmonicLoadJMAGImportOptions":
        return self._Cast_ElectricMachineHarmonicLoadJMAGImportOptions(self)
