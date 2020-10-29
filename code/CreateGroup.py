
# -*- coding: utf-8 -*-

from random import randint, random, shuffle, randrange
from models.Student import Student

class CreateGroup():
    def __init__(self, ngroups, students_per_group, rate_mutation = 0.5):
        self.__ngroups = ngroups
        self.__students_lim = []
        self.__groups = []
        self.__best_group = []
        self.__fitness = []
        self.__students_per_group = students_per_group
        self.__rate_mutation = rate_mutation
        # self.__roulette_rounds = kwargs.get('roulette_rounds', 2)

    @property
    def groups(self):
        return self.__groups

    def main(self, ngenerations = 3):
        self.create_group()
        for i in range(ngenerations):
            self.fitness()
            self.mutate()
        print('Best group')
        print(', '.join(self.__best_group))

    def create_group(self):
        for i in range(self.__ngroups):
            group = []
            for j in range(self.__students_per_group):
                group.append(Student())
            self.__groups.append(group)
        print(f'GROUPS {self.__groups}')

    def fitness(self):
        self.__fitness = []
        for group in self.__groups:
            self.__fitness.append(self.fitness_fn(group))
        print(f'FITNESS {self.__fitness}')


    def fitness_fn(self, group):
        fit = 0
        for student in group:
            fit = fit + student.average
        return fit / self.__students_per_group


    def selection(self):
        total_fitness = sum(self.__fitness)
        relative_fitness = []
        for fitness in self.__fitness:
            relative_fitness.append(fitness/total_fitness)

        beta = 0.0
        index_group = randint(0, self.__ngroups) 
        max_capable = max(relative_fitness)
        new_groups = []

        for i in range(self.__ngroups):
            beta += random() * 2.0 * max_capable
            while beta > relative_fitness[index_group]:
                beta -= relative_fitness[index_group]
                index_group = (index_group + 1) % self.__ngroups
            new_groups.append(self.__groups[index_group])
            shuffle(new_groups)
        # self.__groups = new_groups
        return new_groups

    def crossing(self):
        pass

    def mutate(self):
        groups_mutate = self.__groups[:]
        for group in groups_mutate:
            if(random() < self.__rate_mutation):
                mutation_point = randrange(0, self.__students_per_group, 1)
                group[mutation_point].random_note()
        self.__groups = groups_mutate

if __name__ == "__main__":
    ngroups = 5
    student_per_group = 3
    group = CreateGroup(ngroups, student_per_group)
    group.main()