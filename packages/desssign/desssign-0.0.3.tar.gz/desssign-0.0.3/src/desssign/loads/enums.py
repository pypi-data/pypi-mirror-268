from framesss.enums import CaseInsensitiveStrEnum


class LoadBehavior(CaseInsensitiveStrEnum):
    """Enumeration of possible behavior of action."""

    UNFAVOURABLE = "unfavourable"
    FAVOURABLE = "favourable"


class LoadType(CaseInsensitiveStrEnum):
    """Enumeration of possible type of action."""

    PERMANENT = "permanent"
    VARIABLE = "variable"
    ACCIDENTAL = "accidental"


class LimitState(CaseInsensitiveStrEnum):
    """
    Enumeration of limit states.

    :cvar ULS: Ultimate limit state.
    :cvar SLS: Serviceability limit state.
    """

    ULS = "uls"
    SLS = "sls"


class UltimateLimitStates(CaseInsensitiveStrEnum):
    """Enumeration of ultimate limit states."""

    EQU = "equ"
    STR = "str"
    GEO = "geo"
    FAT = "fat"
    UPL = "upl"
    HYD = "hyd"


class ULSCombination(CaseInsensitiveStrEnum):
    """
    Enumeration of ultimate limit state combinations according to EN 1990.

    :cvar BASIC: Basic combination according to equation 6.10 of EN 1990.
    :cvar ALTERNATIVE: Alternative combinations according to equations 6.10a and 6.10b of EN 1990.
                       In this case, two variants of the combinations are considered in calculations,
                       one with reduced constant load cases and the other with reduced principal
                       variable load cases.
    :cvar ACCIDENTAL: Accidental combinations according to equations 6.11 of EN 1990.
    """

    BASIC = "basic"
    ALTERNATIVE = "alternative"
    ACCIDENTAL = "accidental"


class ULSAlternativeCombination(CaseInsensitiveStrEnum):
    """
    Enumeration of ULS alternative combination types.

    :cvar REDUCED_PERMANENT: Combination with reduced permanent load cases.
    :cvar REDUCED_VARIABLE: Combination with reduced leading variable load case.
    """

    REDUCED_VARIABLE = "6.10a"
    REDUCED_PERMANENT = "6.10b"


class SLSCombination(CaseInsensitiveStrEnum):
    """
    Enumeration of serviceability limit state combinations according to EN 1990.

    :cvar CHARACTERISTIC: Combination according to equations 6.14 of EN 1990.
    :cvar FREQUENT: Combination according to equation 6.15 of EN 1990.
    :cvar QUASIPERMANENT: Combination according to equation 6.16 of EN 1990.
    """

    CHARACTERISTIC = "characteristic"
    FREQUENT = "frequent"
    QUASIPERMANENT = "quasipermanent"


class VariableCategory(CaseInsensitiveStrEnum):
    """Enumeration of possible variable loads."""

    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"
    H = "h"
    SNOW_ABOVE_1000_M = "snow > 1000 m"
    SNOW_BELLOW_1000_M = "snow < 1000 m"
    WIND = "wind"
    TEMPERATURE = "temperature"


class LoadCaseRelation(CaseInsensitiveStrEnum):
    """
    Enumeration of possible relation of load cases.

    :cvar EXCLUSIVE: Load cases from the same load group will never act together.
    :cvar STANDARD: Load cases from the same load group may (or may not) act together.
    :cvar TOGETHER: Load cases from the same load group always act together.
    """

    EXCLUSIVE = "exclusive"
    STANDARD = "standard"
    TOGETHER = "together"


class LoadDurationClass(CaseInsensitiveStrEnum):
    """
    Enum for load duration classes.

    EN 1995-1-1, 2.3.1.2 Load-duration classes.

    The load-duration classes are characterised by the effect of a constant load acting for a
    certain period of time in the life of the structure. For a variable action the appropriate class shall
    be determined on the basis of an estimate of the typical variation of the load with time.

    :cvar PERMANENT: more than 10 years, e.g. self-weight
    :cvar LONG_TERM: 6 months - 10 years, e.g. storage
    :cvar MEDIUM_TERM: 1 week - 6 months, e.g. imposed floor load, snow
    :cvar SHORT_TERM: less than 1 week, e.g. snow, wind
    :cvar INSTANTANEOUS: instantaneous, e.g. wind, accidental load
    """

    PERMANENT = "permanent"
    LONG_TERM = "long-term"
    MEDIUM_TERM = "medium-term"
    SHORT_TERM = "short-term"
    INSTANTANEOUS = "instantaneous"


LOAD_DURATION_MAPPING = {
    LoadDurationClass.INSTANTANEOUS: 1,
    LoadDurationClass.SHORT_TERM: 2,
    LoadDurationClass.MEDIUM_TERM: 3,
    LoadDurationClass.LONG_TERM: 4,
    LoadDurationClass.PERMANENT: 5,
}
