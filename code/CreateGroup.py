
# -*- coding: utf-8 -*-

from random import randint, random
from math import sqrt
from models.Student import Student

class CreateGroup():
    def __init__(self, ngroups, students_per_group, rate_mutation = 0.03, roulette_rounds = 20, scale_factor = 100):
        self.__ngroups = ngroups
        self.__groups = []
        self.__best_group = []
        self.__fitness = []
        self.__best_fitness = 0
        self.__euclidian_distance = []
        self.__best_euclidian_distance = 0
        self.__selected_groups = []
        self.__students_per_group = students_per_group
        self.__rate_mutation = rate_mutation
        self.__roulette_rounds = roulette_rounds
        self.__scale_factor = scale_factor

    @property
    def groups(self):
        return self.__groups

    @property
    def best_euclidian_distance(self):
        return self.__best_euclidian_distance

    def main(self, ngenerations = 3):
        print('MAIN')
        self.create_groups()
        for i in range(ngenerations):
            print(f'EXECUTION N: {i}')
            print(f'GROUPS:\n  {self.__groups}')
            self.fitness()
            self.roulette_selection()
            self.crossover()
            self.mutate()
        self.get_best_group()
        # print(f'BEST GROUP:\n  {self.__best_group}')
        print(f'BEST EUCLIDIAN DISTANCE:\n  {self.__best_euclidian_distance}')
        print(f'BEST FITNESS:\n  {self.__best_fitness}')

    def create_groups(self):
        print(f'CREATING GROUPS')
        for i in range(self.__ngroups):
            group = []
            for j in range(self.__students_per_group):
                group.append(Student())
            self.__groups.append(group)
            print(f'CREATED GROUP\n  {group}')

    def fitness(self):
        self.__fitness = []
        ages = []
        access_times = []
        averages = []
        for group in self.__groups:
            for student in group:
                ages.append(student.age)
                access_times.append(student.access_time)
                averages.append(student.average)

        min_age, max_age = min(ages), max(ages)
        min_access_times, max_access_times = min(access_times), max(access_times)
        min_average, max_average = min(averages), max(averages)

        for group in self.__groups:
            for student in group:
                student.normalize(min_age, max_age, min_access_times, max_access_times, min_average, max_average)

        for group in self.__groups:
            euclidian_distance, fitness = self.fitness_fn(group)
            self.__fitness.append(fitness)
            self.__euclidian_distance.append(euclidian_distance)
        print(f'GROUPS FITNESS:  \n{self.__fitness}')

    def fitness_fn(self, group):
        total_euclidian_distance = 0
        for i, student in enumerate(group):
            start = i + 1
            distance_acc = 0
            for j in range(start, len(group)):
                euclidian_distance = sqrt(
                    pow((group[j].normalize_value - student.normalize_value), 2)
                )
                distance_acc += euclidian_distance
            total_euclidian_distance += distance_acc
        return [total_euclidian_distance, self.__scale_factor / (1 + total_euclidian_distance)]

    def roulette_selection(self):
        self.__selected_groups = []
        total_fitness = sum(self.__fitness)
        relative_fitness = []
        for fitness in self.__fitness:
            relative_fitness.append(fitness/total_fitness)

        probs = []
        for i in range(len(relative_fitness)):
            probs.append(sum(relative_fitness[:i+1]))

        selected_groups = []
        for roulette_round in range(self.__roulette_rounds):
            for i, group in enumerate(self.__groups):
                if random() <= probs[i]:
                    selected_groups.append(group)
                    break
        print(f'SELECTED GROUPS:\n  {selected_groups}')
        self.__selected_groups = selected_groups

    def crossover(self):
        for i in range(0, len(self.__selected_groups), 2):
            cross_point = randint(0, self.__students_per_group - 1)
            father = self.__selected_groups[i]
            mother = self.__selected_groups[i+1]
            print(f'MUTATION POINT  :{cross_point}')
            print(f'BEFORE CROSSOVER:\n  {father}\n  {mother}')
            for i in range(cross_point):
                father[i], mother[i] = mother[i], father[i]
            print(f'AFTER CROSSOVER:\n  {father}\n  {mother}')
            print(f'------')

    def mutate(self):
        for group in self.__groups:
            if(random() >= self.__rate_mutation):
                student = randint(0, self.__students_per_group - 1)
                print(f'BEFORE MUTATE:\n  {group[student]}')
                group[student].mutate()
                print(f'AFTER MUTATE :\n  {group[student]}')

    def get_best_group(self):
        best_group_index = self.__fitness.index(max(self.__fitness))
        print(f'ALL FITNESS:\n  {self.__fitness}')
        self.__best_euclidian_distance = self.__euclidian_distance[best_group_index]
        self.__best_fitness = self.__fitness[best_group_index]
        self.__best_group = self.__groups[best_group_index]
