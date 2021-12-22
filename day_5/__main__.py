import os

from .solution import part_1_solution, part_2_solution
from util import retrieve_input_data

if __name__ == "__main__":
    inputdata = retrieve_input_data(os.path.dirname(os.path.abspath(__file__)) + "/input.txt")
    p1_solution = part_1_solution(inputdata)
    print(f"Part 1 Solution: {p1_solution}")

    p2_solution = part_2_solution(inputdata)
    print(f"Part 2 Solution: {p2_solution}")
