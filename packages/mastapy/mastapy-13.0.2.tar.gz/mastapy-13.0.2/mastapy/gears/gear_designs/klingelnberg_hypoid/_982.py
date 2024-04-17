"""KlingelnbergCycloPalloidHypoidGearMeshDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.klingelnberg_conical import _986
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergHypoid",
    "KlingelnbergCycloPalloidHypoidGearMeshDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _983, _981, _984
    from mastapy.gears.gear_designs.conical import _1161
    from mastapy.gears.gear_designs import _953, _952


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshDesign",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMeshDesign")


class KlingelnbergCycloPalloidHypoidGearMeshDesign(
    _986.KlingelnbergConicalGearMeshDesign
):
    """KlingelnbergCycloPalloidHypoidGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DESIGN
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshDesign to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshDesign",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_gear_mesh_design(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign",
        ) -> "_986.KlingelnbergConicalGearMeshDesign":
            return self._parent._cast(_986.KlingelnbergConicalGearMeshDesign)

        @property
        def conical_gear_mesh_design(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign",
        ) -> "_1161.ConicalGearMeshDesign":
            from mastapy.gears.gear_designs.conical import _1161

            return self._parent._cast(_1161.ConicalGearMeshDesign)

        @property
        def gear_mesh_design(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign",
        ) -> "_953.GearMeshDesign":
            from mastapy.gears.gear_designs import _953

            return self._parent._cast(_953.GearMeshDesign)

        @property
        def gear_design_component(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign",
        ) -> "_952.GearDesignComponent":
            from mastapy.gears.gear_designs import _952

            return self._parent._cast(_952.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshDesign":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshDesign.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: Self,
    ) -> "_983.KlingelnbergCycloPalloidHypoidGearSetDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears(
        self: Self,
    ) -> "List[_981.KlingelnbergCycloPalloidHypoidGearDesign]":
        """List[mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshed_gears(
        self: Self,
    ) -> "List[_984.KlingelnbergCycloPalloidHypoidMeshedGearDesign]":
        """List[mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidMeshedGearDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshedGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshDesign._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshDesign(self)
