from __future__ import annotations

from itertools import product
from typing import TYPE_CHECKING

from desssign.loads.enums import LimitState
from desssign.loads.enums import LoadType
from desssign.loads.enums import SLSCombination
from desssign.loads.enums import ULSAlternativeCombination
from desssign.loads.enums import ULSCombination
from desssign.loads.load_case_combination import DesignLoadCaseCombination
from desssign.utils import flatten_list

if TYPE_CHECKING:
    from desssign.loads.load_case_group import DesignLoadCaseGroup


class CombinationsGenerator:
    """
    A class used to generate all possible combinations of load cases for a specific limit state.

    :ivar limit_state: The limit state of the combination group. Either ULS or SLS.
    :ivar combination_type: The type of the combination group. For ULS: basic, alternative or accidental,
                            for SLS: characteristic, frequent or quasi-permanent.
    """

    def __init__(
        self,
        limit_state: str | LimitState,
        combination_type: str | SLSCombination | ULSCombination,
    ) -> None:
        """
        Initialize the CombinationsGenerator class.

        :param limit_state: The limit state of the combination group. Either ULS or SLS.
        :type limit_state: str | LimitState
        :param combination_type: The type of the combination group. For ULS: basic, alternative or accidental,
                                 for SLS: characteristic, frequent or quasi-permanent.
        :type combination_type: str | SLSCombination | ULSCombination
        :raises AttributeError: If the combination type does not match the limit state.
        """
        self.limit_state = LimitState(limit_state)

        if self.limit_state == LimitState.ULS:
            self.combination_type = ULSCombination(combination_type)
        elif self.limit_state == LimitState.SLS:
            self.combination_type = SLSCombination(combination_type)
        else:
            raise AttributeError(
                f"Can't set combination type: '{combination_type}' to limit state: '{limit_state}'."
            )

    def generate_combinations(
        self, *args: list[DesignLoadCaseGroup,]
    ) -> list[DesignLoadCaseCombination]:
        """
        Generate all possible combinations of load cases.

        :param args: Variable length argument list of LoadCaseGroup lists.
        return:A list of all generated combinations of load cases.
        """
        generated_combinations = []
        # get all possible combinations
        all_iterables = []
        for load_groups in args:
            all_iterables.append(
                [load_group.combinations for load_group in load_groups]
            )

        combinations = []
        for iterables in all_iterables:
            combinations.extend(
                [flatten_list(combination) for combination in product(*iterables)]
            )

        # get all possible unique combinations
        unique_combinations = []
        for combination in combinations:
            if combination not in unique_combinations:
                unique_combinations.append(combination)

        label = f"{self.limit_state.value.upper()}-{self.combination_type.value}"

        c = 1
        for unique_combination in unique_combinations:
            permanent_cases = [
                case
                for case in unique_combination
                if case.load_type == LoadType.PERMANENT
            ]
            variable_cases = [
                case
                for case in unique_combination
                if case.load_type == LoadType.VARIABLE
            ]

            if variable_cases:
                for i, leading_variable_case in enumerate(variable_cases):
                    # loop through every possible combination of leading + other variable for this unique combination
                    other_variable_cases = variable_cases[:i] + variable_cases[i + 1 :]

                    if self.combination_type == ULSCombination.ALTERNATIVE:
                        generated_combinations.append(
                            DesignLoadCaseCombination(
                                label=f"{label}({c}a)",
                                limit_state=self.limit_state,
                                combination_type=self.combination_type,
                                permanent_cases=permanent_cases,
                                leading_variable_case=leading_variable_case,
                                other_variable_cases=other_variable_cases,
                                alternative_combination=ULSAlternativeCombination.REDUCED_VARIABLE,
                            )
                        )
                        generated_combinations.append(
                            DesignLoadCaseCombination(
                                label=f"{label}({c}b)",
                                limit_state=self.limit_state,
                                combination_type=self.combination_type,
                                permanent_cases=permanent_cases,
                                leading_variable_case=leading_variable_case,
                                other_variable_cases=other_variable_cases,
                                alternative_combination=ULSAlternativeCombination.REDUCED_PERMANENT,
                            )
                        )
                    else:
                        generated_combinations.append(
                            DesignLoadCaseCombination(
                                label=f"{label}({c})",
                                limit_state=self.limit_state,
                                combination_type=self.combination_type,
                                permanent_cases=permanent_cases,
                                leading_variable_case=leading_variable_case,
                                other_variable_cases=other_variable_cases,
                            )
                        )

                    c += 1
            else:  # in case there are only permanent cases
                if self.combination_type == ULSCombination.ALTERNATIVE:
                    generated_combinations.append(
                        DesignLoadCaseCombination(
                            label=f"{label}({c}a)",
                            limit_state=self.limit_state,
                            combination_type=self.combination_type,
                            permanent_cases=permanent_cases,
                            leading_variable_case=None,
                            other_variable_cases=[],
                            alternative_combination=ULSAlternativeCombination.REDUCED_VARIABLE,
                        )
                    )
                    generated_combinations.append(
                        DesignLoadCaseCombination(
                            label=f"{label}({c}b)",
                            limit_state=self.limit_state,
                            combination_type=self.combination_type,
                            permanent_cases=permanent_cases,
                            leading_variable_case=None,
                            other_variable_cases=[],
                            alternative_combination=ULSAlternativeCombination.REDUCED_PERMANENT,
                        )
                    )
                else:
                    generated_combinations.append(
                        DesignLoadCaseCombination(
                            label=f"{label}({c})",
                            limit_state=self.limit_state,
                            combination_type=self.combination_type,
                            permanent_cases=permanent_cases,
                            leading_variable_case=None,
                            other_variable_cases=[],
                        )
                    )
                c += 1

        return generated_combinations
