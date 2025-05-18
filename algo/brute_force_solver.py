import time
from itertools import product
from typing import Dict, List, Optional, Set, Tuple

from functions.helpers.get_variables import get_variables


def solve_cnf_brute_force(cnf: List[List[int]]) -> Optional[Dict[int, bool]]:
    """
    Solve a CNF formula using brute force approach.

    Args:
        cnf: A list of clauses, where each clause is a list of integers.
             Positive integers represent positive literals, negative integers
             represent negative literals.

    Returns:
        A dictionary mapping variables to their truth values if the formula is satisfiable,
        None otherwise.
    """

    global start_time
    start_time = time.time()

    # print(f"Starting brute force solver for CNF: {cnf}")
    # Extract all variables (absolute values of literals)
    variables = get_variables(cnf)
    variables = sorted(list(variables))  # Sort for consistent ordering

    # Generate all possible assignments
    for values in product([False, True], repeat=len(variables)):
        if (time.time() - start_time) > 600:
            print("Timeout: Brute Force solver took too long (over 10 minutes)")
            return None

        # Create a mapping of variable indices to their assigned values
        assignment = {var: val for var, val in zip(variables, values)}

        # Check if this assignment satisfies all clauses
        if all(is_clause_satisfied(clause, assignment) for clause in cnf):
            print(f"Brute force solver took {time.time() - start_time:.4f} seconds")
            return assignment

    # No satisfying assignment found
    return None


def is_clause_satisfied(clause: List[int], assignment: Dict[int, bool]) -> bool:
    """
    Check if a clause is satisfied under the given assignment.

    Args:
        clause: A list of integers representing literals in a clause
        assignment: A dictionary mapping variables to their truth values

    Returns:
        True if the clause is satisfied, False otherwise
    """
    # print(f"Checking clause: {clause} with assignment: {assignment}")
    for literal in clause:
        var = abs(literal)
        is_positive = literal > 0

        # A clause is satisfied if any literal is true
        if assignment[var] == is_positive:
            return True

    # All literals are false
    return False
