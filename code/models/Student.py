
# -*- coding: utf-8 -*-

from random import uniform, randrange

from models.Subject import Subject

class Student():
    def __init__(self, amount_subjects = 3):
        self.__subjects = [Subject()]*amount_subjects
        self.__average = 0
        self.calc_average()

    def __repr__(self):
        # subjects_notes = ", ".join([subject.note for subject in self.__subjects])
        # return "notas: {subject_notes} - media: {:.2f}".format(subjects_notes, self.__average)
        return "{:.2f}".format(self.__average)

    @property
    def average(self):
        return self.__average

    def mutate_note(self):
        self.__subjects[randrange(0, len(self.__subjects), 1)].set_random_note()
        self.calc_average()

    def calc_average(self):
        subjects_notes = [subject.note for subject in self.__subjects]
        self.__average = sum(subjects_notes) / len(subjects_notes)