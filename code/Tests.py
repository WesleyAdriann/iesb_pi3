
# -*- coding: utf-8 -*-

from CreateGroup import CreateGroup

def run():
    values = []
    for i in range(100, 1100, 100):
        ngroups = i
        student_per_group = 10
        group = CreateGroup(ngroups, student_per_group, 0.6)
        group.main(100)
        values.append((i, group.best_euclidian_distance, group.best_fitness))
    for v in values:
        print(v)

run()
