"""GearMeshingOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESHING_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "GearMeshingOptions"
)

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1205


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshingOptions",)


Self = TypeVar("Self", bound="GearMeshingOptions")


class GearMeshingOptions(_0.APIBase):
    """GearMeshingOptions

    This is a mastapy class.
    """

    TYPE = _GEAR_MESHING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshingOptions")

    class _Cast_GearMeshingOptions:
        """Special nested class for casting GearMeshingOptions to subclasses."""

        def __init__(
            self: "GearMeshingOptions._Cast_GearMeshingOptions",
            parent: "GearMeshingOptions",
        ):
            self._parent = parent

        @property
        def gear_meshing_options(
            self: "GearMeshingOptions._Cast_GearMeshingOptions",
        ) -> "GearMeshingOptions":
            return self._parent

        def __getattr__(self: "GearMeshingOptions._Cast_GearMeshingOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def mesh_teeth(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.MeshTeeth

        if temp is None:
            return False

        return temp

    @mesh_teeth.setter
    @enforce_parameter_types
    def mesh_teeth(self: Self, value: "bool"):
        self.wrapped.MeshTeeth = bool(value) if value is not None else False

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
    def offset_of_gear_centre_calculated_from_fe(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OffsetOfGearCentreCalculatedFromFE

        if temp is None:
            return ""

        return temp

    @property
    def element_settings(self: Self) -> "_1205.GearMeshingElementOptions":
        """mastapy.gears.fe_model.GearMeshingElementOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElementSettings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshingOptions._Cast_GearMeshingOptions":
        return self._Cast_GearMeshingOptions(self)
