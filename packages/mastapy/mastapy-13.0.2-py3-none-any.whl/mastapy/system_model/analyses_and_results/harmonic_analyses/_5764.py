"""GearMeshMisalignmentExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5762
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_MISALIGNMENT_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "GearMeshMisalignmentExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshMisalignmentExcitationDetail",)


Self = TypeVar("Self", bound="GearMeshMisalignmentExcitationDetail")


class GearMeshMisalignmentExcitationDetail(_5762.GearMeshExcitationDetail):
    """GearMeshMisalignmentExcitationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_MISALIGNMENT_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshMisalignmentExcitationDetail")

    class _Cast_GearMeshMisalignmentExcitationDetail:
        """Special nested class for casting GearMeshMisalignmentExcitationDetail to subclasses."""

        def __init__(
            self: "GearMeshMisalignmentExcitationDetail._Cast_GearMeshMisalignmentExcitationDetail",
            parent: "GearMeshMisalignmentExcitationDetail",
        ):
            self._parent = parent

        @property
        def gear_mesh_excitation_detail(
            self: "GearMeshMisalignmentExcitationDetail._Cast_GearMeshMisalignmentExcitationDetail",
        ) -> "_5762.GearMeshExcitationDetail":
            return self._parent._cast(_5762.GearMeshExcitationDetail)

        @property
        def abstract_periodic_excitation_detail(
            self: "GearMeshMisalignmentExcitationDetail._Cast_GearMeshMisalignmentExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def gear_mesh_misalignment_excitation_detail(
            self: "GearMeshMisalignmentExcitationDetail._Cast_GearMeshMisalignmentExcitationDetail",
        ) -> "GearMeshMisalignmentExcitationDetail":
            return self._parent

        def __getattr__(
            self: "GearMeshMisalignmentExcitationDetail._Cast_GearMeshMisalignmentExcitationDetail",
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
        self: Self, instance_to_wrap: "GearMeshMisalignmentExcitationDetail.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshMisalignmentExcitationDetail._Cast_GearMeshMisalignmentExcitationDetail":
        return self._Cast_GearMeshMisalignmentExcitationDetail(self)
