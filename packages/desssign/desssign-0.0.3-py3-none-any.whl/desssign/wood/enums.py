from enum import IntEnum

from framesss.enums import CaseInsensitiveStrEnum


class WoodType(CaseInsensitiveStrEnum):
    """Enum for wood types."""

    SOLID_TIMBER = "solid timber"
    GLUED_LAMINATED_TIMBER = "glued laminated timber"
    LVL = "lvl"
    PLYWOOD = "plywood"
    OSB = "osb"
    PARTICLEBOARD = "particleboard"
    HARD_FIBREBOARD = "hard fibreboard"
    MEDIUM_FIBREBOARD = "medium fibreboard"
    MDF_FIBREBOARD = "mdf fibreboard"
    SOFT_FIBREBOARD = "soft fibreboard"


class JointType(CaseInsensitiveStrEnum):
    """Enum for joint types."""

    CONNECTION = "connection"
    PUNCHED_METAL_PLATE_FASTENERS = "punched metal plate fasteners"


class ServiceClass(IntEnum):
    """
    Enum for service classes.

    EN 1995-1-1, 2.3.1.3

    :cvar SC1: Service class 1 is characterised by a moisture content in the materials corresponding
               to a temperature of 20°C and the relative humidity of the surrounding air only
               exceeding 65 % for a few weeks per year. In service class 1 the average moisture content
               in most softwoods will not exceed 12 %.
    :cvar SC2: Service class 2 is characterised by a moisture content in the materials corresponding
               to a temperature of 20°C and the relative humidity of the surrounding air only
               exceeding 85 % for a few weeks per year. In service class 2 the average moisture content
               in most softwoods will not exceed 20 %.
    :cvar SC3: Service class 3 is characterised by climatic conditions leading to higher moisture
               contents than in service class 2.
    """

    SC1 = 1
    SC2 = 2
    SC3 = 3


class CheckResult(CaseInsensitiveStrEnum):
    """
    Enum for design results.

    :cvar PASS: Design check passed.
    :cvar FAIL: Design check failed.
    """

    PASS = "pass"
    FAIL = "fail"
