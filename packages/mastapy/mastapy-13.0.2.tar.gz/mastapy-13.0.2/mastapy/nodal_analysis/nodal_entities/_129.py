"""Bar"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.nodal_analysis.nodal_entities import _145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR = python_net_import("SMT.MastaAPI.NodalAnalysis.NodalEntities", "Bar")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _51
    from mastapy.system_model.analyses_and_results.system_deflections import _2811
    from mastapy.nodal_analysis.nodal_entities import _147


__docformat__ = "restructuredtext en"
__all__ = ("Bar",)


Self = TypeVar("Self", bound="Bar")


class Bar(_145.NodalComponent):
    """Bar

    This is a mastapy class.
    """

    TYPE = _BAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Bar")

    class _Cast_Bar:
        """Special nested class for casting Bar to subclasses."""

        def __init__(self: "Bar._Cast_Bar", parent: "Bar"):
            self._parent = parent

        @property
        def nodal_component(self: "Bar._Cast_Bar") -> "_145.NodalComponent":
            return self._parent._cast(_145.NodalComponent)

        @property
        def nodal_entity(self: "Bar._Cast_Bar") -> "_147.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _147

            return self._parent._cast(_147.NodalEntity)

        @property
        def shaft_section_system_deflection(
            self: "Bar._Cast_Bar",
        ) -> "_2811.ShaftSectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.ShaftSectionSystemDeflection)

        @property
        def bar(self: "Bar._Cast_Bar") -> "Bar":
            return self._parent

        def __getattr__(self: "Bar._Cast_Bar", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Bar.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def oil_dip_coefficient_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilDipCoefficientInner

        if temp is None:
            return 0.0

        return temp

    @property
    def oil_dip_coefficient_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OilDipCoefficientOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_compliance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorsionalCompliance

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_stiffness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @torsional_stiffness.setter
    @enforce_parameter_types
    def torsional_stiffness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TorsionalStiffness = value

    @property
    def windage_loss_resistive_torque_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindageLossResistiveTorqueInner

        if temp is None:
            return 0.0

        return temp

    @property
    def windage_loss_resistive_torque_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindageLossResistiveTorqueOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def windage_power_loss_inner(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindagePowerLossInner

        if temp is None:
            return 0.0

        return temp

    @property
    def windage_power_loss_outer(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WindagePowerLossOuter

        if temp is None:
            return 0.0

        return temp

    @property
    def bar_geometry(self: Self) -> "_51.BarGeometry":
        """mastapy.nodal_analysis.BarGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BarGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "Bar._Cast_Bar":
        return self._Cast_Bar(self)
