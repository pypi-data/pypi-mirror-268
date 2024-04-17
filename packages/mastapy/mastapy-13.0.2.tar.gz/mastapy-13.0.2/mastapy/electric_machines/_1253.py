"""CADElectricMachineDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines import _1268
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "CADElectricMachineDetail"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.geometry_modeller_link import _160
    from mastapy.electric_machines import _1256, _1257


__docformat__ = "restructuredtext en"
__all__ = ("CADElectricMachineDetail",)


Self = TypeVar("Self", bound="CADElectricMachineDetail")


class CADElectricMachineDetail(_1268.ElectricMachineDetail):
    """CADElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _CAD_ELECTRIC_MACHINE_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CADElectricMachineDetail")

    class _Cast_CADElectricMachineDetail:
        """Special nested class for casting CADElectricMachineDetail to subclasses."""

        def __init__(
            self: "CADElectricMachineDetail._Cast_CADElectricMachineDetail",
            parent: "CADElectricMachineDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_detail(
            self: "CADElectricMachineDetail._Cast_CADElectricMachineDetail",
        ) -> "_1268.ElectricMachineDetail":
            return self._parent._cast(_1268.ElectricMachineDetail)

        @property
        def cad_electric_machine_detail(
            self: "CADElectricMachineDetail._Cast_CADElectricMachineDetail",
        ) -> "CADElectricMachineDetail":
            return self._parent

        def __getattr__(
            self: "CADElectricMachineDetail._Cast_CADElectricMachineDetail", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CADElectricMachineDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def geometry_modeller_dimensions(self: Self) -> "_160.GeometryModellerDimensions":
        """mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimensions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryModellerDimensions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rotor(self: Self) -> "_1256.CADRotor":
        """mastapy.electric_machines.CADRotor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rotor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stator(self: Self) -> "_1257.CADStator":
        """mastapy.electric_machines.CADStator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def embed_geometry_modeller_file(self: Self):
        """Method does not return."""
        self.wrapped.EmbedGeometryModellerFile()

    def open_embedded_geometry_modeller_file(self: Self):
        """Method does not return."""
        self.wrapped.OpenEmbeddedGeometryModellerFile()

    def reread_geometry_from_geometry_modeller(self: Self):
        """Method does not return."""
        self.wrapped.RereadGeometryFromGeometryModeller()

    @property
    def cast_to(
        self: Self,
    ) -> "CADElectricMachineDetail._Cast_CADElectricMachineDetail":
        return self._Cast_CADElectricMachineDetail(self)
