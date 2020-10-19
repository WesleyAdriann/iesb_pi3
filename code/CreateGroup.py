
# -*- coding: utf-8 -*-

from random import randint

class CreateGroup():
    def __init__(self, ngroups, students_lim, **kwa):
        self.__ngroups = ngroups
        self.__students_lim = students_lim
        self.__groups = []
        self.__best_group = []
        self.__fitness = []

    @property
    def groups(self):
        return self.__groups

    @property
    def best_group(self):
        return self.__best_group

    def create_group(self):
        nstudents = len(self.__students_lim)
        for i in range(self.__ngroups):
            student = []
            for j in range(nstudents):
                lim_inf, lim_sup = self.__students_lim[j]
                student.append(randint(0, 1001) * (lim_sup-lim_inf) + lim_inf)
            self.__groups.append(student)

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
        pass