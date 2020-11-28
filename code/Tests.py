
# -*- coding: utf-8 -*-

from CreateGroup import CreateGroup

def run():
    ngroups = 1000
    student_per_group = 10
    group = CreateGroup(ngroups, student_per_group)
    group.main(100)

run()
