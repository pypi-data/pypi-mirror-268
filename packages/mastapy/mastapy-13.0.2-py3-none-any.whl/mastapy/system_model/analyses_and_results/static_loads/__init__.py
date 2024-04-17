"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6812 import LoadCase
    from ._6813 import StaticLoadCase
    from ._6814 import TimeSeriesLoadCase
    from ._6815 import AbstractAssemblyLoadCase
    from ._6816 import AbstractShaftLoadCase
    from ._6817 import AbstractShaftOrHousingLoadCase
    from ._6818 import AbstractShaftToMountableComponentConnectionLoadCase
    from ._6819 import AdditionalAccelerationOptions
    from ._6820 import AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
    from ._6821 import AdvancedTimeSteppingAnalysisForModulationType
    from ._6822 import AGMAGleasonConicalGearLoadCase
    from ._6823 import AGMAGleasonConicalGearMeshLoadCase
    from ._6824 import AGMAGleasonConicalGearSetLoadCase
    from ._6825 import AllRingPinsManufacturingError
    from ._6826 import AnalysisType
    from ._6827 import AssemblyLoadCase
    from ._6828 import BearingLoadCase
    from ._6829 import BeltConnectionLoadCase
    from ._6830 import BeltDriveLoadCase
    from ._6831 import BevelDifferentialGearLoadCase
    from ._6832 import BevelDifferentialGearMeshLoadCase
    from ._6833 import BevelDifferentialGearSetLoadCase
    from ._6834 import BevelDifferentialPlanetGearLoadCase
    from ._6835 import BevelDifferentialSunGearLoadCase
    from ._6836 import BevelGearLoadCase
    from ._6837 import BevelGearMeshLoadCase
    from ._6838 import BevelGearSetLoadCase
    from ._6839 import BoltedJointLoadCase
    from ._6840 import BoltLoadCase
    from ._6841 import ClutchConnectionLoadCase
    from ._6842 import ClutchHalfLoadCase
    from ._6843 import ClutchLoadCase
    from ._6844 import CMSElementFaceGroupWithSelectionOption
    from ._6845 import CoaxialConnectionLoadCase
    from ._6846 import ComponentLoadCase
    from ._6847 import ConceptCouplingConnectionLoadCase
    from ._6848 import ConceptCouplingHalfLoadCase
    from ._6849 import ConceptCouplingLoadCase
    from ._6850 import ConceptGearLoadCase
    from ._6851 import ConceptGearMeshLoadCase
    from ._6852 import ConceptGearSetLoadCase
    from ._6853 import ConicalGearLoadCase
    from ._6854 import ConicalGearManufactureError
    from ._6855 import ConicalGearMeshLoadCase
    from ._6856 import ConicalGearSetHarmonicLoadData
    from ._6857 import ConicalGearSetLoadCase
    from ._6858 import ConnectionLoadCase
    from ._6859 import ConnectorLoadCase
    from ._6860 import CouplingConnectionLoadCase
    from ._6861 import CouplingHalfLoadCase
    from ._6862 import CouplingLoadCase
    from ._6863 import CVTBeltConnectionLoadCase
    from ._6864 import CVTLoadCase
    from ._6865 import CVTPulleyLoadCase
    from ._6866 import CycloidalAssemblyLoadCase
    from ._6867 import CycloidalDiscCentralBearingConnectionLoadCase
    from ._6868 import CycloidalDiscLoadCase
    from ._6869 import CycloidalDiscPlanetaryBearingConnectionLoadCase
    from ._6870 import CylindricalGearLoadCase
    from ._6871 import CylindricalGearManufactureError
    from ._6872 import CylindricalGearMeshLoadCase
    from ._6873 import CylindricalGearSetHarmonicLoadData
    from ._6874 import CylindricalGearSetLoadCase
    from ._6875 import CylindricalPlanetGearLoadCase
    from ._6876 import DataFromMotorPackagePerMeanTorque
    from ._6877 import DataFromMotorPackagePerSpeed
    from ._6878 import DatumLoadCase
    from ._6879 import ElectricMachineDataImportType
    from ._6880 import ElectricMachineHarmonicLoadData
    from ._6881 import ElectricMachineHarmonicLoadDataFromExcel
    from ._6882 import ElectricMachineHarmonicLoadDataFromFlux
    from ._6883 import ElectricMachineHarmonicLoadDataFromJMAG
    from ._6884 import ElectricMachineHarmonicLoadDataFromMASTA
    from ._6885 import ElectricMachineHarmonicLoadDataFromMotorCAD
    from ._6886 import ElectricMachineHarmonicLoadDataFromMotorPackages
    from ._6887 import ElectricMachineHarmonicLoadExcelImportOptions
    from ._6888 import ElectricMachineHarmonicLoadFluxImportOptions
    from ._6889 import ElectricMachineHarmonicLoadImportOptionsBase
    from ._6890 import ElectricMachineHarmonicLoadJMAGImportOptions
    from ._6891 import ElectricMachineHarmonicLoadMotorCADImportOptions
    from ._6892 import ExternalCADModelLoadCase
    from ._6893 import FaceGearLoadCase
    from ._6894 import FaceGearMeshLoadCase
    from ._6895 import FaceGearSetLoadCase
    from ._6896 import FEPartLoadCase
    from ._6897 import FlexiblePinAssemblyLoadCase
    from ._6898 import ForceAndTorqueScalingFactor
    from ._6899 import GearLoadCase
    from ._6900 import GearManufactureError
    from ._6901 import GearMeshLoadCase
    from ._6902 import GearMeshTEOrderType
    from ._6903 import GearSetHarmonicLoadData
    from ._6904 import GearSetLoadCase
    from ._6905 import GuideDxfModelLoadCase
    from ._6906 import HarmonicExcitationType
    from ._6907 import HarmonicLoadDataCSVImport
    from ._6908 import HarmonicLoadDataExcelImport
    from ._6909 import HarmonicLoadDataFluxImport
    from ._6910 import HarmonicLoadDataImportBase
    from ._6911 import HarmonicLoadDataImportFromMotorPackages
    from ._6912 import HarmonicLoadDataJMAGImport
    from ._6913 import HarmonicLoadDataMotorCADImport
    from ._6914 import HypoidGearLoadCase
    from ._6915 import HypoidGearMeshLoadCase
    from ._6916 import HypoidGearSetLoadCase
    from ._6917 import ImportType
    from ._6918 import InformationAtRingPinToDiscContactPointFromGeometry
    from ._6919 import InnerDiameterReference
    from ._6920 import InterMountableComponentConnectionLoadCase
    from ._6921 import KlingelnbergCycloPalloidConicalGearLoadCase
    from ._6922 import KlingelnbergCycloPalloidConicalGearMeshLoadCase
    from ._6923 import KlingelnbergCycloPalloidConicalGearSetLoadCase
    from ._6924 import KlingelnbergCycloPalloidHypoidGearLoadCase
    from ._6925 import KlingelnbergCycloPalloidHypoidGearMeshLoadCase
    from ._6926 import KlingelnbergCycloPalloidHypoidGearSetLoadCase
    from ._6927 import KlingelnbergCycloPalloidSpiralBevelGearLoadCase
    from ._6928 import KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
    from ._6929 import KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
    from ._6930 import MassDiscLoadCase
    from ._6931 import MeasurementComponentLoadCase
    from ._6932 import MeshStiffnessSource
    from ._6933 import MountableComponentLoadCase
    from ._6934 import NamedSpeed
    from ._6935 import OilSealLoadCase
    from ._6936 import ParametricStudyType
    from ._6937 import PartLoadCase
    from ._6938 import PartToPartShearCouplingConnectionLoadCase
    from ._6939 import PartToPartShearCouplingHalfLoadCase
    from ._6940 import PartToPartShearCouplingLoadCase
    from ._6941 import PlanetaryConnectionLoadCase
    from ._6942 import PlanetaryGearSetLoadCase
    from ._6943 import PlanetarySocketManufactureError
    from ._6944 import PlanetCarrierLoadCase
    from ._6945 import PlanetManufactureError
    from ._6946 import PointLoadHarmonicLoadData
    from ._6947 import PointLoadLoadCase
    from ._6948 import PowerLoadLoadCase
    from ._6949 import PulleyLoadCase
    from ._6950 import ResetMicroGeometryOptions
    from ._6951 import RingPinManufacturingError
    from ._6952 import RingPinsLoadCase
    from ._6953 import RingPinsToDiscConnectionLoadCase
    from ._6954 import RollingRingAssemblyLoadCase
    from ._6955 import RollingRingConnectionLoadCase
    from ._6956 import RollingRingLoadCase
    from ._6957 import RootAssemblyLoadCase
    from ._6958 import ShaftHubConnectionLoadCase
    from ._6959 import ShaftLoadCase
    from ._6960 import ShaftToMountableComponentConnectionLoadCase
    from ._6961 import SpecialisedAssemblyLoadCase
    from ._6962 import SpiralBevelGearLoadCase
    from ._6963 import SpiralBevelGearMeshLoadCase
    from ._6964 import SpiralBevelGearSetLoadCase
    from ._6965 import SpringDamperConnectionLoadCase
    from ._6966 import SpringDamperHalfLoadCase
    from ._6967 import SpringDamperLoadCase
    from ._6968 import StraightBevelDiffGearLoadCase
    from ._6969 import StraightBevelDiffGearMeshLoadCase
    from ._6970 import StraightBevelDiffGearSetLoadCase
    from ._6971 import StraightBevelGearLoadCase
    from ._6972 import StraightBevelGearMeshLoadCase
    from ._6973 import StraightBevelGearSetLoadCase
    from ._6974 import StraightBevelPlanetGearLoadCase
    from ._6975 import StraightBevelSunGearLoadCase
    from ._6976 import SynchroniserHalfLoadCase
    from ._6977 import SynchroniserLoadCase
    from ._6978 import SynchroniserPartLoadCase
    from ._6979 import SynchroniserSleeveLoadCase
    from ._6980 import TEExcitationType
    from ._6981 import TorqueConverterConnectionLoadCase
    from ._6982 import TorqueConverterLoadCase
    from ._6983 import TorqueConverterPumpLoadCase
    from ._6984 import TorqueConverterTurbineLoadCase
    from ._6985 import TorqueRippleInputType
    from ._6986 import TorqueSpecificationForSystemDeflection
    from ._6987 import TransmissionEfficiencySettings
    from ._6988 import UnbalancedMassHarmonicLoadData
    from ._6989 import UnbalancedMassLoadCase
    from ._6990 import VirtualComponentLoadCase
    from ._6991 import WormGearLoadCase
    from ._6992 import WormGearMeshLoadCase
    from ._6993 import WormGearSetLoadCase
    from ._6994 import ZerolBevelGearLoadCase
    from ._6995 import ZerolBevelGearMeshLoadCase
    from ._6996 import ZerolBevelGearSetLoadCase
