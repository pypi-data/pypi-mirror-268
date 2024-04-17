"""CylindricalMeshLinearBacklashSpecification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.cylindrical import _1089
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_LINEAR_BACKLASH_SPECIFICATION = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical",
    "CylindricalMeshLinearBacklashSpecification",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1041, _1072


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalMeshLinearBacklashSpecification",)


Self = TypeVar("Self", bound="CylindricalMeshLinearBacklashSpecification")


class CylindricalMeshLinearBacklashSpecification(
    _1089.TolerancedValueSpecification["_1003.BacklashSpecification"]
):
    """CylindricalMeshLinearBacklashSpecification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_LINEAR_BACKLASH_SPECIFICATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalMeshLinearBacklashSpecification"
    )

    class _Cast_CylindricalMeshLinearBacklashSpecification:
        """Special nested class for casting CylindricalMeshLinearBacklashSpecification to subclasses."""

        def __init__(
            self: "CylindricalMeshLinearBacklashSpecification._Cast_CylindricalMeshLinearBacklashSpecification",
            parent: "CylindricalMeshLinearBacklashSpecification",
        ):
            self._parent = parent

        @property
        def toleranced_value_specification(
            self: "CylindricalMeshLinearBacklashSpecification._Cast_CylindricalMeshLinearBacklashSpecification",
        ) -> "_1089.TolerancedValueSpecification":
            return self._parent._cast(_1089.TolerancedValueSpecification)

        @property
        def relative_measurement_view_model(
            self: "CylindricalMeshLinearBacklashSpecification._Cast_CylindricalMeshLinearBacklashSpecification",
        ) -> "_1072.RelativeMeasurementViewModel":
            from mastapy.gears.gear_designs.cylindrical import _1072

            return self._parent._cast(_1072.RelativeMeasurementViewModel)

        @property
        def cylindrical_mesh_angular_backlash(
            self: "CylindricalMeshLinearBacklashSpecification._Cast_CylindricalMeshLinearBacklashSpecification",
        ) -> "_1041.CylindricalMeshAngularBacklash":
            from mastapy.gears.gear_designs.cylindrical import _1041

            return self._parent._cast(_1041.CylindricalMeshAngularBacklash)

        @property
        def cylindrical_mesh_linear_backlash_specification(
            self: "CylindricalMeshLinearBacklashSpecification._Cast_CylindricalMeshLinearBacklashSpecification",
        ) -> "CylindricalMeshLinearBacklashSpecification":
            return self._parent

        def __getattr__(
            self: "CylindricalMeshLinearBacklashSpecification._Cast_CylindricalMeshLinearBacklashSpecification",
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
        self: Self, instance_to_wrap: "CylindricalMeshLinearBacklashSpecification.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measurement_type(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeasurementType

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalMeshLinearBacklashSpecification._Cast_CylindricalMeshLinearBacklashSpecification":
        return self._Cast_CylindricalMeshLinearBacklashSpecification(self)
