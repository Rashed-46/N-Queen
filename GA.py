import random

# Problem size
N = 8
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
MAX_GENERATIONS = 1000

def generate_individual():
    return random.sample(range(N), N)

def generate_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def fitness(individual):
    non_attacking = 0
    for i in range(N):
        for j in range(i + 1, N):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != j - i:
                non_attacking += 1
    return non_attacking

def select_parent(population):
    tournament = random.sample(population, 5)
    return max(tournament, key=fitness)

def crossover(parent1, parent2):
    cut = random.randint(1, N - 2)
    child = parent1[:cut] + [x for x in parent2 if x not in parent1[:cut]]
    return child

def mutate(individual):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(N), 2)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm():
    population = generate_population()
    max_fitness = N * (N - 1) // 2

    for generation in range(MAX_GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)

        if fitness(population[0]) == max_fitness:
            print(f"Solution found in generation {generation}")
            return population[0]

        new_population = population[:10]  # elitism

        while len(new_population) < POPULATION_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = new_population

    print("No solution found.")
    return None

solution = genetic_algorithm()
print("Solution:", solution)
