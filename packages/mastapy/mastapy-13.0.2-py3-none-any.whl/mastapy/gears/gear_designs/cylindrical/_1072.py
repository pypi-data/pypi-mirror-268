"""RelativeMeasurementViewModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RELATIVE_MEASUREMENT_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Cylindrical", "RelativeMeasurementViewModel"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1041, _1044, _1089
    from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
        _1097,
        _1098,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RelativeMeasurementViewModel",)


Self = TypeVar("Self", bound="RelativeMeasurementViewModel")
T = TypeVar("T")


class RelativeMeasurementViewModel(_0.APIBase, Generic[T]):
    """RelativeMeasurementViewModel

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _RELATIVE_MEASUREMENT_VIEW_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RelativeMeasurementViewModel")

    class _Cast_RelativeMeasurementViewModel:
        """Special nested class for casting RelativeMeasurementViewModel to subclasses."""

        def __init__(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
            parent: "RelativeMeasurementViewModel",
        ):
            self._parent = parent

        @property
        def cylindrical_mesh_angular_backlash(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ) -> "_1041.CylindricalMeshAngularBacklash":
            from mastapy.gears.gear_designs.cylindrical import _1041

            return self._parent._cast(_1041.CylindricalMeshAngularBacklash)

        @property
        def cylindrical_mesh_linear_backlash_specification(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ) -> "_1044.CylindricalMeshLinearBacklashSpecification":
            from mastapy.gears.gear_designs.cylindrical import _1044

            return self._parent._cast(_1044.CylindricalMeshLinearBacklashSpecification)

        @property
        def toleranced_value_specification(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ) -> "_1089.TolerancedValueSpecification":
            from mastapy.gears.gear_designs.cylindrical import _1089

            return self._parent._cast(_1089.TolerancedValueSpecification)

        @property
        def nominal_value_specification(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ) -> "_1097.NominalValueSpecification":
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
                _1097,
            )

            return self._parent._cast(_1097.NominalValueSpecification)

        @property
        def no_value_specification(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ) -> "_1098.NoValueSpecification":
            from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import (
                _1098,
            )

            return self._parent._cast(_1098.NoValueSpecification)

        @property
        def relative_measurement_view_model(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
        ) -> "RelativeMeasurementViewModel":
            return self._parent

        def __getattr__(
            self: "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RelativeMeasurementViewModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "RelativeMeasurementViewModel._Cast_RelativeMeasurementViewModel":
        return self._Cast_RelativeMeasurementViewModel(self)
