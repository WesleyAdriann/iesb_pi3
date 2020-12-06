
# -*- coding: utf-8 -*-

from random import randint
from os import path

from models.Subject import Subject
from utils.read_file import read_file

class Student():
    def __init__(self, nsubjects = 6):
        self.__subjects = [Subject()]*nsubjects
        self.__age = randint(10, 20)
        self.__average = 0
        self.__access_time = randint(0, 240)
        self.__normalize_value = 0
        self.__calc_average()

    def __repr__(self):
        repr_string = f'< Age: {self.__age} | Average: {self.__average:.2f} | Acess Time: {self.__access_time} | Subjects: {self.__subjects} >\n'
        return repr_string

    @property
    def average(self):
        return self.__average

    @property
    def age(self):
        return self.__age

    @property
    def access_time(self):
        return self.__access_time

    @property
    def normalize_value(self):
        return self.__normalize_value

    def mutate(self):
        mutations_types = [self.__mutate_note, self.__mutate_age, self.__mutate_access_time]
        mutations_types[randint(0, len(mutations_types) - 1)]()

    def __mutate_note(self):
        self.__subjects[randint(0, len(self.__subjects) - 1)].set_random_note()
        self.__calc_average()

    def __mutate_age(self):
        self.__age = randint(10, 20)

    def __mutate_access_time(self):
        self.__access_time = randint(0, 240)

    def __calc_average(self):
        self.__average = sum(self.__subjects) / len(self.__subjects)

    def normalize(self, min_age, max_age, min_average, max_average, min_access_time, max_access_time):
        self.__normalize_value = (
            ((self.__age - min_age) / (max_age - min_age)) +
            ((self.__average - min_average) / (max_average - min_average)) +
            ((self.__access_time - min_access_time) / (max_access_time - min_access_time))
        )
