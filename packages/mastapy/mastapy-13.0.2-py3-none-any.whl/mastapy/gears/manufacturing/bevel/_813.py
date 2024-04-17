"""PinionRoughMachineSetting"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PINION_ROUGH_MACHINE_SETTING = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "PinionRoughMachineSetting"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1162
    from mastapy.gears.manufacturing.bevel import _791


__docformat__ = "restructuredtext en"
__all__ = ("PinionRoughMachineSetting",)


Self = TypeVar("Self", bound="PinionRoughMachineSetting")


class PinionRoughMachineSetting(_0.APIBase):
    """PinionRoughMachineSetting

    This is a mastapy class.
    """

    TYPE = _PINION_ROUGH_MACHINE_SETTING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PinionRoughMachineSetting")

    class _Cast_PinionRoughMachineSetting:
        """Special nested class for casting PinionRoughMachineSetting to subclasses."""

        def __init__(
            self: "PinionRoughMachineSetting._Cast_PinionRoughMachineSetting",
            parent: "PinionRoughMachineSetting",
        ):
            self._parent = parent

        @property
        def pinion_rough_machine_setting(
            self: "PinionRoughMachineSetting._Cast_PinionRoughMachineSetting",
        ) -> "PinionRoughMachineSetting":
            return self._parent

        def __getattr__(
            self: "PinionRoughMachineSetting._Cast_PinionRoughMachineSetting", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PinionRoughMachineSetting.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_increment_in_machine_centre_to_back(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteIncrementInMachineCentreToBack

        if temp is None:
            return 0.0

        return temp

    @property
    def blank_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BlankOffset

        if temp is None:
            return 0.0

        return temp

    @blank_offset.setter
    @enforce_parameter_types
    def blank_offset(self: Self, value: "float"):
        self.wrapped.BlankOffset = float(value) if value is not None else 0.0

    @property
    def cone_distance_of_reference_point(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ConeDistanceOfReferencePoint

        if temp is None:
            return 0.0

        return temp

    @cone_distance_of_reference_point.setter
    @enforce_parameter_types
    def cone_distance_of_reference_point(self: Self, value: "float"):
        self.wrapped.ConeDistanceOfReferencePoint = (
            float(value) if value is not None else 0.0
        )

    @property
    def height_of_reference_point(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HeightOfReferencePoint

        if temp is None:
            return 0.0

        return temp

    @height_of_reference_point.setter
    @enforce_parameter_types
    def height_of_reference_point(self: Self, value: "float"):
        self.wrapped.HeightOfReferencePoint = float(value) if value is not None else 0.0

    @property
    def increment_of_pinion_workpiece_mounting_distance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.IncrementOfPinionWorkpieceMountingDistance

        if temp is None:
            return 0.0

        return temp

    @increment_of_pinion_workpiece_mounting_distance.setter
    @enforce_parameter_types
    def increment_of_pinion_workpiece_mounting_distance(self: Self, value: "float"):
        self.wrapped.IncrementOfPinionWorkpieceMountingDistance = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_allowed_finish_stock(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumAllowedFinishStock

        if temp is None:
            return 0.0

        return temp

    @minimum_allowed_finish_stock.setter
    @enforce_parameter_types
    def minimum_allowed_finish_stock(self: Self, value: "float"):
        self.wrapped.MinimumAllowedFinishStock = (
            float(value) if value is not None else 0.0
        )

    @property
    def spiral_angle_at_reference_point(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpiralAngleAtReferencePoint

        if temp is None:
            return 0.0

        return temp

    @spiral_angle_at_reference_point.setter
    @enforce_parameter_types
    def spiral_angle_at_reference_point(self: Self, value: "float"):
        self.wrapped.SpiralAngleAtReferencePoint = (
            float(value) if value is not None else 0.0
        )

    @property
    def gear_set(self: Self) -> "_1162.ConicalGearSetDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_config(self: Self) -> "_791.ConicalPinionManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalPinionManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PinionRoughMachineSetting._Cast_PinionRoughMachineSetting":
        return self._Cast_PinionRoughMachineSetting(self)
