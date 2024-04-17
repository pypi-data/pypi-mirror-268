"""KlingelnbergConicalGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs.conical import _1161
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergConical",
    "KlingelnbergConicalGearMeshDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _978
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _982
    from mastapy.gears.gear_designs import _953, _952


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalGearMeshDesign",)


Self = TypeVar("Self", bound="KlingelnbergConicalGearMeshDesign")


class KlingelnbergConicalGearMeshDesign(_1161.ConicalGearMeshDesign):
    """KlingelnbergConicalGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_MESH_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergConicalGearMeshDesign")

    class _Cast_KlingelnbergConicalGearMeshDesign:
        """Special nested class for casting KlingelnbergConicalGearMeshDesign to subclasses."""

        def __init__(
            self: "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign",
            parent: "KlingelnbergConicalGearMeshDesign",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_design(
            self: "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign",
        ) -> "_1161.ConicalGearMeshDesign":
            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
            self: "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign",
        ) -> "_978.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _978

            return self._parent._cast(
                _978.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
            self: "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign",
        ) -> "_982.KlingelnbergCycloPalloidHypoidGearMeshDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _982

            return self._parent._cast(_982.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(
            self: "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign",
        ) -> "KlingelnbergConicalGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "KlingelnbergConicalGearMeshDesign.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def application_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ApplicationFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @application_factor.setter
    @enforce_parameter_types
    def application_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ApplicationFactor = value

    @property
    def effective_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def load_distribution_factor_longitudinal(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.LoadDistributionFactorLongitudinal

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @load_distribution_factor_longitudinal.setter
    @enforce_parameter_types
    def load_distribution_factor_longitudinal(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.LoadDistributionFactorLongitudinal = value

    @property
    def net_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NetFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergConicalGearMeshDesign._Cast_KlingelnbergConicalGearMeshDesign":
        return self._Cast_KlingelnbergConicalGearMeshDesign(self)
