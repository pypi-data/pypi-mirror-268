"""RingPinsToDiscConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.math_utility.hertzian_contact import _1580
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.system_model.analyses_and_results.static_loads import _6920
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RingPinsToDiscConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2348
    from mastapy.system_model.analyses_and_results.static_loads import _6858
    from mastapy.system_model.analyses_and_results import _2657, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionLoadCase",)


Self = TypeVar("Self", bound="RingPinsToDiscConnectionLoadCase")


class RingPinsToDiscConnectionLoadCase(_6920.InterMountableComponentConnectionLoadCase):
    """RingPinsToDiscConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsToDiscConnectionLoadCase")

    class _Cast_RingPinsToDiscConnectionLoadCase:
        """Special nested class for casting RingPinsToDiscConnectionLoadCase to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase",
            parent: "RingPinsToDiscConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_load_case(
            self: "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase",
        ) -> "_6920.InterMountableComponentConnectionLoadCase":
            return self._parent._cast(_6920.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase",
        ) -> "_6858.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase",
        ) -> "_2657.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase",
        ) -> "RingPinsToDiscConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsToDiscConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hertzian_contact_deflection_calculation_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod":
        """EnumWithSelectedValue[mastapy.math_utility.hertzian_contact.HertzianContactDeflectionCalculationMethod]"""
        temp = self.wrapped.HertzianContactDeflectionCalculationMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @hertzian_contact_deflection_calculation_method.setter
    @enforce_parameter_types
    def hertzian_contact_deflection_calculation_method(
        self: Self, value: "_1580.HertzianContactDeflectionCalculationMethod"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.HertzianContactDeflectionCalculationMethod = value

    @property
    def number_of_lobes_passed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfLobesPassed

        if temp is None:
            return 0.0

        return temp

    @number_of_lobes_passed.setter
    @enforce_parameter_types
    def number_of_lobes_passed(self: Self, value: "float"):
        self.wrapped.NumberOfLobesPassed = float(value) if value is not None else 0.0

    @property
    def number_of_steps_for_one_lobe_pass(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfStepsForOneLobePass

        if temp is None:
            return 0

        return temp

    @property
    def specified_contact_stiffness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.SpecifiedContactStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @specified_contact_stiffness.setter
    @enforce_parameter_types
    def specified_contact_stiffness(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.SpecifiedContactStiffness = value

    @property
    def use_constant_mesh_stiffness(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseConstantMeshStiffness

        if temp is None:
            return False

        return temp

    @use_constant_mesh_stiffness.setter
    @enforce_parameter_types
    def use_constant_mesh_stiffness(self: Self, value: "bool"):
        self.wrapped.UseConstantMeshStiffness = (
            bool(value) if value is not None else False
        )

    @property
    def connection_design(self: Self) -> "_2348.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RingPinsToDiscConnectionLoadCase._Cast_RingPinsToDiscConnectionLoadCase":
        return self._Cast_RingPinsToDiscConnectionLoadCase(self)
