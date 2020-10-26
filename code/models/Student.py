
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

    def random_note(self):
        note = uniform(0, 11)
        subjects = (self.__matematica,self.__portugues)
        subjects[randrange(0, len(subjects), 1)].set_note(note)
        self.calc_average()

    def calc_average(self):
        subjects_notes = (self.__matematica.note, self.__portugues.note)
        self.__average = sum(subjects_notes) / len(subjects_notes)
