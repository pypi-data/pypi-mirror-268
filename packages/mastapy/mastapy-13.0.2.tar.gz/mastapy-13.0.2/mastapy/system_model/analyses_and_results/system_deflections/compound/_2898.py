"""CouplingHalfCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2937
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CouplingHalfCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2738
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2882,
        _2887,
        _2901,
        _2942,
        _2948,
        _2952,
        _2965,
        _2975,
        _2976,
        _2977,
        _2980,
        _2981,
        _2884,
        _2939,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7554, _7551
    from mastapy.system_model.analyses_and_results import _2659


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfCompoundSystemDeflection")


class CouplingHalfCompoundSystemDeflection(
    _2937.MountableComponentCompoundSystemDeflection
):
    """CouplingHalfCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundSystemDeflection")

    class _Cast_CouplingHalfCompoundSystemDeflection:
        """Special nested class for casting CouplingHalfCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
            parent: "CouplingHalfCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2937.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2937.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2884.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2884,
            )

            return self._parent._cast(_2884.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2939.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_7554.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7554

            return self._parent._cast(_7554.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_7551.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2659.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.DesignEntityAnalysis)

        @property
        def clutch_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2882.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ClutchHalfCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2887.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(_2887.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2901.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2901,
            )

            return self._parent._cast(_2901.CVTPulleyCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2942.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def pulley_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2948.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(_2948.PulleyCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2952.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.RollingRingCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2965.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2965,
            )

            return self._parent._cast(_2965.SpringDamperHalfCompoundSystemDeflection)

        @property
        def synchroniser_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2975.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(_2975.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2976.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2977.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2980.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2980,
            )

            return self._parent._cast(_2980.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "_2981.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(
                _2981.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def coupling_half_compound_system_deflection(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
        ) -> "CouplingHalfCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2738.CouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2738.CouplingHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundSystemDeflection._Cast_CouplingHalfCompoundSystemDeflection":
        return self._Cast_CouplingHalfCompoundSystemDeflection(self)
