
# -*- coding: utf-8 -*-

from Population import Population

if __name__ == "__main__":
    pop_size = 3
    nchrom = 10
    chromlim = [[0, 255]]*nchrom
    pop = Population(pop_size, chromlim)
    pop.new()
    print(pop.new_pop)