"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1619 import Acceleration
    from ._1620 import Angle
    from ._1621 import AnglePerUnitTemperature
    from ._1622 import AngleSmall
    from ._1623 import AngleVerySmall
    from ._1624 import AngularAcceleration
    from ._1625 import AngularCompliance
    from ._1626 import AngularJerk
    from ._1627 import AngularStiffness
    from ._1628 import AngularVelocity
    from ._1629 import Area
    from ._1630 import AreaSmall
    from ._1631 import CarbonEmissionFactor
    from ._1632 import CurrentDensity
    from ._1633 import CurrentPerLength
    from ._1634 import Cycles
    from ._1635 import Damage
    from ._1636 import DamageRate
    from ._1637 import DataSize
    from ._1638 import Decibel
    from ._1639 import Density
    from ._1640 import ElectricalResistance
    from ._1641 import ElectricalResistivity
    from ._1642 import ElectricCurrent
    from ._1643 import Energy
    from ._1644 import EnergyPerUnitArea
    from ._1645 import EnergyPerUnitAreaSmall
    from ._1646 import EnergySmall
    from ._1647 import Enum
    from ._1648 import FlowRate
    from ._1649 import Force
    from ._1650 import ForcePerUnitLength
    from ._1651 import ForcePerUnitPressure
    from ._1652 import ForcePerUnitTemperature
    from ._1653 import FractionMeasurementBase
    from ._1654 import FractionPerTemperature
    from ._1655 import Frequency
    from ._1656 import FuelConsumptionEngine
    from ._1657 import FuelEfficiencyVehicle
    from ._1658 import Gradient
    from ._1659 import HeatConductivity
    from ._1660 import HeatTransfer
    from ._1661 import HeatTransferCoefficientForPlasticGearTooth
    from ._1662 import HeatTransferResistance
    from ._1663 import Impulse
    from ._1664 import Index
    from ._1665 import Inductance
    from ._1666 import Integer
    from ._1667 import InverseShortLength
    from ._1668 import InverseShortTime
    from ._1669 import Jerk
    from ._1670 import KinematicViscosity
    from ._1671 import LengthLong
    from ._1672 import LengthMedium
    from ._1673 import LengthPerUnitTemperature
    from ._1674 import LengthShort
    from ._1675 import LengthToTheFourth
    from ._1676 import LengthVeryLong
    from ._1677 import LengthVeryShort
    from ._1678 import LengthVeryShortPerLengthShort
    from ._1679 import LinearAngularDamping
    from ._1680 import LinearAngularStiffnessCrossTerm
    from ._1681 import LinearDamping
    from ._1682 import LinearFlexibility
    from ._1683 import LinearStiffness
    from ._1684 import MagneticFieldStrength
    from ._1685 import MagneticFlux
    from ._1686 import MagneticFluxDensity
    from ._1687 import MagneticVectorPotential
    from ._1688 import MagnetomotiveForce
    from ._1689 import Mass
    from ._1690 import MassPerUnitLength
    from ._1691 import MassPerUnitTime
    from ._1692 import MomentOfInertia
    from ._1693 import MomentOfInertiaPerUnitLength
    from ._1694 import MomentPerUnitPressure
    from ._1695 import Number
    from ._1696 import Percentage
    from ._1697 import Power
    from ._1698 import PowerPerSmallArea
    from ._1699 import PowerPerUnitTime
    from ._1700 import PowerSmall
    from ._1701 import PowerSmallPerArea
    from ._1702 import PowerSmallPerMass
    from ._1703 import PowerSmallPerUnitAreaPerUnitTime
    from ._1704 import PowerSmallPerUnitTime
    from ._1705 import PowerSmallPerVolume
    from ._1706 import Pressure
    from ._1707 import PressurePerUnitTime
    from ._1708 import PressureVelocityProduct
    from ._1709 import PressureViscosityCoefficient
    from ._1710 import Price
    from ._1711 import PricePerUnitMass
    from ._1712 import QuadraticAngularDamping
    from ._1713 import QuadraticDrag
    from ._1714 import RescaledMeasurement
    from ._1715 import Rotatum
    from ._1716 import SafetyFactor
    from ._1717 import SpecificAcousticImpedance
    from ._1718 import SpecificHeat
    from ._1719 import SquareRootOfUnitForcePerUnitArea
    from ._1720 import StiffnessPerUnitFaceWidth
    from ._1721 import Stress
    from ._1722 import Temperature
    from ._1723 import TemperatureDifference
    from ._1724 import TemperaturePerUnitTime
    from ._1725 import Text
    from ._1726 import ThermalContactCoefficient
    from ._1727 import ThermalExpansionCoefficient
    from ._1728 import ThermoElasticFactor
    from ._1729 import Time
    from ._1730 import TimeShort
    from ._1731 import TimeVeryShort
    from ._1732 import Torque
    from ._1733 import TorqueConverterInverseK
    from ._1734 import TorqueConverterK
    from ._1735 import TorquePerCurrent
    from ._1736 import TorquePerSquareRootOfPower
    from ._1737 import TorquePerUnitTemperature
    from ._1738 import Velocity
    from ._1739 import VelocitySmall
    from ._1740 import Viscosity
    from ._1741 import Voltage
    from ._1742 import VoltagePerAngularVelocity
    from ._1743 import Volume
    from ._1744 import WearCoefficient
    from ._1745 import Yank
