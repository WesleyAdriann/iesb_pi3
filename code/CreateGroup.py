
# -*- coding: utf-8 -*-

from random import randint

class CreateGroup():
    def __init__(self, ngroups, students_lim):
        self.__ngroups = ngroups
        self.__students_lim = students_lim
        self.__groups = []

    @property
    def groups(self):
        return self.__groups

    def create_group(self):
        nstudents = len(self.__students_lim)
        for i in range(self.__ngroups):
            student = []
            for j in range(nstudents):
                lim_inf, lim_sup = self.__students_lim[j]
                student.append(randint(0, 1001) * (lim_sup-lim_inf) + lim_inf)
            self.__groups.append(student)

    def fitness(self):
        pass

    def crossing(self):
        pass

    def mutate(self):
        pass