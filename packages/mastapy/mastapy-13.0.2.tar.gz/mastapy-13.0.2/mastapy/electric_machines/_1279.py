"""HarmonicLoadDataControlExcitationOptionForElectricMachineMode"""

from __future__ import annotations

from typing import TypeVar

from mastapy.electric_machines.harmonic_load_data import _1388
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CONTROL_EXCITATION_OPTION_FOR_ELECTRIC_MACHINE_MODE = (
    python_net_import(
        "SMT.MastaAPI.ElectricMachines",
        "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    )
)


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicLoadDataControlExcitationOptionForElectricMachineMode",)


Self = TypeVar(
    "Self", bound="HarmonicLoadDataControlExcitationOptionForElectricMachineMode"
)


class HarmonicLoadDataControlExcitationOptionForElectricMachineMode(
    _1388.HarmonicLoadDataControlExcitationOptionBase
):
    """HarmonicLoadDataControlExcitationOptionForElectricMachineMode

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_CONTROL_EXCITATION_OPTION_FOR_ELECTRIC_MACHINE_MODE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
    )

    class _Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode:
        """Special nested class for casting HarmonicLoadDataControlExcitationOptionForElectricMachineMode to subclasses."""

        def __init__(
            self: "HarmonicLoadDataControlExcitationOptionForElectricMachineMode._Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
            parent: "HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_control_excitation_option_base(
            self: "HarmonicLoadDataControlExcitationOptionForElectricMachineMode._Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
        ) -> "_1388.HarmonicLoadDataControlExcitationOptionBase":
            return self._parent._cast(_1388.HarmonicLoadDataControlExcitationOptionBase)

        @property
        def harmonic_load_data_control_excitation_option_for_electric_machine_mode(
            self: "HarmonicLoadDataControlExcitationOptionForElectricMachineMode._Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
        ) -> "HarmonicLoadDataControlExcitationOptionForElectricMachineMode":
            return self._parent

        def __getattr__(
            self: "HarmonicLoadDataControlExcitationOptionForElectricMachineMode._Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode",
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
        instance_to_wrap: "HarmonicLoadDataControlExcitationOptionForElectricMachineMode.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicLoadDataControlExcitationOptionForElectricMachineMode._Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode":
        return self._Cast_HarmonicLoadDataControlExcitationOptionForElectricMachineMode(
            self
        )
