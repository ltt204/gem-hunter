def get_grid_constraints(matrix):
    """
    Extract constraint values (k) and neighboring cells from a 2D grid.

    Args:
        matrix (list[list[str]]): 2D grid with numbers and '_' representing cells

    Returns:
        dict: Dictionary mapping cell positions to their constraints and neighbors
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    constraints = {}

    # Function to calculate unique cell ID
    def cell_id(r, c):
        return r * cols + c + 1  # 1-based indexing

    # Function to get valid neighbors
    def get_neighbors(r, c):
        neighbors = []
        # Check all 8 adjacent cells (horizontally, vertically, and diagonally)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                # Skip the cell itself
                if dr == 0 and dc == 0:
                    continue

                nr, nc = r + dr, c + dc
                # Check if neighbor is within bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbors.append(cell_id(nr, nc))
        return neighbors

    # Process each cell in the matrix
    for r in range(rows):
        for c in range(cols):
            cell = matrix[r][c]
            if cell != "_" and cell.isdigit():  # Cell has a numeric constraint
                cell_position = cell_id(r, c)
                k_value = int(cell)
                neighbors = get_neighbors(r, c)

                # Minus 1 to convert to 0-based index for the dictionary
                constraints[cell_position] = {
                    "k": k_value,
                    "neighbors": neighbors,
                    "position": (r, c),
                }

    return constraints
