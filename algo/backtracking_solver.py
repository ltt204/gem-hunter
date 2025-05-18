import time
from itertools import product
from typing import Dict, List, Optional, Set, Tuple

from functions.helpers.get_variables import get_variables

# Global variables to track timeout state
start_time = 0.0
timeout_reported = False


def backtracking_pruning(cnf: List[List[int]], assignment, var_index, n):
    """
    Backtracking algorithm to solve a CNF (Conjunctive Normal Form) problem.

    Args:
        cnf (List[List[int]]): The CNF formula represented as a list of clauses.
        assignment (Dict[int, bool]): Current variable assignments.
        var_index (int): Current index in the CNF formula.
        n (int): Total number of variables.

    Returns:
        Optional[Dict[int, bool]]: A satisfying assignment if found, otherwise None.
    """

    global start_time, timeout_reported

    # Get the current time to check for timeout
    if (time.time() - start_time) > 600:
        if not timeout_reported:
            print("Timeout: Backtracking solver took too long (over 10 minutes)")
            timeout_reported = True
        return False
    # Base case: all variables have been assigned
    if var_index == n:
        return all(
            any(
                (lit > 0 and assignment[abs(lit) - 1] is True)
                or (lit < 0 and assignment[abs(lit) - 1] is False)
                for lit in clause
            )
            for clause in cnf
        )

    for value in [True, False]:
        assignment[var_index] = value

        # Pruning: Check if the current partial assignment already violates any clause
        conflict = False
        for clause in cnf:
            clause_satisfied = False
            unassigned = False

            for lit in clause:
                var = abs(lit) - 1  # Convert to 0-based indexing

                # Skip literals that reference variables we haven't assigned yet
                if var > var_index:
                    unassigned = True
                    continue

                # Check if this literal is satisfied
                if (lit > 0 and assignment[var] is True) or (
                    lit < 0 and assignment[var] is False
                ):
                    clause_satisfied = True
                    break

            # If clause has no satisfied literals and all its variables are assigned,
            # then this assignment cannot lead to a solution
            if not clause_satisfied and not unassigned:
                conflict = True
                break

        if not conflict:
            if backtracking_pruning(cnf, assignment, var_index + 1, n):
                return True

        # Backtrack: Undo this assignment
        assignment[var_index] = None

    # No solution found with this partial assignment
    return False


def solve_cnf_with_backtracking(cnf: List[List[int]]):
    """
    Solve a CNF formula using backtracking.

    Args:
        cnf: A list of clauses, where each clause is a list of integers.
             Positive integers represent positive literals, negative integers
             represent negative literals.

    Returns:
        A dictionary mapping variables to their truth values if the formula is satisfiable,
        None otherwise.
    """
    variables = get_variables(cnf)
    n = max(variables) if variables else 0  # Number of variables
    assignment = [None] * n

    # Reset timeout state
    global start_time, timeout_reported
    start_time = time.time()
    timeout_reported = False

    if backtracking_pruning(cnf, assignment, 0, n):
        print(f"Backtracking solver took {time.time() - start_time:.4f} seconds")
        # Convert to dictionary format for return value (1-based indexing)
        return {i + 1: val for i, val in enumerate(assignment) if val is not None}
    else:
        return None
