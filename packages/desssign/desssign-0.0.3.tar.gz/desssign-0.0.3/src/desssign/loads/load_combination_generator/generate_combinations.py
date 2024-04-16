from __future__ import annotations

from desssign.loads.enums import LoadBehavior
from desssign.loads.enums import SLSCombination
from desssign.loads.enums import ULSAlternativeCombination
from desssign.loads.enums import ULSCombination
from desssign.loads.enums import VariableCategory
from desssign.loads.load_case import DesignLoadCase
from desssign.loads.load_combination_generator.constants import GAMMA_VALUES
from desssign.loads.load_combination_generator.constants import PSI_FACTORS
from desssign.loads.load_combination_generator.constants import XI


def generate_combination(
    permanent_cases: list[DesignLoadCase],
    leading_variable_case: DesignLoadCase | None,
    other_variable_cases: list[DesignLoadCase],
    combination: SLSCombination | ULSCombination,
    alternative_combination: ULSAlternativeCombination | None = None,
) -> tuple[dict[DesignLoadCase, float], str]:
    """
    Generate a combination of load cases according to the limit state and combination type.

    :param permanent_cases: A list of permanent load cases.
    :param leading_variable_case: The leading variable load case.
    :param other_variable_cases: A list of other variable load cases.
    :param combination: Type of SLS or ULS combination.
    :param alternative_combination: Specifier for the used equation, only required for ULS alternative combinations.
                                    Either '6.10a' or '6.10b'.
    :raises AttributeError: If the combination type is unknown.
    """
    if combination == SLSCombination.CHARACTERISTIC:
        return generate_sls_characteristic_combination(
            permanent_cases, leading_variable_case, other_variable_cases
        )

    if combination == SLSCombination.FREQUENT:
        return generate_sls_frequent_combination(
            permanent_cases, leading_variable_case, other_variable_cases
        )

    if combination == SLSCombination.QUASIPERMANENT:
        return generate_sls_quasipermanent_combination(
            permanent_cases, leading_variable_case, other_variable_cases
        )

    if combination == ULSCombination.BASIC:
        return generate_uls_basic_combination(
            permanent_cases, leading_variable_case, other_variable_cases
        )

    if combination == ULSCombination.ALTERNATIVE:
        if alternative_combination == ULSAlternativeCombination.REDUCED_VARIABLE:
            return generate_uls_alternative_a_combination(
                permanent_cases, leading_variable_case, other_variable_cases
            )

        if alternative_combination == ULSAlternativeCombination.REDUCED_PERMANENT:
            return generate_uls_alternative_b_combination(
                permanent_cases, leading_variable_case, other_variable_cases
            )

        raise AttributeError(
            f"Unknown alternative combination: '{alternative_combination}'."
        )

    raise AttributeError(f"Unknown combination: '{combination}'.")


def generate_sls_characteristic_combination(
    permanent_cases: list[DesignLoadCase],
    leading_variable_case: DesignLoadCase | None,
    other_variable_cases: list[DesignLoadCase],
) -> tuple[dict[DesignLoadCase, float], str]:
    """
    Generate a characteristic combination of load cases for serviceability limit state.

    Combination is generated according to equations 6.14 of EN 1990.
    The combination is normally used for irreversible limit states.

    :param permanent_cases: A list of permanent load cases.
    :param leading_variable_case: The leading variable load case.
    :param other_variable_cases: A list of other variable load cases.
    """
    cases = {}
    key = ""

    for case in permanent_cases:
        cases[case] = 1.0
        key += f"{case.label}+"

    if leading_variable_case is not None:
        cases[leading_variable_case] = 1.0
        key += f"{leading_variable_case.label}+"

    for case in other_variable_cases:
        factor = PSI_FACTORS[VariableCategory(case.category)]["psi_0"]
        cases[case] = factor
        key += f"{factor}*{case.label}+"

    return cases, key[:-1]


def generate_sls_frequent_combination(
    permanent_cases: list[DesignLoadCase],
    leading_variable_case: DesignLoadCase | None,
    other_variable_cases: list[DesignLoadCase],
) -> tuple[dict[DesignLoadCase, float], str]:
    """
    Generate a frequent combination of load cases for serviceability limit state.

    Combination is generated according to equations 6.15 of EN 1990.
    The combination is normally used for reversible limit states.

    :param permanent_cases: A list of permanent load cases.
    :param leading_variable_case: The leading variable load case.
    :param other_variable_cases: A list of other variable load cases.
    """
    cases = {}
    key = ""

    for case in permanent_cases:
        cases[case] = 1.0
        key += f"{case.label}+"

    if leading_variable_case is not None:
        factor = PSI_FACTORS[VariableCategory(leading_variable_case.category)]["psi_1"]
        cases[leading_variable_case] = factor
        key += f"{factor}*{leading_variable_case.label}+"

    for case in other_variable_cases:
        factor = PSI_FACTORS[VariableCategory(case.category)]["psi_2"]
        cases[case] = factor
        key += f"{factor}*{case.label}+"

    return cases, key[:-1]


