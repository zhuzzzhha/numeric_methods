#метод Зейделя

import numpy as np

def zeidel(A, b, x0=None, eps=0.001):
    matrix = np.hstack((A, b.reshape(-1, 1)))
    n = len(matrix)
    x0 = np.zeros(n) if x0 is None else x0
    x_new = x0.copy()
    x_old = x_new.copy()

    if np.linalg.norm(x_new - x_old) >= eps:
        x_old = x_new.copy()

        for i in range(n):
            x_new[i] = (matrix[i, -1] - np.dot(matrix[i,:i], x_new[:i]) - np.dot(matrix[i,i+1:-1], x_old[i+1:])) / matrix[i,i]

    return x_new

# Пример использования
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]], dtype=float)
b = np.array([15, 10, 10], dtype=float)

result = zeidel(A, b)
print("Решение системы уравнений:", result)
