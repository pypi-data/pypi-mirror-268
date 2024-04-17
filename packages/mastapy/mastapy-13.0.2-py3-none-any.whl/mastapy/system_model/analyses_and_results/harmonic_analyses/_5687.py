"""AbstractPeriodicExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractPeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.electric_machines.harmonic_load_data import _1387
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5741,
        _5742,
        _5743,
        _5744,
        _5745,
        _5746,
        _5747,
        _5748,
        _5749,
        _5750,
        _5751,
        _5752,
        _5762,
        _5764,
        _5765,
        _5767,
        _5800,
        _5817,
        _5843,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractPeriodicExcitationDetail",)


Self = TypeVar("Self", bound="AbstractPeriodicExcitationDetail")


class AbstractPeriodicExcitationDetail(_0.APIBase):
    """AbstractPeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractPeriodicExcitationDetail")

    class _Cast_AbstractPeriodicExcitationDetail:
        """Special nested class for casting AbstractPeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
            parent: "AbstractPeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5741.ElectricMachinePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(_5741.ElectricMachinePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5742.ElectricMachineRotorXForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(
                _5742.ElectricMachineRotorXForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5743.ElectricMachineRotorXMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(
                _5743.ElectricMachineRotorXMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5744.ElectricMachineRotorYForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5744,
            )

            return self._parent._cast(
                _5744.ElectricMachineRotorYForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5745.ElectricMachineRotorYMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(
                _5745.ElectricMachineRotorYMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5746.ElectricMachineRotorZForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(
                _5746.ElectricMachineRotorZForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5747.ElectricMachineStatorToothAxialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5747,
            )

            return self._parent._cast(
                _5747.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5748.ElectricMachineStatorToothLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(
                _5748.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5749.ElectricMachineStatorToothMomentsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(
                _5749.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5750.ElectricMachineStatorToothRadialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5750,
            )

            return self._parent._cast(
                _5750.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5751.ElectricMachineStatorToothTangentialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(
                _5751.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5752.ElectricMachineTorqueRipplePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(
                _5752.ElectricMachineTorqueRipplePeriodicExcitationDetail
            )

        @property
        def gear_mesh_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5762.GearMeshExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5762,
            )

            return self._parent._cast(_5762.GearMeshExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5764.GearMeshMisalignmentExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5764,
            )

            return self._parent._cast(_5764.GearMeshMisalignmentExcitationDetail)

        @property
        def gear_mesh_te_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5765.GearMeshTEExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5765,
            )

            return self._parent._cast(_5765.GearMeshTEExcitationDetail)

        @property
        def general_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5767.GeneralPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(_5767.GeneralPeriodicExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5800.PeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PeriodicExcitationWithReferenceShaft)

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5817.SingleNodePeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(
                _5817.SingleNodePeriodicExcitationWithReferenceShaft
            )

        @property
        def unbalanced_mass_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "_5843.UnbalancedMassExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.UnbalancedMassExcitationDetail)

        @property
        def abstract_periodic_excitation_detail(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
        ) -> "AbstractPeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractPeriodicExcitationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def harmonic_load_data(self: Self) -> "_1387.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicLoadData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractPeriodicExcitationDetail._Cast_AbstractPeriodicExcitationDetail":
        return self._Cast_AbstractPeriodicExcitationDetail(self)
