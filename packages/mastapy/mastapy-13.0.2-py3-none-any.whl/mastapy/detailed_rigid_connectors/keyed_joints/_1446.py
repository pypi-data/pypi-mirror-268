"""KeywayJointHalfDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.detailed_rigid_connectors.interference_fits import _1453
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KEYWAY_JOINT_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.KeyedJoints", "KeywayJointHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors import _1395


__docformat__ = "restructuredtext en"
__all__ = ("KeywayJointHalfDesign",)


Self = TypeVar("Self", bound="KeywayJointHalfDesign")


class KeywayJointHalfDesign(_1453.InterferenceFitHalfDesign):
    """KeywayJointHalfDesign

    This is a mastapy class.
    """

    TYPE = _KEYWAY_JOINT_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KeywayJointHalfDesign")

    class _Cast_KeywayJointHalfDesign:
        """Special nested class for casting KeywayJointHalfDesign to subclasses."""

        def __init__(
            self: "KeywayJointHalfDesign._Cast_KeywayJointHalfDesign",
            parent: "KeywayJointHalfDesign",
        ):
            self._parent = parent

        @property
        def interference_fit_half_design(
            self: "KeywayJointHalfDesign._Cast_KeywayJointHalfDesign",
        ) -> "_1453.InterferenceFitHalfDesign":
            return self._parent._cast(_1453.InterferenceFitHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "KeywayJointHalfDesign._Cast_KeywayJointHalfDesign",
        ) -> "_1395.DetailedRigidConnectorHalfDesign":
            from mastapy.detailed_rigid_connectors import _1395

            return self._parent._cast(_1395.DetailedRigidConnectorHalfDesign)

        @property
        def keyway_joint_half_design(
            self: "KeywayJointHalfDesign._Cast_KeywayJointHalfDesign",
        ) -> "KeywayJointHalfDesign":
            return self._parent

        def __getattr__(
            self: "KeywayJointHalfDesign._Cast_KeywayJointHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "KeywayJointHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_keyway_depth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveKeywayDepth

        if temp is None:
            return 0.0

        return temp

    @property
    def hardness_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HardnessFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def is_case_hardened(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.IsCaseHardened

        if temp is None:
            return False

        return temp

    @is_case_hardened.setter
    @enforce_parameter_types
    def is_case_hardened(self: Self, value: "bool"):
        self.wrapped.IsCaseHardened = bool(value) if value is not None else False

    @property
    def keyway_chamfer_depth(self: Self) -> "float":
        """float"""
        temp = self.wrapped.KeywayChamferDepth

        if temp is None:
            return 0.0

        return temp

    @keyway_chamfer_depth.setter
    @enforce_parameter_types
    def keyway_chamfer_depth(self: Self, value: "float"):
        self.wrapped.KeywayChamferDepth = float(value) if value is not None else 0.0

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
    def support_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SupportFactor

        if temp is None:
            return 0.0

        return temp

    @support_factor.setter
    @enforce_parameter_types
    def support_factor(self: Self, value: "float"):
        self.wrapped.SupportFactor = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "KeywayJointHalfDesign._Cast_KeywayJointHalfDesign":
        return self._Cast_KeywayJointHalfDesign(self)
