"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2627 import CompoundAnalysis
    from ._2628 import SingleAnalysis
    from ._2629 import AdvancedSystemDeflectionAnalysis
    from ._2630 import AdvancedSystemDeflectionSubAnalysis
    from ._2631 import AdvancedTimeSteppingAnalysisForModulation
    from ._2632 import CompoundParametricStudyToolAnalysis
    from ._2633 import CriticalSpeedAnalysis
    from ._2634 import DynamicAnalysis
    from ._2635 import DynamicModelAtAStiffnessAnalysis
    from ._2636 import DynamicModelForHarmonicAnalysis
    from ._2637 import DynamicModelForModalAnalysis
    from ._2638 import DynamicModelForStabilityAnalysis
    from ._2639 import DynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2640 import HarmonicAnalysis
    from ._2641 import HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
    from ._2642 import HarmonicAnalysisOfSingleExcitationAnalysis
    from ._2643 import ModalAnalysis
    from ._2644 import ModalAnalysisAtASpeed
    from ._2645 import ModalAnalysisAtAStiffness
    from ._2646 import ModalAnalysisForHarmonicAnalysis
    from ._2647 import MultibodyDynamicsAnalysis
    from ._2648 import ParametricStudyToolAnalysis
    from ._2649 import PowerFlowAnalysis
    from ._2650 import StabilityAnalysis
    from ._2651 import SteadyStateSynchronousResponseAnalysis
    from ._2652 import SteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2653 import SteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2654 import SystemDeflectionAnalysis
    from ._2655 import TorsionalSystemDeflectionAnalysis
    from ._2656 import AnalysisCaseVariable
    from ._2657 import ConnectionAnalysis
    from ._2658 import Context
    from ._2659 import DesignEntityAnalysis
    from ._2660 import DesignEntityGroupAnalysis
    from ._2661 import DesignEntitySingleContextAnalysis
    from ._2665 import PartAnalysis
    from ._2666 import CompoundAdvancedSystemDeflectionAnalysis
    from ._2667 import CompoundAdvancedSystemDeflectionSubAnalysis
    from ._2668 import CompoundAdvancedTimeSteppingAnalysisForModulation
    from ._2669 import CompoundCriticalSpeedAnalysis
    from ._2670 import CompoundDynamicAnalysis
    from ._2671 import CompoundDynamicModelAtAStiffnessAnalysis
    from ._2672 import CompoundDynamicModelForHarmonicAnalysis
    from ._2673 import CompoundDynamicModelForModalAnalysis
    from ._2674 import CompoundDynamicModelForStabilityAnalysis
    from ._2675 import CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis
    from ._2676 import CompoundHarmonicAnalysis
    from ._2677 import (
        CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation,
    )
    from ._2678 import CompoundHarmonicAnalysisOfSingleExcitationAnalysis
    from ._2679 import CompoundModalAnalysis
    from ._2680 import CompoundModalAnalysisAtASpeed
    from ._2681 import CompoundModalAnalysisAtAStiffness
    from ._2682 import CompoundModalAnalysisForHarmonicAnalysis
    from ._2683 import CompoundMultibodyDynamicsAnalysis
    from ._2684 import CompoundPowerFlowAnalysis
    from ._2685 import CompoundStabilityAnalysis
    from ._2686 import CompoundSteadyStateSynchronousResponseAnalysis
    from ._2687 import CompoundSteadyStateSynchronousResponseAtASpeedAnalysis
    from ._2688 import CompoundSteadyStateSynchronousResponseOnAShaftAnalysis
    from ._2689 import CompoundSystemDeflectionAnalysis
    from ._2690 import CompoundTorsionalSystemDeflectionAnalysis
    from ._2691 import TESetUpForDynamicAnalysisOptions
    from ._2692 import TimeOptions
