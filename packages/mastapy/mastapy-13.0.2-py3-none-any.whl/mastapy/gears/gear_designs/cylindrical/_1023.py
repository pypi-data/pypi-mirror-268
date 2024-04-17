"""CylindricalGearMeshFlankDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_FLANK_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "CylindricalGearMeshFlankDesign"
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1874


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshFlankDesign",)


Self = TypeVar("Self", bound="CylindricalGearMeshFlankDesign")


class CylindricalGearMeshFlankDesign(_0.APIBase):
    """CylindricalGearMeshFlankDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_FLANK_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshFlankDesign")

    class _Cast_CylindricalGearMeshFlankDesign:
        """Special nested class for casting CylindricalGearMeshFlankDesign to subclasses."""

        def __init__(
            self: "CylindricalGearMeshFlankDesign._Cast_CylindricalGearMeshFlankDesign",
            parent: "CylindricalGearMeshFlankDesign",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_mesh_flank_design(
            self: "CylindricalGearMeshFlankDesign._Cast_CylindricalGearMeshFlankDesign",
        ) -> "CylindricalGearMeshFlankDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshFlankDesign._Cast_CylindricalGearMeshFlankDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMeshFlankDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_tooth_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DegreeOfToothLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankName

        if temp is None:
            return ""

        return temp

    @property
    def length_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LengthOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def specific_sliding_chart(self: Self) -> "_1874.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpecificSlidingChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sum_of_base_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SumOfBaseRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def tooth_loss_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothLossFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def total_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def working_normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def working_transverse_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WorkingTransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshFlankDesign._Cast_CylindricalGearMeshFlankDesign":
        return self._Cast_CylindricalGearMeshFlankDesign(self)
