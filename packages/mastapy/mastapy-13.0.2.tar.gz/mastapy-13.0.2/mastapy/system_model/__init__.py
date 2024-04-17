"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._2207 import Design
    from ._2208 import ComponentDampingOption
    from ._2209 import ConceptCouplingSpeedRatioSpecificationMethod
    from ._2210 import DesignEntity
    from ._2211 import DesignEntityId
    from ._2212 import DesignSettings
    from ._2213 import DutyCycleImporter
    from ._2214 import DutyCycleImporterDesignEntityMatch
    from ._2215 import ElectricMachineGroup
    from ._2216 import ExternalFullFELoader
    from ._2217 import HypoidWindUpRemovalMethod
    from ._2218 import IncludeDutyCycleOption
    from ._2219 import MASTASettings
    from ._2220 import MemorySummary
    from ._2221 import MeshStiffnessModel
    from ._2222 import PlanetPinManufacturingErrorsCoordinateSystem
    from ._2223 import PowerLoadDragTorqueSpecificationMethod
    from ._2224 import PowerLoadInputTorqueSpecificationMethod
    from ._2225 import PowerLoadPIDControlSpeedInputType
    from ._2226 import PowerLoadType
    from ._2227 import RelativeComponentAlignment
    from ._2228 import RelativeOffsetOption
    from ._2229 import SystemReporting
    from ._2230 import ThermalExpansionOptionForGroundedNodes
    from ._2231 import TransmissionTemperatureSet
else:
    import_structure = {
        "_2207": ["Design"],
        "_2208": ["ComponentDampingOption"],
        "_2209": ["ConceptCouplingSpeedRatioSpecificationMethod"],
        "_2210": ["DesignEntity"],
        "_2211": ["DesignEntityId"],
        "_2212": ["DesignSettings"],
        "_2213": ["DutyCycleImporter"],
        "_2214": ["DutyCycleImporterDesignEntityMatch"],
        "_2215": ["ElectricMachineGroup"],
        "_2216": ["ExternalFullFELoader"],
        "_2217": ["HypoidWindUpRemovalMethod"],
        "_2218": ["IncludeDutyCycleOption"],
        "_2219": ["MASTASettings"],
        "_2220": ["MemorySummary"],
        "_2221": ["MeshStiffnessModel"],
        "_2222": ["PlanetPinManufacturingErrorsCoordinateSystem"],
        "_2223": ["PowerLoadDragTorqueSpecificationMethod"],
        "_2224": ["PowerLoadInputTorqueSpecificationMethod"],
        "_2225": ["PowerLoadPIDControlSpeedInputType"],
        "_2226": ["PowerLoadType"],
        "_2227": ["RelativeComponentAlignment"],
        "_2228": ["RelativeOffsetOption"],
        "_2229": ["SystemReporting"],
        "_2230": ["ThermalExpansionOptionForGroundedNodes"],
        "_2231": ["TransmissionTemperatureSet"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Design",
    "ComponentDampingOption",
    "ConceptCouplingSpeedRatioSpecificationMethod",
    "DesignEntity",
    "DesignEntityId",
    "DesignSettings",
    "DutyCycleImporter",
    "DutyCycleImporterDesignEntityMatch",
    "ElectricMachineGroup",
    "ExternalFullFELoader",
    "HypoidWindUpRemovalMethod",
    "IncludeDutyCycleOption",
    "MASTASettings",
    "MemorySummary",
    "MeshStiffnessModel",
    "PlanetPinManufacturingErrorsCoordinateSystem",
    "PowerLoadDragTorqueSpecificationMethod",
    "PowerLoadInputTorqueSpecificationMethod",
    "PowerLoadPIDControlSpeedInputType",
    "PowerLoadType",
    "RelativeComponentAlignment",
    "RelativeOffsetOption",
    "SystemReporting",
    "ThermalExpansionOptionForGroundedNodes",
    "TransmissionTemperatureSet",
)
