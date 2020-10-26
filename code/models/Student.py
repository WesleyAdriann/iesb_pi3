
# -*- coding: utf-8 -*-

from random import uniform, randrange

from models.Subject import Subject

class Student():
    def __init__(self):
        self.__matematica = Subject()
        self.__portugues = Subject()
        self.__average = 0
        self.calc_average()

    def __repr__(self):
        return "{:.2f}".format(self.__average)

    @property
    def average(self):
        return self.__average

    def calc_average(self):
        self.__average = (self.__matematica + self.__portugues) / 2
