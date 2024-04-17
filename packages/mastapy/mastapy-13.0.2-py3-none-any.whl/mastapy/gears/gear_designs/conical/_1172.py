"""KIMoSBevelHypoidSingleLoadCaseResultsData"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KI_MO_S_BEVEL_HYPOID_SINGLE_LOAD_CASE_RESULTS_DATA = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical",
    "KIMoSBevelHypoidSingleLoadCaseResultsData",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1173


__docformat__ = "restructuredtext en"
__all__ = ("KIMoSBevelHypoidSingleLoadCaseResultsData",)


Self = TypeVar("Self", bound="KIMoSBevelHypoidSingleLoadCaseResultsData")


class KIMoSBevelHypoidSingleLoadCaseResultsData(_0.APIBase):
    """KIMoSBevelHypoidSingleLoadCaseResultsData

    This is a mastapy class.
    """

    TYPE = _KI_MO_S_BEVEL_HYPOID_SINGLE_LOAD_CASE_RESULTS_DATA
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KIMoSBevelHypoidSingleLoadCaseResultsData"
    )

    class _Cast_KIMoSBevelHypoidSingleLoadCaseResultsData:
        """Special nested class for casting KIMoSBevelHypoidSingleLoadCaseResultsData to subclasses."""

        def __init__(
            self: "KIMoSBevelHypoidSingleLoadCaseResultsData._Cast_KIMoSBevelHypoidSingleLoadCaseResultsData",
            parent: "KIMoSBevelHypoidSingleLoadCaseResultsData",
        ):
            self._parent = parent

        @property
        def ki_mo_s_bevel_hypoid_single_load_case_results_data(
            self: "KIMoSBevelHypoidSingleLoadCaseResultsData._Cast_KIMoSBevelHypoidSingleLoadCaseResultsData",
        ) -> "KIMoSBevelHypoidSingleLoadCaseResultsData":
            return self._parent

        def __getattr__(
            self: "KIMoSBevelHypoidSingleLoadCaseResultsData._Cast_KIMoSBevelHypoidSingleLoadCaseResultsData",
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
        self: Self, instance_to_wrap: "KIMoSBevelHypoidSingleLoadCaseResultsData.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_mesh_stiffness_per_unit_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AverageMeshStiffnessPerUnitFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def contact_pressure_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPressureChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def contact_ratio_under_load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactRatioUnderLoad

        if temp is None:
            return 0.0

        return temp

    @property
    def efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Efficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def flash_temperature_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlashTemperatureChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def friction_coefficient_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrictionCoefficientChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def maximum_contact_pressure(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumContactPressure

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_flash_temperature(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFlashTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_friction_coefficient(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumFrictionCoefficient

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_pinion_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPinionRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_sliding_velocity(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumSlidingVelocity

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_wheel_root_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumWheelRootStress

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_te_linear_loaded(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakTELinearLoaded

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_te_linear_unloaded(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakTELinearUnloaded

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_root_stress_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRootStressChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def pressure_velocity_pv_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureVelocityPVChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def sliding_velocity_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SlidingVelocityChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def wheel_root_stress_chart(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelRootStressChart

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def single_rotation_angle_results(
        self: Self,
    ) -> "List[_1173.KIMoSBevelHypoidSingleRotationAngleResult]":
        """List[mastapy.gears.gear_designs.conical.KIMoSBevelHypoidSingleRotationAngleResult]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SingleRotationAngleResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KIMoSBevelHypoidSingleLoadCaseResultsData._Cast_KIMoSBevelHypoidSingleLoadCaseResultsData":
        return self._Cast_KIMoSBevelHypoidSingleLoadCaseResultsData(self)
