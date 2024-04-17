"""KIMoSBevelHypoidSingleRotationAngleResult"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KI_MO_S_BEVEL_HYPOID_SINGLE_ROTATION_ANGLE_RESULT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical",
    "KIMoSBevelHypoidSingleRotationAngleResult",
)


__docformat__ = "restructuredtext en"
__all__ = ("KIMoSBevelHypoidSingleRotationAngleResult",)


Self = TypeVar("Self", bound="KIMoSBevelHypoidSingleRotationAngleResult")


class KIMoSBevelHypoidSingleRotationAngleResult(_0.APIBase):
    """KIMoSBevelHypoidSingleRotationAngleResult

    This is a mastapy class.
    """

    TYPE = _KI_MO_S_BEVEL_HYPOID_SINGLE_ROTATION_ANGLE_RESULT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KIMoSBevelHypoidSingleRotationAngleResult"
    )

    class _Cast_KIMoSBevelHypoidSingleRotationAngleResult:
        """Special nested class for casting KIMoSBevelHypoidSingleRotationAngleResult to subclasses."""

        def __init__(
            self: "KIMoSBevelHypoidSingleRotationAngleResult._Cast_KIMoSBevelHypoidSingleRotationAngleResult",
            parent: "KIMoSBevelHypoidSingleRotationAngleResult",
        ):
            self._parent = parent

        @property
        def ki_mo_s_bevel_hypoid_single_rotation_angle_result(
            self: "KIMoSBevelHypoidSingleRotationAngleResult._Cast_KIMoSBevelHypoidSingleRotationAngleResult",
        ) -> "KIMoSBevelHypoidSingleRotationAngleResult":
            return self._parent

        def __getattr__(
            self: "KIMoSBevelHypoidSingleRotationAngleResult._Cast_KIMoSBevelHypoidSingleRotationAngleResult",
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
        self: Self, instance_to_wrap: "KIMoSBevelHypoidSingleRotationAngleResult.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def linear_transmission_error_loaded(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearTransmissionErrorLoaded

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_transmission_error_unloaded(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearTransmissionErrorUnloaded

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pinion_root_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumPinionRootStress

        if temp is None:
            return 0.0

        return temp

    @maximum_pinion_root_stress.setter
    @enforce_parameter_types
    def maximum_pinion_root_stress(self: Self, value: "float"):
        self.wrapped.MaximumPinionRootStress = (
            float(value) if value is not None else 0.0
        )

    @property
    def maximum_wheel_root_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumWheelRootStress

        if temp is None:
            return 0.0

        return temp

    @maximum_wheel_root_stress.setter
    @enforce_parameter_types
    def maximum_wheel_root_stress(self: Self, value: "float"):
        self.wrapped.MaximumWheelRootStress = float(value) if value is not None else 0.0

    @property
    def mesh_stiffness_per_unit_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshStiffnessPerUnitFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_rotation_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRotationAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "KIMoSBevelHypoidSingleRotationAngleResult._Cast_KIMoSBevelHypoidSingleRotationAngleResult":
        return self._Cast_KIMoSBevelHypoidSingleRotationAngleResult(self)
