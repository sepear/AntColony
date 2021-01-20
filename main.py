from dataReading import readResults, readData

from evaluation import evaluateSet, dataWriter

# Press the green button in the gutter to run the script.



if __name__ == '__main__':
    data40 = readData("data/wt40.txt")
    data50 = readData("data/wt50.txt")
    data100 = readData("data/wt100.txt")

    wtopt50 = readResults("data/wtopt50.txt")#examples of reading results
    wtopt40 = readResults("data/wtopt40.txt")
    wtbest100a = readResults("data/wtbest100a.txt")
    wtbest100b = readResults("data/wtbest100b.txt")


    #best_results, results = evaluateSet(data=data40, generations=40, results_name="data40results",benchmark_dir="data/wtopt40.txt")

    best_results, results = evaluateSet(data=data100, generations=40, results_name="data100results",
                                        benchmark_dir="data/wtbest100b.txt")







