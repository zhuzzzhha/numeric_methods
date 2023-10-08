#выбор ведущего элемента матрицы
import numpy as np
def search_pivot(matrix):

    n = len(matrix)
    for i in range(n):
        # Поиск максимального элемента в столбце под главной диагональю
        max_row = np.argmax(np.abs(matrix[i:, i])) + i
        matrix[[i, max_row]] = matrix[[max_row, i]]
    return matrix

A = np.array([[2, 1, -1],
              [0, -1, 2],
              [3, 1, -2]])
print(search_pivot(A))
