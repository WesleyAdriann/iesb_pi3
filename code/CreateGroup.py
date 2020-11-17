
# -*- coding: utf-8 -*-

from random import randint, random
from models.Student import Student

class CreateGroup():
    def __init__(self, ngroups, students_per_group, roulette_rounds = 2, rate_mutation = 0.5):
        self.__ngroups = ngroups
        self.__groups = []
        self.__best_group = []
        self.__fitness = []
        self.__selected_groups = []
        self.__students_per_group = students_per_group
        self.__rate_mutation = rate_mutation
        self.__roulette_rounds = roulette_rounds

    @property
    def groups(self):
        return self.__groups

    def main(self, ngenerations = 3):
        print('MAIN|\n')
        self.create_groups()
        for i in range(ngenerations):
            print(f'N: {i}')
            print(f'GROUPS: {self.__groups}')
            self.fitness()
            self.roulette_selection()
            self.crossover()
            self.mutate()
        print('Best group')
        print(', '.join(self.__best_group))

    def create_groups(self):
        for i in range(self.__ngroups):
            group = []
            for j in range(self.__students_per_group):
                group.append(Student())
            self.__groups.append(group)

    def fitness(self):
        self.__fitness = []
        for group in self.__groups:
            self.__fitness.append(self.fitness_fn(group))

    def fitness_fn(self, group):
        fit = 0
        for student in group:
            fit = fit + student.average
        return fit / self.__students_per_group

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
        self.__selected_groups = selected_groups

    def crossover(self):
        for i in range(0, len(self.__selected_groups), 2):
            cross_point = randint(0, self.__students_per_group - 1)
            father = self.__selected_groups[i]
            mother = self.__selected_groups[i+1]
            print(f'BEFORE CROSSOVER: {father} {mother}')
            for i in range(cross_point):
                father[i], mother[i] = mother[i], father[i]
            print(f'AFTER CROSSOVER : {father} {mother}')
            print(f'------')

    def mutate(self):
        for group in self.__groups:
            if(random() >= self.__rate_mutation):
                student = randint(0, self.__students_per_group - 1)
                print(f'BEFORE MUTATE: {group[student]}')
                group[student].mutate()
                print(f'AFTER MUTATE : {group[student]}')

    def get_best_group(self):
        pass

if __name__ == "__main__":
    ngroups = 5
    student_per_group = 3
    group = CreateGroup(ngroups, student_per_group, 6)
    group.main()
