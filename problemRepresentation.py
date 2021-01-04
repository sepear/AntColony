class Job:
    def __init__(self, processing_time, due_date, weight):
        # Those 3 atributes are given
        self.processing_time = processing_time
        self.due_date = due_date
        self.weight = weight

        # self.completition_time = completition_time
        # self.tardiness = self.getTardiness()

    # def getTardiness(self):
    #    return self.weight * max(0, self.completition_time - self.due_date)


class SMTWTproblem:
    def __init__(self, problems, index):  # receives a data about problems and
        # an index that indicates the problem to build

        if index < 0 or index >= 125:
            raise ValueError('index must be: 0>=index<125')

        self.jobs = list()

        for i in range(len(problems['processing_time'][0])):
            processing_time = problems['processing_time'][index][i]
            due_date = problems['due_date'][index][i]
            weight = problems['weight'][index][i]
            self.jobs.append(Job(processing_time, due_date, weight))

    #def getTotalTardiness(self):
    #    total_tardiness = 0  # summation stored here
    #    for job in self.jobs:
    #        total_tardiness += job.getTardiness()
    #    return total_tardiness
