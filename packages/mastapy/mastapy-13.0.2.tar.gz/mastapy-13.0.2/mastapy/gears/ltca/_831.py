"""CylindricalGearFilletNodeStressResults"""

from __future__ import annotations

from typing import TypeVar

from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.gears.ltca import _840
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "CylindricalGearFilletNodeStressResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearFilletNodeStressResults",)


Self = TypeVar("Self", bound="CylindricalGearFilletNodeStressResults")


class CylindricalGearFilletNodeStressResults(_840.GearFilletNodeStressResults):
    """CylindricalGearFilletNodeStressResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FILLET_NODE_STRESS_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearFilletNodeStressResults"
    )

    class _Cast_CylindricalGearFilletNodeStressResults:
        """Special nested class for casting CylindricalGearFilletNodeStressResults to subclasses."""

        def __init__(
            self: "CylindricalGearFilletNodeStressResults._Cast_CylindricalGearFilletNodeStressResults",
            parent: "CylindricalGearFilletNodeStressResults",
        ):
            self._parent = parent

        @property
        def gear_fillet_node_stress_results(
            self: "CylindricalGearFilletNodeStressResults._Cast_CylindricalGearFilletNodeStressResults",
        ) -> "_840.GearFilletNodeStressResults":
            return self._parent._cast(_840.GearFilletNodeStressResults)

        @property
        def cylindrical_gear_fillet_node_stress_results(
            self: "CylindricalGearFilletNodeStressResults._Cast_CylindricalGearFilletNodeStressResults",
        ) -> "CylindricalGearFilletNodeStressResults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearFilletNodeStressResults._Cast_CylindricalGearFilletNodeStressResults",
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
        self: Self, instance_to_wrap: "CylindricalGearFilletNodeStressResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_along_fillet(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceAlongFillet

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width_position(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceWidthPosition

        if temp is None:
            return 0.0

        return temp

    @property
    def radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @property
    def position(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Position

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearFilletNodeStressResults._Cast_CylindricalGearFilletNodeStressResults":
        return self._Cast_CylindricalGearFilletNodeStressResults(self)
