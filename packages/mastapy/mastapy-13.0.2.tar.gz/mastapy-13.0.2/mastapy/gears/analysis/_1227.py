"""GearImplementationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationDetail"
)

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1748
    from mastapy.gears.manufacturing.cylindrical import _615
    from mastapy.gears.manufacturing.bevel import _779, _780, _781, _791, _792, _797
    from mastapy.gears.gear_designs.face import _997
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1106,
        _1107,
        _1110,
    )
    from mastapy.gears.fe_model import _1203
    from mastapy.gears.fe_model.cylindrical import _1207
    from mastapy.gears.fe_model.conical import _1210
    from mastapy.gears.analysis import _1221


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationDetail",)


Self = TypeVar("Self", bound="GearImplementationDetail")


class GearImplementationDetail(_1224.GearDesignAnalysis):
    """GearImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearImplementationDetail")

    class _Cast_GearImplementationDetail:
        """Special nested class for casting GearImplementationDetail to subclasses."""

        def __init__(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
            parent: "GearImplementationDetail",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1224.GearDesignAnalysis":
            return self._parent._cast(_1224.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1221.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1221

            return self._parent._cast(_1221.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_615.CylindricalGearManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalGearManufacturingConfig)

        @property
        def conical_gear_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_779.ConicalGearManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _779

            return self._parent._cast(_779.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_780.ConicalGearMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _780

            return self._parent._cast(_780.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_781.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _781

            return self._parent._cast(_781.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_791.ConicalPinionManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_792.ConicalPinionMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_797.ConicalWheelManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ConicalWheelManufacturingConfig)

        @property
        def face_gear_micro_geometry(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_997.FaceGearMicroGeometry":
            from mastapy.gears.gear_designs.face import _997

            return self._parent._cast(_997.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1106.CylindricalGearMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1106

            return self._parent._cast(_1106.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1107.CylindricalGearMicroGeometryBase":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107

            return self._parent._cast(_1107.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1110.CylindricalGearMicroGeometryPerTooth":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1110

            return self._parent._cast(_1110.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1203.GearFEModel":
            from mastapy.gears.fe_model import _1203

            return self._parent._cast(_1203.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1207.CylindricalGearFEModel":
            from mastapy.gears.fe_model.cylindrical import _1207

            return self._parent._cast(_1207.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1210.ConicalGearFEModel":
            from mastapy.gears.fe_model.conical import _1210

            return self._parent._cast(_1210.ConicalGearFEModel)

        @property
        def gear_implementation_detail(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "GearImplementationDetail":
            return self._parent

        def __getattr__(
            self: "GearImplementationDetail._Cast_GearImplementationDetail", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearImplementationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def user_specified_data(self: Self) -> "_1748.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearImplementationDetail._Cast_GearImplementationDetail":
        return self._Cast_GearImplementationDetail(self)
