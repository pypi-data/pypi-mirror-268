"""ElectricMachineMeshingOptionsBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.nodal_analysis import _61
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_MESHING_OPTIONS_BASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "ElectricMachineMeshingOptionsBase"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1270, _1271


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineMeshingOptionsBase",)


Self = TypeVar("Self", bound="ElectricMachineMeshingOptionsBase")


class ElectricMachineMeshingOptionsBase(_61.FEMeshingOptions):
    """ElectricMachineMeshingOptionsBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_MESHING_OPTIONS_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineMeshingOptionsBase")

    class _Cast_ElectricMachineMeshingOptionsBase:
        """Special nested class for casting ElectricMachineMeshingOptionsBase to subclasses."""

        def __init__(
            self: "ElectricMachineMeshingOptionsBase._Cast_ElectricMachineMeshingOptionsBase",
            parent: "ElectricMachineMeshingOptionsBase",
        ):
            self._parent = parent

        @property
        def fe_meshing_options(
            self: "ElectricMachineMeshingOptionsBase._Cast_ElectricMachineMeshingOptionsBase",
        ) -> "_61.FEMeshingOptions":
            return self._parent._cast(_61.FEMeshingOptions)

        @property
        def electric_machine_mechanical_analysis_meshing_options(
            self: "ElectricMachineMeshingOptionsBase._Cast_ElectricMachineMeshingOptionsBase",
        ) -> "_1270.ElectricMachineMechanicalAnalysisMeshingOptions":
            from mastapy.electric_machines import _1270

            return self._parent._cast(
                _1270.ElectricMachineMechanicalAnalysisMeshingOptions
            )

        @property
        def electric_machine_meshing_options(
            self: "ElectricMachineMeshingOptionsBase._Cast_ElectricMachineMeshingOptionsBase",
        ) -> "_1271.ElectricMachineMeshingOptions":
            from mastapy.electric_machines import _1271

            return self._parent._cast(_1271.ElectricMachineMeshingOptions)

        @property
        def electric_machine_meshing_options_base(
            self: "ElectricMachineMeshingOptionsBase._Cast_ElectricMachineMeshingOptionsBase",
        ) -> "ElectricMachineMeshingOptionsBase":
            return self._parent

        def __getattr__(
            self: "ElectricMachineMeshingOptionsBase._Cast_ElectricMachineMeshingOptionsBase",
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
        self: Self, instance_to_wrap: "ElectricMachineMeshingOptionsBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def autogenerate_mesh(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.AutogenerateMesh

        if temp is None:
            return False

        return temp

    @autogenerate_mesh.setter
    @enforce_parameter_types
    def autogenerate_mesh(self: Self, value: "bool"):
        self.wrapped.AutogenerateMesh = bool(value) if value is not None else False

    @property
    def p_element_order(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PElementOrder

        if temp is None:
            return 0

        return temp

    @p_element_order.setter
    @enforce_parameter_types
    def p_element_order(self: Self, value: "int"):
        self.wrapped.PElementOrder = int(value) if value is not None else 0

    @property
    def use_p_elements(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UsePElements

        if temp is None:
            return False

        return temp

    @use_p_elements.setter
    @enforce_parameter_types
    def use_p_elements(self: Self, value: "bool"):
        self.wrapped.UsePElements = bool(value) if value is not None else False

    @property
    def utilise_periodicity_when_meshing_geometry(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UtilisePeriodicityWhenMeshingGeometry

        if temp is None:
            return False

        return temp

    @utilise_periodicity_when_meshing_geometry.setter
    @enforce_parameter_types
    def utilise_periodicity_when_meshing_geometry(self: Self, value: "bool"):
        self.wrapped.UtilisePeriodicityWhenMeshingGeometry = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineMeshingOptionsBase._Cast_ElectricMachineMeshingOptionsBase":
        return self._Cast_ElectricMachineMeshingOptionsBase(self)
