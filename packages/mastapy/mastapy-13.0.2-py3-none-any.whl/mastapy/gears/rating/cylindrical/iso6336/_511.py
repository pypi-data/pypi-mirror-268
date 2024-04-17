"""CylindricalGearToothFatigueFractureResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "CylindricalGearToothFatigueFractureResults",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.cylindrical.iso6336 import _527


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearToothFatigueFractureResults",)


Self = TypeVar("Self", bound="CylindricalGearToothFatigueFractureResults")


class CylindricalGearToothFatigueFractureResults(_0.APIBase):
    """CylindricalGearToothFatigueFractureResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearToothFatigueFractureResults"
    )

    class _Cast_CylindricalGearToothFatigueFractureResults:
        """Special nested class for casting CylindricalGearToothFatigueFractureResults to subclasses."""

        def __init__(
            self: "CylindricalGearToothFatigueFractureResults._Cast_CylindricalGearToothFatigueFractureResults",
            parent: "CylindricalGearToothFatigueFractureResults",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_tooth_fatigue_fracture_results(
            self: "CylindricalGearToothFatigueFractureResults._Cast_CylindricalGearToothFatigueFractureResults",
        ) -> "CylindricalGearToothFatigueFractureResults":
            return self._parent

        def __getattr__(
            self: "CylindricalGearToothFatigueFractureResults._Cast_CylindricalGearToothFatigueFractureResults",
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
        self: Self, instance_to_wrap: "CylindricalGearToothFatigueFractureResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_material_exposure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumMaterialExposure

        if temp is None:
            return 0.0

        return temp

    @property
    def witzigs_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WitzigsSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def critical_section(self: Self) -> "_527.ToothFlankFractureAnalysisContactPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_contact_point_a_section(
        self: Self,
    ) -> "_527.ToothFlankFractureAnalysisContactPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshContactPointASection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_contact_point_ab_section(
        self: Self,
    ) -> "_527.ToothFlankFractureAnalysisContactPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshContactPointABSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_contact_point_b_section(
        self: Self,
    ) -> "_527.ToothFlankFractureAnalysisContactPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshContactPointBSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_contact_point_c_section(
        self: Self,
    ) -> "_527.ToothFlankFractureAnalysisContactPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshContactPointCSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_contact_point_d_section(
        self: Self,
    ) -> "_527.ToothFlankFractureAnalysisContactPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshContactPointDSection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_contact_point_de_section(
        self: Self,
    ) -> "_527.ToothFlankFractureAnalysisContactPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshContactPointDESection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_contact_point_e_section(
        self: Self,
    ) -> "_527.ToothFlankFractureAnalysisContactPoint":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshContactPointESection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def analysis_rows(
        self: Self,
    ) -> "List[_527.ToothFlankFractureAnalysisContactPoint]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPoint]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AnalysisRows

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearToothFatigueFractureResults._Cast_CylindricalGearToothFatigueFractureResults":
        return self._Cast_CylindricalGearToothFatigueFractureResults(self)
