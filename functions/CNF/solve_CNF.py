from pysat.solvers import Solver


def solve_CNF(matrix, cnf_formula, solver_name: str = "glucose3"):
    """
    Solve the CNF formula using a SAT solver and apply the solution to create a grid with traps and gems.

    Args:
        matrix (list[list[str]]): The 2D matrix representing the game board.
        cnf_formula (CNF): The CNF formula to solve.
        solver_name (str): The SAT solver to use. Default is 'glucose3'.

    Returns:
        list[list[str]]: The solution grid with 'T' for traps, 'G' for gems, and original numbers.
                         Returns None if no solution exists.
    """
    # Initialize the SAT solver
    with Solver(name=solver_name) as solver:
        solver.append_formula(cnf_formula)

        # Solve the CNF formula
        if not solver.solve():
            print("No solution found.")
            return None

        print("\nSolution found!")

        model = solver.get_model()
        # print(f"Model: {model}")

        # Extract rows and columns from the board
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        # Create a new grid to represent the solution
        solution_grid = [["_" for _ in range(cols)] for _ in range(rows)]

        # Convert the model (list of integers) to a set of positive literals for easier lookup
        true_literals = set(lit for lit in model if lit > 0)

        # Function to calculate cell ID from position (same as in get_grid_constraints)
        def cell_id(r, c):
            return r * cols + c + 1  # 1-based indexing

        # Place traps and gems in the solution grid based on the model
        for r in range(rows):
            for c in range(cols):
                cell_id_val = cell_id(r, c)

                # For debugging: print the cell ID and its value
                # print(f"Cell ID: {cell_id_val}, row: {r}, col: {c}")
                # print(f"Cell ID: {cell_id_val}, Value: {matrix[r][c]}")

                # If the cell is a constraint cell (has a number), keep the number
                cell_value = matrix[r][c]
                if cell_value != "_" and cell_value.isdigit():
                    solution_grid[r][c] = cell_value
                else:
                    # Otherwise, it's either a trap (T) or gem (G)
                    if cell_id_val in true_literals:  # Positive literal means trap
                        solution_grid[r][c] = "T"
                    else:  # Negative or absent literal means gem
                        solution_grid[r][c] = "G"

        # Verify the solution
        from functions.helpers.grid_helper import get_grid_constraints

        constraints = get_grid_constraints(matrix)

        all_valid = True
        for cell_id_val, data in constraints.items():
            r, c = data["position"]
            k = data["k"]
            neighbors = data["neighbors"]

            # Count traps in neighbors
            trap_count = sum(1 for neighbor in neighbors if neighbor in true_literals)

            if trap_count != k:
                all_valid = False
                print(f"  INVALID: Cell ({r},{c}) constraint violated!")

        if all_valid:
            print("\nSolution is valid! All constraints are satisfied.")
        else:
            print("\nWARNING: Solution has constraint violations!")

        return solution_grid
