from functions.encoders.encode_exactly_k import encode_exactly_k


def gen_CNF(constraints):
    all_clauses = []
    for cell_id, data in constraints.items():
        k = data["k"]
        neighbors = data["neighbors"]

        # Giả sử encode_exactly_k trả về list các clause (list of list of int)
        clauses = encode_exactly_k(
            neighbors, k
        )  # implement encode_exactly_k theo tổ hợp hoặc pysat CardEnc

        all_clauses.extend(clauses)

    # Loại bỏ clause trùng (tuỳ chọn)
    unique_clauses = []
    seen = set()
    for cl in all_clauses:
        cl_tuple = tuple(sorted(cl))
        if cl_tuple not in seen:
            seen.add(cl_tuple)
            unique_clauses.append(cl)

    return unique_clauses
