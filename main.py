import random
from math import sin
import bisect
from random import randint
populationSize = 10

class Individual:
    def __init__(self):
        self.chromosome = random.getrandbits(22)
        self.quality = 0



    def mapToRange(self, xmin=-1.0, xmax=2.0, numOfBits=22):
        maxBit = 2 ** numOfBits - 1
        minBit = 0
        return (self.chromosome - minBit) / (maxBit - minBit) * (xmax - xmin) + xmin

    def fitness(self):
        return -(self.mapToRange()**2)

    def __ge__(self, other):
        return self.fitness() >= other.fitnes()

    def __gt__(self, other):
        return self.fitness() > other.fitness()

    def __le__(self, other):
        return self.fitness() <= other.fitnes()

    def __lt__(self, other):
        return self.fitness() < other.fitness()


def selection(population, bestFraction=0.5):
    return population[int(len(population) * bestFraction):]

def crossover(pop):
    i, j = randint(0, len(pop)), randint(0, len(pop))
####TODO
    return newIndividual

def nextGeneration(populationn):
    newGeneration = []
    for i in range(0, populationSize):
        newIndividual = crossover(populationn)
        return newGeneration

def mutation(populationn):
    return False


population = []
for i in range(0, populationSize):
    bisect.insort(population, Individual())
for i in population:
    print(i.mapToRange())

print("\n\n")

# for generation in range(0, 3):
#     population = selection(population)
#     nextGeneration(population)
#     mutation(population)
#     for it in population:
#         print(it.mapToRange())
#     print("\n")

print(type(population[0].chromosome))





