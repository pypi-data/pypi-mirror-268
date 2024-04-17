"""NonCADElectricMachineDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines import _1268
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "NonCADElectricMachineDetail"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1306, _1282, _1296, _1310, _1312, _1327


__docformat__ = "restructuredtext en"
__all__ = ("NonCADElectricMachineDetail",)


Self = TypeVar("Self", bound="NonCADElectricMachineDetail")


class NonCADElectricMachineDetail(_1268.ElectricMachineDetail):
    """NonCADElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _NON_CAD_ELECTRIC_MACHINE_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NonCADElectricMachineDetail")

    class _Cast_NonCADElectricMachineDetail:
        """Special nested class for casting NonCADElectricMachineDetail to subclasses."""

        def __init__(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
            parent: "NonCADElectricMachineDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_detail(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1268.ElectricMachineDetail":
            return self._parent._cast(_1268.ElectricMachineDetail)

        @property
        def interior_permanent_magnet_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1282.InteriorPermanentMagnetMachine":
            from mastapy.electric_machines import _1282

            return self._parent._cast(_1282.InteriorPermanentMagnetMachine)

        @property
        def permanent_magnet_assisted_synchronous_reluctance_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1296.PermanentMagnetAssistedSynchronousReluctanceMachine":
            from mastapy.electric_machines import _1296

            return self._parent._cast(
                _1296.PermanentMagnetAssistedSynchronousReluctanceMachine
            )

        @property
        def surface_permanent_magnet_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1310.SurfacePermanentMagnetMachine":
            from mastapy.electric_machines import _1310

            return self._parent._cast(_1310.SurfacePermanentMagnetMachine)

        @property
        def synchronous_reluctance_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1312.SynchronousReluctanceMachine":
            from mastapy.electric_machines import _1312

            return self._parent._cast(_1312.SynchronousReluctanceMachine)

        @property
        def wound_field_synchronous_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1327.WoundFieldSynchronousMachine":
            from mastapy.electric_machines import _1327

            return self._parent._cast(_1327.WoundFieldSynchronousMachine)

        @property
        def non_cad_electric_machine_detail(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "NonCADElectricMachineDetail":
            return self._parent

        def __getattr__(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NonCADElectricMachineDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stator(self: Self) -> "_1306.Stator":
        """mastapy.electric_machines.Stator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail":
        return self._Cast_NonCADElectricMachineDetail(self)
