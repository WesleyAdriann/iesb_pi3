
# -*- coding: utf-8 -*-

from random import uniform

class Subject():
    def __init__(self, name = ''):
        self.__note = uniform(0, 10.01)
        self.__name = name

    def __repr__(self):
        return "{}: {:.2f}".format(self.__name, self.__note)

    @property
    def note(self):
        return self.__note

    def set_random_note(self):
        self.__note = uniform(0, 10.01)