
# -*- coding: utf-8 -*-

from random import uniform, randint
from os import path

from models.Subject import Subject
from utils.read_file import read_file

class Student():
    __subjects_list = []
    __subjects_list = __subjects_list if len(__subjects_list) else read_file(path.abspath('subject_names.txt'))

    def __init__(self):
        print('Creating Student')
        self.__subjects = [Subject(subject) for subject in self.__subjects_list]
        self.__favorite_subject = self.__subjects_list[randint(0, len(self.__subjects_list) - 1)]
        self.__age = randint(18, 60)
        self.__average = 0
        self.calc_average()

    def __repr__(self):
        repr_string = f'Age: {self.__age} | Average: {self.__average:.2f} | Favorite Subject: {self.__favorite_subject} | Subjects: {self.__subjects}'
        return repr_string

    @property
    def average(self):
        return self.__average

    def mutate_note(self):
        self.__subjects[randrange(0, len(self.__subjects), 1)].set_random_note()
        self.calc_average()

    def calc_average(self):
        subjects_notes = [subject.note for subject in self.__subjects]
        self.__average = sum(subjects_notes) / len(subjects_notes)