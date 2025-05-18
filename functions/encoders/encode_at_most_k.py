def encode_at_most_k(variables, k, next_var=None):
    """
    Encode the at most k constraint for a given set of neighbors.

    Parameters:
    neighbors (list): List of neighbors to be encoded.
    k (int): The maximum number of neighbors that can be selected.

    Returns:
    pysat.formula.CNF: The CNF formula representing the at most k constraint.
    """
    # Create a new CNF formula
    n = len(variables)
    cnf = []

    # Trivial cases
    if k >= n:
        return cnf  # Always satisfied
    if k < 0:
        # Contradiction: add (x) and (¬x)
        if variables:
            cnf.append([variables[0]])
            cnf.append([-variables[0]])
        return cnf

    # Pairwise encoding for at most 1
    if k == 1:
        for i in range(n):
            for j in range(i + 1, n):
                cnf.append([-variables[i], -variables[j]])
        return cnf

    # General case: at most k (pairwise for k=1, combinatorial for k>1)
    # For every subset of k+1 variables, at least one must be False
    from itertools import combinations

    for subset in combinations(variables, k + 1):
        cnf.append([-v for v in subset])

    return cnf