else:
    import_structure = {
        "_2627": ["CompoundAnalysis"],
        "_2628": ["SingleAnalysis"],
        "_2629": ["AdvancedSystemDeflectionAnalysis"],
        "_2630": ["AdvancedSystemDeflectionSubAnalysis"],
        "_2631": ["AdvancedTimeSteppingAnalysisForModulation"],
        "_2632": ["CompoundParametricStudyToolAnalysis"],
        "_2633": ["CriticalSpeedAnalysis"],
        "_2634": ["DynamicAnalysis"],
        "_2635": ["DynamicModelAtAStiffnessAnalysis"],
        "_2636": ["DynamicModelForHarmonicAnalysis"],
        "_2637": ["DynamicModelForModalAnalysis"],
        "_2638": ["DynamicModelForStabilityAnalysis"],
        "_2639": ["DynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2640": ["HarmonicAnalysis"],
        "_2641": ["HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"],
        "_2642": ["HarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2643": ["ModalAnalysis"],
        "_2644": ["ModalAnalysisAtASpeed"],
        "_2645": ["ModalAnalysisAtAStiffness"],
        "_2646": ["ModalAnalysisForHarmonicAnalysis"],
        "_2647": ["MultibodyDynamicsAnalysis"],
        "_2648": ["ParametricStudyToolAnalysis"],
        "_2649": ["PowerFlowAnalysis"],
        "_2650": ["StabilityAnalysis"],
        "_2651": ["SteadyStateSynchronousResponseAnalysis"],
        "_2652": ["SteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2653": ["SteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2654": ["SystemDeflectionAnalysis"],
        "_2655": ["TorsionalSystemDeflectionAnalysis"],
        "_2656": ["AnalysisCaseVariable"],
        "_2657": ["ConnectionAnalysis"],
        "_2658": ["Context"],
        "_2659": ["DesignEntityAnalysis"],
        "_2660": ["DesignEntityGroupAnalysis"],
        "_2661": ["DesignEntitySingleContextAnalysis"],
        "_2665": ["PartAnalysis"],
        "_2666": ["CompoundAdvancedSystemDeflectionAnalysis"],
        "_2667": ["CompoundAdvancedSystemDeflectionSubAnalysis"],
        "_2668": ["CompoundAdvancedTimeSteppingAnalysisForModulation"],
        "_2669": ["CompoundCriticalSpeedAnalysis"],
        "_2670": ["CompoundDynamicAnalysis"],
        "_2671": ["CompoundDynamicModelAtAStiffnessAnalysis"],
        "_2672": ["CompoundDynamicModelForHarmonicAnalysis"],
        "_2673": ["CompoundDynamicModelForModalAnalysis"],
        "_2674": ["CompoundDynamicModelForStabilityAnalysis"],
        "_2675": ["CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis"],
        "_2676": ["CompoundHarmonicAnalysis"],
        "_2677": [
            "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_2678": ["CompoundHarmonicAnalysisOfSingleExcitationAnalysis"],
        "_2679": ["CompoundModalAnalysis"],
        "_2680": ["CompoundModalAnalysisAtASpeed"],
        "_2681": ["CompoundModalAnalysisAtAStiffness"],
        "_2682": ["CompoundModalAnalysisForHarmonicAnalysis"],
        "_2683": ["CompoundMultibodyDynamicsAnalysis"],
        "_2684": ["CompoundPowerFlowAnalysis"],
        "_2685": ["CompoundStabilityAnalysis"],
        "_2686": ["CompoundSteadyStateSynchronousResponseAnalysis"],
        "_2687": ["CompoundSteadyStateSynchronousResponseAtASpeedAnalysis"],
        "_2688": ["CompoundSteadyStateSynchronousResponseOnAShaftAnalysis"],
        "_2689": ["CompoundSystemDeflectionAnalysis"],
        "_2690": ["CompoundTorsionalSystemDeflectionAnalysis"],
        "_2691": ["TESetUpForDynamicAnalysisOptions"],
        "_2692": ["TimeOptions"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CompoundAnalysis",
    "SingleAnalysis",
    "AdvancedSystemDeflectionAnalysis",
    "AdvancedSystemDeflectionSubAnalysis",
    "AdvancedTimeSteppingAnalysisForModulation",
    "CompoundParametricStudyToolAnalysis",
    "CriticalSpeedAnalysis",
    "DynamicAnalysis",
    "DynamicModelAtAStiffnessAnalysis",
    "DynamicModelForHarmonicAnalysis",
    "DynamicModelForModalAnalysis",
    "DynamicModelForStabilityAnalysis",
    "DynamicModelForSteadyStateSynchronousResponseAnalysis",
    "HarmonicAnalysis",
    "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "HarmonicAnalysisOfSingleExcitationAnalysis",
    "ModalAnalysis",
    "ModalAnalysisAtASpeed",
    "ModalAnalysisAtAStiffness",
    "ModalAnalysisForHarmonicAnalysis",
    "MultibodyDynamicsAnalysis",
    "ParametricStudyToolAnalysis",
    "PowerFlowAnalysis",
    "StabilityAnalysis",
    "SteadyStateSynchronousResponseAnalysis",
    "SteadyStateSynchronousResponseAtASpeedAnalysis",
    "SteadyStateSynchronousResponseOnAShaftAnalysis",
    "SystemDeflectionAnalysis",
    "TorsionalSystemDeflectionAnalysis",
    "AnalysisCaseVariable",
    "ConnectionAnalysis",
    "Context",
    "DesignEntityAnalysis",
    "DesignEntityGroupAnalysis",
    "DesignEntitySingleContextAnalysis",
    "PartAnalysis",
    "CompoundAdvancedSystemDeflectionAnalysis",
    "CompoundAdvancedSystemDeflectionSubAnalysis",
    "CompoundAdvancedTimeSteppingAnalysisForModulation",
    "CompoundCriticalSpeedAnalysis",
    "CompoundDynamicAnalysis",
    "CompoundDynamicModelAtAStiffnessAnalysis",
    "CompoundDynamicModelForHarmonicAnalysis",
    "CompoundDynamicModelForModalAnalysis",
    "CompoundDynamicModelForStabilityAnalysis",
    "CompoundDynamicModelForSteadyStateSynchronousResponseAnalysis",
    "CompoundHarmonicAnalysis",
    "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "CompoundHarmonicAnalysisOfSingleExcitationAnalysis",
    "CompoundModalAnalysis",
    "CompoundModalAnalysisAtASpeed",
    "CompoundModalAnalysisAtAStiffness",
    "CompoundModalAnalysisForHarmonicAnalysis",
    "CompoundMultibodyDynamicsAnalysis",
    "CompoundPowerFlowAnalysis",
    "CompoundStabilityAnalysis",
    "CompoundSteadyStateSynchronousResponseAnalysis",
    "CompoundSteadyStateSynchronousResponseAtASpeedAnalysis",
    "CompoundSteadyStateSynchronousResponseOnAShaftAnalysis",
    "CompoundSystemDeflectionAnalysis",
    "CompoundTorsionalSystemDeflectionAnalysis",
    "TESetUpForDynamicAnalysisOptions",
    "TimeOptions",
)
