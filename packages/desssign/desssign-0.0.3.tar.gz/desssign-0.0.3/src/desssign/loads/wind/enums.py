from framesss.enums import CaseInsensitiveStrEnum


class TerrainCategory(CaseInsensitiveStrEnum):
    """Enumeration of terrain categories according to EN 1991-1-4."""

    O = "O"
    I = "I"
    II = "II"
    III = "III"
    IV = "IV"


class WindZone(CaseInsensitiveStrEnum):
    """Enumeration of wind zones according to ČSN EN 1991-1-4."""

    I = "I"
    II = "II"
    III = "III"
    IV = "IV"
    V = "V"


class RoofProfile(CaseInsensitiveStrEnum):
    """Enumeration of roof profiles according to EN 1991-1-4."""

    FLAT = "flat"
    MONOPITCHED = "monopitched"
    DUOPITCHED = "duopitched"


class FlatRoofType(CaseInsensitiveStrEnum):
    """Enumeration of flat roof types according to EN 1991-1-4."""

    SHARP_EAVES = "sharp eaves"
    WITH_PARAPETS = "with parapets"
    # CURVED_EAVES = "curved eaves"
    # MANSARD_EAVES = "mansard eaves"
