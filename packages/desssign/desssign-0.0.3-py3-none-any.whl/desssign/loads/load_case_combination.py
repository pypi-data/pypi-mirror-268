from __future__ import annotations

from typing import cast

from framesss.pre.cases import LoadCase
from framesss.pre.cases import LoadCaseCombination

from desssign.loads.enums import LOAD_DURATION_MAPPING
from desssign.loads.enums import LimitState
from desssign.loads.enums import LoadDurationClass
from desssign.loads.enums import SLSCombination
from desssign.loads.enums import ULSAlternativeCombination
from desssign.loads.enums import ULSCombination
from desssign.loads.load_case import DesignLoadCase
from desssign.loads.load_combination_generator.generate_combinations import (
    generate_combination,
)


class DesignLoadCaseCombination(LoadCaseCombination):
    """
    Represent a combination of load cases in the design process.

    :param label: The label of the load case combination.
    :param limit_state: The limit state of the combination group. Either 'ULS' or 'SLS'.
    :param combination_type: The type of the combination group. For ULS: basic, alternative or accidental,
                             for SLS: characteristic, frequent or quasi-permanent.
    :param permanent_cases: A list of permanent load cases.
    :param leading_variable_case: The leading variable load case.
    :param other_variable_cases: A list of other variable load cases.
    :param alternative_combination: Specifier for the used equation, only required for ULS alternative combinations.
                                    Either '6.10a' or '6.10b'.
    :ivar combination_key: The key of the combination.
    """

    def __init__(
        self,
        label: str,
        limit_state: str | LimitState,
        combination_type: str | SLSCombination | ULSCombination,
        permanent_cases: list[DesignLoadCase],
        leading_variable_case: DesignLoadCase | None,
        other_variable_cases: list[DesignLoadCase],
        alternative_combination: str | ULSAlternativeCombination | None = None,
    ) -> None:
        """Initialize the DesignLoadCaseCombination class."""
        self.limit_state = LimitState(limit_state)

        if self.limit_state == LimitState.ULS:
            self.combination_type = ULSCombination(combination_type)
        elif self.limit_state == LimitState.SLS:
            self.combination_type = SLSCombination(combination_type)
        else:
            raise ValueError(
                f"Can't set combination type: '{combination_type}' to limit state: '{limit_state}'."
            )

        if combination_type == ULSCombination.ALTERNATIVE:
            if alternative_combination is None:
                raise ValueError(
                    "Alternative combination requires an 'alternative_combination'."
                )

        self.alternative_combination = (
            ULSAlternativeCombination(alternative_combination)
            if alternative_combination
            else None
        )

        self.permanent_cases = permanent_cases
        self.leading_variable_case = leading_variable_case
        self.other_variable_cases = other_variable_cases

        load_cases, self.combination_key = generate_combination(
            permanent_cases=self.permanent_cases,
            leading_variable_case=self.leading_variable_case,
            other_variable_cases=self.other_variable_cases,
            combination=self.combination_type,
            alternative_combination=self.alternative_combination,
        )

        super().__init__(label, cast(dict[LoadCase, float], load_cases))

    def _get_combination(self) -> tuple[dict[DesignLoadCase, float], str]:
        """Return the load cases combination and the combination key."""
        return generate_combination(
            permanent_cases=self.permanent_cases,
            leading_variable_case=self.leading_variable_case,
            other_variable_cases=self.other_variable_cases,
            combination=self.combination_type,
            alternative_combination=self.alternative_combination,
        )

    @property
    def load_duration_class(self) -> LoadDurationClass:
        """
        Return the load duration class of the combination.

        EN 1995-1-1, 3.1.3(2):
            If a load combination consists of actions belonging to different load-duration classes a value
            of `k_mod` should be chosen which corresponds to the action with the shortest duration, e.g. for a
            combination of dead load and a short-term load, a value of k_mod corresponding to the short-term
            load should be used.
        """
        # Get the minimum value of all duration classes
        min_duration_value = min(
            [
                LOAD_DURATION_MAPPING[cast(DesignLoadCase, case).load_duration_class]
                for case in self.load_cases
            ]
        )

        # Find the LoadDurationClass corresponding to the minimum value
        for duration_class, value in LOAD_DURATION_MAPPING.items():
            if value == min_duration_value:
                return LoadDurationClass(duration_class)

        # If no matching LoadDurationClass is found, raise an exception
        raise ValueError(
            f"Can't find the load duration class with value: '̈́{min_duration_value}'."
        )
