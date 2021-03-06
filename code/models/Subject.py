
# -*- coding: utf-8 -*-

from random import uniform

class Subject():
    def __init__(self):
        self.__note = uniform(0, 10.01)

    def __repr__(self):
        return f'{self.__note:.2f}'

    def __radd__(self, other):
        return self.__note + other

    @property
    def note(self):
        return self.__note

    def set_random_note(self):
        self.__note = uniform(0, 10.01)
