"""ElectricMachineHarmonicLoadDataFromMotorPackages"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy.system_model.analyses_and_results.static_loads import _6880
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_PACKAGES = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadDataFromMotorPackages",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6889,
        _6882,
        _6883,
        _6885,
    )
    from mastapy.electric_machines.harmonic_load_data import _1385, _1390, _1387


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataFromMotorPackages",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataFromMotorPackages")
T = TypeVar("T", bound="_6889.ElectricMachineHarmonicLoadImportOptionsBase")


class ElectricMachineHarmonicLoadDataFromMotorPackages(
    _6880.ElectricMachineHarmonicLoadData, Generic[T]
):
    """ElectricMachineHarmonicLoadDataFromMotorPackages

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_PACKAGES
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadDataFromMotorPackages"
    )

    class _Cast_ElectricMachineHarmonicLoadDataFromMotorPackages:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromMotorPackages to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
            parent: "ElectricMachineHarmonicLoadDataFromMotorPackages",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
        ) -> "_6880.ElectricMachineHarmonicLoadData":
            return self._parent._cast(_6880.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
        ) -> "_1385.ElectricMachineHarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1385

            return self._parent._cast(_1385.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
        ) -> "_1390.SpeedDependentHarmonicLoadData":
            from mastapy.electric_machines.harmonic_load_data import _1390

            return self._parent._cast(_1390.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
        ) -> "_1387.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1387

            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_flux(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
        ) -> "_6882.ElectricMachineHarmonicLoadDataFromFlux":
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.ElectricMachineHarmonicLoadDataFromFlux)

        @property
        def electric_machine_harmonic_load_data_from_jmag(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
        ) -> "_6883.ElectricMachineHarmonicLoadDataFromJMAG":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.ElectricMachineHarmonicLoadDataFromJMAG)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
        ) -> "_6885.ElectricMachineHarmonicLoadDataFromMotorCAD":
            from mastapy.system_model.analyses_and_results.static_loads import _6885

            return self._parent._cast(_6885.ElectricMachineHarmonicLoadDataFromMotorCAD)

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
        ) -> "ElectricMachineHarmonicLoadDataFromMotorPackages":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages",
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
        instance_to_wrap: "ElectricMachineHarmonicLoadDataFromMotorPackages.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadDataFromMotorPackages._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages":
        return self._Cast_ElectricMachineHarmonicLoadDataFromMotorPackages(self)
