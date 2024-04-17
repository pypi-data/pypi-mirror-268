"""CylindricalGearToothFatigueFractureResultsN1457"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS_N1457 = python_net_import(
    "SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336",
    "CylindricalGearToothFatigueFractureResultsN1457",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1872
    from mastapy.gears.rating.cylindrical.iso6336 import _533, _530


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearToothFatigueFractureResultsN1457",)


Self = TypeVar("Self", bound="CylindricalGearToothFatigueFractureResultsN1457")


class CylindricalGearToothFatigueFractureResultsN1457(_0.APIBase):
    """CylindricalGearToothFatigueFractureResultsN1457

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS_N1457
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearToothFatigueFractureResultsN1457"
    )

    class _Cast_CylindricalGearToothFatigueFractureResultsN1457:
        """Special nested class for casting CylindricalGearToothFatigueFractureResultsN1457 to subclasses."""

        def __init__(
            self: "CylindricalGearToothFatigueFractureResultsN1457._Cast_CylindricalGearToothFatigueFractureResultsN1457",
            parent: "CylindricalGearToothFatigueFractureResultsN1457",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_tooth_fatigue_fracture_results_n1457(
            self: "CylindricalGearToothFatigueFractureResultsN1457._Cast_CylindricalGearToothFatigueFractureResultsN1457",
        ) -> "CylindricalGearToothFatigueFractureResultsN1457":
            return self._parent

        def __getattr__(
            self: "CylindricalGearToothFatigueFractureResultsN1457._Cast_CylindricalGearToothFatigueFractureResultsN1457",
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
        instance_to_wrap: "CylindricalGearToothFatigueFractureResultsN1457.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fatigue_damage_chart(self: Self) -> "_1872.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FatigueDamageChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def maximum_fatigue_damage(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFatigueDamage

        if temp is None:
            return 0.0

        return temp

    @property
    def critical_section(self: Self) -> "_533.ToothFlankFractureAnalysisRowN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisRowN1457

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
    ) -> "_533.ToothFlankFractureAnalysisRowN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisRowN1457

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
    ) -> "_530.ToothFlankFractureAnalysisContactPointN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointN1457

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
    ) -> "_530.ToothFlankFractureAnalysisContactPointN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointN1457

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
    ) -> "_530.ToothFlankFractureAnalysisContactPointN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointN1457

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
    ) -> "_530.ToothFlankFractureAnalysisContactPointN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointN1457

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
    ) -> "_530.ToothFlankFractureAnalysisContactPointN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointN1457

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
    ) -> "_530.ToothFlankFractureAnalysisContactPointN1457":
        """mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointN1457

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshContactPointESection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def analysis_rows(self: Self) -> "List[_533.ToothFlankFractureAnalysisRowN1457]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisRowN1457]

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
    def contact_points(
        self: Self,
    ) -> "List[_530.ToothFlankFractureAnalysisContactPointN1457]":
        """List[mastapy.gears.rating.cylindrical.iso6336.ToothFlankFractureAnalysisContactPointN1457]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearToothFatigueFractureResultsN1457._Cast_CylindricalGearToothFatigueFractureResultsN1457":
        return self._Cast_CylindricalGearToothFatigueFractureResultsN1457(self)
