"""BeltDrive"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDrive"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2584, _2598, _2594
    from mastapy.system_model.connections_and_sockets import _2275
    from mastapy.system_model.part_model import _2441, _2475
    from mastapy.system_model import _2210


__docformat__ = "restructuredtext en"
__all__ = ("BeltDrive",)


Self = TypeVar("Self", bound="BeltDrive")


class BeltDrive(_2483.SpecialisedAssembly):
    """BeltDrive

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDrive")

    class _Cast_BeltDrive:
        """Special nested class for casting BeltDrive to subclasses."""

        def __init__(self: "BeltDrive._Cast_BeltDrive", parent: "BeltDrive"):
            self._parent = parent

        @property
        def specialised_assembly(
            self: "BeltDrive._Cast_BeltDrive",
        ) -> "_2483.SpecialisedAssembly":
            return self._parent._cast(_2483.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "BeltDrive._Cast_BeltDrive",
        ) -> "_2441.AbstractAssembly":
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.AbstractAssembly)

        @property
        def part(self: "BeltDrive._Cast_BeltDrive") -> "_2475.Part":
            from mastapy.system_model.part_model import _2475

            return self._parent._cast(_2475.Part)

        @property
        def design_entity(self: "BeltDrive._Cast_BeltDrive") -> "_2210.DesignEntity":
            from mastapy.system_model import _2210

            return self._parent._cast(_2210.DesignEntity)

        @property
        def cvt(self: "BeltDrive._Cast_BeltDrive") -> "_2594.CVT":
            from mastapy.system_model.part_model.couplings import _2594

            return self._parent._cast(_2594.CVT)

        @property
        def belt_drive(self: "BeltDrive._Cast_BeltDrive") -> "BeltDrive":
            return self._parent

        def __getattr__(self: "BeltDrive._Cast_BeltDrive", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDrive.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltLength

        if temp is None:
            return 0.0

        return temp

    @property
    def belt_mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltMass

        if temp is None:
            return 0.0

        return temp

    @property
    def belt_mass_per_unit_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.BeltMassPerUnitLength

        if temp is None:
            return 0.0

        return temp

    @belt_mass_per_unit_length.setter
    @enforce_parameter_types
    def belt_mass_per_unit_length(self: Self, value: "float"):
        self.wrapped.BeltMassPerUnitLength = float(value) if value is not None else 0.0

    @property
    def pre_tension(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PreTension

        if temp is None:
            return 0.0

        return temp

    @pre_tension.setter
    @enforce_parameter_types
    def pre_tension(self: Self, value: "float"):
        self.wrapped.PreTension = float(value) if value is not None else 0.0

    @property
    def specify_stiffness_for_unit_length(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyStiffnessForUnitLength

        if temp is None:
            return False

        return temp

    @specify_stiffness_for_unit_length.setter
    @enforce_parameter_types
    def specify_stiffness_for_unit_length(self: Self, value: "bool"):
        self.wrapped.SpecifyStiffnessForUnitLength = (
            bool(value) if value is not None else False
        )

    @property
    def stiffness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Stiffness

        if temp is None:
            return 0.0

        return temp

    @stiffness.setter
    @enforce_parameter_types
    def stiffness(self: Self, value: "float"):
        self.wrapped.Stiffness = float(value) if value is not None else 0.0

    @property
    def stiffness_for_unit_length(self: Self) -> "float":
        """float"""
        temp = self.wrapped.StiffnessForUnitLength

        if temp is None:
            return 0.0

        return temp

    @stiffness_for_unit_length.setter
    @enforce_parameter_types
    def stiffness_for_unit_length(self: Self, value: "float"):
        self.wrapped.StiffnessForUnitLength = float(value) if value is not None else 0.0

    @property
    def type_of_belt(self: Self) -> "_2584.BeltDriveType":
        """mastapy.system_model.part_model.couplings.BeltDriveType"""
        temp = self.wrapped.TypeOfBelt

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.Couplings.BeltDriveType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.couplings._2584", "BeltDriveType"
        )(value)

    @type_of_belt.setter
    @enforce_parameter_types
    def type_of_belt(self: Self, value: "_2584.BeltDriveType"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.Couplings.BeltDriveType"
        )
        self.wrapped.TypeOfBelt = value

    @property
    def belt_connections(self: Self) -> "List[_2275.BeltConnection]":
        """List[mastapy.system_model.connections_and_sockets.BeltConnection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltConnections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def pulleys(self: Self) -> "List[_2598.Pulley]":
        """List[mastapy.system_model.part_model.couplings.Pulley]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Pulleys

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "BeltDrive._Cast_BeltDrive":
        return self._Cast_BeltDrive(self)
