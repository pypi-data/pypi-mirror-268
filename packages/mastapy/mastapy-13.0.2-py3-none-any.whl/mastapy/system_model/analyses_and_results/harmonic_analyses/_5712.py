"""ComplianceAndForceData"""

from __future__ import annotations

from typing import TypeVar, List

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPLIANCE_AND_FORCE_DATA = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ComplianceAndForceData",
)


__docformat__ = "restructuredtext en"
__all__ = ("ComplianceAndForceData",)


Self = TypeVar("Self", bound="ComplianceAndForceData")


class ComplianceAndForceData(_0.APIBase):
    """ComplianceAndForceData

    This is a mastapy class.
    """

    TYPE = _COMPLIANCE_AND_FORCE_DATA
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComplianceAndForceData")

    class _Cast_ComplianceAndForceData:
        """Special nested class for casting ComplianceAndForceData to subclasses."""

        def __init__(
            self: "ComplianceAndForceData._Cast_ComplianceAndForceData",
            parent: "ComplianceAndForceData",
        ):
            self._parent = parent

        @property
        def compliance_and_force_data(
            self: "ComplianceAndForceData._Cast_ComplianceAndForceData",
        ) -> "ComplianceAndForceData":
            return self._parent

        def __getattr__(
            self: "ComplianceAndForceData._Cast_ComplianceAndForceData", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComplianceAndForceData.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequencies_for_compliances(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequenciesForCompliances

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def frequencies_for_mesh_forces(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequenciesForMeshForces

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)

        if value is None:
            return None

        return value

    @property
    def gear_a_compliance(self: Self) -> "List[complex]":
        """List[complex]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearACompliance

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_b_compliance(self: Self) -> "List[complex]":
        """List[complex]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBCompliance

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex_list(temp)

        if value is None:
            return None

        return value

    @property
    def mesh_forces_per_unit_te(self: Self) -> "List[complex]":
        """List[complex]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshForcesPerUnitTE

        if temp is None:
            return None

        value = conversion.pn_to_mp_complex_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ComplianceAndForceData._Cast_ComplianceAndForceData":
        return self._Cast_ComplianceAndForceData(self)
