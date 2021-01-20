import numpy as np
from problemSolving import *


class Job:
    def __init__(self, processing_time, due_date, weight):
        # Those 3 atributes are given
        self.processing_time = processing_time
        self.due_date = due_date
        self.weight = weight

        # self.completition_time = completition_time
        # self.tardiness = self.getTardiness()

    def __str__(self):
        return f"proc_time:{self.processing_time},due_date:{self.due_date},weight:{self.weight}"


class SMTWTproblem:
    def __init__(self, problems, index):
        # receives a data about problems,
        # number of ants (M)
        # an index that indicates the problem to build
        if index < 0 or index >= 125:
            raise ValueError('index must be: 0>=index<125')

        self.jobs = list()

        for i in range(len(problems['processing_time'][0])):
            processing_time = problems['processing_time'][index][i]
            due_date = problems['due_date'][index][i]
            weight = problems['weight'][index][i]
            self.jobs.append(Job(processing_time, due_date, weight))

        self.n_jobs = len(self.jobs)
        # we initialize pheromones to 0#ASI NO SE INICIALIZA, SE USA T0

        self.TDD = self.calculateTEDD()
        self.tau_0 = 1 / (m * self.TDD)

        # we initialize pheromones using tau_0


        self.pheromones = [np.repeat(self.tau_0, self.n_jobs) for _ in range(self.n_jobs)]
        

    def calculateTEDD(self):
        # TEDD is the total tardiness of the schedule that is
        # obtained when the jobs are ordered according to the Earliest Deadline First heuristic

        self.sorted_jobs = sorted(self.jobs, key=lambda x: x.due_date)

        actual_time = 0
        total_tardiness = 0

        for job in self.sorted_jobs:
            total_tardiness += max(0, actual_time - job.due_date)
            actual_time += job.processing_time

        total_tardiness = max(0.00001, total_tardiness)#to avoid division by zero
        return total_tardiness
