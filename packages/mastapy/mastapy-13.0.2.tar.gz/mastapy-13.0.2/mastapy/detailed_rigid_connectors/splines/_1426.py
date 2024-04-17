"""StandardSplineHalfDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1421
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STANDARD_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "StandardSplineHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1399, _1403, _1406, _1414
    from mastapy.detailed_rigid_connectors import _1395


__docformat__ = "restructuredtext en"
__all__ = ("StandardSplineHalfDesign",)


Self = TypeVar("Self", bound="StandardSplineHalfDesign")


class StandardSplineHalfDesign(_1421.SplineHalfDesign):
    """StandardSplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _STANDARD_SPLINE_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StandardSplineHalfDesign")

    class _Cast_StandardSplineHalfDesign:
        """Special nested class for casting StandardSplineHalfDesign to subclasses."""

        def __init__(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
            parent: "StandardSplineHalfDesign",
        ):
            self._parent = parent

        @property
        def spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1421.SplineHalfDesign":
            return self._parent._cast(_1421.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1395.DetailedRigidConnectorHalfDesign":
            from mastapy.detailed_rigid_connectors import _1395

            return self._parent._cast(_1395.DetailedRigidConnectorHalfDesign)

        @property
        def din5480_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1399.DIN5480SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1399

            return self._parent._cast(_1399.DIN5480SplineHalfDesign)

        @property
        def gbt3478_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1403.GBT3478SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1403

            return self._parent._cast(_1403.GBT3478SplineHalfDesign)

        @property
        def iso4156_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1406.ISO4156SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1406

            return self._parent._cast(_1406.ISO4156SplineHalfDesign)

        @property
        def sae_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "_1414.SAESplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1414

            return self._parent._cast(_1414.SAESplineHalfDesign)

        @property
        def standard_spline_half_design(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign",
        ) -> "StandardSplineHalfDesign":
            return self._parent

        def __getattr__(
            self: "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StandardSplineHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StandardSplineHalfDesign._Cast_StandardSplineHalfDesign":
        return self._Cast_StandardSplineHalfDesign(self)
