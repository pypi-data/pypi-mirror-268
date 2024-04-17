"""CylindricalMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.load_case import _878
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Cylindrical", "CylindricalMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears import _326, _327
    from mastapy.gears.gear_designs.cylindrical import _1063
    from mastapy.gears.analysis import _1228, _1222


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshLoadCase",)


Self = TypeVar("Self", bound="CylindricalMeshLoadCase")


class CylindricalMeshLoadCase(_878.MeshLoadCase):
    """CylindricalMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalMeshLoadCase")

    class _Cast_CylindricalMeshLoadCase:
        """Special nested class for casting CylindricalMeshLoadCase to subclasses."""

        def __init__(
            self: "CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase",
            parent: "CylindricalMeshLoadCase",
        ):
            self._parent = parent

        @property
        def mesh_load_case(
            self: "CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase",
        ) -> "_878.MeshLoadCase":
            return self._parent._cast(_878.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(
            self: "CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase",
        ) -> "_1228.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase",
        ) -> "_1222.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_load_case(
            self: "CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase",
        ) -> "CylindricalMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_flank(self: Self) -> "_326.CylindricalFlanks":
        """mastapy.gears.CylindricalFlanks

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Gears.CylindricalFlanks")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.gears._326", "CylindricalFlanks")(
            value
        )

    @property
    def equivalent_misalignment(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EquivalentMisalignment

        if temp is None:
            return 0.0

        return temp

    @equivalent_misalignment.setter
    @enforce_parameter_types
    def equivalent_misalignment(self: Self, value: "float"):
        self.wrapped.EquivalentMisalignment = float(value) if value is not None else 0.0

    @property
    def equivalent_misalignment_due_to_system_deflection(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EquivalentMisalignmentDueToSystemDeflection

        if temp is None:
            return 0.0

        return temp

    @equivalent_misalignment_due_to_system_deflection.setter
    @enforce_parameter_types
    def equivalent_misalignment_due_to_system_deflection(self: Self, value: "float"):
        self.wrapped.EquivalentMisalignmentDueToSystemDeflection = (
            float(value) if value is not None else 0.0
        )

    @property
    def gear_a_number_of_load_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearANumberOfLoadCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_number_of_load_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBNumberOfLoadCycles

        if temp is None:
            return 0.0

        return temp

    @property
    def misalignment_source(self: Self) -> "_327.CylindricalMisalignmentDataSource":
        """mastapy.gears.CylindricalMisalignmentDataSource"""
        temp = self.wrapped.MisalignmentSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.CylindricalMisalignmentDataSource"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._327", "CylindricalMisalignmentDataSource"
        )(value)

    @misalignment_source.setter
    @enforce_parameter_types
    def misalignment_source(
        self: Self, value: "_327.CylindricalMisalignmentDataSource"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.CylindricalMisalignmentDataSource"
        )
        self.wrapped.MisalignmentSource = value

    @property
    def misalignment_due_to_micro_geometry_lead_relief(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MisalignmentDueToMicroGeometryLeadRelief

        if temp is None:
            return 0.0

        return temp

    @misalignment_due_to_micro_geometry_lead_relief.setter
    @enforce_parameter_types
    def misalignment_due_to_micro_geometry_lead_relief(self: Self, value: "float"):
        self.wrapped.MisalignmentDueToMicroGeometryLeadRelief = (
            float(value) if value is not None else 0.0
        )

    @property
    def pitch_line_velocity_at_operating_pitch_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLineVelocityAtOperatingPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def load_case_modifiable_settings(
        self: Self,
    ) -> "_1063.LTCALoadCaseModifiableSettings":
        """mastapy.gears.gear_designs.cylindrical.LTCALoadCaseModifiableSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadCaseModifiableSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CylindricalMeshLoadCase._Cast_CylindricalMeshLoadCase":
        return self._Cast_CylindricalMeshLoadCase(self)
