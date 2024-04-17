"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._612 import CutterFlankSections
    from ._613 import CylindricalCutterDatabase
    from ._614 import CylindricalGearBlank
    from ._615 import CylindricalGearManufacturingConfig
    from ._616 import CylindricalGearSpecifiedMicroGeometry
    from ._617 import CylindricalGearSpecifiedProfile
    from ._618 import CylindricalHobDatabase
    from ._619 import CylindricalManufacturedGearDutyCycle
    from ._620 import CylindricalManufacturedGearLoadCase
    from ._621 import CylindricalManufacturedGearMeshDutyCycle
    from ._622 import CylindricalManufacturedGearMeshLoadCase
    from ._623 import CylindricalManufacturedGearSetDutyCycle
    from ._624 import CylindricalManufacturedGearSetLoadCase
    from ._625 import CylindricalMeshManufacturingConfig
    from ._626 import CylindricalMftFinishingMethods
    from ._627 import CylindricalMftRoughingMethods
    from ._628 import CylindricalSetManufacturingConfig
    from ._629 import CylindricalShaperDatabase
    from ._630 import Flank
    from ._631 import GearManufacturingConfigurationViewModel
    from ._632 import GearManufacturingConfigurationViewModelPlaceholder
    from ._633 import GearSetConfigViewModel
    from ._634 import HobEdgeTypes
    from ._635 import LeadModificationSegment
    from ._636 import MicroGeometryInputs
    from ._637 import MicroGeometryInputsLead
    from ._638 import MicroGeometryInputsProfile
    from ._639 import ModificationSegment
    from ._640 import ProfileModificationSegment
    from ._641 import SuitableCutterSetup
else:
    import_structure = {
        "_612": ["CutterFlankSections"],
        "_613": ["CylindricalCutterDatabase"],
        "_614": ["CylindricalGearBlank"],
        "_615": ["CylindricalGearManufacturingConfig"],
        "_616": ["CylindricalGearSpecifiedMicroGeometry"],
        "_617": ["CylindricalGearSpecifiedProfile"],
        "_618": ["CylindricalHobDatabase"],
        "_619": ["CylindricalManufacturedGearDutyCycle"],
        "_620": ["CylindricalManufacturedGearLoadCase"],
        "_621": ["CylindricalManufacturedGearMeshDutyCycle"],
        "_622": ["CylindricalManufacturedGearMeshLoadCase"],
        "_623": ["CylindricalManufacturedGearSetDutyCycle"],
        "_624": ["CylindricalManufacturedGearSetLoadCase"],
        "_625": ["CylindricalMeshManufacturingConfig"],
        "_626": ["CylindricalMftFinishingMethods"],
        "_627": ["CylindricalMftRoughingMethods"],
        "_628": ["CylindricalSetManufacturingConfig"],
        "_629": ["CylindricalShaperDatabase"],
        "_630": ["Flank"],
        "_631": ["GearManufacturingConfigurationViewModel"],
        "_632": ["GearManufacturingConfigurationViewModelPlaceholder"],
        "_633": ["GearSetConfigViewModel"],
        "_634": ["HobEdgeTypes"],
        "_635": ["LeadModificationSegment"],
        "_636": ["MicroGeometryInputs"],
        "_637": ["MicroGeometryInputsLead"],
        "_638": ["MicroGeometryInputsProfile"],
        "_639": ["ModificationSegment"],
        "_640": ["ProfileModificationSegment"],
        "_641": ["SuitableCutterSetup"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "CutterFlankSections",
    "CylindricalCutterDatabase",
    "CylindricalGearBlank",
    "CylindricalGearManufacturingConfig",
    "CylindricalGearSpecifiedMicroGeometry",
    "CylindricalGearSpecifiedProfile",
    "CylindricalHobDatabase",
    "CylindricalManufacturedGearDutyCycle",
    "CylindricalManufacturedGearLoadCase",
    "CylindricalManufacturedGearMeshDutyCycle",
    "CylindricalManufacturedGearMeshLoadCase",
    "CylindricalManufacturedGearSetDutyCycle",
    "CylindricalManufacturedGearSetLoadCase",
    "CylindricalMeshManufacturingConfig",
    "CylindricalMftFinishingMethods",
    "CylindricalMftRoughingMethods",
    "CylindricalSetManufacturingConfig",
    "CylindricalShaperDatabase",
    "Flank",
    "GearManufacturingConfigurationViewModel",
    "GearManufacturingConfigurationViewModelPlaceholder",
    "GearSetConfigViewModel",
    "HobEdgeTypes",
    "LeadModificationSegment",
    "MicroGeometryInputs",
    "MicroGeometryInputsLead",
    "MicroGeometryInputsProfile",
    "ModificationSegment",
    "ProfileModificationSegment",
    "SuitableCutterSetup",
)
