
# -*- coding: utf-8 -*-

def read_file(file_path):
    file = open(file_path , 'r')
    data = file.read()
    file.close()
    data = data.split('\n')
    return data