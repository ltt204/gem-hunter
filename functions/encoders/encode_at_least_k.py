def encode_at_least_k(variables, k, next_var=None):
    """
    Encode the at least k constraint for a given set of neighbors.

    Parameters:
    neighbors (list): List of neighbors to be encoded.
    k (int): The minimum number of neighbors that must be selected.

    Returns:
    pysat.formula.CNF: The CNF formula representing the at least k constraint.
    """
    # Create a new CNF formula
    n = len(variables)
    cnf = []

    # Trivial cases
    if k <= 0:
        return cnf  # Always satisfied
    if k > n:
        # Contradiction: add (x) and (¬x)
        if variables:
            cnf.append([variables[0]])
            cnf.append([-variables[0]])
        return cnf

    # For every subset of n-k+1 variables, at least one must be True
    # (i.e., for all S ⊆ variables, |S| = n-k+1: OR v in S)
    from itertools import combinations

    for subset in combinations(variables, n - k + 1):
        cnf.append(list(subset))

    return cnf
