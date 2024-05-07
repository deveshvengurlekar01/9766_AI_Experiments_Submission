// first install deap using command pip install deap

from deap import base, creator, tools
import numpy as np

# Define problem-specific parameters
num_cities = 4
distance_matrix = np.array([[0, 10, 15, 20],
                            [10, 0, 35, 25],
                            [15, 35, 0, 30],
                            [20, 25, 30, 0]])

# Define fitness and individual classes
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Define functions for initializing individuals and evaluating fitness
def create_individual():
    return np.random.permutation(range(num_cities)).tolist()

def evaluate_individual(individual):
    total_distance = sum(distance_matrix[individual[i], individual[i+1]] for i in range(num_cities - 1))
    total_distance += distance_matrix[individual[-1], individual[0]]  # Return to the starting city
    return total_distance,

# Create Toolbox
toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, create_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluate_individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    population_size = 50
    num_generations = 100

    population = toolbox.population(n=population_size)
    for ind in population:
        ind.fitness.values = toolbox.evaluate(ind)

    for gen in range(num_generations):
        offspring = [toolbox.clone(ind) for ind in population]

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if np.random.rand() < 0.7:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if np.random.rand() < 0.2:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        population[:] = offspring

    best_individual = tools.selBest(population, k=1)[0]
    print("Best solution:", best_individual)
    print("Total distance:", evaluate_individual(best_individual)[0])

if __name__ == "__main__":
    main()
