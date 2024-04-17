"""ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_MISALIGNMENTS_WITH_RESPECT_TO_CROSS_POINT_CALCULATOR = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
        "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    )
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1166


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",)


Self = TypeVar(
    "Self", bound="ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator"
)


class ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator(_0.APIBase):
    """ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_MISALIGNMENTS_WITH_RESPECT_TO_CROSS_POINT_CALCULATOR
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
    )

    class _Cast_ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator:
        """Special nested class for casting ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator to subclasses."""

        def __init__(
            self: "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator._Cast_ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
            parent: "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_misalignments_with_respect_to_cross_point_calculator(
            self: "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator._Cast_ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
        ) -> "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator._Cast_ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator",
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
        instance_to_wrap: "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def misalignments_pinion(self: Self) -> "_1166.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_total(self: Self) -> "_1166.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_wheel(self: Self) -> "_1166.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator._Cast_ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator":
        return self._Cast_ConicalGearMeshMisalignmentsWithRespectToCrossPointCalculator(
            self
        )
