"""GearMeshTEExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5762
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_TE_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "GearMeshTEExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshTEExcitationDetail",)


Self = TypeVar("Self", bound="GearMeshTEExcitationDetail")


class GearMeshTEExcitationDetail(_5762.GearMeshExcitationDetail):
    """GearMeshTEExcitationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_TE_EXCITATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshTEExcitationDetail")

    class _Cast_GearMeshTEExcitationDetail:
        """Special nested class for casting GearMeshTEExcitationDetail to subclasses."""

        def __init__(
            self: "GearMeshTEExcitationDetail._Cast_GearMeshTEExcitationDetail",
            parent: "GearMeshTEExcitationDetail",
        ):
            self._parent = parent

        @property
        def gear_mesh_excitation_detail(
            self: "GearMeshTEExcitationDetail._Cast_GearMeshTEExcitationDetail",
        ) -> "_5762.GearMeshExcitationDetail":
            return self._parent._cast(_5762.GearMeshExcitationDetail)

        @property
        def abstract_periodic_excitation_detail(
            self: "GearMeshTEExcitationDetail._Cast_GearMeshTEExcitationDetail",
        ) -> "_5687.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AbstractPeriodicExcitationDetail)

        @property
        def gear_mesh_te_excitation_detail(
            self: "GearMeshTEExcitationDetail._Cast_GearMeshTEExcitationDetail",
        ) -> "GearMeshTEExcitationDetail":
            return self._parent

        def __getattr__(
            self: "GearMeshTEExcitationDetail._Cast_GearMeshTEExcitationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshTEExcitationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshTEExcitationDetail._Cast_GearMeshTEExcitationDetail":
        return self._Cast_GearMeshTEExcitationDetail(self)
