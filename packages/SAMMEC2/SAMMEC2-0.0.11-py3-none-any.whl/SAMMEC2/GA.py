import numpy as np
from imblearn.metrics import geometric_mean_score
from sklearn.metrics import accuracy_score, matthews_corrcoef
from SAMMEC2 import AdaBoostClassifier_C2V2
import operator

class GA_SAMMEC2():
    def __init__(self, cost=None, n_class=3, lim=0.9, err=0.005, size=10, generations=5, n_estimators=200,
                 random_state=None):
        self.n_class = n_class
        self.size = size
        self.generations = generations
        self.lim = lim
        self.err = err
        self.cost = cost
        self.random_state = random_state
        self.n_estimators = n_estimators

    # first generate population
    def generate_population(self, size):
        population = []
        if self.cost == None:
            # np.random.seed(self.random_state)
            for i in range(size):
                k = 0.999
                individual = [k]
                for j in range(self.n_class - 1):
                    a = np.random.uniform(self.lim, k)
                    individual.append(a)
                    k = a
                individual.reverse()
                population.append(individual)
        else:
            for j in range(size):
                c = 0.999
                v = [0.999]
                individual = self.cost
                for i in range(len(individual) - 1):
                    vv = max(self.lim, individual[len(individual) - i - 2] + np.random.uniform(-self.err, self.err))
                    vvv = min(vv, c)
                    v.append(vvv)
                    c = vvv
                v.reverse()
                population.append(v)
        return population

    def apply_function(self, Xtrain, Xtest, ytrain, ytest, individual):

        SAMME_C2 = AdaBoostClassifier_C2V2(n_estimators=self.n_estimators,
                                                   random_state=self.random_state, cost=individual)
        SAMME_C2.fit = SAMME_C2.fit(Xtrain, ytrain)
        y_pred_SAMMEC2 = SAMME_C2.fit.predict(Xtest)
        return geometric_mean_score(ytest, y_pred_SAMMEC2, correction=0.0001), accuracy_score(ytest, y_pred_SAMMEC2)
        # return matthews_corrcoef(ytest, y_pred_SAMMEC2), accuracy_score(ytest, y_pred_SAMMEC2)

    # sorted_population, fitness_sum

    def choice_by_roulette(self, sorted_population, fitness_sum, i):
        np.random.seed(self.random_state + i)
        draw = np.random.uniform(0, 1)
        accumulated = 0
        for individual in sorted_population:
            fitness = individual[1]
            probability = fitness / fitness_sum
            accumulated += probability

            if draw <= accumulated:
                return individual[0]

    def sort_population_by_fitness(self, previous_function):
        return sorted(previous_function, key=operator.itemgetter(1))

    def crossover(self, individual_a, individual_b):
        z = []
        for i in range(len(individual_a)):
            z.append((individual_a[i] + individual_b[i]) / 2)
        return z

    def mutate(self, individual, i):
        # np.random.seed(self.random_state+i)
        c = 0.999
        v = [0.999]
        for i in range(len(individual) - 1):
            vv = max(self.lim, individual[len(individual) - i - 2] + np.random.uniform(-self.err, self.err))
            vvv = min(vv, c)
            v.append(vvv)
            c = vvv
        v.reverse()
        return v

    def make_next_generation(self, previous_function):
        next_generation = []
        # sorted_by_fitness_population = self.sort_population_by_fitness(previous_function)
        sorted_by_fitness_population = self.sort_population_by_fitness(previous_function)[-self.size:]
        # population_size = len(previous_function)
        population_size = self.size
        # fitness_sum = sum(individual[1] for individual in previous_function)
        fitness_sum = sum(individual[1] for individual in sorted_by_fitness_population)

        for i in range(population_size):
            first_choice = self.choice_by_roulette(sorted_by_fitness_population, fitness_sum,
                                                   i + np.random.randint(1, 10000000, size=1))
            second_choice = self.choice_by_roulette(sorted_by_fitness_population, fitness_sum,
                                                    i + np.random.randint(1, 10000000, size=1))

            individual = self.crossover(first_choice, second_choice)
            individual = self.mutate(individual, i)
            next_generation.append(individual)

        return next_generation

    def fit(self, Xtrain, ytrain, Xtest, ytest):
        gen = self.generations
        population = self.generate_population(size=self.size)  # function

        i = 1
        # fuction_stored=[]
        function = []
        while True:
            print(f" GENERATION {i}")
            # function=[]

            for individual in population:
                metric = self.apply_function(Xtrain, Xtest, ytrain, ytest, individual)
                item = (individual, metric[0])
                function.append(item)
                print(item, metric[1])

            # fuction_stored.append(function)

            if i == gen:
                break

            i += 1

            population = self.make_next_generation(function)

        best_individual = self.sort_population_by_fitness(function)[-1][0]
        print("\n🔬 FINAL RESULT")
        print(best_individual, self.apply_function(Xtrain, Xtest, ytrain, ytest, best_individual))


