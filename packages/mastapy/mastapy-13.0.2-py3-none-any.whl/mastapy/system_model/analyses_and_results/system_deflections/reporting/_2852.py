"""GearInMeshDeflectionResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IN_MESH_DEFLECTION_RESULTS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Reporting",
    "GearInMeshDeflectionResults",
)


__docformat__ = "restructuredtext en"
__all__ = ("GearInMeshDeflectionResults",)


Self = TypeVar("Self", bound="GearInMeshDeflectionResults")


class GearInMeshDeflectionResults(_0.APIBase):
    """GearInMeshDeflectionResults

    This is a mastapy class.
    """

    TYPE = _GEAR_IN_MESH_DEFLECTION_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearInMeshDeflectionResults")

    class _Cast_GearInMeshDeflectionResults:
        """Special nested class for casting GearInMeshDeflectionResults to subclasses."""

        def __init__(
            self: "GearInMeshDeflectionResults._Cast_GearInMeshDeflectionResults",
            parent: "GearInMeshDeflectionResults",
        ):
            self._parent = parent

        @property
        def gear_in_mesh_deflection_results(
            self: "GearInMeshDeflectionResults._Cast_GearInMeshDeflectionResults",
        ) -> "GearInMeshDeflectionResults":
            return self._parent

        def __getattr__(
            self: "GearInMeshDeflectionResults._Cast_GearInMeshDeflectionResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearInMeshDeflectionResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def microgeometry(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Microgeometry

        if temp is None:
            return 0.0

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
    def transverse_deflection(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseDeflection

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_deflection_with_microgeometry(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TransverseDeflectionWithMicrogeometry

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GearInMeshDeflectionResults._Cast_GearInMeshDeflectionResults":
        return self._Cast_GearInMeshDeflectionResults(self)
