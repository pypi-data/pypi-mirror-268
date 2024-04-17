"""KeyedJointDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors.interference_fits import _1452
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KEYED_JOINT_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints", "KeyedJointDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.keyed_joints import _1445, _1447
    from mastapy.detailed_rigid_connectors import _1394


__docformat__ = "restructuredtext en"
__all__ = ("KeyedJointDesign",)


Self = TypeVar("Self", bound="KeyedJointDesign")


class KeyedJointDesign(_1452.InterferenceFitDesign):
    """KeyedJointDesign

    This is a mastapy class.
    """

    TYPE = _KEYED_JOINT_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KeyedJointDesign")

    class _Cast_KeyedJointDesign:
        """Special nested class for casting KeyedJointDesign to subclasses."""

        def __init__(
            self: "KeyedJointDesign._Cast_KeyedJointDesign", parent: "KeyedJointDesign"
        ):
            self._parent = parent

        @property
        def interference_fit_design(
            self: "KeyedJointDesign._Cast_KeyedJointDesign",
        ) -> "_1452.InterferenceFitDesign":
            return self._parent._cast(_1452.InterferenceFitDesign)

        @property
        def detailed_rigid_connector_design(
            self: "KeyedJointDesign._Cast_KeyedJointDesign",
        ) -> "_1394.DetailedRigidConnectorDesign":
            from mastapy.detailed_rigid_connectors import _1394

            return self._parent._cast(_1394.DetailedRigidConnectorDesign)

        @property
        def keyed_joint_design(
            self: "KeyedJointDesign._Cast_KeyedJointDesign",
        ) -> "KeyedJointDesign":
            return self._parent

        def __getattr__(self: "KeyedJointDesign._Cast_KeyedJointDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "KeyedJointDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_contact_stress_for_inner_component(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStressForInnerComponent

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress_for_key(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStressForKey

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress_for_outer_component(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStressForOuterComponent

        if temp is None:
            return 0.0

        return temp

    @property
    def edge_chamfer(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EdgeChamfer

        if temp is None:
            return 0.0

        return temp

    @edge_chamfer.setter
    @enforce_parameter_types
    def edge_chamfer(self: Self, value: "float"):
        self.wrapped.EdgeChamfer = float(value) if value is not None else 0.0

    @property
    def geometry_type(self: Self) -> "_1445.KeyTypes":
        """mastapy.detailed_rigid_connectors.keyed_joints.KeyTypes"""
        temp = self.wrapped.GeometryType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints.KeyTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.keyed_joints._1445", "KeyTypes"
        )(value)

    @geometry_type.setter
    @enforce_parameter_types
    def geometry_type(self: Self, value: "_1445.KeyTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints.KeyTypes"
        )
        self.wrapped.GeometryType = value

    @property
    def height(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Height

        if temp is None:
            return 0.0

        return temp

    @height.setter
    @enforce_parameter_types
    def height(self: Self, value: "float"):
        self.wrapped.Height = float(value) if value is not None else 0.0

    @property
    def inclined_underside_chamfer(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InclinedUndersideChamfer

        if temp is None:
            return 0.0

        return temp

    @inclined_underside_chamfer.setter
    @enforce_parameter_types
    def inclined_underside_chamfer(self: Self, value: "float"):
        self.wrapped.InclinedUndersideChamfer = (
            float(value) if value is not None else 0.0
        )

    @property
    def interference_fit_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.InterferenceFitLength

        if temp is None:
            return 0.0

        return temp

    @interference_fit_length.setter
    @enforce_parameter_types
    def interference_fit_length(self: Self, value: "float"):
        self.wrapped.InterferenceFitLength = float(value) if value is not None else 0.0

    @property
    def is_interference_fit(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsInterferenceFit

        if temp is None:
            return False

        return temp

    @is_interference_fit.setter
    @enforce_parameter_types
    def is_interference_fit(self: Self, value: "bool"):
        self.wrapped.IsInterferenceFit = bool(value) if value is not None else False

    @property
    def is_key_case_hardened(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsKeyCaseHardened

        if temp is None:
            return False

        return temp

    @is_key_case_hardened.setter
    @enforce_parameter_types
    def is_key_case_hardened(self: Self, value: "bool"):
        self.wrapped.IsKeyCaseHardened = bool(value) if value is not None else False

    @property
    def key_effective_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KeyEffectiveLength

        if temp is None:
            return 0.0

        return temp

    @property
    def keyway_depth_inner_component(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.KeywayDepthInnerComponent

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @keyway_depth_inner_component.setter
    @enforce_parameter_types
    def keyway_depth_inner_component(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.KeywayDepthInnerComponent = value

    @property
    def keyway_depth_outer_component(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.KeywayDepthOuterComponent

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @keyway_depth_outer_component.setter
    @enforce_parameter_types
    def keyway_depth_outer_component(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.KeywayDepthOuterComponent = value

    @property
    def length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: Self, value: "float"):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def number_of_keys(self: Self) -> "_1447.NumberOfKeys":
        """mastapy.detailed_rigid_connectors.keyed_joints.NumberOfKeys"""
        temp = self.wrapped.NumberOfKeys

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints.NumberOfKeys"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.keyed_joints._1447", "NumberOfKeys"
        )(value)

    @number_of_keys.setter
    @enforce_parameter_types
    def number_of_keys(self: Self, value: "_1447.NumberOfKeys"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints.NumberOfKeys"
        )
        self.wrapped.NumberOfKeys = value

    @property
    def position_offset(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PositionOffset

        if temp is None:
            return 0.0

        return temp

    @position_offset.setter
    @enforce_parameter_types
    def position_offset(self: Self, value: "float"):
        self.wrapped.PositionOffset = float(value) if value is not None else 0.0

    @property
    def tensile_yield_strength(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TensileYieldStrength

        if temp is None:
            return 0.0

        return temp

    @tensile_yield_strength.setter
    @enforce_parameter_types
    def tensile_yield_strength(self: Self, value: "float"):
        self.wrapped.TensileYieldStrength = float(value) if value is not None else 0.0

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "KeyedJointDesign._Cast_KeyedJointDesign":
        return self._Cast_KeyedJointDesign(self)
