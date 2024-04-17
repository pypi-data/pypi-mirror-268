"""RollerRibDetail"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_RIB_DETAIL = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "RollerRibDetail"
)


__docformat__ = "restructuredtext en"
__all__ = ("RollerRibDetail",)


Self = TypeVar("Self", bound="RollerRibDetail")


class RollerRibDetail(_0.APIBase):
    """RollerRibDetail

    This is a mastapy class.
    """

    TYPE = _ROLLER_RIB_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerRibDetail")

    class _Cast_RollerRibDetail:
        """Special nested class for casting RollerRibDetail to subclasses."""

        def __init__(
            self: "RollerRibDetail._Cast_RollerRibDetail", parent: "RollerRibDetail"
        ):
            self._parent = parent

        @property
        def roller_rib_detail(
            self: "RollerRibDetail._Cast_RollerRibDetail",
        ) -> "RollerRibDetail":
            return self._parent

        def __getattr__(self: "RollerRibDetail._Cast_RollerRibDetail", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerRibDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chamfer(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Chamfer

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @chamfer.setter
    @enforce_parameter_types
    def chamfer(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Chamfer = value

    @property
    def diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Diameter = value

    @property
    def height_above_race(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HeightAboveRace

        if temp is None:
            return 0.0

        return temp

    @property
    def layback_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LaybackAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @layback_angle.setter
    @enforce_parameter_types
    def layback_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LaybackAngle = value

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
    def nominal_contact_height_above_race(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NominalContactHeightAboveRace

        if temp is None:
            return 0.0

        return temp

    @property
    def present(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.Present

        if temp is None:
            return False

        return temp

    @present.setter
    @enforce_parameter_types
    def present(self: Self, value: "bool"):
        self.wrapped.Present = bool(value) if value is not None else False

    @property
    def undercut_axial_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UndercutAxialAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @undercut_axial_angle.setter
    @enforce_parameter_types
    def undercut_axial_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UndercutAxialAngle = value

    @property
    def undercut_axial_start_offset(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UndercutAxialStartOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @undercut_axial_start_offset.setter
    @enforce_parameter_types
    def undercut_axial_start_offset(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UndercutAxialStartOffset = value

    @property
    def undercut_radial_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UndercutRadialAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @undercut_radial_angle.setter
    @enforce_parameter_types
    def undercut_radial_angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UndercutRadialAngle = value

    @property
    def undercut_radial_start_offset(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UndercutRadialStartOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @undercut_radial_start_offset.setter
    @enforce_parameter_types
    def undercut_radial_start_offset(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UndercutRadialStartOffset = value

    @property
    def undercut_radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.UndercutRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @undercut_radius.setter
    @enforce_parameter_types
    def undercut_radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.UndercutRadius = value

    @property
    def cast_to(self: Self) -> "RollerRibDetail._Cast_RollerRibDetail":
        return self._Cast_RollerRibDetail(self)
