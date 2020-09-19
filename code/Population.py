
# -*- coding: utf-8 -*-

from random import randint

class Population():
    def __init__(self, nind, chromlim):
        self.__nind = nind
        self.__chromlim = chromlim
        self.__new_pop = [[None]*len(chromlim)]*nind

    @property
    def new_pop(self):
        return self.__new_pop

    def new(self):
        nchrom = len(self.__chromlim)
        for i in range(self.__nind):
            for j in range(nchrom):
                inf = self.__chromlim[j][0]
                sup = self.__chromlim[j][1]
                self.__new_pop[i][j] = randint(0, 1000) * (sup-inf) + inf