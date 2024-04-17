"""CylindricalCutterSimulatableGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_CUTTER_SIMULATABLE_GEAR = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation",
    "CylindricalCutterSimulatableGear",
)

if TYPE_CHECKING:
    from mastapy.geometry.two_d import _315


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalCutterSimulatableGear",)


Self = TypeVar("Self", bound="CylindricalCutterSimulatableGear")


class CylindricalCutterSimulatableGear(_0.APIBase):
    """CylindricalCutterSimulatableGear

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_CUTTER_SIMULATABLE_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalCutterSimulatableGear")

    class _Cast_CylindricalCutterSimulatableGear:
        """Special nested class for casting CylindricalCutterSimulatableGear to subclasses."""

        def __init__(
            self: "CylindricalCutterSimulatableGear._Cast_CylindricalCutterSimulatableGear",
            parent: "CylindricalCutterSimulatableGear",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_simulatable_gear(
            self: "CylindricalCutterSimulatableGear._Cast_CylindricalCutterSimulatableGear",
        ) -> "CylindricalCutterSimulatableGear":
            return self._parent

        def __getattr__(
            self: "CylindricalCutterSimulatableGear._Cast_CylindricalCutterSimulatableGear",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalCutterSimulatableGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def generating_profile_shift_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeneratingProfileShiftCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def helix_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def internal_external(self: Self) -> "_315.InternalExternalType":
        """mastapy.geometry.two_d.InternalExternalType

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InternalExternal

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Geometry.TwoD.InternalExternalType"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.geometry.two_d._315", "InternalExternalType"
        )(value)

    @property
    def is_left_handed(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLeftHanded

        if temp is None:
            return False

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def normal_module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_thickness(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalThickness

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_teeth_unsigned(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTeethUnsigned

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def root_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RootFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tip_form_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TipFormDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalCutterSimulatableGear._Cast_CylindricalCutterSimulatableGear":
        return self._Cast_CylindricalCutterSimulatableGear(self)
