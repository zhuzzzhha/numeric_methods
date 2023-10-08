import numpy as np

def gauss_method(matrix, vector):
    n = len(matrix)
    matrix = np.hstack((matrix, vector.reshape(-1,1)))

    # Прямой ход
    for i in range(n):
        pivot = matrix[i, i]

        for k in range(i + 1, n):
            factor = matrix[k, i] / pivot
            matrix[k, i:] -= factor * matrix[i, i:]

    # Обратный ход
    n = len(matrix)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (matrix[i, -1] - np.dot(matrix[i, i + 1:n], x[i + 1:n])) / matrix[i, i]

    return x


A = np.array([[2, 1, 4],
              [3, 2, 1],
              [1, 3, 3]], dtype=float)

b = np.array([16, 10, 16], dtype=float)

result = gauss_method(A, b)
print("Решение системы уравнений:", result)
