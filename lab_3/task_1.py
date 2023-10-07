#метод простых итераций
import numpy as np

def simple_iteration(A, b, x_0=None, eps=1e-10):
    n = len(b)
    x = np.zeros(n) if x_0 is None else np.copy(x_0)
    B = np.zeros_like(A)
    c = np.zeros_like(b)

    for i in range(n):
        B[i, :] = -A[i, :] / A[i, i]
        B[i, i] = 0
        c[i] = b[i] / A[i, i]
    x_new = np.dot(B, x) + c
    while np.linalg.norm(x_new - x) >= eps:
        x_new = np.dot(B, x) + c
        x = x_new
    return x_new

# Пример использования
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 3]])

b = np.array([15, 10, 10])
x0 = np.array([0, 0, 0])

result = simple_iteration(A, b, x0)
print("Решение:", result)
