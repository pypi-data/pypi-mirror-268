"""PointLoadHarmonicLoadData"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.electric_machines.harmonic_load_data import _1390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_HARMONIC_LOAD_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PointLoadHarmonicLoadData",
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1511, _1520
    from mastapy.electric_machines.harmonic_load_data import _1387


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadHarmonicLoadData",)


Self = TypeVar("Self", bound="PointLoadHarmonicLoadData")


class PointLoadHarmonicLoadData(_1390.SpeedDependentHarmonicLoadData):
    """PointLoadHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_HARMONIC_LOAD_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadHarmonicLoadData")

    class _Cast_PointLoadHarmonicLoadData:
        """Special nested class for casting PointLoadHarmonicLoadData to subclasses."""

        def __init__(
            self: "PointLoadHarmonicLoadData._Cast_PointLoadHarmonicLoadData",
            parent: "PointLoadHarmonicLoadData",
        ):
            self._parent = parent

        @property
        def speed_dependent_harmonic_load_data(
            self: "PointLoadHarmonicLoadData._Cast_PointLoadHarmonicLoadData",
        ) -> "_1390.SpeedDependentHarmonicLoadData":
            return self._parent._cast(_1390.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "PointLoadHarmonicLoadData._Cast_PointLoadHarmonicLoadData",
        ) -> "_1387.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1387

            return self._parent._cast(_1387.HarmonicLoadDataBase)

        @property
        def point_load_harmonic_load_data(
            self: "PointLoadHarmonicLoadData._Cast_PointLoadHarmonicLoadData",
        ) -> "PointLoadHarmonicLoadData":
            return self._parent

        def __getattr__(
            self: "PointLoadHarmonicLoadData._Cast_PointLoadHarmonicLoadData", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadHarmonicLoadData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degree_of_freedom(self: Self) -> "_1511.DegreeOfFreedom":
        """mastapy.math_utility.DegreeOfFreedom"""
        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.DegreeOfFreedom"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1511", "DegreeOfFreedom"
        )(value)

    @degree_of_freedom.setter
    @enforce_parameter_types
    def degree_of_freedom(self: Self, value: "_1511.DegreeOfFreedom"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.DegreeOfFreedom"
        )
        self.wrapped.DegreeOfFreedom = value

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

    @property
    def cast_to(
        self: Self,
    ) -> "PointLoadHarmonicLoadData._Cast_PointLoadHarmonicLoadData":
        return self._Cast_PointLoadHarmonicLoadData(self)
