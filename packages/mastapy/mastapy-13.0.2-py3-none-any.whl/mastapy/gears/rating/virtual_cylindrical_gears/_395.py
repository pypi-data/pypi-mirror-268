"""VirtualCylindricalGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears", "VirtualCylindricalGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.virtual_cylindrical_gears import (
        _392,
        _382,
        _383,
        _385,
        _386,
        _390,
        _396,
        _397,
    )


__docformat__ = "restructuredtext en"
__all__ = ("VirtualCylindricalGearSet",)


Self = TypeVar("Self", bound="VirtualCylindricalGearSet")
T = TypeVar("T", bound="_392.VirtualCylindricalGearBasic")


class VirtualCylindricalGearSet(_0.APIBase, Generic[T]):
    """VirtualCylindricalGearSet

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualCylindricalGearSet")

    class _Cast_VirtualCylindricalGearSet:
        """Special nested class for casting VirtualCylindricalGearSet to subclasses."""

        def __init__(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
            parent: "VirtualCylindricalGearSet",
        ):
            self._parent = parent

        @property
        def bevel_virtual_cylindrical_gear_set_iso10300_method_b1(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
        ) -> "_382.BevelVirtualCylindricalGearSetISO10300MethodB1":
            from mastapy.gears.rating.virtual_cylindrical_gears import _382

            return self._parent._cast(
                _382.BevelVirtualCylindricalGearSetISO10300MethodB1
            )

        @property
        def bevel_virtual_cylindrical_gear_set_iso10300_method_b2(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
        ) -> "_383.BevelVirtualCylindricalGearSetISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _383

            return self._parent._cast(
                _383.BevelVirtualCylindricalGearSetISO10300MethodB2
            )

        @property
        def hypoid_virtual_cylindrical_gear_set_iso10300_method_b1(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
        ) -> "_385.HypoidVirtualCylindricalGearSetISO10300MethodB1":
            from mastapy.gears.rating.virtual_cylindrical_gears import _385

            return self._parent._cast(
                _385.HypoidVirtualCylindricalGearSetISO10300MethodB1
            )

        @property
        def hypoid_virtual_cylindrical_gear_set_iso10300_method_b2(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
        ) -> "_386.HypoidVirtualCylindricalGearSetISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _386

            return self._parent._cast(
                _386.HypoidVirtualCylindricalGearSetISO10300MethodB2
            )

        @property
        def klingelnberg_virtual_cylindrical_gear_set(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
        ) -> "_390.KlingelnbergVirtualCylindricalGearSet":
            from mastapy.gears.rating.virtual_cylindrical_gears import _390

            return self._parent._cast(_390.KlingelnbergVirtualCylindricalGearSet)

        @property
        def virtual_cylindrical_gear_set_iso10300_method_b1(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
        ) -> "_396.VirtualCylindricalGearSetISO10300MethodB1":
            from mastapy.gears.rating.virtual_cylindrical_gears import _396

            return self._parent._cast(_396.VirtualCylindricalGearSetISO10300MethodB1)

        @property
        def virtual_cylindrical_gear_set_iso10300_method_b2(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
        ) -> "_397.VirtualCylindricalGearSetISO10300MethodB2":
            from mastapy.gears.rating.virtual_cylindrical_gears import _397

            return self._parent._cast(_397.VirtualCylindricalGearSetISO10300MethodB2)

        @property
        def virtual_cylindrical_gear_set(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet",
        ) -> "VirtualCylindricalGearSet":
            return self._parent

        def __getattr__(
            self: "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualCylindricalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_face_width_of_virtual_cylindrical_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveFaceWidthOfVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def face_contact_ratio_transverse_for_virtual_cylindrical_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceContactRatioTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_of_virtual_cylindrical_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthOfVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio_normal_for_virtual_cylindrical_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseContactRatioNormalForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_contact_ratio_for_virtual_cylindrical_gears(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseContactRatioForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_contact_ratio_transverse_for_virtual_cylindrical_gears(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualContactRatioTransverseForVirtualCylindricalGears

        if temp is None:
            return 0.0

        return temp

    @property
    def virtual_pinion(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def virtual_wheel(self: Self) -> "T":
        """T

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def virtual_cylindrical_gears(self: Self) -> "List[T]":
        """List[T]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VirtualCylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualCylindricalGearSet._Cast_VirtualCylindricalGearSet":
        return self._Cast_VirtualCylindricalGearSet(self)
