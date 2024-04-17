"""CylindricalGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.gears import _2320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "CylindricalGearMesh"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1496
    from mastapy.gears.gear_designs.cylindrical import _1022
    from mastapy.system_model.part_model.gears import _2533, _2532
    from mastapy.system_model.connections_and_sockets import _2288, _2279
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMesh",)


Self = TypeVar("Self", bound="CylindricalGearMesh")


class CylindricalGearMesh(_2320.GearMesh):
    """CylindricalGearMesh

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMesh")

    class _Cast_CylindricalGearMesh:
        """Special nested class for casting CylindricalGearMesh to subclasses."""

        def __init__(
            self: "CylindricalGearMesh._Cast_CylindricalGearMesh",
            parent: "CylindricalGearMesh",
        ):
            self._parent = parent

        @property
        def gear_mesh(
            self: "CylindricalGearMesh._Cast_CylindricalGearMesh",
        ) -> "_2320.GearMesh":
            return self._parent._cast(_2320.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "CylindricalGearMesh._Cast_CylindricalGearMesh",
        ) -> "_2288.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2288

            return self._parent._cast(_2288.InterMountableComponentConnection)

        @property
        def connection(
            self: "CylindricalGearMesh._Cast_CylindricalGearMesh",
        ) -> "_2279.Connection":
            from mastapy.system_model.connections_and_sockets import _2279

            return self._parent._cast(_2279.Connection)

        @property
        def design_entity(
            self: "CylindricalGearMesh._Cast_CylindricalGearMesh",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cylindrical_gear_mesh(
            self: "CylindricalGearMesh._Cast_CylindricalGearMesh",
        ) -> "CylindricalGearMesh":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMesh._Cast_CylindricalGearMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CentreDistance

        if temp is None:
            return 0.0

        return temp

    @centre_distance.setter
    @enforce_parameter_types
    def centre_distance(self: Self, value: "float"):
        self.wrapped.CentreDistance = float(value) if value is not None else 0.0

    @property
    def centre_distance_range(self: Self) -> "_1496.Range":
        """mastapy.math_utility.Range

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreDistanceRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def centre_distance_with_normal_module_adjustment_by_scaling_entire_model(
        self: Self,
    ) -> "float":
        """float"""
        temp = self.wrapped.CentreDistanceWithNormalModuleAdjustmentByScalingEntireModel

        if temp is None:
            return 0.0

        return temp

    @centre_distance_with_normal_module_adjustment_by_scaling_entire_model.setter
    @enforce_parameter_types
    def centre_distance_with_normal_module_adjustment_by_scaling_entire_model(
        self: Self, value: "float"
    ):
        self.wrapped.CentreDistanceWithNormalModuleAdjustmentByScalingEntireModel = (
            float(value) if value is not None else 0.0
        )

    @property
    def is_centre_distance_ready_to_change(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsCentreDistanceReadyToChange

        if temp is None:
            return False

        return temp

    @property
    def override_design_pocketing_power_loss_coefficients(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.OverrideDesignPocketingPowerLossCoefficients

        if temp is None:
            return False

        return temp

    @override_design_pocketing_power_loss_coefficients.setter
    @enforce_parameter_types
    def override_design_pocketing_power_loss_coefficients(self: Self, value: "bool"):
        self.wrapped.OverrideDesignPocketingPowerLossCoefficients = (
            bool(value) if value is not None else False
        )

    @property
    def active_gear_mesh_design(self: Self) -> "_1022.CylindricalGearMeshDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_mesh_design(self: Self) -> "_1022.CylindricalGearMeshDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_set(self: Self) -> "_2533.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears(self: Self) -> "List[_2532.CylindricalGear]":
        """List[mastapy.system_model.part_model.gears.CylindricalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "CylindricalGearMesh._Cast_CylindricalGearMesh":
        return self._Cast_CylindricalGearMesh(self)
