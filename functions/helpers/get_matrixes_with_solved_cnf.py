from itertools import product
from typing import List, Optional


def get_matrix_result(solution, matrix) -> Optional[List[List[str]]]:
    """
    Convert the CNF solution to a matrix representation.

    Args:
        cnf: A list of clauses, where each clause is a list of integers.
        matrix: The original matrix to be filled with traps and gems.

    Returns:
        A matrix with 'T' for traps, 'G' for gems, and original numbers.
    """
    # Create a new grid to represent the solution
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    solution_grid = [["_" for _ in range(cols)] for _ in range(rows)]

    # Fill the solution grid based on the assignment
    for r in range(rows):
        for c in range(cols):
            cell_id_val = r * cols + c + 1  # 1-based indexing
            cell_value = matrix[r][c]
            if cell_value != "_" and cell_value.isdigit():
                solution_grid[r][c] = cell_value
            else:
                if (
                    cell_id_val in solution and solution[cell_id_val]
                ):  # Positive literal means trap
                    solution_grid[r][c] = "T"
                else:
                    solution_grid[r][c] = "G"

    return solution_grid
