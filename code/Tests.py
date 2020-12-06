
# -*- coding: utf-8 -*-

from CreateGroup import CreateGroup

def run():
    values = []
    for i in range(100, 300, 100):
        ngroups = i
        student_per_group = 10
        group = CreateGroup(ngroups, student_per_group, 0.03)
        group.main(50)
        values.append((i, group.best_euclidian_distance, group.best_fitness, group.best_group))
    print('\n\n')
    for ngroups, distance, fitness, group in values:
        print(f'GROUPS: {ngroups}  |  DISTANCE: {distance}  |  FITNESS: {fitness}  |\nBEST GROUP: \n{group}\n')

run()
