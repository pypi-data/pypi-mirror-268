"""GearSetLoadCaseBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.analysis import _1232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_CASE_BASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase", "GearSetLoadCaseBase"
)

if TYPE_CHECKING:
    from mastapy.gears.load_case.worm import _880
    from mastapy.gears.load_case.face import _883
    from mastapy.gears.load_case.cylindrical import _886
    from mastapy.gears.load_case.conical import _889
    from mastapy.gears.load_case.concept import _892
    from mastapy.gears.load_case.bevel import _896
    from mastapy.gears.analysis import _1223


__docformat__ = "restructuredtext en"
__all__ = ("GearSetLoadCaseBase",)


Self = TypeVar("Self", bound="GearSetLoadCaseBase")


class GearSetLoadCaseBase(_1232.GearSetDesignAnalysis):
    """GearSetLoadCaseBase

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_CASE_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetLoadCaseBase")

    class _Cast_GearSetLoadCaseBase:
        """Special nested class for casting GearSetLoadCaseBase to subclasses."""

        def __init__(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
            parent: "GearSetLoadCaseBase",
        ):
            self._parent = parent

        @property
        def gear_set_design_analysis(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "_1232.GearSetDesignAnalysis":
            return self._parent._cast(_1232.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "_1223.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.AbstractGearSetAnalysis)

        @property
        def worm_gear_set_load_case(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "_880.WormGearSetLoadCase":
            from mastapy.gears.load_case.worm import _880

            return self._parent._cast(_880.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "_883.FaceGearSetLoadCase":
            from mastapy.gears.load_case.face import _883

            return self._parent._cast(_883.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "_886.CylindricalGearSetLoadCase":
            from mastapy.gears.load_case.cylindrical import _886

            return self._parent._cast(_886.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "_889.ConicalGearSetLoadCase":
            from mastapy.gears.load_case.conical import _889

            return self._parent._cast(_889.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "_892.ConceptGearSetLoadCase":
            from mastapy.gears.load_case.concept import _892

            return self._parent._cast(_892.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "_896.BevelSetLoadCase":
            from mastapy.gears.load_case.bevel import _896

            return self._parent._cast(_896.BevelSetLoadCase)

        @property
        def gear_set_load_case_base(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase",
        ) -> "GearSetLoadCaseBase":
            return self._parent

        def __getattr__(
            self: "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetLoadCaseBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def unit_duration(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UnitDuration

        if temp is None:
            return 0.0

        return temp

    @unit_duration.setter
    @enforce_parameter_types
    def unit_duration(self: Self, value: "float"):
        self.wrapped.UnitDuration = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "GearSetLoadCaseBase._Cast_GearSetLoadCaseBase":
        return self._Cast_GearSetLoadCaseBase(self)
