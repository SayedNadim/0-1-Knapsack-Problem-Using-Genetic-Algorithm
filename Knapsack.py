import random
from functools import reduce
from itertools import compress, chain
from random import randint

from bitarray import bitarray


class Knapsack:
    def __init__(self, weights, profits, optimal_best, num_genes, max_weight, num_iterations):
        self.weights = weights
        self.itemlen = len(weights)
        self.profits = profits
        self.num_genes = num_genes
        self.genes = num_genes * [None]  # Making list with none values according to the population number
        self.max_weight = max_weight
        self.num_iterations = num_iterations
        self.optimal_best = optimal_best

    def random_boolean_list(self, num_of_bools):
        """
        Function to generate random boolean list for randomizing genes
        :param num_of_bools: Number of items
        :return: Randomized boolean list
        """
        return [random.choice([True, False]) for i in range(0, num_of_bools)]

    def randomize_genes(self):
        """
        Generates randomized population
        :return: Randomized population
        """
        generated_genes = self.num_genes * [None]
        for i in range(0, self.num_genes):
            generated_genes[i] = bitarray(self.random_boolean_list(self.itemlen))
        return generated_genes

    def compute_temp_fitness_for_population(self, to_reduce, population):
        """
        Computes fitness for population/population
        :param to_reduce: Parameters to be reduced
        :param population: Population
        :return: Fitness for population
        """
        compressed = compress(to_reduce, population)
        return reduce(lambda x, y: x + y, compressed, 0)

    def crossover(self, bitarr1, bitarr2):
        r = randint(1, self.itemlen)
        return bitarr1[:r] + bitarr2[r:], bitarr2[:r] + bitarr1[r:]

    def paired_children(self, iterable):
        i = iter(iterable)
        while True:
            yield next(i), next(i)

    def mutate(self, bitarr, probability):
        # random bit flip
        for i in range(0, self.itemlen):
            if random.random() < probability:
                bitarr[i] = not bitarr[i]
        return bitarr

    def generate_children(self, population_list):
        children_list = self.num_genes * [None]
        i = 0
        for ba1, ba2 in self.paired_children(population_list):
            child1, child2 = self.crossover(ba1, ba2)
            mut_child1 = self.mutate(child1, 0.7)
            mut_child2 = self.mutate(child2, 0.3)
            children_list[i] = mut_child1
            children_list[i + 1] = mut_child2
            i = i + 2
        return children_list

    def compute_weights_values(self, population_list):
        fitness_size = self.num_genes * 2
        values_list = fitness_size * [None]
        for index, a_gene in enumerate(population_list):
            canidate = True
            value = self.compute_temp_fitness_for_population(self.profits, a_gene)
            weight = self.compute_temp_fitness_for_population(self.weights, a_gene)
            if weight > self.max_weight:
                canidate = False
            values_list[index] = (a_gene, value, weight, canidate)  # profit, weight
        maximized_profits = sorted(values_list, key=lambda x: x[1], reverse=True)
        sorted_list = sorted(maximized_profits, key=lambda x: x[3], reverse=True)
        return sorted_list

    def truncation_selection(self, selection_list, num):
        selection = selection_list[0:num]
        return selection

    def main_function(self):
        randomized_genes = self.randomize_genes()
        self.genes = randomized_genes
        iteration = 0
        stop = False
        the_best = 0
        while stop is False:
            children_list = self.generate_children(self.genes)
            combined_list = chain(self.genes, children_list)
            fit_list = self.compute_weights_values(combined_list)
            best_half = self.truncation_selection(fit_list, self.num_genes)
            best = best_half[0]
            if best != the_best:
                print("_______________________")
                print("Current Iteration:     " + str(iteration))
                print("_______________________")
                print("Current Best Solution :", best[0])
                print("Current Best Profit   :", best[1])
                print("Current Best Capacity :", best[2])
                print("_______________________")
            iteration = iteration + 1
            the_best = best
            self.genes = [i[0] for i in best_half]
            if iteration > self.num_iterations:
                stop = True
                if best[0] == bitarray(self.optimal_best):
                    print("_______________________")
                    print("Optimization Done!     ")
                    print("_______________________")
                    print("_______________________")
                    print("Overall Best Solution :", best[0])
                    print("Overall Best Profit   :", best[1])
                    print("Overall Best Capacity :", best[2])
                    print("Total Iteration Used  :", iteration)
        return self.genes
