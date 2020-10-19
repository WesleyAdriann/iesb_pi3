
# -*- coding: utf-8 -*-

from CreateGroup import CreateGroup

if __name__ == "__main__":
    ngroups = 5
    student_per_group = 3
    group = CreateGroup(ngroups, students_lim)
    group.create_group()
    print(group.groups)