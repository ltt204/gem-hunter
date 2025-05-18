def convert_string_to_2D(input_matrix: str) -> list[list[str]]:
    matrix = []
    rows = input_matrix.strip().split("\n")

    for row in rows:
        row = row.replace(", ", "")
        # Convert characters to integers or keep as characters depending on your needs
        # Option 1: Keep as characters
        matrix.append(list(row))

    return matrix
