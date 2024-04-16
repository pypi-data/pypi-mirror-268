from framesss.enums import CaseInsensitiveStrEnum


class Topography(CaseInsensitiveStrEnum):
    """Enumeration of topographies according to EN 1991-1-13."""

    WINDSWEPT = "windswept"
    NORMAL = "normal"
    SHELTERED = "sheltered"


class SnowZone(CaseInsensitiveStrEnum):
    """Enumeration of snow zones according to ČSN EN 1991-1-3."""

    I = "I"
    II = "II"
    III = "III"
    IV = "IV"
    V = "V"
    VI = "VI"
    VII = "VII"
    VIII = "VIII"
