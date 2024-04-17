"""UnbalancedMassHarmonicLoadData"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1511
from mastapy._internal import enum_with_selected_value_runtime, conversion
from mastapy.electric_machines.harmonic_load_data import _1390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "UnbalancedMassHarmonicLoadData",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1520
    from mastapy.electric_machines.harmonic_load_data import _1387


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassHarmonicLoadData",)


Self = TypeVar("Self", bound="UnbalancedMassHarmonicLoadData")


class UnbalancedMassHarmonicLoadData(_1390.SpeedDependentHarmonicLoadData):
    """UnbalancedMassHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_HARMONIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassHarmonicLoadData")

    class _Cast_UnbalancedMassHarmonicLoadData:
        """Special nested class for casting UnbalancedMassHarmonicLoadData to subclasses."""

        def __init__(
            self: "UnbalancedMassHarmonicLoadData._Cast_UnbalancedMassHarmonicLoadData",
            parent: "UnbalancedMassHarmonicLoadData",
        ):
            self._parent = parent

        @property
        def speed_dependent_harmonic_load_data(
            self: "UnbalancedMassHarmonicLoadData._Cast_UnbalancedMassHarmonicLoadData",
        ) -> "_1390.SpeedDependentHarmonicLoadData":
            return self._parent._cast(_1390.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "UnbalancedMassHarmonicLoadData._Cast_UnbalancedMassHarmonicLoadData",
        ) -> "_1387.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1387

            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def unbalanced_mass_harmonic_load_data(
            self: "UnbalancedMassHarmonicLoadData._Cast_UnbalancedMassHarmonicLoadData",
        ) -> "UnbalancedMassHarmonicLoadData":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassHarmonicLoadData._Cast_UnbalancedMassHarmonicLoadData",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassHarmonicLoadData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_freedom(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DegreeOfFreedom":
        """EnumWithSelectedValue[mastapy.math_utility.DegreeOfFreedom]"""
        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DegreeOfFreedom.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @degree_of_freedom.setter
    @enforce_parameter_types
    def degree_of_freedom(self: Self, value: "_1511.DegreeOfFreedom"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DegreeOfFreedom.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DegreeOfFreedom = value

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

    @property
    def cast_to(
        self: Self,
    ) -> "UnbalancedMassHarmonicLoadData._Cast_UnbalancedMassHarmonicLoadData":
        return self._Cast_UnbalancedMassHarmonicLoadData(self)
