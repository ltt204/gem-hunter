import time

from algo.backtracking_solver import solve_cnf_with_backtracking
from algo.brute_force_solver import solve_cnf_brute_force
from functions.CNF.clean_clause import clean_clause
from functions.CNF.gen_CNF import gen_CNF
from functions.CNF.solve_CNF import solve_CNF
from functions.helpers.convert_string_to_2D import convert_string_to_2D
from functions.helpers.get_matrixes_with_solved_cnf import get_matrix_result
from functions.helpers.get_variables import get_variables
from functions.helpers.grid_helper import get_grid_constraints
from functions.helpers.read_file import read_file

INPUT_ROUTE = "input/"
OUTPUT_ROUTE = "output/"
FILE_NAME_PREFIX = "input_"
FILE_NAME_EXTENSION = ".txt"

# Read console for input
file_input = input("Enter the test case: (1, 2 or 3): ")

converted_matrix = convert_string_to_2D(
    read_file(INPUT_ROUTE + FILE_NAME_PREFIX + file_input + FILE_NAME_EXTENSION)
)

print("Working on: ", FILE_NAME_PREFIX + file_input + FILE_NAME_EXTENSION)

# print("Converted 2D Matrix:")
# for row in converted_matrix:
#     print(row)

constraints = get_grid_constraints(converted_matrix)

# Create a single CNF formula for all constraints
final_cnf = gen_CNF(constraints)

# Remove duplicated clauses
original_count = len(final_cnf)
# Convert each clause to a tuple (since lists are not hashable) and use a set to remove duplicates
unique_clauses = clean_clause(final_cnf).clauses

# Convert back to list of lists
final_cnf = [list(clause) for clause in unique_clauses]

print("\nFinal CNF formula has", len(final_cnf), "clauses")

print("Before clean:", original_count, "clauses")
print("After  clean:", len(unique_clauses), "clauses")

print("==" * 20)

# Solve the CNF formula using a SAT solver
print("\nSolving CNF formula with Pysat...")
start = time.time()
solution = solve_CNF(converted_matrix, final_cnf)
end = time.time()
output_content = ""
if solution != None:
    result = get_matrix_result(solution, converted_matrix)
    for row in result:
        output_content += ", ".join(row) + "\n"
    print(output_content)

output_name = "output" + "_" + file_input + ".txt"
print("Output file name: ", output_name)
with open(OUTPUT_ROUTE + output_name, "a") as f:
    f.truncate(0)  # Clear the file if it's not empty
    f.write(output_content)

print("==" * 20)

print("\nSolving CNF formula with Backtracking...")
solution = solve_cnf_with_backtracking(final_cnf)
if solution != None:
    result = get_matrix_result(solution, converted_matrix)
    for row in result:
        print(", ".join(row))

print("==" * 20)

print("\nSolving CNF formula with Brute force...")
solution = solve_cnf_brute_force(final_cnf)
if solution != None:
    result = get_matrix_result(solution, converted_matrix)
    for row in result:
        print(", ".join(row))
