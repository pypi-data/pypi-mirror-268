"""ShaftHubConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from PIL.Image import Image

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.part_model.couplings import _2599, _2602, _2603
from mastapy.detailed_rigid_connectors.splines import _1402
from mastapy.system_model.part_model import _2454
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_ARRAY = python_net_import("System", "Array")
_SHAFT_HUB_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ShaftHubConnection"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1417, _1422
    from mastapy.system_model.part_model.couplings import _2600, _2607, _2601
    from mastapy.detailed_rigid_connectors.interference_fits import _1452
    from mastapy.nodal_analysis import _57
    from mastapy.system_model.part_model import _2471, _2451, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnection",)


Self = TypeVar("Self", bound="ShaftHubConnection")


class ShaftHubConnection(_2454.Connector):
    """ShaftHubConnection

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftHubConnection")

    class _Cast_ShaftHubConnection:
        """Special nested class for casting ShaftHubConnection to subclasses."""

        def __init__(
            self: "ShaftHubConnection._Cast_ShaftHubConnection",
            parent: "ShaftHubConnection",
        ):
            self._parent = parent

        @property
        def connector(
            self: "ShaftHubConnection._Cast_ShaftHubConnection",
        ) -> "_2454.Connector":
            return self._parent._cast(_2454.Connector)

        @property
        def mountable_component(
            self: "ShaftHubConnection._Cast_ShaftHubConnection",
        ) -> "_2471.MountableComponent":
            from mastapy.system_model.part_model import _2471

            return self._parent._cast(_2471.MountableComponent)

        @property
        def component(
            self: "ShaftHubConnection._Cast_ShaftHubConnection",
        ) -> "_2451.Component":
            from mastapy.system_model.part_model import _2451

            return self._parent._cast(_2451.Component)

        @property
        def part(self: "ShaftHubConnection._Cast_ShaftHubConnection") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(
            self: "ShaftHubConnection._Cast_ShaftHubConnection",
        ) -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def shaft_hub_connection(
            self: "ShaftHubConnection._Cast_ShaftHubConnection",
        ) -> "ShaftHubConnection":
            return self._parent

        def __getattr__(self: "ShaftHubConnection._Cast_ShaftHubConnection", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftHubConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_spline_drawing(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDSplineDrawing

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def additional_tilt_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AdditionalTiltStiffness

        if temp is None:
            return 0.0

        return temp

    @additional_tilt_stiffness.setter
    @enforce_parameter_types
    def additional_tilt_stiffness(self: Self, value: "float"):
        self.wrapped.AdditionalTiltStiffness = (
            float(value) if value is not None else 0.0
        )

    @property
    def angle_of_first_connection_point(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AngleOfFirstConnectionPoint

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle_of_first_connection_point.setter
    @enforce_parameter_types
    def angle_of_first_connection_point(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AngleOfFirstConnectionPoint = value

    @property
    def angular_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def angular_extent_of_external_teeth(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AngularExtentOfExternalTeeth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angular_extent_of_external_teeth.setter
    @enforce_parameter_types
    def angular_extent_of_external_teeth(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AngularExtentOfExternalTeeth = value

    @property
    def axial_preload(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialPreload

        if temp is None:
            return 0.0

        return temp

    @axial_preload.setter
    @enforce_parameter_types
    def axial_preload(self: Self, value: "float"):
        self.wrapped.AxialPreload = float(value) if value is not None else 0.0

    @property
    def axial_stiffness_shaft_hub_connection(self: Self) -> "float":
        """float"""
        temp = self.wrapped.AxialStiffnessShaftHubConnection

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness_shaft_hub_connection.setter
    @enforce_parameter_types
    def axial_stiffness_shaft_hub_connection(self: Self, value: "float"):
        self.wrapped.AxialStiffnessShaftHubConnection = (
            float(value) if value is not None else 0.0
        )

    @property
    def centre_angle_of_first_external_tooth(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.CentreAngleOfFirstExternalTooth

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @centre_angle_of_first_external_tooth.setter
    @enforce_parameter_types
    def centre_angle_of_first_external_tooth(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.CentreAngleOfFirstExternalTooth = value

    @property
    def coefficient_of_friction(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientOfFriction

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_friction.setter
    @enforce_parameter_types
    def coefficient_of_friction(self: Self, value: "float"):
        self.wrapped.CoefficientOfFriction = float(value) if value is not None else 0.0

    @property
    def contact_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ContactDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @contact_diameter.setter
    @enforce_parameter_types
    def contact_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ContactDiameter = value

    @property
    def flank_contact_stiffness(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.FlankContactStiffness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @flank_contact_stiffness.setter
    @enforce_parameter_types
    def flank_contact_stiffness(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.FlankContactStiffness = value

    @property
    def helix_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    @enforce_parameter_types
    def helix_angle(self: Self, value: "float"):
        self.wrapped.HelixAngle = float(value) if value is not None else 0.0

    @property
    def inner_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.InnerDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @inner_diameter.setter
    @enforce_parameter_types
    def inner_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.InnerDiameter = value

    @property
    def inner_half_material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.InnerHalfMaterial.SelectedItemName

        if temp is None:
            return ""

        return temp

    @inner_half_material.setter
    @enforce_parameter_types
    def inner_half_material(self: Self, value: "str"):
        self.wrapped.InnerHalfMaterial.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def left_flank_helix_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LeftFlankHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @left_flank_helix_angle.setter
    @enforce_parameter_types
    def left_flank_helix_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LeftFlankHelixAngle = value

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
    def major_diameter_contact_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MajorDiameterContactStiffness

        if temp is None:
            return 0.0

        return temp

    @major_diameter_contact_stiffness.setter
    @enforce_parameter_types
    def major_diameter_contact_stiffness(self: Self, value: "float"):
        self.wrapped.MajorDiameterContactStiffness = (
            float(value) if value is not None else 0.0
        )

    @property
    def major_diameter_diametral_clearance(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MajorDiameterDiametralClearance

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @major_diameter_diametral_clearance.setter
    @enforce_parameter_types
    def major_diameter_diametral_clearance(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MajorDiameterDiametralClearance = value

    @property
    def normal_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalClearance

        if temp is None:
            return 0.0

        return temp

    @normal_clearance.setter
    @enforce_parameter_types
    def normal_clearance(self: Self, value: "float"):
        self.wrapped.NormalClearance = float(value) if value is not None else 0.0

    @property
    def number_of_connection_points(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfConnectionPoints

        if temp is None:
            return 0

        return temp

    @number_of_connection_points.setter
    @enforce_parameter_types
    def number_of_connection_points(self: Self, value: "int"):
        self.wrapped.NumberOfConnectionPoints = int(value) if value is not None else 0

    @property
    def number_of_contacts_per_direction(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfContactsPerDirection

        if temp is None:
            return 0

        return temp

    @number_of_contacts_per_direction.setter
    @enforce_parameter_types
    def number_of_contacts_per_direction(self: Self, value: "int"):
        self.wrapped.NumberOfContactsPerDirection = (
            int(value) if value is not None else 0
        )

    @property
    def outer_diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.OuterDiameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @outer_diameter.setter
    @enforce_parameter_types
    def outer_diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.OuterDiameter = value

    @property
    def outer_half_material(self: Self) -> "str":
        """str"""
        temp = self.wrapped.OuterHalfMaterial.SelectedItemName

        if temp is None:
            return ""

        return temp

    @outer_half_material.setter
    @enforce_parameter_types
    def outer_half_material(self: Self, value: "str"):
        self.wrapped.OuterHalfMaterial.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PressureAngle

        if temp is None:
            return 0.0

        return temp

    @pressure_angle.setter
    @enforce_parameter_types
    def pressure_angle(self: Self, value: "float"):
        self.wrapped.PressureAngle = float(value) if value is not None else 0.0

    @property
    def radial_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialClearance

        if temp is None:
            return 0.0

        return temp

    @radial_clearance.setter
    @enforce_parameter_types
    def radial_clearance(self: Self, value: "float"):
        self.wrapped.RadialClearance = float(value) if value is not None else 0.0

    @property
    def radial_stiffness_shaft_hub_connection(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RadialStiffnessShaftHubConnection

        if temp is None:
            return 0.0

        return temp

    @radial_stiffness_shaft_hub_connection.setter
    @enforce_parameter_types
    def radial_stiffness_shaft_hub_connection(self: Self, value: "float"):
        self.wrapped.RadialStiffnessShaftHubConnection = (
            float(value) if value is not None else 0.0
        )

    @property
    def right_flank_helix_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RightFlankHelixAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @right_flank_helix_angle.setter
    @enforce_parameter_types
    def right_flank_helix_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RightFlankHelixAngle = value

    @property
    def spline_type(self: Self) -> "_1417.SplineDesignTypes":
        """mastapy.detailed_rigid_connectors.splines.SplineDesignTypes"""
        temp = self.wrapped.SplineType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.DetailedRigidConnectors.Splines.SplineDesignTypes"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.detailed_rigid_connectors.splines._1417", "SplineDesignTypes"
        )(value)

    @spline_type.setter
    @enforce_parameter_types
    def spline_type(self: Self, value: "_1417.SplineDesignTypes"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.DetailedRigidConnectors.Splines.SplineDesignTypes"
        )
        self.wrapped.SplineType = value

    @property
    def stiffness_type(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RigidConnectorStiffnessType":
        """EnumWithSelectedValue[mastapy.system_model.part_model.couplings.RigidConnectorStiffnessType]"""
        temp = self.wrapped.StiffnessType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RigidConnectorStiffnessType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @stiffness_type.setter
    @enforce_parameter_types
    def stiffness_type(self: Self, value: "_2599.RigidConnectorStiffnessType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RigidConnectorStiffnessType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.StiffnessType = value

    @property
    def tangential_stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TangentialStiffness

        if temp is None:
            return 0.0

        return temp

    @tangential_stiffness.setter
    @enforce_parameter_types
    def tangential_stiffness(self: Self, value: "float"):
        self.wrapped.TangentialStiffness = float(value) if value is not None else 0.0

    @property
    def tilt_clearance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltClearance

        if temp is None:
            return 0.0

        return temp

    @tilt_clearance.setter
    @enforce_parameter_types
    def tilt_clearance(self: Self, value: "float"):
        self.wrapped.TiltClearance = float(value) if value is not None else 0.0

    @property
    def tilt_stiffness_shaft_hub_connection(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TiltStiffnessShaftHubConnection

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness_shaft_hub_connection.setter
    @enforce_parameter_types
    def tilt_stiffness_shaft_hub_connection(self: Self, value: "float"):
        self.wrapped.TiltStiffnessShaftHubConnection = (
            float(value) if value is not None else 0.0
        )

    @property
    def tilt_stiffness_type(self: Self) -> "_2600.RigidConnectorTiltStiffnessTypes":
        """mastapy.system_model.part_model.couplings.RigidConnectorTiltStiffnessTypes"""
        temp = self.wrapped.TiltStiffnessType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.PartModel.Couplings.RigidConnectorTiltStiffnessTypes",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.couplings._2600",
            "RigidConnectorTiltStiffnessTypes",
        )(value)

    @tilt_stiffness_type.setter
    @enforce_parameter_types
    def tilt_stiffness_type(
        self: Self, value: "_2600.RigidConnectorTiltStiffnessTypes"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.PartModel.Couplings.RigidConnectorTiltStiffnessTypes",
        )
        self.wrapped.TiltStiffnessType = value

    @property
    def tooth_spacing_type(
        self: Self,
    ) -> (
        "enum_with_selected_value.EnumWithSelectedValue_RigidConnectorToothSpacingType"
    ):
        """EnumWithSelectedValue[mastapy.system_model.part_model.couplings.RigidConnectorToothSpacingType]"""
        temp = self.wrapped.ToothSpacingType

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RigidConnectorToothSpacingType.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @tooth_spacing_type.setter
    @enforce_parameter_types
    def tooth_spacing_type(self: Self, value: "_2602.RigidConnectorToothSpacingType"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RigidConnectorToothSpacingType.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ToothSpacingType = value

    @property
    def torsional_stiffness_shaft_hub_connection(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.TorsionalStiffnessShaftHubConnection

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @torsional_stiffness_shaft_hub_connection.setter
    @enforce_parameter_types
    def torsional_stiffness_shaft_hub_connection(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.TorsionalStiffnessShaftHubConnection = value

    @property
    def torsional_twist_preload(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TorsionalTwistPreload

        if temp is None:
            return 0.0

        return temp

    @torsional_twist_preload.setter
    @enforce_parameter_types
    def torsional_twist_preload(self: Self, value: "float"):
        self.wrapped.TorsionalTwistPreload = float(value) if value is not None else 0.0

    @property
    def type_(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_RigidConnectorTypes":
        """EnumWithSelectedValue[mastapy.system_model.part_model.couplings.RigidConnectorTypes]"""
        temp = self.wrapped.Type

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_RigidConnectorTypes.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @type_.setter
    @enforce_parameter_types
    def type_(self: Self, value: "_2603.RigidConnectorTypes"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_RigidConnectorTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Type = value

    @property
    def type_of_fit(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_FitTypes":
        """EnumWithSelectedValue[mastapy.detailed_rigid_connectors.splines.FitTypes]"""
        temp = self.wrapped.TypeOfFit

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_FitTypes.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @type_of_fit.setter
    @enforce_parameter_types
    def type_of_fit(self: Self, value: "_1402.FitTypes"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_FitTypes.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TypeOfFit = value

    @property
    def interference_fit_design(self: Self) -> "_1452.InterferenceFitDesign":
        """mastapy.detailed_rigid_connectors.interference_fits.InterferenceFitDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterferenceFitDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def left_flank_lead_relief(self: Self) -> "_2607.SplineLeadRelief":
        """mastapy.system_model.part_model.couplings.SplineLeadRelief

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankLeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def non_linear_stiffness(self: Self) -> "_57.DiagonalNonLinearStiffness":
        """mastapy.nodal_analysis.DiagonalNonLinearStiffness

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NonLinearStiffness

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_lead_relief(self: Self) -> "_2607.SplineLeadRelief":
        """mastapy.system_model.part_model.couplings.SplineLeadRelief

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankLeadRelief

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spline_joint_design(self: Self) -> "_1422.SplineJointDesign":
        """mastapy.detailed_rigid_connectors.splines.SplineJointDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SplineJointDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def lead_reliefs(self: Self) -> "List[_2607.SplineLeadRelief]":
        """List[mastapy.system_model.part_model.couplings.SplineLeadRelief]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeadReliefs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def tooth_locations_external_spline_half(
        self: Self,
    ) -> "List[_2601.RigidConnectorToothLocation]":
        """List[mastapy.system_model.part_model.couplings.RigidConnectorToothLocation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ToothLocationsExternalSplineHalf

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def full_stiffness_matrix(self: Self) -> "List[List[float]]":
        """List[List[float]]"""
        temp = self.wrapped.FullStiffnessMatrix

        if temp is None:
            return None

        value = conversion.pn_to_mp_list_float_2d(temp)

        if value is None:
            return None

        return value

    @full_stiffness_matrix.setter
    @enforce_parameter_types
    def full_stiffness_matrix(self: Self, value: "List[List[float]]"):
        value = conversion.mp_to_pn_list_float_2d(value)
        self.wrapped.FullStiffnessMatrix = value

    @property
    def cast_to(self: Self) -> "ShaftHubConnection._Cast_ShaftHubConnection":
        return self._Cast_ShaftHubConnection(self)
