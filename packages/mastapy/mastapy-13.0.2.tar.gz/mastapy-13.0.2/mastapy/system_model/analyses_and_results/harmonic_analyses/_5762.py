"""GearMeshExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "GearMeshExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2767
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5712,
        _5764,
        _5765,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshExcitationDetail",)


Self = TypeVar("Self", bound="GearMeshExcitationDetail")


class GearMeshExcitationDetail(_5687.AbstractPeriodicExcitationDetail):
    """GearMeshExcitationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshExcitationDetail")

    class _Cast_GearMeshExcitationDetail:
        """Special nested class for casting GearMeshExcitationDetail to subclasses."""

        def __init__(
            self: "GearMeshExcitationDetail._Cast_GearMeshExcitationDetail",
            parent: "GearMeshExcitationDetail",
        ):
            self._parent = parent

        @property
        def abstract_periodic_excitation_detail(
            self: "GearMeshExcitationDetail._Cast_GearMeshExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(
            self: "GearMeshExcitationDetail._Cast_GearMeshExcitationDetail",
        ) -> "_5764.GearMeshMisalignmentExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5764,
            )

            return self._parent._cast(_5764.GearMeshMisalignmentExcitationDetail)

        @property
        def gear_mesh_te_excitation_detail(
            self: "GearMeshExcitationDetail._Cast_GearMeshExcitationDetail",
        ) -> "_5765.GearMeshTEExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5765,
            )

            return self._parent._cast(_5765.GearMeshTEExcitationDetail)

        @property
        def gear_mesh_excitation_detail(
            self: "GearMeshExcitationDetail._Cast_GearMeshExcitationDetail",
        ) -> "GearMeshExcitationDetail":
            return self._parent

        def __getattr__(
            self: "GearMeshExcitationDetail._Cast_GearMeshExcitationDetail", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshExcitationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh(self: Self) -> "_2767.GearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_compliance_and_force_data(self: Self) -> "_5712.ComplianceAndForceData":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ComplianceAndForceData"""
        method_result = self.wrapped.GetComplianceAndForceData()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshExcitationDetail._Cast_GearMeshExcitationDetail":
        return self._Cast_GearMeshExcitationDetail(self)