else:
    import_structure = {
        "_1619": ["Acceleration"],
        "_1620": ["Angle"],
        "_1621": ["AnglePerUnitTemperature"],
        "_1622": ["AngleSmall"],
        "_1623": ["AngleVerySmall"],
        "_1624": ["AngularAcceleration"],
        "_1625": ["AngularCompliance"],
        "_1626": ["AngularJerk"],
        "_1627": ["AngularStiffness"],
        "_1628": ["AngularVelocity"],
        "_1629": ["Area"],
        "_1630": ["AreaSmall"],
        "_1631": ["CarbonEmissionFactor"],
        "_1632": ["CurrentDensity"],
        "_1633": ["CurrentPerLength"],
        "_1634": ["Cycles"],
        "_1635": ["Damage"],
        "_1636": ["DamageRate"],
        "_1637": ["DataSize"],
        "_1638": ["Decibel"],
        "_1639": ["Density"],
        "_1640": ["ElectricalResistance"],
        "_1641": ["ElectricalResistivity"],
        "_1642": ["ElectricCurrent"],
        "_1643": ["Energy"],
        "_1644": ["EnergyPerUnitArea"],
        "_1645": ["EnergyPerUnitAreaSmall"],
        "_1646": ["EnergySmall"],
        "_1647": ["Enum"],
        "_1648": ["FlowRate"],
        "_1649": ["Force"],
        "_1650": ["ForcePerUnitLength"],
        "_1651": ["ForcePerUnitPressure"],
        "_1652": ["ForcePerUnitTemperature"],
        "_1653": ["FractionMeasurementBase"],
        "_1654": ["FractionPerTemperature"],
        "_1655": ["Frequency"],
        "_1656": ["FuelConsumptionEngine"],
        "_1657": ["FuelEfficiencyVehicle"],
        "_1658": ["Gradient"],
        "_1659": ["HeatConductivity"],
        "_1660": ["HeatTransfer"],
        "_1661": ["HeatTransferCoefficientForPlasticGearTooth"],
        "_1662": ["HeatTransferResistance"],
        "_1663": ["Impulse"],
        "_1664": ["Index"],
        "_1665": ["Inductance"],
        "_1666": ["Integer"],
        "_1667": ["InverseShortLength"],
        "_1668": ["InverseShortTime"],
        "_1669": ["Jerk"],
        "_1670": ["KinematicViscosity"],
        "_1671": ["LengthLong"],
        "_1672": ["LengthMedium"],
        "_1673": ["LengthPerUnitTemperature"],
        "_1674": ["LengthShort"],
        "_1675": ["LengthToTheFourth"],
        "_1676": ["LengthVeryLong"],
        "_1677": ["LengthVeryShort"],
        "_1678": ["LengthVeryShortPerLengthShort"],
        "_1679": ["LinearAngularDamping"],
        "_1680": ["LinearAngularStiffnessCrossTerm"],
        "_1681": ["LinearDamping"],
        "_1682": ["LinearFlexibility"],
        "_1683": ["LinearStiffness"],
        "_1684": ["MagneticFieldStrength"],
        "_1685": ["MagneticFlux"],
        "_1686": ["MagneticFluxDensity"],
        "_1687": ["MagneticVectorPotential"],
        "_1688": ["MagnetomotiveForce"],
        "_1689": ["Mass"],
        "_1690": ["MassPerUnitLength"],
        "_1691": ["MassPerUnitTime"],
        "_1692": ["MomentOfInertia"],
        "_1693": ["MomentOfInertiaPerUnitLength"],
        "_1694": ["MomentPerUnitPressure"],
        "_1695": ["Number"],
        "_1696": ["Percentage"],
        "_1697": ["Power"],
        "_1698": ["PowerPerSmallArea"],
        "_1699": ["PowerPerUnitTime"],
        "_1700": ["PowerSmall"],
        "_1701": ["PowerSmallPerArea"],
        "_1702": ["PowerSmallPerMass"],
        "_1703": ["PowerSmallPerUnitAreaPerUnitTime"],
        "_1704": ["PowerSmallPerUnitTime"],
        "_1705": ["PowerSmallPerVolume"],
        "_1706": ["Pressure"],
        "_1707": ["PressurePerUnitTime"],
        "_1708": ["PressureVelocityProduct"],
        "_1709": ["PressureViscosityCoefficient"],
        "_1710": ["Price"],
        "_1711": ["PricePerUnitMass"],
        "_1712": ["QuadraticAngularDamping"],
        "_1713": ["QuadraticDrag"],
        "_1714": ["RescaledMeasurement"],
        "_1715": ["Rotatum"],
        "_1716": ["SafetyFactor"],
        "_1717": ["SpecificAcousticImpedance"],
        "_1718": ["SpecificHeat"],
        "_1719": ["SquareRootOfUnitForcePerUnitArea"],
        "_1720": ["StiffnessPerUnitFaceWidth"],
        "_1721": ["Stress"],
        "_1722": ["Temperature"],
        "_1723": ["TemperatureDifference"],
        "_1724": ["TemperaturePerUnitTime"],
        "_1725": ["Text"],
        "_1726": ["ThermalContactCoefficient"],
        "_1727": ["ThermalExpansionCoefficient"],
        "_1728": ["ThermoElasticFactor"],
        "_1729": ["Time"],
        "_1730": ["TimeShort"],
        "_1731": ["TimeVeryShort"],
        "_1732": ["Torque"],
        "_1733": ["TorqueConverterInverseK"],
        "_1734": ["TorqueConverterK"],
        "_1735": ["TorquePerCurrent"],
        "_1736": ["TorquePerSquareRootOfPower"],
        "_1737": ["TorquePerUnitTemperature"],
        "_1738": ["Velocity"],
        "_1739": ["VelocitySmall"],
        "_1740": ["Viscosity"],
        "_1741": ["Voltage"],
        "_1742": ["VoltagePerAngularVelocity"],
        "_1743": ["Volume"],
        "_1744": ["WearCoefficient"],
        "_1745": ["Yank"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Acceleration",
    "Angle",
    "AnglePerUnitTemperature",
    "AngleSmall",
    "AngleVerySmall",
    "AngularAcceleration",
    "AngularCompliance",
    "AngularJerk",
    "AngularStiffness",
    "AngularVelocity",
    "Area",
    "AreaSmall",
    "CarbonEmissionFactor",
    "CurrentDensity",
    "CurrentPerLength",
    "Cycles",
    "Damage",
    "DamageRate",
    "DataSize",
    "Decibel",
    "Density",
    "ElectricalResistance",
    "ElectricalResistivity",
    "ElectricCurrent",
    "Energy",
    "EnergyPerUnitArea",
    "EnergyPerUnitAreaSmall",
    "EnergySmall",
    "Enum",
    "FlowRate",
    "Force",
    "ForcePerUnitLength",
    "ForcePerUnitPressure",
    "ForcePerUnitTemperature",
    "FractionMeasurementBase",
    "FractionPerTemperature",
    "Frequency",
    "FuelConsumptionEngine",
    "FuelEfficiencyVehicle",
    "Gradient",
    "HeatConductivity",
    "HeatTransfer",
    "HeatTransferCoefficientForPlasticGearTooth",
    "HeatTransferResistance",
    "Impulse",
    "Index",
    "Inductance",
    "Integer",
    "InverseShortLength",
    "InverseShortTime",
    "Jerk",
    "KinematicViscosity",
    "LengthLong",
    "LengthMedium",
    "LengthPerUnitTemperature",
    "LengthShort",
    "LengthToTheFourth",
    "LengthVeryLong",
    "LengthVeryShort",
    "LengthVeryShortPerLengthShort",
    "LinearAngularDamping",
    "LinearAngularStiffnessCrossTerm",
    "LinearDamping",
    "LinearFlexibility",
    "LinearStiffness",
    "MagneticFieldStrength",
    "MagneticFlux",
    "MagneticFluxDensity",
    "MagneticVectorPotential",
    "MagnetomotiveForce",
    "Mass",
    "MassPerUnitLength",
    "MassPerUnitTime",
    "MomentOfInertia",
    "MomentOfInertiaPerUnitLength",
    "MomentPerUnitPressure",
    "Number",
    "Percentage",
    "Power",
    "PowerPerSmallArea",
    "PowerPerUnitTime",
    "PowerSmall",
    "PowerSmallPerArea",
    "PowerSmallPerMass",
    "PowerSmallPerUnitAreaPerUnitTime",
    "PowerSmallPerUnitTime",
    "PowerSmallPerVolume",
    "Pressure",
    "PressurePerUnitTime",
    "PressureVelocityProduct",
    "PressureViscosityCoefficient",
    "Price",
    "PricePerUnitMass",
    "QuadraticAngularDamping",
    "QuadraticDrag",
    "RescaledMeasurement",
    "Rotatum",
    "SafetyFactor",
    "SpecificAcousticImpedance",
    "SpecificHeat",
    "SquareRootOfUnitForcePerUnitArea",
    "StiffnessPerUnitFaceWidth",
    "Stress",
    "Temperature",
    "TemperatureDifference",
    "TemperaturePerUnitTime",
    "Text",
    "ThermalContactCoefficient",
    "ThermalExpansionCoefficient",
    "ThermoElasticFactor",
    "Time",
    "TimeShort",
    "TimeVeryShort",
    "Torque",
    "TorqueConverterInverseK",
    "TorqueConverterK",
    "TorquePerCurrent",
    "TorquePerSquareRootOfPower",
    "TorquePerUnitTemperature",
    "Velocity",
    "VelocitySmall",
    "Viscosity",
    "Voltage",
    "VoltagePerAngularVelocity",
    "Volume",
    "WearCoefficient",
    "Yank",
)
