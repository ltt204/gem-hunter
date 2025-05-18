from typing import Dict, List, Optional, Set, Tuple


def get_variables(cnf: List[List[int]]) -> Set[int]:
    """
    Extract all unique variables from a CNF formula.

    Args:
        cnf: A list of clauses, where each clause is a list of integers.
             Positive integers represent positive literals, negative integers
             represent negative literals.

    Returns:
        A set of unique variables (absolute values of literals).
    """
    variables = set()
    for clause in cnf:
        for literal in clause:
            variables.add(abs(literal))
    return variables
