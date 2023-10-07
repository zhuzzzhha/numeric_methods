#поиск ведущего элемента матрицы
import numpy as np

def find_pivot_element(matrix, row, col):
    max_row = row
    n = len(matrix)

    for i in range(row + 1, n):
        if abs(matrix[i, col]) > abs(matrix[max_row, col]):
            max_row = i

    return max_row, col

# Пример использования
A = np.array([[2, 1, -1],
              [0, -1, 2],
              [1, 1, -2]])

row, col = find_pivot_element(A, 0, 0)
print(f"Ведущий элемент: {A[row, col]}")
