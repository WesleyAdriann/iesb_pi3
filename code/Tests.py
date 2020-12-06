
# -*- coding: utf-8 -*-

from CreateGroup import CreateGroup

def run():
    values = []
    mutations_rate = [0.03, 0.05, 0.1, 0.3, 0.6]
    point = 4
    for i in range(100, 1100, 100):
        ngroups = i
        student_per_group = 10
        group = CreateGroup(ngroups, student_per_group, mutations_rate[point])
        group.main(100)
        values.append((i, group.best_euclidian_distance, group.best_fitness, group.best_group))
    print('\n\n')
    print(f'tm: {mutations_rate[point]}')
    for ngroups, distance, fitness, group in values:
        print(f'GROUPS: {ngroups}  |  DISTANCE: {distance}  |  FITNESS: {fitness}  |\nBEST GROUP: \n{group}\n')
        # print(f'GROUPS: {ngroups}  |  DISTANCE: {distance}  |  FITNESS: {fitness}')

run()
