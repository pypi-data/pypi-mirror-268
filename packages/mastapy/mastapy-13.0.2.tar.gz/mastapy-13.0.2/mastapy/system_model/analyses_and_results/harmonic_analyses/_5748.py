"""ElectricMachineStatorToothLoadsExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5741
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_STATOR_TOOTH_LOADS_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachineStatorToothLoadsExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5747,
        _5749,
        _5750,
        _5751,
        _5800,
        _5687,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineStatorToothLoadsExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachineStatorToothLoadsExcitationDetail")


class ElectricMachineStatorToothLoadsExcitationDetail(
    _5741.ElectricMachinePeriodicExcitationDetail
):
    """ElectricMachineStatorToothLoadsExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_STATOR_TOOTH_LOADS_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineStatorToothLoadsExcitationDetail"
    )

    class _Cast_ElectricMachineStatorToothLoadsExcitationDetail:
        """Special nested class for casting ElectricMachineStatorToothLoadsExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
            parent: "ElectricMachineStatorToothLoadsExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "_5741.ElectricMachinePeriodicExcitationDetail":
            return self._parent._cast(_5741.ElectricMachinePeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "_5800.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "_5747.ElectricMachineStatorToothAxialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5747,
            )

            return self._parent._cast(
                _5747.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "_5749.ElectricMachineStatorToothMomentsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(
                _5749.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "_5750.ElectricMachineStatorToothRadialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(
                _5750.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "_5751.ElectricMachineStatorToothTangentialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(
                _5751.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
        ) -> "ElectricMachineStatorToothLoadsExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail",
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
        instance_to_wrap: "ElectricMachineStatorToothLoadsExcitationDetail.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineStatorToothLoadsExcitationDetail._Cast_ElectricMachineStatorToothLoadsExcitationDetail":
        return self._Cast_ElectricMachineStatorToothLoadsExcitationDetail(self)
