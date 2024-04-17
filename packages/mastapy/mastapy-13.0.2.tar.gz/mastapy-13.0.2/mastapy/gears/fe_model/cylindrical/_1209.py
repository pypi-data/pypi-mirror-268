"""CylindricalGearSetFEModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.fe_model import _1206
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_FE_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Cylindrical", "CylindricalGearSetFEModel"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1035
    from mastapy.gears.analysis import _1237, _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetFEModel",)


Self = TypeVar("Self", bound="CylindricalGearSetFEModel")


class CylindricalGearSetFEModel(_1206.GearSetFEModel):
    """CylindricalGearSetFEModel

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetFEModel")

    class _Cast_CylindricalGearSetFEModel:
        """Special nested class for casting CylindricalGearSetFEModel to subclasses."""

        def __init__(
            self: "CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel",
            parent: "CylindricalGearSetFEModel",
        ):
            self._parent = parent

        @property
        def gear_set_fe_model(
            self: "CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel",
        ) -> "_1206.GearSetFEModel":
            return self._parent._cast(_1206.GearSetFEModel)

        @property
        def gear_set_implementation_detail(
            self: "CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel",
        ) -> "_1237.GearSetImplementationDetail":
            from mastapy.gears.analysis import _1237

            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_fe_model(
            self: "CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel",
        ) -> "CylindricalGearSetFEModel":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearSetFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_coupled_teeth_either_side(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfCoupledTeethEitherSide

        if temp is None:
            return 0

        return temp

    @number_of_coupled_teeth_either_side.setter
    @enforce_parameter_types
    def number_of_coupled_teeth_either_side(self: Self, value: "int"):
        self.wrapped.NumberOfCoupledTeethEitherSide = (
            int(value) if value is not None else 0
        )

    @property
    def remove_local_compressive_stress_due_to_applied_point_load_from_root_stress(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = (
            self.wrapped.RemoveLocalCompressiveStressDueToAppliedPointLoadFromRootStress
        )

        if temp is None:
            return False

        return temp

    @remove_local_compressive_stress_due_to_applied_point_load_from_root_stress.setter
    @enforce_parameter_types
    def remove_local_compressive_stress_due_to_applied_point_load_from_root_stress(
        self: Self, value: "bool"
    ):
        self.wrapped.RemoveLocalCompressiveStressDueToAppliedPointLoadFromRootStress = (
            bool(value) if value is not None else False
        )

    @property
    def use_manufactured_profile_shape(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseManufacturedProfileShape

        if temp is None:
            return False

        return temp

    @use_manufactured_profile_shape.setter
    @enforce_parameter_types
    def use_manufactured_profile_shape(self: Self, value: "bool"):
        self.wrapped.UseManufacturedProfileShape = (
            bool(value) if value is not None else False
        )

    @property
    def manufacturing_configuration_selection(
        self: Self,
    ) -> "_1035.CylindricalGearSetManufacturingConfigurationSelection":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetManufacturingConfigurationSelection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManufacturingConfigurationSelection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetFEModel._Cast_CylindricalGearSetFEModel":
        return self._Cast_CylindricalGearSetFEModel(self)
