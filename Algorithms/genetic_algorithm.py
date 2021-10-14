import random
# 3x + 2y + z + q = 34
# 1 <= x, y, z, q <= 20
class PT():
    def __init__(self):
        self.n_generation = 10000
        self.n_population = 6
        self.r_crossover = 0.8
        self.r_mutation = 0.02
        self.r_reproduce = 0.18
        self.n_gene = 4
        # constraint values of chromosome
        self.max_chromosome = 20
        self.min_chromosome = 1
    def objective(self,gene: list[int]) -> int:
        # f(x, y, z, q) = | 3x + 2y + z + q | - 34
        return abs(3 * gene[0] + 2 * gene[1] + gene[2] + gene[3] - 34)


    def initial(self) -> list[list[int]]:
        population: list[list[int]] = []
        for i in range(self.n_population):
            population.append([])
            for j in range(self.n_gene):
                r = random.randint(self.min_chromosome,self.max_chromosome)
                population[i].append(r)

        return population


    def evaluate(self,population) -> list[int]:
        return [self.objective(c) for c in population]


    def selection(self,population: list[list[int]], scores: list[int]) -> None:
        temp = scores.copy()
        temp.sort()
        threshold = temp[round(self.n_population * (1 - self.r_reproduce))]

        for i in range(self.n_population):
            if scores[i] > threshold:
                # reproduction
                reproduce_candidate_index = random.randint(0, self.n_population - 1)
                population[i] = population[reproduce_candidate_index].copy()


    def crossover(self,p1: list[int], p2: list[int], ):
        pt = random.randint(1, self.n_gene - 1)

        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]

        return [c1, c2]


    def mutation(self,gene: list[int]):
        if random.random() <= self.r_mutation:
            index = random.randint(0,self.n_gene - 1)
            new_value = gene[index]

            while new_value == gene[index]:
                new_value = random.randint(self.min_chromosome, self.max_chromosome)

            gene[index] = new_value


    def genetic_algorithm(self):
        population = self.initial()
        best_generation = 0
        best_value = self.objective(population[0])
        gen = 0

        for gen in range(self.n_generation):
            children: list[list[int]] = []
            # Evaluate
            scores = self.evaluate(population)
            # Check for best solution
            for i in range(self.n_population):
                if scores[i] < best_value:
                    best_generation = population[i]
                    best_value = scores[i]

            self.selection(population, scores)
            for i in range(0, self.n_population, 2):
                p1, p2 = population[i], population[i + 1]
                for c in self.crossover(p1, p2):
                    self.mutation(c)
                    children.append(c)
            population = children
            if best_value == 0:
                break
        return [best_generation, best_value, gen + 1]

Pt=PT();
best, val, g = Pt.genetic_algorithm()
print('\nBest: ', best)
print('Value: ', val)
print('Generation: ', g)
