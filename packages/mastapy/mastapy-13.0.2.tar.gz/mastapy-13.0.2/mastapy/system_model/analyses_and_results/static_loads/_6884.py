"""ElectricMachineHarmonicLoadDataFromMASTA"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6880
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MASTA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadDataFromMASTA",
)

if TYPE_CHECKING:
    from mastapy.electric_machines.harmonic_load_data import _1385, _1390, _1387


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataFromMASTA",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataFromMASTA")


class ElectricMachineHarmonicLoadDataFromMASTA(_6880.ElectricMachineHarmonicLoadData):
    """ElectricMachineHarmonicLoadDataFromMASTA

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MASTA
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadDataFromMASTA"
    )

    class _Cast_ElectricMachineHarmonicLoadDataFromMASTA:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromMASTA to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA",
            parent: "ElectricMachineHarmonicLoadDataFromMASTA",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA",
        ) -> "_6880.ElectricMachineHarmonicLoadData":
            return self._parent._cast(_6880.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA",
        ) -> "_1385.ElectricMachineHarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1385

            return self._parent._cast(_1385.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA",
        ) -> "_1390.SpeedDependentHarmonicLoadData":
            from mastapy.electric_machines.harmonic_load_data import _1390

            return self._parent._cast(_1390.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA",
        ) -> "_1387.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1387

            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_masta(
            self: "ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA",
        ) -> "ElectricMachineHarmonicLoadDataFromMASTA":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA",
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
        self: Self, instance_to_wrap: "ElectricMachineHarmonicLoadDataFromMASTA.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadDataFromMASTA._Cast_ElectricMachineHarmonicLoadDataFromMASTA":
        return self._Cast_ElectricMachineHarmonicLoadDataFromMASTA(self)
