"""GearSetHarmonicLoadData"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.electric_machines.harmonic_load_data import _1387
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearSetHarmonicLoadData"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6902,
        _6856,
        _6873,
    )
    from mastapy.math_utility import _1520


__docformat__ = "restructuredtext en"
__all__ = ("GearSetHarmonicLoadData",)


Self = TypeVar("Self", bound="GearSetHarmonicLoadData")


class GearSetHarmonicLoadData(_1387.HarmonicLoadDataBase):
    """GearSetHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_HARMONIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetHarmonicLoadData")

    class _Cast_GearSetHarmonicLoadData:
        """Special nested class for casting GearSetHarmonicLoadData to subclasses."""

        def __init__(
            self: "GearSetHarmonicLoadData._Cast_GearSetHarmonicLoadData",
            parent: "GearSetHarmonicLoadData",
        ):
            self._parent = parent

        @property
        def harmonic_load_data_base(
            self: "GearSetHarmonicLoadData._Cast_GearSetHarmonicLoadData",
        ) -> "_1387.HarmonicLoadDataBase":
            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def conical_gear_set_harmonic_load_data(
            self: "GearSetHarmonicLoadData._Cast_GearSetHarmonicLoadData",
        ) -> "_6856.ConicalGearSetHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.ConicalGearSetHarmonicLoadData)

        @property
        def cylindrical_gear_set_harmonic_load_data(
            self: "GearSetHarmonicLoadData._Cast_GearSetHarmonicLoadData",
        ) -> "_6873.CylindricalGearSetHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.CylindricalGearSetHarmonicLoadData)

        @property
        def gear_set_harmonic_load_data(
            self: "GearSetHarmonicLoadData._Cast_GearSetHarmonicLoadData",
        ) -> "GearSetHarmonicLoadData":
            return self._parent

        def __getattr__(
            self: "GearSetHarmonicLoadData._Cast_GearSetHarmonicLoadData", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetHarmonicLoadData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_order_as_rotational_order_of_shaft(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ExcitationOrderAsRotationalOrderOfShaft

        if temp is None:
            return 0.0

        return temp

    @excitation_order_as_rotational_order_of_shaft.setter
    @enforce_parameter_types
    def excitation_order_as_rotational_order_of_shaft(self: Self, value: "float"):
        self.wrapped.ExcitationOrderAsRotationalOrderOfShaft = (
            float(value) if value is not None else 0.0
        )

    @property
    def gear_mesh_te_order_type(self: Self) -> "_6902.GearMeshTEOrderType":
        """mastapy.system_model.analyses_and_results.static_loads.GearMeshTEOrderType"""
        temp = self.wrapped.GearMeshTEOrderType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.GearMeshTEOrderType",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.static_loads._6902",
            "GearMeshTEOrderType",
        )(value)

    @gear_mesh_te_order_type.setter
    @enforce_parameter_types
    def gear_mesh_te_order_type(self: Self, value: "_6902.GearMeshTEOrderType"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.GearMeshTEOrderType",
        )
        self.wrapped.GearMeshTEOrderType = value

    @property
    def reference_shaft(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.ReferenceShaft

        if temp is None:
            return ""

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @reference_shaft.setter
    @enforce_parameter_types
    def reference_shaft(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.ReferenceShaft = value

    @property
    def excitations(self: Self) -> "List[_1520.FourierSeries]":
        """List[mastapy.math_utility.FourierSeries]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Excitations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def copy_data_to_duplicate_planetary_meshes(self: Self):
        """Method does not return."""
        self.wrapped.CopyDataToDuplicatePlanetaryMeshes()

    @property
    def cast_to(self: Self) -> "GearSetHarmonicLoadData._Cast_GearSetHarmonicLoadData":
        return self._Cast_GearSetHarmonicLoadData(self)
