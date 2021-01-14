from dataReading import readResults, readData

from evaluation import evaluateSet

# Press the green button in the gutter to run the script.

import copy

if __name__ == '__main__':
    data40 = readData("data/wt40.txt")
    data50 = readData("data/wt50.txt")
    data100 = readData("data/wt100.txt")

    wtopt50 = readResults("data/wtopt50.txt")
    wtopt40 = readResults("data/wtopt40.txt")
    wtbest100a = readResults("data/wtbest100a.txt")
    wtbest100b = readResults("data/wtbest100b.txt")

    best_results, results = evaluateSet(data40,20)

    #test_problem = SMTWTproblem(data40, 124)

    #test_problem2 = SMTWTproblem(data100, 40)
    #print("The processing_time of job number 3 (starting from 0) of the problem 0 is:")
    #print(test_problem.jobs[3].processing_time)





