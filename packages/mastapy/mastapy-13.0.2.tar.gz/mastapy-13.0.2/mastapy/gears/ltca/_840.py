"""GearFilletNodeStressResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_FILLET_NODE_STRESS_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearFilletNodeStressResults"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca import _828, _831


__docformat__ = "restructuredtext en"
__all__ = ("GearFilletNodeStressResults",)


Self = TypeVar("Self", bound="GearFilletNodeStressResults")


class GearFilletNodeStressResults(_0.APIBase):
    """GearFilletNodeStressResults

    This is a mastapy class.
    """

    TYPE = _GEAR_FILLET_NODE_STRESS_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearFilletNodeStressResults")

    class _Cast_GearFilletNodeStressResults:
        """Special nested class for casting GearFilletNodeStressResults to subclasses."""

        def __init__(
            self: "GearFilletNodeStressResults._Cast_GearFilletNodeStressResults",
            parent: "GearFilletNodeStressResults",
        ):
            self._parent = parent

        @property
        def conical_gear_fillet_stress_results(
            self: "GearFilletNodeStressResults._Cast_GearFilletNodeStressResults",
        ) -> "_828.ConicalGearFilletStressResults":
            from mastapy.gears.ltca import _828

            return self._parent._cast(_828.ConicalGearFilletStressResults)

        @property
        def cylindrical_gear_fillet_node_stress_results(
            self: "GearFilletNodeStressResults._Cast_GearFilletNodeStressResults",
        ) -> "_831.CylindricalGearFilletNodeStressResults":
            from mastapy.gears.ltca import _831

            return self._parent._cast(_831.CylindricalGearFilletNodeStressResults)

        @property
        def gear_fillet_node_stress_results(
            self: "GearFilletNodeStressResults._Cast_GearFilletNodeStressResults",
        ) -> "GearFilletNodeStressResults":
            return self._parent

        def __getattr__(
            self: "GearFilletNodeStressResults._Cast_GearFilletNodeStressResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearFilletNodeStressResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fillet_column_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilletColumnIndex

        if temp is None:
            return 0

        return temp

    @property
    def fillet_row_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FilletRowIndex

        if temp is None:
            return 0

        return temp

    @property
    def first_principal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FirstPrincipalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_tensile_principal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTensilePrincipalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def second_principal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SecondPrincipalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def stress_intensity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressIntensity

        if temp is None:
            return 0.0

        return temp

    @property
    def third_principal_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ThirdPrincipalStress

        if temp is None:
            return 0.0

        return temp

    @property
    def von_mises_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VonMisesStress

        if temp is None:
            return 0.0

        return temp

    @property
    def x_component(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XComponent

        if temp is None:
            return 0.0

        return temp

    @property
    def xy_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XYShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def xz_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.XZShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def y_component(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YComponent

        if temp is None:
            return 0.0

        return temp

    @property
    def yz_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.YZShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def z_component(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZComponent

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GearFilletNodeStressResults._Cast_GearFilletNodeStressResults":
        return self._Cast_GearFilletNodeStressResults(self)
