#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        tlist = []
        for j in range(len(matrix[i])):
            tlist.append(matrix[i][j]**2)
        new.append(tlist)
    return new
