from functions.encoders.encode_at_least_k import encode_at_least_k
from functions.encoders.encode_at_most_k import encode_at_most_k


def encode_exactly_k(variables, k):
    """
    Encode the exactly k const raint for a given set of neighbors.

    Parameters:
    neighbors (list): List of neighbors to be encoded.
    k (int): The exact number of neighbors that must be selected.

    Returns:
    pysat.formula.CNF: The CNF formula representing the exactly k constraint.
    """
    cnf = []

    # Edge cases
    if not variables:
        return cnf
    if k < 0 or k > len(variables):
        # Contradiction: add (x) and (¬x)
        if variables:
            cnf.append([variables[0]])
            cnf.append([-variables[0]])
        return cnf

    # At least k True
    cnf.extend(encode_at_least_k(variables, k))
    # At most k True
    cnf.extend(encode_at_most_k(variables, k))

    return cnf
