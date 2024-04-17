"""ShaftFEMeshingOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.nodal_analysis import _61
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_FE_MESHING_OPTIONS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis", "ShaftFEMeshingOptions"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _76


__docformat__ = "restructuredtext en"
__all__ = ("ShaftFEMeshingOptions",)


Self = TypeVar("Self", bound="ShaftFEMeshingOptions")


class ShaftFEMeshingOptions(_61.FEMeshingOptions):
    """ShaftFEMeshingOptions

    This is a mastapy class.
    """

    TYPE = _SHAFT_FE_MESHING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftFEMeshingOptions")

    class _Cast_ShaftFEMeshingOptions:
        """Special nested class for casting ShaftFEMeshingOptions to subclasses."""

        def __init__(
            self: "ShaftFEMeshingOptions._Cast_ShaftFEMeshingOptions",
            parent: "ShaftFEMeshingOptions",
        ):
            self._parent = parent

        @property
        def fe_meshing_options(
            self: "ShaftFEMeshingOptions._Cast_ShaftFEMeshingOptions",
        ) -> "_61.FEMeshingOptions":
            return self._parent._cast(_61.FEMeshingOptions)

        @property
        def shaft_fe_meshing_options(
            self: "ShaftFEMeshingOptions._Cast_ShaftFEMeshingOptions",
        ) -> "ShaftFEMeshingOptions":
            return self._parent

        def __getattr__(
            self: "ShaftFEMeshingOptions._Cast_ShaftFEMeshingOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftFEMeshingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def corner_tolerance(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CornerTolerance

        if temp is None:
            return 0.0

        return temp

    @corner_tolerance.setter
    @enforce_parameter_types
    def corner_tolerance(self: Self, value: "float"):
        self.wrapped.CornerTolerance = float(value) if value is not None else 0.0

    @property
    def element_size(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ElementSize

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @element_size.setter
    @enforce_parameter_types
    def element_size(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ElementSize = value

    @property
    def meshing_diameter_for_gear(self: Self) -> "_76.MeshingDiameterForGear":
        """mastapy.nodal_analysis.MeshingDiameterForGear"""
        temp = self.wrapped.MeshingDiameterForGear

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.MeshingDiameterForGear"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._76", "MeshingDiameterForGear"
        )(value)

    @meshing_diameter_for_gear.setter
    @enforce_parameter_types
    def meshing_diameter_for_gear(self: Self, value: "_76.MeshingDiameterForGear"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.MeshingDiameterForGear"
        )
        self.wrapped.MeshingDiameterForGear = value

    @property
    def minimum_fillet_radius_to_include(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumFilletRadiusToInclude

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_fillet_radius_to_include.setter
    @enforce_parameter_types
    def minimum_fillet_radius_to_include(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumFilletRadiusToInclude = value

    @property
    def smooth_corners(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SmoothCorners

        if temp is None:
            return False

        return temp

    @smooth_corners.setter
    @enforce_parameter_types
    def smooth_corners(self: Self, value: "bool"):
        self.wrapped.SmoothCorners = bool(value) if value is not None else False

    @property
    def cast_to(self: Self) -> "ShaftFEMeshingOptions._Cast_ShaftFEMeshingOptions":
        return self._Cast_ShaftFEMeshingOptions(self)
