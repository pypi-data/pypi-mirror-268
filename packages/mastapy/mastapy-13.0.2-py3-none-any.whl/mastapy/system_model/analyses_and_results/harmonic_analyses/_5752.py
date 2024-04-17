"""ElectricMachineTorqueRipplePeriodicExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_TORQUE_RIPPLE_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineTorqueRipplePeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5800, _5687


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineTorqueRipplePeriodicExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineTorqueRipplePeriodicExcitationDetail")


class ElectricMachineTorqueRipplePeriodicExcitationDetail(
    _5741.ElectricMachinePeriodicExcitationDetail
):
    """ElectricMachineTorqueRipplePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_TORQUE_RIPPLE_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail"
    )

    class _Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail:
        """Special nested class for casting ElectricMachineTorqueRipplePeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineTorqueRipplePeriodicExcitationDetail._Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail",
            parent: "ElectricMachineTorqueRipplePeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineTorqueRipplePeriodicExcitationDetail._Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail",
        ) -> "_5741.ElectricMachinePeriodicExcitationDetail":
            return self._parent._cast(_5741.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineTorqueRipplePeriodicExcitationDetail._Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail",
        ) -> "_5800.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineTorqueRipplePeriodicExcitationDetail._Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "ElectricMachineTorqueRipplePeriodicExcitationDetail._Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail",
        ) -> "ElectricMachineTorqueRipplePeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineTorqueRipplePeriodicExcitationDetail._Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail",
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
        instance_to_wrap: "ElectricMachineTorqueRipplePeriodicExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineTorqueRipplePeriodicExcitationDetail._Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail":
        return self._Cast_ElectricMachineTorqueRipplePeriodicExcitationDetail(self)
