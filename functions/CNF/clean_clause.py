from pysat.formula import CNF

from functions.encoders.encode_exactly_k import encode_exactly_k


def clean_clause(cnf_clauses) -> CNF:
    def is_taut(clause):
        s = set(clause)
        return any(-lit in s for lit in s)

    def subsumption_elimination(clauses):
        subsumed = set()
        clauses_set = [set(cl) for cl in clauses]
        for i, ci in enumerate(clauses_set):
            for j, cj in enumerate(clauses_set):
                if i != j and ci.issubset(cj):
                    subsumed.add(tuple(cj))
        return [list(clause) for clause in clauses_set if tuple(clause) not in subsumed]

    """
    Remove duplicate clauses from the CNF formula.
    
    Args:
        cnf (CNF): The CNF formula to clean.
        
    Returns:
        CNF: A new CNF formula with duplicate clauses removed.
    """
    # Convert each clause to a tuple (since lists are not hashable) and use a set to remove duplicates
    unique_clauses = set(tuple(sorted(clause)) for clause in cnf_clauses)

    # Convert back to list of lists
    cleaned_clauses = [list(clause) for clause in unique_clauses]

    # Create a new CNF object with the cleaned clauses
    cleaned_cnf = CNF()
    cleaned_cnf.extend(cleaned_clauses)

    # Remove tautological clauses
    cleaned_cnf.clauses = [
        clause for clause in cleaned_cnf.clauses if not is_taut(clause)
    ]

    # Remove subsumed clauses
    cleaned_cnf.clauses = subsumption_elimination(cleaned_cnf.clauses)

    # Remove empty clauses
    cleaned_cnf.clauses = [clause for clause in cleaned_cnf.clauses if clause]

    return cleaned_cnf