def generate_sls_quasipermanent_combination(
    permanent_cases: list[DesignLoadCase],
    leading_variable_case: DesignLoadCase | None,
    other_variable_cases: list[DesignLoadCase],
) -> tuple[dict[DesignLoadCase, float], str]:
    """
    Generate a quasipermanent combination of load cases for serviceability limit state.

    Combination is generated according to equations 6.16 of EN 1990.
    The combination is normally used for long-term effects and the appearance of the structure.

    :param permanent_cases: A list of permanent load cases.
    :param leading_variable_case: The leading variable load case.
    :param other_variable_cases: A list of other variable load cases.
    """
    cases = {}
    key = ""

    for case in permanent_cases:
        cases[case] = 1.0
        key += f"{case.label}+"

    if leading_variable_case is not None:
        factor = PSI_FACTORS[VariableCategory(leading_variable_case.category)]["psi_2"]
        cases[leading_variable_case] = factor
        key += f"{factor}*{leading_variable_case.label}+"

    for case in other_variable_cases:
        factor = PSI_FACTORS[VariableCategory(case.category)]["psi_2"]
        cases[case] = factor
        key += f"{factor}*{case.label}+"

    return cases, key[:-1]


def generate_uls_basic_combination(
    permanent_cases: list[DesignLoadCase],
    leading_variable_case: DesignLoadCase | None,
    other_variable_cases: list[DesignLoadCase],
) -> tuple[dict[DesignLoadCase, float], str]:
    """
    Generate a basic combination of load cases for ultimate limit state.

    Combination is generated according to equations 6.10 of EN 1990.

    :param permanent_cases: A list of permanent load cases.
    :param leading_variable_case: The leading variable load case.
    :param other_variable_cases: A list of other variable load cases.
    """
    cases = {}
    key = ""

    for case in permanent_cases:
        factor = GAMMA_VALUES["Set B"][case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        cases[case] = factor
        key += f"{factor}*{case.label}+"

    if leading_variable_case is not None:
        factor = GAMMA_VALUES["Set B"][leading_variable_case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        cases[leading_variable_case] = factor
        key += f"{factor}*{leading_variable_case.label}+"

    for case in other_variable_cases:
        gamma = GAMMA_VALUES["Set B"][case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        psi = PSI_FACTORS[VariableCategory(case.category)]["psi_0"]
        cases[case] = gamma * psi
        key += f"{gamma}*{psi}*{case.label}+"

    return cases, key[:-1]


def generate_uls_alternative_a_combination(
    permanent_cases: list[DesignLoadCase],
    leading_variable_case: DesignLoadCase | None,
    other_variable_cases: list[DesignLoadCase],
) -> tuple[dict[DesignLoadCase, float], str]:
    """
    Generate two alternative combinations of load cases for ultimate limit state.

    Combinations are generated according to equation 6.10a of EN 1990.

    :param permanent_cases: A list of permanent load cases.
    :param leading_variable_case: The leading variable load case.
    :param other_variable_cases: A list of other variable load cases.
    """
    cases = {}
    key = ""

    for case in permanent_cases:
        gamma = GAMMA_VALUES["Set B"][case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        cases[case] = gamma
        key += f"{gamma}*{case.label}+"

    if leading_variable_case is not None:
        gamma = GAMMA_VALUES["Set B"][leading_variable_case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        psi = PSI_FACTORS[VariableCategory(leading_variable_case.category)]["psi_0"]
        cases[leading_variable_case] = gamma * psi
        key += f"{gamma}*{psi}*{leading_variable_case.label}+"

    for case in other_variable_cases:
        gamma = GAMMA_VALUES["Set B"][case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        psi = PSI_FACTORS[VariableCategory(case.category)]["psi_0"]
        cases[case] = gamma * psi
        key += f"{gamma}*{psi}*{case.label}+"

    return cases, key[:-1]


def generate_uls_alternative_b_combination(
    permanent_cases: list[DesignLoadCase],
    leading_variable_case: DesignLoadCase | None,
    other_variable_cases: list[DesignLoadCase],
) -> tuple[dict[DesignLoadCase, float], str]:
    """
    Generate two alternative combinations of load cases for ultimate limit state.

    Combinations are generated according to equation 6.10b of EN 1990.

    :param permanent_cases: A list of permanent load cases.
    :param leading_variable_case: The leading variable load case.
    :param other_variable_cases: A list of other variable load cases.
    """
    cases = {}
    key = ""

    for case in permanent_cases:
        gamma = GAMMA_VALUES["Set B"][case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        cases[case] = gamma * XI
        key += f"{XI}*{gamma}*{case.label}+"

    if leading_variable_case is not None:
        gamma = GAMMA_VALUES["Set B"][leading_variable_case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        cases[leading_variable_case] = gamma
        key += f"{gamma}*{leading_variable_case.label}+"

    for case in other_variable_cases:
        gamma = GAMMA_VALUES["Set B"][case.load_type][
            LoadBehavior.UNFAVOURABLE
        ]  # TODO: Favourable?
        psi = PSI_FACTORS[VariableCategory(case.category)]["psi_0"]
        cases[case] = gamma * psi
        key += f"{gamma}*{psi}*{case.label}+"

    return cases, key[:-1]
