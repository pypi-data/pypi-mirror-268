"""ConicalSetFEModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.sentinels import ListWithSelectedItem_None
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.manufacturing.bevel import _794
from mastapy.gears.fe_model import _1206
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_FE_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.FEModel.Conical", "ConicalSetFEModel"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _58
    from mastapy.gears.fe_model.conical import _1213
    from mastapy.gears.analysis import _1237, _1232, _1223


__docformat__ = "restructuredtext en"
__all__ = ("ConicalSetFEModel",)


Self = TypeVar("Self", bound="ConicalSetFEModel")


class ConicalSetFEModel(_1206.GearSetFEModel):
    """ConicalSetFEModel

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalSetFEModel")

    class _Cast_ConicalSetFEModel:
        """Special nested class for casting ConicalSetFEModel to subclasses."""

        def __init__(
            self: "ConicalSetFEModel._Cast_ConicalSetFEModel",
            parent: "ConicalSetFEModel",
        ):
            self._parent = parent

        @property
        def gear_set_fe_model(
            self: "ConicalSetFEModel._Cast_ConicalSetFEModel",
        ) -> "_1206.GearSetFEModel":
            return self._parent._cast(_1206.GearSetFEModel)

        @property
        def gear_set_implementation_detail(
            self: "ConicalSetFEModel._Cast_ConicalSetFEModel",
        ) -> "_1237.GearSetImplementationDetail":
            from mastapy.gears.analysis import _1237

            return self._parent._cast(_1237.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "ConicalSetFEModel._Cast_ConicalSetFEModel",
        ) -> "_1232.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalSetFEModel._Cast_ConicalSetFEModel",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def conical_set_fe_model(
            self: "ConicalSetFEModel._Cast_ConicalSetFEModel",
        ) -> "ConicalSetFEModel":
            return self._parent

        def __getattr__(self: "ConicalSetFEModel._Cast_ConicalSetFEModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalSetFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def element_order(self: Self) -> "_58.ElementOrder":
        """mastapy.nodal_analysis.ElementOrder"""
        temp = self.wrapped.ElementOrder

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.ElementOrder"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._58", "ElementOrder"
        )(value)

    @element_order.setter
    @enforce_parameter_types
    def element_order(self: Self, value: "_58.ElementOrder"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.ElementOrder"
        )
        self.wrapped.ElementOrder = value

    @property
    def flank_data_source(self: Self) -> "_1213.FlankDataSource":
        """mastapy.gears.fe_model.conical.FlankDataSource"""
        temp = self.wrapped.FlankDataSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.FEModel.Conical.FlankDataSource"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.fe_model.conical._1213", "FlankDataSource"
        )(value)

    @flank_data_source.setter
    @enforce_parameter_types
    def flank_data_source(self: Self, value: "_1213.FlankDataSource"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.FEModel.Conical.FlankDataSource"
        )
        self.wrapped.FlankDataSource = value

    @property
    def selected_design(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_ConicalSetManufacturingConfig":
        """ListWithSelectedItem[mastapy.gears.manufacturing.bevel.ConicalSetManufacturingConfig]"""
        temp = self.wrapped.SelectedDesign

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ConicalSetManufacturingConfig",
        )(temp)

    @selected_design.setter
    @enforce_parameter_types
    def selected_design(self: Self, value: "_794.ConicalSetManufacturingConfig"):
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ConicalSetManufacturingConfig.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ConicalSetManufacturingConfig.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        self.wrapped.SelectedDesign = value

    @property
    def cast_to(self: Self) -> "ConicalSetFEModel._Cast_ConicalSetFEModel":
        return self._Cast_ConicalSetFEModel(self)
