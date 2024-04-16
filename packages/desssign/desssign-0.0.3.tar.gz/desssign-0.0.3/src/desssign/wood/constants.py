from __future__ import annotations

from desssign.loads.enums import LoadDurationClass
from desssign.wood.enums import JointType
from desssign.wood.enums import ServiceClass
from desssign.wood.enums import WoodType

PARTIAL_FACTORS = {
    WoodType.SOLID_TIMBER: 1.3,
    WoodType.GLUED_LAMINATED_TIMBER: 1.25,
    WoodType.LVL: 1.2,
    WoodType.PLYWOOD: 1.2,
    WoodType.OSB: 1.2,
    WoodType.PARTICLEBOARD: 1.3,
    WoodType.HARD_FIBREBOARD: 1.3,
    WoodType.MEDIUM_FIBREBOARD: 1.3,
    WoodType.MDF_FIBREBOARD: 1.3,
    WoodType.SOFT_FIBREBOARD: 1.3,
    JointType.CONNECTION: 1.3,
    JointType.PUNCHED_METAL_PLATE_FASTENERS: 1.25,
}


def get_partial_factor(material: str | WoodType | JointType) -> float:
    """
    Partial factor according to EN 1995-1-1, table 2.5.

    :param material: Material or joint type.
    :return: Partial factor.
    """
    return PARTIAL_FACTORS[material]


MODIFICATION_FACTORS = {
    WoodType.SOLID_TIMBER: {
        ServiceClass.SC1: {
            LoadDurationClass.PERMANENT: 0.6,
            LoadDurationClass.LONG_TERM: 0.7,
            LoadDurationClass.MEDIUM_TERM: 0.8,
            LoadDurationClass.SHORT_TERM: 0.9,
            LoadDurationClass.INSTANTANEOUS: 1.1,
        },
        ServiceClass.SC2: {
            LoadDurationClass.PERMANENT: 0.6,
            LoadDurationClass.LONG_TERM: 0.7,
            LoadDurationClass.MEDIUM_TERM: 0.8,
            LoadDurationClass.SHORT_TERM: 0.9,
            LoadDurationClass.INSTANTANEOUS: 1.1,
        },
        ServiceClass.SC3: {
            LoadDurationClass.PERMANENT: 0.5,
            LoadDurationClass.LONG_TERM: 0.55,
            LoadDurationClass.MEDIUM_TERM: 0.65,
            LoadDurationClass.SHORT_TERM: 0.7,
            LoadDurationClass.INSTANTANEOUS: 0.9,
        },
    },
    WoodType.GLUED_LAMINATED_TIMBER: {
        ServiceClass.SC1: {
            LoadDurationClass.PERMANENT: 0.6,
            LoadDurationClass.LONG_TERM: 0.7,
            LoadDurationClass.MEDIUM_TERM: 0.8,
            LoadDurationClass.SHORT_TERM: 0.9,
            LoadDurationClass.INSTANTANEOUS: 1.1,
        },
        ServiceClass.SC2: {
            LoadDurationClass.PERMANENT: 0.6,
            LoadDurationClass.LONG_TERM: 0.7,
            LoadDurationClass.MEDIUM_TERM: 0.8,
            LoadDurationClass.SHORT_TERM: 0.9,
            LoadDurationClass.INSTANTANEOUS: 1.1,
        },
        ServiceClass.SC3: {
            LoadDurationClass.PERMANENT: 0.5,
            LoadDurationClass.LONG_TERM: 0.55,
            LoadDurationClass.MEDIUM_TERM: 0.65,
            LoadDurationClass.SHORT_TERM: 0.7,
            LoadDurationClass.INSTANTANEOUS: 0.9,
        },
    },
    # TODO: Add k_mod values for other wood types
}


def get_modification_factor(
    wood_type: str | WoodType,
    service_class: int | ServiceClass,
    load_duration_class: str | LoadDurationClass,
) -> float:
    """
    Modification factor according to EN 1995-1-1, 3.2, table 3.1.

    :param wood_type: Material type.
    :param service_class: Service class.
    :param load_duration_class: Load duration class.
    :return: Modification factor.
    """
    wood_type = WoodType(wood_type)
    service_class = ServiceClass(service_class)
    load_duration_class = LoadDurationClass(load_duration_class)

    return MODIFICATION_FACTORS[wood_type][service_class][load_duration_class]


DEFORMATION_FACTORS = {
    WoodType.SOLID_TIMBER: {
        ServiceClass.SC1: 0.6,
        ServiceClass.SC2: 0.8,
        ServiceClass.SC3: 2.0,
    },
    WoodType.GLUED_LAMINATED_TIMBER: {
        ServiceClass.SC1: 0.6,
        ServiceClass.SC2: 0.8,
        ServiceClass.SC3: 2.0,
    },
    # TODO: Add k_def values for other wood types
}


def get_deformation_factor(
    wood_type: str | WoodType,
    service_class: int | ServiceClass,
) -> float:
    """
    Deformation factor according to EN 1995-1-1, 3.3, table 3.2.

    :param wood_type: Wood type.
    :param service_class: Service class.
    :return: Deformation factor.
    """
    wood_type = WoodType(wood_type)
    service_class = ServiceClass(service_class)

    return DEFORMATION_FACTORS[wood_type][service_class]
