"""BoostPressureLoadCaseInputOptions"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model.gears import _2533
from mastapy._internal import constructor
from mastapy.utility_gui import _1854
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOOST_PRESSURE_LOAD_CASE_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition",
    "BoostPressureLoadCaseInputOptions",
)


__docformat__ = "restructuredtext en"
__all__ = ("BoostPressureLoadCaseInputOptions",)


Self = TypeVar("Self", bound="BoostPressureLoadCaseInputOptions")


class BoostPressureLoadCaseInputOptions(_1854.ColumnInputOptions):
    """BoostPressureLoadCaseInputOptions

    This is a mastapy class.
    """

    TYPE = _BOOST_PRESSURE_LOAD_CASE_INPUT_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoostPressureLoadCaseInputOptions")

    class _Cast_BoostPressureLoadCaseInputOptions:
        """Special nested class for casting BoostPressureLoadCaseInputOptions to subclasses."""

        def __init__(
            self: "BoostPressureLoadCaseInputOptions._Cast_BoostPressureLoadCaseInputOptions",
            parent: "BoostPressureLoadCaseInputOptions",
        ):
            self._parent = parent

        @property
        def column_input_options(
            self: "BoostPressureLoadCaseInputOptions._Cast_BoostPressureLoadCaseInputOptions",
        ) -> "_1854.ColumnInputOptions":
            return self._parent._cast(_1854.ColumnInputOptions)

        @property
        def boost_pressure_load_case_input_options(
            self: "BoostPressureLoadCaseInputOptions._Cast_BoostPressureLoadCaseInputOptions",
        ) -> "BoostPressureLoadCaseInputOptions":
            return self._parent

        def __getattr__(
            self: "BoostPressureLoadCaseInputOptions._Cast_BoostPressureLoadCaseInputOptions",
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
        self: Self, instance_to_wrap: "BoostPressureLoadCaseInputOptions.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotor_set(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_CylindricalGearSet":
        """ListWithSelectedItem[mastapy.system_model.part_model.gears.CylindricalGearSet]"""
        temp = self.wrapped.RotorSet

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_CylindricalGearSet",
        )(temp)

    @rotor_set.setter
    @enforce_parameter_types
    def rotor_set(self: Self, value: "_2533.CylindricalGearSet"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_CylindricalGearSet.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.RotorSet = value

    @property
    def cast_to(
        self: Self,
    ) -> "BoostPressureLoadCaseInputOptions._Cast_BoostPressureLoadCaseInputOptions":
        return self._Cast_BoostPressureLoadCaseInputOptions(self)
