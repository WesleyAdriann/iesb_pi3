
# -*- coding: utf-8 -*-

from random import randint
from os import path

from models.Subject import Subject
from utils.read_file import read_file

class Student():
    __subjects_list = []
    __subjects_list = __subjects_list if len(__subjects_list) else read_file(path.abspath('subject_names.txt'))

    def __init__(self):
        print('Creating Student')
        self.__subjects = [Subject(subject_name) for subject_name in self.__subjects_list]
        self.__age = randint(10, 20)
        self.__average = 0
        self.__access_time = randint(0, 240)
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
        subjects_notes = [subject.note for subject in self.__subjects]
        self.__average = sum(subjects_notes) / len(subjects_notes)