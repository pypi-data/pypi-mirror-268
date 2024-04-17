"""ElectricMachineRotorXForcePeriodicExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_ROTOR_X_FORCE_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineRotorXForcePeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800, _5687


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineRotorXForcePeriodicExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineRotorXForcePeriodicExcitationDetail")


class ElectricMachineRotorXForcePeriodicExcitationDetail(
    _5741.ElectricMachinePeriodicExcitationDetail
):
    """ElectricMachineRotorXForcePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_ROTOR_X_FORCE_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineRotorXForcePeriodicExcitationDetail"
    )

    class _Cast_ElectricMachineRotorXForcePeriodicExcitationDetail:
        """Special nested class for casting ElectricMachineRotorXForcePeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineRotorXForcePeriodicExcitationDetail._Cast_ElectricMachineRotorXForcePeriodicExcitationDetail",
            parent: "ElectricMachineRotorXForcePeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineRotorXForcePeriodicExcitationDetail._Cast_ElectricMachineRotorXForcePeriodicExcitationDetail",
        ) -> "_5741.ElectricMachinePeriodicExcitationDetail":
            return self._parent._cast(_5741.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineRotorXForcePeriodicExcitationDetail._Cast_ElectricMachineRotorXForcePeriodicExcitationDetail",
        ) -> "_5800.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineRotorXForcePeriodicExcitationDetail._Cast_ElectricMachineRotorXForcePeriodicExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "ElectricMachineRotorXForcePeriodicExcitationDetail._Cast_ElectricMachineRotorXForcePeriodicExcitationDetail",
        ) -> "ElectricMachineRotorXForcePeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineRotorXForcePeriodicExcitationDetail._Cast_ElectricMachineRotorXForcePeriodicExcitationDetail",
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
        instance_to_wrap: "ElectricMachineRotorXForcePeriodicExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineRotorXForcePeriodicExcitationDetail._Cast_ElectricMachineRotorXForcePeriodicExcitationDetail":
        return self._Cast_ElectricMachineRotorXForcePeriodicExcitationDetail(self)
