"""PointLoadLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, Union, Tuple
from enum import Enum

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.analyses_and_results.static_loads import _6990
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PointLoadLoadCase"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.varying_input_components import _98, _99
    from mastapy.system_model.part_model import _2478
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6946,
        _6933,
        _6846,
        _6937,
    )
    from mastapy.system_model.analyses_and_results import _2665, _2661, _2659


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadLoadCase",)


Self = TypeVar("Self", bound="PointLoadLoadCase")


class PointLoadLoadCase(_6990.VirtualComponentLoadCase):
    """PointLoadLoadCase

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_LOAD_CASE

    class ForceSpecification(Enum):
        """ForceSpecification is a nested enum."""

        @classmethod
        def type_(cls):
            return _POINT_LOAD_LOAD_CASE.ForceSpecification

        RADIAL_TANGENTIAL = 0
        FORCE_X_FORCE_Y = 1

    def __enum_setattr(self: Self, attr: str, value: Any):
        raise AttributeError("Cannot set the attributes of an Enum.") from None

    def __enum_delattr(self: Self, attr: str):
        raise AttributeError("Cannot delete the attributes of an Enum.") from None

    ForceSpecification.__setattr__ = __enum_setattr
    ForceSpecification.__delattr__ = __enum_delattr
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadLoadCase")

    class _Cast_PointLoadLoadCase:
        """Special nested class for casting PointLoadLoadCase to subclasses."""

        def __init__(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
            parent: "PointLoadLoadCase",
        ):
            self._parent = parent

        @property
        def virtual_component_load_case(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
        ) -> "_6990.VirtualComponentLoadCase":
            return self._parent._cast(_6990.VirtualComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
        ) -> "_6933.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
        ) -> "_6846.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ComponentLoadCase)

        @property
        def part_load_case(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
        ) -> "_6937.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6937

            return self._parent._cast(_6937.PartLoadCase)

        @property
        def part_analysis(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
        ) -> "_2665.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2665

            return self._parent._cast(_2665.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
        ) -> "_2661.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2661

            return self._parent._cast(_2661.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def point_load_load_case(
            self: "PointLoadLoadCase._Cast_PointLoadLoadCase",
        ) -> "PointLoadLoadCase":
            return self._parent

        def __getattr__(self: "PointLoadLoadCase._Cast_PointLoadLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PointLoadLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_radial_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AngleOfRadialForce

        if temp is None:
            return 0.0

        return temp

    @angle_of_radial_force.setter
    @enforce_parameter_types
    def angle_of_radial_force(self: Self, value: "float"):
        self.wrapped.AngleOfRadialForce = float(value) if value is not None else 0.0

    @property
    def displacement_x(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DisplacementX

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @displacement_x.setter
    @enforce_parameter_types
    def displacement_x(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DisplacementX = value

    @property
    def displacement_y(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DisplacementY

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @displacement_y.setter
    @enforce_parameter_types
    def displacement_y(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DisplacementY = value

    @property
    def displacement_z(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DisplacementZ

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @displacement_z.setter
    @enforce_parameter_types
    def displacement_z(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DisplacementZ = value

    @property
    def force_specification_options(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase.ForceSpecification]"""
        temp = self.wrapped.ForceSpecificationOptions

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @force_specification_options.setter
    @enforce_parameter_types
    def force_specification_options(
        self: Self, value: "PointLoadLoadCase.ForceSpecification"
    ):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ForceSpecificationOptions = value

    @property
    def magnitude_radial_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnitudeRadialForce

        if temp is None:
            return 0.0

        return temp

    @magnitude_radial_force.setter
    @enforce_parameter_types
    def magnitude_radial_force(self: Self, value: "float"):
        self.wrapped.MagnitudeRadialForce = float(value) if value is not None else 0.0

    @property
    def radial_load(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialLoad

        if temp is None:
            return 0.0

        return temp

    @radial_load.setter
    @enforce_parameter_types
    def radial_load(self: Self, value: "float"):
        self.wrapped.RadialLoad = float(value) if value is not None else 0.0

    @property
    def tangential_load(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TangentialLoad

        if temp is None:
            return 0.0

        return temp

    @tangential_load.setter
    @enforce_parameter_types
    def tangential_load(self: Self, value: "float"):
        self.wrapped.TangentialLoad = float(value) if value is not None else 0.0

    @property
    def twist_theta_x(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TwistThetaX

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @twist_theta_x.setter
    @enforce_parameter_types
    def twist_theta_x(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TwistThetaX = value

    @property
    def twist_theta_y(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TwistThetaY

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @twist_theta_y.setter
    @enforce_parameter_types
    def twist_theta_y(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TwistThetaY = value

    @property
    def twist_theta_z(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TwistThetaZ

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @twist_theta_z.setter
    @enforce_parameter_types
    def twist_theta_z(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TwistThetaZ = value

    @property
    def axial_load(self: Self) -> "_98.ForceInputComponent":
        """mastapy.nodal_analysis.varying_input_components.ForceInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialLoad

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2478.PointLoad":
        """mastapy.system_model.part_model.PointLoad

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_x(self: Self) -> "_98.ForceInputComponent":
        """mastapy.nodal_analysis.varying_input_components.ForceInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceX

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_y(self: Self) -> "_98.ForceInputComponent":
        """mastapy.nodal_analysis.varying_input_components.ForceInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceY

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def moment_x(self: Self) -> "_99.MomentInputComponent":
        """mastapy.nodal_analysis.varying_input_components.MomentInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentX

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def moment_y(self: Self) -> "_99.MomentInputComponent":
        """mastapy.nodal_analysis.varying_input_components.MomentInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentY

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def moment_z(self: Self) -> "_99.MomentInputComponent":
        """mastapy.nodal_analysis.varying_input_components.MomentInputComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentZ

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6946.PointLoadHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.PointLoadHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PointLoadLoadCase._Cast_PointLoadLoadCase":
        return self._Cast_PointLoadLoadCase(self)
