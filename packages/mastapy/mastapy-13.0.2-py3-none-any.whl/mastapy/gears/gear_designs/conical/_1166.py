"""ConicalMeshMisalignments"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MISALIGNMENTS = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalMeshMisalignments"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshMisalignments",)


Self = TypeVar("Self", bound="ConicalMeshMisalignments")


class ConicalMeshMisalignments(_0.APIBase):
    """ConicalMeshMisalignments

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MISALIGNMENTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshMisalignments")

    class _Cast_ConicalMeshMisalignments:
        """Special nested class for casting ConicalMeshMisalignments to subclasses."""

        def __init__(
            self: "ConicalMeshMisalignments._Cast_ConicalMeshMisalignments",
            parent: "ConicalMeshMisalignments",
        ):
            self._parent = parent

        @property
        def conical_mesh_misalignments(
            self: "ConicalMeshMisalignments._Cast_ConicalMeshMisalignments",
        ) -> "ConicalMeshMisalignments":
            return self._parent

        def __getattr__(
            self: "ConicalMeshMisalignments._Cast_ConicalMeshMisalignments", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshMisalignments.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def delta_e(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaE

        if temp is None:
            return 0.0

        return temp

    @delta_e.setter
    @enforce_parameter_types
    def delta_e(self: Self, value: "float"):
        self.wrapped.DeltaE = float(value) if value is not None else 0.0

    @property
    def delta_sigma(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaSigma

        if temp is None:
            return 0.0

        return temp

    @delta_sigma.setter
    @enforce_parameter_types
    def delta_sigma(self: Self, value: "float"):
        self.wrapped.DeltaSigma = float(value) if value is not None else 0.0

    @property
    def delta_xp(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaXP

        if temp is None:
            return 0.0

        return temp

    @delta_xp.setter
    @enforce_parameter_types
    def delta_xp(self: Self, value: "float"):
        self.wrapped.DeltaXP = float(value) if value is not None else 0.0

    @property
    def delta_xw(self: Self) -> "float":
        """float"""
        temp = self.wrapped.DeltaXW

        if temp is None:
            return 0.0

        return temp

    @delta_xw.setter
    @enforce_parameter_types
    def delta_xw(self: Self, value: "float"):
        self.wrapped.DeltaXW = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshMisalignments._Cast_ConicalMeshMisalignments":
        return self._Cast_ConicalMeshMisalignments(self)
