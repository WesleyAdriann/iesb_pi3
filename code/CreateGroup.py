
# -*- coding: utf-8 -*-

from random import randint, random
from models.Student import Student

class CreateGroup():
    def __init__(self, ngroups, students_per_group, **kwargs):
        self.__ngroups = ngroups
        self.__students_lim = []
        self.__groups = []
        self.__best_group = []
        self.__fitness = []
        self.__students_per_group = students_per_group
        self.__rate_mutation = kwargs.get('rate_mutation', 0.5)

    @property
    def groups(self):
        return self.__groups

    def main(self, ngenerations = 3):
        self.create_group()
        for i in range(ngenerations):
            print('gens')
            # pass
        print('Best group')
        print(', '.join(self.__best_group))

    def create_group(self):
        for i in range(self.__ngroups):
            student = []
            for j in range(self.__students_per_group):
                student.append(Student())
            self.__groups.append(student)
        print(f'GROUPS {self.__groups}')

    def fitness(self):
        for group in self.groups:
            self.fitness.append(self.fitness_fn(group))


    def fitness_fn(self, group):
        fit = 0
        for student in group:
            fit = fit + student
        return fit


    def selection(self):
        pass

    def crossing(self):
        pass

    def mutate(self):
        groups_mutate = self.__groups[:]
        for i, group in enumerate(groups_mutate):
            if(random() < self.__rate_mutation):
                mutation_point = randint(0, self.__students_per_group)
                groups_mutate[i][mutation_point] = randint(0, 1000)
        self.__groups = groups_mutate

if __name__ == "__main__":
    ngroups = 5
    student_per_group = 3
    group = CreateGroup(ngroups, student_per_group)
    group.main()