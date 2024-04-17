"""RealPlungeShaverOutputs"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _654
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_REAL_PLUNGE_SHAVER_OUTPUTS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving",
    "RealPlungeShaverOutputs",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _648
    from mastapy.gears.manufacturing.cylindrical import _616
    from mastapy.gears.manufacturing.cylindrical.cutters import _713


__docformat__ = "restructuredtext en"
__all__ = ("RealPlungeShaverOutputs",)


Self = TypeVar("Self", bound="RealPlungeShaverOutputs")


class RealPlungeShaverOutputs(_654.PlungeShaverOutputs):
    """RealPlungeShaverOutputs

    This is a mastapy class.
    """

    TYPE = _REAL_PLUNGE_SHAVER_OUTPUTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RealPlungeShaverOutputs")

    class _Cast_RealPlungeShaverOutputs:
        """Special nested class for casting RealPlungeShaverOutputs to subclasses."""

        def __init__(
            self: "RealPlungeShaverOutputs._Cast_RealPlungeShaverOutputs",
            parent: "RealPlungeShaverOutputs",
        ):
            self._parent = parent

        @property
        def plunge_shaver_outputs(
            self: "RealPlungeShaverOutputs._Cast_RealPlungeShaverOutputs",
        ) -> "_654.PlungeShaverOutputs":
            return self._parent._cast(_654.PlungeShaverOutputs)

        @property
        def real_plunge_shaver_outputs(
            self: "RealPlungeShaverOutputs._Cast_RealPlungeShaverOutputs",
        ) -> "RealPlungeShaverOutputs":
            return self._parent

        def __getattr__(
            self: "RealPlungeShaverOutputs._Cast_RealPlungeShaverOutputs", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RealPlungeShaverOutputs.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def highest_shaver_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HighestShaverTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def lead_measurement_method(self: Self) -> "_648.MicroGeometryDefinitionMethod":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod"""
        temp = self.wrapped.LeadMeasurementMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.plunge_shaving._648",
            "MicroGeometryDefinitionMethod",
        )(value)

    @lead_measurement_method.setter
    @enforce_parameter_types
    def lead_measurement_method(
        self: Self, value: "_648.MicroGeometryDefinitionMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )
        self.wrapped.LeadMeasurementMethod = value

    @property
    def lowest_shaver_tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LowestShaverTipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def profile_measurement_method(self: Self) -> "_648.MicroGeometryDefinitionMethod":
        """mastapy.gears.manufacturing.cylindrical.plunge_shaving.MicroGeometryDefinitionMethod"""
        temp = self.wrapped.ProfileMeasurementMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.manufacturing.cylindrical.plunge_shaving._648",
            "MicroGeometryDefinitionMethod",
        )(value)

    @profile_measurement_method.setter
    @enforce_parameter_types
    def profile_measurement_method(
        self: Self, value: "_648.MicroGeometryDefinitionMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving.MicroGeometryDefinitionMethod",
        )
        self.wrapped.ProfileMeasurementMethod = value

    @property
    def specify_face_width(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SpecifyFaceWidth

        if temp is None:
            return False

        return temp

    @specify_face_width.setter
    @enforce_parameter_types
    def specify_face_width(self: Self, value: "bool"):
        self.wrapped.SpecifyFaceWidth = bool(value) if value is not None else False

    @property
    def left_flank_micro_geometry(
        self: Self,
    ) -> "_616.CylindricalGearSpecifiedMicroGeometry":
        """mastapy.gears.manufacturing.cylindrical.CylindricalGearSpecifiedMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_micro_geometry(
        self: Self,
    ) -> "_616.CylindricalGearSpecifiedMicroGeometry":
        """mastapy.gears.manufacturing.cylindrical.CylindricalGearSpecifiedMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaver(self: Self) -> "_713.CylindricalGearPlungeShaver":
        """mastapy.gears.manufacturing.cylindrical.cutters.CylindricalGearPlungeShaver

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Shaver

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry(
        self: Self,
    ) -> "List[_616.CylindricalGearSpecifiedMicroGeometry]":
        """List[mastapy.gears.manufacturing.cylindrical.CylindricalGearSpecifiedMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def calculate_micro_geometry(self: Self):
        """Method does not return."""
        self.wrapped.CalculateMicroGeometry()

    def face_width_requires_calculation(self: Self):
        """Method does not return."""
        self.wrapped.FaceWidthRequiresCalculation()

    @property
    def cast_to(self: Self) -> "RealPlungeShaverOutputs._Cast_RealPlungeShaverOutputs":
        return self._Cast_RealPlungeShaverOutputs(self)
