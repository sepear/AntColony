from dataReading import readResults, readData
from problemRepresentation import SMTWTproblem
from problemSolving import generateSolution
import matplotlib.pyplot as plt
import time

N_RUNS = 4  # number of times we evaluate a problem


def generatePlot(results,benchmark, dir):
    plt.clf()
    plt.ylabel('best tardiness obtained')
    plt.xlabel('problem')

    plt.plot([i for i in range(len(benchmark))], results, label="Our results ")

    plt.plot([i for i in range(len(benchmark))], benchmark, label="Benchmark ")
    plt.legend()
    plt.title("Comparison between our algorithm and benchmark")
    
    plt.savefig(dir)


def compareResults(our_results, given_results):#address of our results, address of results given

    total_sum = sum(our_results)
    average_difference = (sum(given_results)-total_sum)/(len(given_results)-1)
    print(f"Average difference:{average_difference}")
    print(f"Total sum:{total_sum}")

def evaluateSet(data, generations=500, results_name="default",benchmark_dir="data/wtopt40.txt"):
    filedir = "results/"+results_name+".txt"
    imagedir ="figures/"+results_name+".png"
    best_results = list()  # list with the best result for every problem
    results = list()  # list of lists of results
    for problem_index in range(125):  # for every problem:
        print(f"problema: {problem_index}")
        problem_results = list()
        for run_index in range(N_RUNS):  # four times
            print(f"\t{run_index}")

            problem = SMTWTproblem(data, problem_index)
            # built inside to reset pheromones


            tardiness, route = generateSolution(problem, generations)
            print(f"tardiness:{tardiness}")
            problem_results.append(tardiness)
        results.append(problem_results)
        best_results.append(min(problem_results))

    given_results = readResults(benchmark_dir)
    compareResults(best_results, given_results)
    dataWriter(best_results, filedir)
    generatePlot(best_results, given_results, imagedir)
    return best_results, results


def dataWriter(results, file_address):  # writes best results on a file
    with open(file_address, 'w') as f:
        for item in results:
            f.write(f"{item}\n")