else:
    import_structure = {
        "_6812": ["LoadCase"],
        "_6813": ["StaticLoadCase"],
        "_6814": ["TimeSeriesLoadCase"],
        "_6815": ["AbstractAssemblyLoadCase"],
        "_6816": ["AbstractShaftLoadCase"],
        "_6817": ["AbstractShaftOrHousingLoadCase"],
        "_6818": ["AbstractShaftToMountableComponentConnectionLoadCase"],
        "_6819": ["AdditionalAccelerationOptions"],
        "_6820": ["AdvancedTimeSteppingAnalysisForModulationStaticLoadCase"],
        "_6821": ["AdvancedTimeSteppingAnalysisForModulationType"],
        "_6822": ["AGMAGleasonConicalGearLoadCase"],
        "_6823": ["AGMAGleasonConicalGearMeshLoadCase"],
        "_6824": ["AGMAGleasonConicalGearSetLoadCase"],
        "_6825": ["AllRingPinsManufacturingError"],
        "_6826": ["AnalysisType"],
        "_6827": ["AssemblyLoadCase"],
        "_6828": ["BearingLoadCase"],
        "_6829": ["BeltConnectionLoadCase"],
        "_6830": ["BeltDriveLoadCase"],
        "_6831": ["BevelDifferentialGearLoadCase"],
        "_6832": ["BevelDifferentialGearMeshLoadCase"],
        "_6833": ["BevelDifferentialGearSetLoadCase"],
        "_6834": ["BevelDifferentialPlanetGearLoadCase"],
        "_6835": ["BevelDifferentialSunGearLoadCase"],
        "_6836": ["BevelGearLoadCase"],
        "_6837": ["BevelGearMeshLoadCase"],
        "_6838": ["BevelGearSetLoadCase"],
        "_6839": ["BoltedJointLoadCase"],
        "_6840": ["BoltLoadCase"],
        "_6841": ["ClutchConnectionLoadCase"],
        "_6842": ["ClutchHalfLoadCase"],
        "_6843": ["ClutchLoadCase"],
        "_6844": ["CMSElementFaceGroupWithSelectionOption"],
        "_6845": ["CoaxialConnectionLoadCase"],
        "_6846": ["ComponentLoadCase"],
        "_6847": ["ConceptCouplingConnectionLoadCase"],
        "_6848": ["ConceptCouplingHalfLoadCase"],
        "_6849": ["ConceptCouplingLoadCase"],
        "_6850": ["ConceptGearLoadCase"],
        "_6851": ["ConceptGearMeshLoadCase"],
        "_6852": ["ConceptGearSetLoadCase"],
        "_6853": ["ConicalGearLoadCase"],
        "_6854": ["ConicalGearManufactureError"],
        "_6855": ["ConicalGearMeshLoadCase"],
        "_6856": ["ConicalGearSetHarmonicLoadData"],
        "_6857": ["ConicalGearSetLoadCase"],
        "_6858": ["ConnectionLoadCase"],
        "_6859": ["ConnectorLoadCase"],
        "_6860": ["CouplingConnectionLoadCase"],
        "_6861": ["CouplingHalfLoadCase"],
        "_6862": ["CouplingLoadCase"],
        "_6863": ["CVTBeltConnectionLoadCase"],
        "_6864": ["CVTLoadCase"],
        "_6865": ["CVTPulleyLoadCase"],
        "_6866": ["CycloidalAssemblyLoadCase"],
        "_6867": ["CycloidalDiscCentralBearingConnectionLoadCase"],
        "_6868": ["CycloidalDiscLoadCase"],
        "_6869": ["CycloidalDiscPlanetaryBearingConnectionLoadCase"],
        "_6870": ["CylindricalGearLoadCase"],
        "_6871": ["CylindricalGearManufactureError"],
        "_6872": ["CylindricalGearMeshLoadCase"],
        "_6873": ["CylindricalGearSetHarmonicLoadData"],
        "_6874": ["CylindricalGearSetLoadCase"],
        "_6875": ["CylindricalPlanetGearLoadCase"],
        "_6876": ["DataFromMotorPackagePerMeanTorque"],
        "_6877": ["DataFromMotorPackagePerSpeed"],
        "_6878": ["DatumLoadCase"],
        "_6879": ["ElectricMachineDataImportType"],
        "_6880": ["ElectricMachineHarmonicLoadData"],
        "_6881": ["ElectricMachineHarmonicLoadDataFromExcel"],
        "_6882": ["ElectricMachineHarmonicLoadDataFromFlux"],
        "_6883": ["ElectricMachineHarmonicLoadDataFromJMAG"],
        "_6884": ["ElectricMachineHarmonicLoadDataFromMASTA"],
        "_6885": ["ElectricMachineHarmonicLoadDataFromMotorCAD"],
        "_6886": ["ElectricMachineHarmonicLoadDataFromMotorPackages"],
        "_6887": ["ElectricMachineHarmonicLoadExcelImportOptions"],
        "_6888": ["ElectricMachineHarmonicLoadFluxImportOptions"],
        "_6889": ["ElectricMachineHarmonicLoadImportOptionsBase"],
        "_6890": ["ElectricMachineHarmonicLoadJMAGImportOptions"],
        "_6891": ["ElectricMachineHarmonicLoadMotorCADImportOptions"],
        "_6892": ["ExternalCADModelLoadCase"],
        "_6893": ["FaceGearLoadCase"],
        "_6894": ["FaceGearMeshLoadCase"],
        "_6895": ["FaceGearSetLoadCase"],
        "_6896": ["FEPartLoadCase"],
        "_6897": ["FlexiblePinAssemblyLoadCase"],
        "_6898": ["ForceAndTorqueScalingFactor"],
        "_6899": ["GearLoadCase"],
        "_6900": ["GearManufactureError"],
        "_6901": ["GearMeshLoadCase"],
        "_6902": ["GearMeshTEOrderType"],
        "_6903": ["GearSetHarmonicLoadData"],
        "_6904": ["GearSetLoadCase"],
        "_6905": ["GuideDxfModelLoadCase"],
        "_6906": ["HarmonicExcitationType"],
        "_6907": ["HarmonicLoadDataCSVImport"],
        "_6908": ["HarmonicLoadDataExcelImport"],
        "_6909": ["HarmonicLoadDataFluxImport"],
        "_6910": ["HarmonicLoadDataImportBase"],
        "_6911": ["HarmonicLoadDataImportFromMotorPackages"],
        "_6912": ["HarmonicLoadDataJMAGImport"],
        "_6913": ["HarmonicLoadDataMotorCADImport"],
        "_6914": ["HypoidGearLoadCase"],
        "_6915": ["HypoidGearMeshLoadCase"],
        "_6916": ["HypoidGearSetLoadCase"],
        "_6917": ["ImportType"],
        "_6918": ["InformationAtRingPinToDiscContactPointFromGeometry"],
        "_6919": ["InnerDiameterReference"],
        "_6920": ["InterMountableComponentConnectionLoadCase"],
        "_6921": ["KlingelnbergCycloPalloidConicalGearLoadCase"],
        "_6922": ["KlingelnbergCycloPalloidConicalGearMeshLoadCase"],
        "_6923": ["KlingelnbergCycloPalloidConicalGearSetLoadCase"],
        "_6924": ["KlingelnbergCycloPalloidHypoidGearLoadCase"],
        "_6925": ["KlingelnbergCycloPalloidHypoidGearMeshLoadCase"],
        "_6926": ["KlingelnbergCycloPalloidHypoidGearSetLoadCase"],
        "_6927": ["KlingelnbergCycloPalloidSpiralBevelGearLoadCase"],
        "_6928": ["KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase"],
        "_6929": ["KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase"],
        "_6930": ["MassDiscLoadCase"],
        "_6931": ["MeasurementComponentLoadCase"],
        "_6932": ["MeshStiffnessSource"],
        "_6933": ["MountableComponentLoadCase"],
        "_6934": ["NamedSpeed"],
        "_6935": ["OilSealLoadCase"],
        "_6936": ["ParametricStudyType"],
        "_6937": ["PartLoadCase"],
        "_6938": ["PartToPartShearCouplingConnectionLoadCase"],
        "_6939": ["PartToPartShearCouplingHalfLoadCase"],
        "_6940": ["PartToPartShearCouplingLoadCase"],
        "_6941": ["PlanetaryConnectionLoadCase"],
        "_6942": ["PlanetaryGearSetLoadCase"],
        "_6943": ["PlanetarySocketManufactureError"],
        "_6944": ["PlanetCarrierLoadCase"],
        "_6945": ["PlanetManufactureError"],
        "_6946": ["PointLoadHarmonicLoadData"],
        "_6947": ["PointLoadLoadCase"],
        "_6948": ["PowerLoadLoadCase"],
        "_6949": ["PulleyLoadCase"],
        "_6950": ["ResetMicroGeometryOptions"],
        "_6951": ["RingPinManufacturingError"],
        "_6952": ["RingPinsLoadCase"],
        "_6953": ["RingPinsToDiscConnectionLoadCase"],
        "_6954": ["RollingRingAssemblyLoadCase"],
        "_6955": ["RollingRingConnectionLoadCase"],
        "_6956": ["RollingRingLoadCase"],
        "_6957": ["RootAssemblyLoadCase"],
        "_6958": ["ShaftHubConnectionLoadCase"],
        "_6959": ["ShaftLoadCase"],
        "_6960": ["ShaftToMountableComponentConnectionLoadCase"],
        "_6961": ["SpecialisedAssemblyLoadCase"],
        "_6962": ["SpiralBevelGearLoadCase"],
        "_6963": ["SpiralBevelGearMeshLoadCase"],
        "_6964": ["SpiralBevelGearSetLoadCase"],
        "_6965": ["SpringDamperConnectionLoadCase"],
        "_6966": ["SpringDamperHalfLoadCase"],
        "_6967": ["SpringDamperLoadCase"],
        "_6968": ["StraightBevelDiffGearLoadCase"],
        "_6969": ["StraightBevelDiffGearMeshLoadCase"],
        "_6970": ["StraightBevelDiffGearSetLoadCase"],
        "_6971": ["StraightBevelGearLoadCase"],
        "_6972": ["StraightBevelGearMeshLoadCase"],
        "_6973": ["StraightBevelGearSetLoadCase"],
        "_6974": ["StraightBevelPlanetGearLoadCase"],
        "_6975": ["StraightBevelSunGearLoadCase"],
        "_6976": ["SynchroniserHalfLoadCase"],
        "_6977": ["SynchroniserLoadCase"],
        "_6978": ["SynchroniserPartLoadCase"],
        "_6979": ["SynchroniserSleeveLoadCase"],
        "_6980": ["TEExcitationType"],
        "_6981": ["TorqueConverterConnectionLoadCase"],
        "_6982": ["TorqueConverterLoadCase"],
        "_6983": ["TorqueConverterPumpLoadCase"],
        "_6984": ["TorqueConverterTurbineLoadCase"],
        "_6985": ["TorqueRippleInputType"],
        "_6986": ["TorqueSpecificationForSystemDeflection"],
        "_6987": ["TransmissionEfficiencySettings"],
        "_6988": ["UnbalancedMassHarmonicLoadData"],
        "_6989": ["UnbalancedMassLoadCase"],
        "_6990": ["VirtualComponentLoadCase"],
        "_6991": ["WormGearLoadCase"],
        "_6992": ["WormGearMeshLoadCase"],
        "_6993": ["WormGearSetLoadCase"],
        "_6994": ["ZerolBevelGearLoadCase"],
        "_6995": ["ZerolBevelGearMeshLoadCase"],
        "_6996": ["ZerolBevelGearSetLoadCase"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "LoadCase",
    "StaticLoadCase",
    "TimeSeriesLoadCase",
    "AbstractAssemblyLoadCase",
    "AbstractShaftLoadCase",
    "AbstractShaftOrHousingLoadCase",
    "AbstractShaftToMountableComponentConnectionLoadCase",
    "AdditionalAccelerationOptions",
    "AdvancedTimeSteppingAnalysisForModulationStaticLoadCase",
    "AdvancedTimeSteppingAnalysisForModulationType",
    "AGMAGleasonConicalGearLoadCase",
    "AGMAGleasonConicalGearMeshLoadCase",
    "AGMAGleasonConicalGearSetLoadCase",
    "AllRingPinsManufacturingError",
    "AnalysisType",
    "AssemblyLoadCase",
    "BearingLoadCase",
    "BeltConnectionLoadCase",
    "BeltDriveLoadCase",
    "BevelDifferentialGearLoadCase",
    "BevelDifferentialGearMeshLoadCase",
    "BevelDifferentialGearSetLoadCase",
    "BevelDifferentialPlanetGearLoadCase",
    "BevelDifferentialSunGearLoadCase",
    "BevelGearLoadCase",
    "BevelGearMeshLoadCase",
    "BevelGearSetLoadCase",
    "BoltedJointLoadCase",
    "BoltLoadCase",
    "ClutchConnectionLoadCase",
    "ClutchHalfLoadCase",
    "ClutchLoadCase",
    "CMSElementFaceGroupWithSelectionOption",
    "CoaxialConnectionLoadCase",
    "ComponentLoadCase",
    "ConceptCouplingConnectionLoadCase",
    "ConceptCouplingHalfLoadCase",
    "ConceptCouplingLoadCase",
    "ConceptGearLoadCase",
    "ConceptGearMeshLoadCase",
    "ConceptGearSetLoadCase",
    "ConicalGearLoadCase",
    "ConicalGearManufactureError",
    "ConicalGearMeshLoadCase",
    "ConicalGearSetHarmonicLoadData",
    "ConicalGearSetLoadCase",
    "ConnectionLoadCase",
    "ConnectorLoadCase",
    "CouplingConnectionLoadCase",
    "CouplingHalfLoadCase",
    "CouplingLoadCase",
    "CVTBeltConnectionLoadCase",
    "CVTLoadCase",
    "CVTPulleyLoadCase",
    "CycloidalAssemblyLoadCase",
    "CycloidalDiscCentralBearingConnectionLoadCase",
    "CycloidalDiscLoadCase",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
    "CylindricalGearLoadCase",
    "CylindricalGearManufactureError",
    "CylindricalGearMeshLoadCase",
    "CylindricalGearSetHarmonicLoadData",
    "CylindricalGearSetLoadCase",
    "CylindricalPlanetGearLoadCase",
    "DataFromMotorPackagePerMeanTorque",
    "DataFromMotorPackagePerSpeed",
    "DatumLoadCase",
    "ElectricMachineDataImportType",
    "ElectricMachineHarmonicLoadData",
    "ElectricMachineHarmonicLoadDataFromExcel",
    "ElectricMachineHarmonicLoadDataFromFlux",
    "ElectricMachineHarmonicLoadDataFromJMAG",
    "ElectricMachineHarmonicLoadDataFromMASTA",
    "ElectricMachineHarmonicLoadDataFromMotorCAD",
    "ElectricMachineHarmonicLoadDataFromMotorPackages",
    "ElectricMachineHarmonicLoadExcelImportOptions",
    "ElectricMachineHarmonicLoadFluxImportOptions",
    "ElectricMachineHarmonicLoadImportOptionsBase",
    "ElectricMachineHarmonicLoadJMAGImportOptions",
    "ElectricMachineHarmonicLoadMotorCADImportOptions",
    "ExternalCADModelLoadCase",
    "FaceGearLoadCase",
    "FaceGearMeshLoadCase",
    "FaceGearSetLoadCase",
    "FEPartLoadCase",
    "FlexiblePinAssemblyLoadCase",
    "ForceAndTorqueScalingFactor",
    "GearLoadCase",
    "GearManufactureError",
    "GearMeshLoadCase",
    "GearMeshTEOrderType",
    "GearSetHarmonicLoadData",
    "GearSetLoadCase",
    "GuideDxfModelLoadCase",
    "HarmonicExcitationType",
    "HarmonicLoadDataCSVImport",
    "HarmonicLoadDataExcelImport",
    "HarmonicLoadDataFluxImport",
    "HarmonicLoadDataImportBase",
    "HarmonicLoadDataImportFromMotorPackages",
    "HarmonicLoadDataJMAGImport",
    "HarmonicLoadDataMotorCADImport",
    "HypoidGearLoadCase",
    "HypoidGearMeshLoadCase",
    "HypoidGearSetLoadCase",
    "ImportType",
    "InformationAtRingPinToDiscContactPointFromGeometry",
    "InnerDiameterReference",
    "InterMountableComponentConnectionLoadCase",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    "MassDiscLoadCase",
    "MeasurementComponentLoadCase",
    "MeshStiffnessSource",
    "MountableComponentLoadCase",
    "NamedSpeed",
    "OilSealLoadCase",
    "ParametricStudyType",
    "PartLoadCase",
    "PartToPartShearCouplingConnectionLoadCase",
    "PartToPartShearCouplingHalfLoadCase",
    "PartToPartShearCouplingLoadCase",
    "PlanetaryConnectionLoadCase",
    "PlanetaryGearSetLoadCase",
    "PlanetarySocketManufactureError",
    "PlanetCarrierLoadCase",
    "PlanetManufactureError",
    "PointLoadHarmonicLoadData",
    "PointLoadLoadCase",
    "PowerLoadLoadCase",
    "PulleyLoadCase",
    "ResetMicroGeometryOptions",
    "RingPinManufacturingError",
    "RingPinsLoadCase",
    "RingPinsToDiscConnectionLoadCase",
    "RollingRingAssemblyLoadCase",
    "RollingRingConnectionLoadCase",
    "RollingRingLoadCase",
    "RootAssemblyLoadCase",
    "ShaftHubConnectionLoadCase",
    "ShaftLoadCase",
    "ShaftToMountableComponentConnectionLoadCase",
    "SpecialisedAssemblyLoadCase",
    "SpiralBevelGearLoadCase",
    "SpiralBevelGearMeshLoadCase",
    "SpiralBevelGearSetLoadCase",
    "SpringDamperConnectionLoadCase",
    "SpringDamperHalfLoadCase",
    "SpringDamperLoadCase",
    "StraightBevelDiffGearLoadCase",
    "StraightBevelDiffGearMeshLoadCase",
    "StraightBevelDiffGearSetLoadCase",
    "StraightBevelGearLoadCase",
    "StraightBevelGearMeshLoadCase",
    "StraightBevelGearSetLoadCase",
    "StraightBevelPlanetGearLoadCase",
    "StraightBevelSunGearLoadCase",
    "SynchroniserHalfLoadCase",
    "SynchroniserLoadCase",
    "SynchroniserPartLoadCase",
    "SynchroniserSleeveLoadCase",
    "TEExcitationType",
    "TorqueConverterConnectionLoadCase",
    "TorqueConverterLoadCase",
    "TorqueConverterPumpLoadCase",
    "TorqueConverterTurbineLoadCase",
    "TorqueRippleInputType",
    "TorqueSpecificationForSystemDeflection",
    "TransmissionEfficiencySettings",
    "UnbalancedMassHarmonicLoadData",
    "UnbalancedMassLoadCase",
    "VirtualComponentLoadCase",
    "WormGearLoadCase",
    "WormGearMeshLoadCase",
    "WormGearSetLoadCase",
    "ZerolBevelGearLoadCase",
    "ZerolBevelGearMeshLoadCase",
    "ZerolBevelGearSetLoadCase",
)
