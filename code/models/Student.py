
# -*- coding: utf-8 -*-

from random import uniform

class Student():
    def __init__(self):
        self.__matematica = uniform(0, 11)
        self.__portugues = uniform(0, 11)
        self.__average = 0
        self.calc_average()

    def __repr__(self):
        return "{:.2f}".format(self.__average)

    @property
    def average(self):
        return self.__average

    def calc_average(self):
        self.__average = (self.__matematica + self.__portugues) / 2
