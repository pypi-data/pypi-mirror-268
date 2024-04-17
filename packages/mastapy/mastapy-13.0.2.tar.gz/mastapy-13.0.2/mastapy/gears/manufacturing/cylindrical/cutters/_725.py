"""RoughCutterCreationSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROUGH_CUTTER_CREATION_SETTINGS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "RoughCutterCreationSettings",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1088
    from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _744


__docformat__ = "restructuredtext en"
__all__ = ("RoughCutterCreationSettings",)


Self = TypeVar("Self", bound="RoughCutterCreationSettings")


class RoughCutterCreationSettings(_0.APIBase):
    """RoughCutterCreationSettings

    This is a mastapy class.
    """

    TYPE = _ROUGH_CUTTER_CREATION_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RoughCutterCreationSettings")

    class _Cast_RoughCutterCreationSettings:
        """Special nested class for casting RoughCutterCreationSettings to subclasses."""

        def __init__(
            self: "RoughCutterCreationSettings._Cast_RoughCutterCreationSettings",
            parent: "RoughCutterCreationSettings",
        ):
            self._parent = parent

        @property
        def rough_cutter_creation_settings(
            self: "RoughCutterCreationSettings._Cast_RoughCutterCreationSettings",
        ) -> "RoughCutterCreationSettings":
            return self._parent

        def __getattr__(
            self: "RoughCutterCreationSettings._Cast_RoughCutterCreationSettings",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RoughCutterCreationSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_thickness_used_to_generate_cutter(
        self: Self,
    ) -> "_1088.TolerancedMetalMeasurements":
        """mastapy.gears.gear_designs.cylindrical.TolerancedMetalMeasurements"""
        temp = self.wrapped.FinishThicknessUsedToGenerateCutter

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TolerancedMetalMeasurements",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1088",
            "TolerancedMetalMeasurements",
        )(value)

    @finish_thickness_used_to_generate_cutter.setter
    @enforce_parameter_types
    def finish_thickness_used_to_generate_cutter(
        self: Self, value: "_1088.TolerancedMetalMeasurements"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TolerancedMetalMeasurements",
        )
        self.wrapped.FinishThicknessUsedToGenerateCutter = value

    @property
    def rough_thickness_used_to_generate_cutter(
        self: Self,
    ) -> "_1088.TolerancedMetalMeasurements":
        """mastapy.gears.gear_designs.cylindrical.TolerancedMetalMeasurements"""
        temp = self.wrapped.RoughThicknessUsedToGenerateCutter

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TolerancedMetalMeasurements",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.cylindrical._1088",
            "TolerancedMetalMeasurements",
        )(value)

    @rough_thickness_used_to_generate_cutter.setter
    @enforce_parameter_types
    def rough_thickness_used_to_generate_cutter(
        self: Self, value: "_1088.TolerancedMetalMeasurements"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.GearDesigns.Cylindrical.TolerancedMetalMeasurements",
        )
        self.wrapped.RoughThicknessUsedToGenerateCutter = value

    @property
    def finish_tool_clearances(self: Self) -> "_744.ManufacturingOperationConstraints":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.ManufacturingOperationConstraints

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FinishToolClearances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rough_tool_clearances(self: Self) -> "_744.ManufacturingOperationConstraints":
        """mastapy.gears.manufacturing.cylindrical.cutter_simulation.ManufacturingOperationConstraints

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RoughToolClearances

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RoughCutterCreationSettings._Cast_RoughCutterCreationSettings":
        return self._Cast_RoughCutterCreationSettings(self)
