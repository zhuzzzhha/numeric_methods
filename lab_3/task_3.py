import numpy as np


def gauss_method(matrix, vector):
    n = len(matrix)

    # Прямой ход
    for i in range(n):
        max_row = np.argmax(np.abs(matrix[i:, i])) + i
        matrix[[i, max_row]] = matrix[[max_row, i]]
        vector[i], vector[max_row] = vector[max_row], vector[i]

        for k in range(i + 1, n):
            factor = matrix[k, i] / matrix[i, i]
            matrix[k, i:] -= factor * matrix[i, i:]
            vector[k] -= factor * vector[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (vector[i] - np.dot(matrix[i, i + 1:], x[i + 1:])) / matrix[i, i]

    return x


A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]], dtype=float)

b = np.array([1, -2, 0], dtype=float)

result = gauss_method(A, b)
print("Решение системы уравнений:", result)
