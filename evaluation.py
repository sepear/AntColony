from dataReading import readResults, readData
from problemRepresentation import SMTWTproblem
from problemSolving import generateSolution

import time

N_RUNS = 4  # number of times we evaluate a problem


def evaluateSet(data,generations=500):
    best_results = list()  # list with the best result for every problem
    results = list()  # list of lists of results
    for problem_index in range(125):  # for every problem:
        print(f"problema: {problem_index}")
        problem_results = list()
        for run_index in range(4):  # four times
            print(f"\t{run_index}")

            problem = SMTWTproblem(data, problem_index)
            # built inside to reset pheromones

            start = time.time()

            tardiness, route = generateSolution(problem, generations)#TODO: PONER ESTO A NADA O A 500
            print(f"tardiness:{tardiness}")
            problem_results.append(tardiness)
        results.append(problem_results)
        best_results.append(min(problem_results))

    return best_results, results
