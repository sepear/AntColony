from dataReading import readResults, readData
from problemRepresentation import SMTWTproblem

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data40 = readData("data/wt40.txt")
    data50 = readData("data/wt50.txt")
    data100 = readData("data/wt100.txt")
    # print(data40['processing_time'][0])
    # print(data40['due_date'][0])
    # print(data40['weight'][0])
    wtopt50 = readResults("data/wtopt50.txt")
    wtopt40 = readResults("data/wtopt40.txt")
    wtbest100a = readResults("data/wtbest100a.txt")
    wtbest100b = readResults("data/wtbest100b.txt")
    # print(wtopt50)
    # print(wtopt40)
    # print(wtbest100a)
    # print(wtbest100b)

    test_problem = SMTWTproblem(data40, 0)

    test_problem2 = SMTWTproblem(data100, 40)
    print("The processing_time of job number 3 (starting from 0) of the problem 0 is:")
    print(test_problem.jobs[3].processing_time)
    print("#####################")
    for job in test_problem2.jobs:
        print(job)
    print("#####################")
    for job in test_problem2.sorted_jobs:
        print(job)




