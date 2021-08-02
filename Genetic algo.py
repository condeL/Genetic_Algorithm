import random

#funtion to generate the intial population based on size
def generate_population(size):
    initial_population = []
    for i in range(size):
        chromosome = []
        for j in range(20):
            chromosome.append(random.randint(0,1))
        initial_population.append(chromosome)
    return initial_population

#function to measure the fitness of the chromosome by counting the number of 1s
def measure_fitness(chromosome):
    fit = 0
    for x in chromosome:
        if x == 1:
            fit += 1
    return fit

#function to choose chromosomes randomly based on fitness
def roulette(population, total_fitness):
    accumulation = 0

    roulette_draw = random.random()

    for x in population:
        fitness = measure_fitness(x)
        accumulation += fitness/total_fitness
        if roulette_draw <= accumulation:
            return x
    return population[random.randint(0,99)]

#function for the crossover that cuts each chromosomes in half and joins them together
def crossover(chromosomeX, total_fitness):
    chromosomeX = chromosomeX[:10]

    chromosomeY = roulette(population, total_fitness)
    chromosomeY = chromosomeY[-10:]

    return chromosomeX + chromosomeY

#mutation function that flips bits randomly
def mutate(chromosome):
    mutation_rate = 0.001
    #mutation_rate = 0
    #mutation_rate = 0.5
    for x in range(len(chromosome)):
        if mutation_rate >= random.random():
            if chromosome[x] == 0:
                chromosome[x] = 1
            elif chromosome[x] == 1:
                chromosome[x] = 0
    return chromosome

#function to populate the new generation
def next_generation(old_generation, size):
    new_generation = []
    crossover_rate = 0.7
    #crossover_rate = 0
    #crossover_rate = 0.5

    total_fitness = 0

    for x in range(len(old_generation)):
        fitness = measure_fitness(old_generation[x])
        total_fitness += fitness

    for i in range(size):
        roulette(population, total_fitness)
        chromosomeX = roulette(population, total_fitness)
        if crossover_rate >= random.random():
            new_chromosome = crossover(chromosomeX,total_fitness)
        else:
            new_chromosome = chromosomeX

        new_chromosome = mutate(new_chromosome)

        new_generation.append(new_chromosome)

    return new_generation

#function that checks if an optimal chromosome is found
def checkValidity(population):
    isvalid = False
    for chromosome in population:
        for x in range(len(chromosome)):
            if chromosome[x] == 0:
                isvalid = False
                break
            elif x == 19:
                isvalid = True
                return isvalid
    return isvalid


#start of the program

population_size = 100
population = generate_population(population_size)

i = 1
while True:
    print(f"GENERATION {i}")

    for individual in population:
        print(individual)

    if checkValidity(population):
        print(f"It took {i} generations to find a fitting gene")
        break

    i += 1
    population = next_generation(population, population_size)

