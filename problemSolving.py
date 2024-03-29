"""
The parameters used for the test runs are: α = 1, β =
1, ρ = 0.1, q 0 ∈ {0, 0.9}. The number of ants in every
generation was m = 20. Every test was performed with
4 runs on every instance. Every run was stopped after
500 generations.


"""
import random
import numpy as np
import copy
import time

m = 20  # number of ants

q0 = 0.9  # parameter for the algorithm; a probability

alpha = 1  # relative influence of pheromone values
beta = 1  # relative influence of heuristic value

p = 0.1  # constant for the pheromone update


def optSwap_2(route, i, k):  # performs a 2-opt given i and k
    new_route = list()

    new_route += route[:i]

    middle_part = route[i:k]
    middle_part.reverse()

    new_route += middle_part
    new_route += route[k:]

    return new_route


def localOpt(problem, route, tardiness):  # tries every 2-opt swap and returns the best one

    best_route = route
    best_tardiness = tardiness

    for i in range(0, (len(route) - 1)):
        for k in range(i + 1, len(route)):
            new_route = optSwap_2(route, i, k)
            new_tardiness = evaluateRoute(problem, new_route)
            if new_tardiness < best_tardiness:
                best_route = new_route
                best_tardiness = new_tardiness

    return best_route, best_tardiness


def evaluateRoute(problem, route):
    totalWeightedTardiness = 0
    actual_time = 0

    for i in route:
        this_job = problem.jobs[i]
        totalWeightedTardiness += this_job.weight * max(0, actual_time - this_job.due_date)
        actual_time += this_job.processing_time

    return totalWeightedTardiness


def calculateHeuristicValue(T, job):

    heuristic = job.weight * (1 / (max(T + job.processing_time, job.due_date) - T))

    return heuristic


def generateRoute(problem, local_pheromones):  # genera la ruta de una hormiga

    S = [index for index in range(problem.n_jobs)]  # indices of available jobs to select next
    # when we select a next job, we eliminate it from S

    route = []  # list with route indices ordered by selection

    T = 0  # total processing time of all jobs already scheduled

    for schedule_position in range(problem.n_jobs):
        if random.random() <= q0:  # camino A)

            start1 = time.time()

            best_index = 0
            best_value = -float('Inf')
            for job_index in S:
                sumtkj = np.sum(local_pheromones[job_index])
                nkj = (calculateHeuristicValue(T, problem.jobs[job_index]))
                value = (sumtkj ** alpha) * (nkj ** beta)

                if value > best_value:
                    best_index = job_index
                    best_value = value

            next_job = best_index  # EN ESTE PUNTO SE TOMA EL TRABAJO BEST_INDEX

            end1 = time.time()
            total = end1 - start1
            # print(f"tiempo camino A: {total}")

        else:  # camino B)

            start1 = time.time()

            pj = []  # probabilidad de j

            numerators = {
                h: ((np.sum(local_pheromones[h]) ** alpha) * (calculateHeuristicValue(T, problem.jobs[h]) ** beta))
                for h in S}#a dictionary index_numerator
            denominator = np.sum(list(numerators.values()))

            for job_index in S:
                nij = (calculateHeuristicValue(T, problem.jobs[job_index]))

                pj.append( numerators[job_index] / denominator)
            #print(f"suma probabilidades{sum(pj)}")
            next_job = np.random.choice(S, p=pj)  # choice from S using pj probability distribution

            end1 = time.time()
            total = end1 - start1
            #print(f"tiempo camino B: {total}")
            # AQUÍ SE ESCOJE PROBABILISTICAMENTE EL SIGUIENTE TRABAJO, MIRAR FUERTE LO DE ABAJO
            # https: // docs.scipy.org / doc / numpy - 1.13.0 / reference / generated / numpy.random.choice.html

        # ACTUALIZAMOS LA FEROMONA DE FORMA LOCAL

        local_pheromones[next_job][schedule_position] = (1 - p) * local_pheromones[next_job][schedule_position] \
                                                        + p * problem.tau_0

        # SE HACEN ACTUALIZACIONES LOCALES, GLOBALES SOLO CON LA MEJOR

        T += problem.jobs[next_job].processing_time  # Updating T adding the selected job processing time
        S.remove(next_job)  # eliminamos la tarea escogida
        route.append(next_job)  # lo añadimos a la lista con los indices de la ruta

    return route


# una hormiga usa información heuristica e información de feromona para construir su solución
def generateSolution(problem, generations=500):
    absolute_best_route = []
    absolute_best_TWTardiness = float('Inf')

    evaporation = lambda x: (1 - p) * x

    convergence_list = list()  # here we add the best known each generation to see convergence
    for generation in range(generations):  # for every generation:
        print(f"\t\tgeneration:{generation}")
        best_route = []
        best_TWTardiness = float('Inf')
        # we are looking for small numbers

        local_pheromones = copy.deepcopy(problem.pheromones)  # hacemos un deepcopy de las feromonas actuales,
        # que se usará de forma local en toda la generación

        for _ in range(m):  # for every ant:

            route = generateRoute(problem, local_pheromones)

            TWTardiness = evaluateRoute(problem, route)

            if TWTardiness < best_TWTardiness:
                best_TWTardiness = TWTardiness
                best_route = route

        for ferom_job in problem.pheromones:  # Evaporation
            ferom_job = evaporation(ferom_job)

        best_route, best_TWTardiness = localOpt(problem, best_route, best_TWTardiness)

        for schedule_position in range(len(best_route)):  # Pheromone uptade
            actual_job = best_route[schedule_position]
            problem.pheromones[actual_job][schedule_position] = problem.pheromones[actual_job][schedule_position] \
                                                                + p * (1 / max(0.00001, best_TWTardiness))

        if best_TWTardiness < absolute_best_TWTardiness:
            absolute_best_TWTardiness = best_TWTardiness
            absolute_best_route = best_route
        convergence_list.append(absolute_best_TWTardiness)

    return absolute_best_TWTardiness, absolute_best_route
