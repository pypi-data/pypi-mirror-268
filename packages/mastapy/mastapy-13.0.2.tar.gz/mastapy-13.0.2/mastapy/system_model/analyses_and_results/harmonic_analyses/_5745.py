"""ElectricMachineRotorYMomentPeriodicExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ROTOR_Y_MOMENT_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineRotorYMomentPeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800, _5687


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineRotorYMomentPeriodicExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineRotorYMomentPeriodicExcitationDetail")


class ElectricMachineRotorYMomentPeriodicExcitationDetail(
    _5741.ElectricMachinePeriodicExcitationDetail
):
    """ElectricMachineRotorYMomentPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ROTOR_Y_MOMENT_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail"
    )

    class _Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail:
        """Special nested class for casting ElectricMachineRotorYMomentPeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineRotorYMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail",
            parent: "ElectricMachineRotorYMomentPeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineRotorYMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail",
        ) -> "_5741.ElectricMachinePeriodicExcitationDetail":
            return self._parent._cast(_5741.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineRotorYMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail",
        ) -> "_5800.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineRotorYMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "ElectricMachineRotorYMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail",
        ) -> "ElectricMachineRotorYMomentPeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineRotorYMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail",
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
        instance_to_wrap: "ElectricMachineRotorYMomentPeriodicExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineRotorYMomentPeriodicExcitationDetail._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail":
        return self._Cast_ElectricMachineRotorYMomentPeriodicExcitationDetail(self)
