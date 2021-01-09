"""
The parameters used for the test runs are: α = 1, β =
1, ρ = 0.1, q 0 ∈ {0, 0.9}. The number of ants in every
generation was m = 20. Every test was performed with
4 runs on every instance. Every run was stopped after
500 generations.


"""
import random
import numpy as np

m=20 #number of ants

q0=0.4 #parameter for the algorithm; a probability

alpha=1 #relative influence of pheromone values
beta=1 #relative influence of heuristic value

p=0.1 #constant for the pheromone update



#para cada posicion en la planificación y cada trabajo, hay una información de feromona
#t_ij, donde i es posicion en la planificacion y j el trabajo

#se usa el sumatorio de todas las posiciones para un mismo trabajo
def calculateHeuristicValue(T, job):

    #TODO: AQUI TENGO DUDA DE COMO VA LO DE "MULTIPLICAMOS TODO VALOR POR W_j"
    # DE MOMENTO PUESTO DE FORMA CHAPUZA

    heuristic= job.weight*(1/(max(T+job.processing_time,job.due_date)-T))

    return heuristic



def generateRoute(problem):#genera la ruta de una hormiga

    S = [index for index in range(problem.n_jobs)]#indices of available jobs to select next
    #when we select a next job, we eliminate it from S

    schedule_place=0#actual position to calculate in the schedule
    T=0#total processing time of all jobs already scheduled


#TODO: ESTO VA CON UN BUCLE PARA CADA SCHEDULE PLACE(TANTAS COMO TRABAJOS)
    if random.random() <=q0:#camino A)
        """
        se selecciona el siguiente:
        maximo trabajo tal que: 
        (sumatorio de feromonas)^alpha * (heuristica de ese trabajo en ese punto)^beta
        
        """
        best_index=0
        best_value=0
        for job_index in S:

            value= (np.sum(problem.pheromones[job_index]))^alpha \
            *(calculateHeuristicValue(T, problem.jobs[job_index]))

            if value>best_value:
                best_index = job_index
                best_value = value

        next_job=best_index #EN ESTE PUNTO SE TOMA EL TRABAJO BEST_INDEX

    else:#camino B)

        #AQUÍ SE ESCOJE PROBABILISTICAMENTE EL SIGUIENTE TRABAJO, MIRAR FUERTE LO DE ABAJO
        #https: // docs.scipy.org / doc / numpy - 1.13.0 / reference / generated / numpy.random.choice.html
        #TODO: AQUÍ TENGO QUE CALCULAR EL SIGUIENTE CON LAS PROBABILIDADES


    #TODO:MIRAR LA ACTUALIZACIÓN DE LA FEROMONA MAS EN PROFUNDIDAD
#una hormiga usa información heuristica e información de feromona para construir su solución
