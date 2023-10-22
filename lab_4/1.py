import numpy as np


def power_iteration(A, first_val, eps, max_iterations=1000):
    x = first_val
    eigenvalue_prev = 0

    for i in range(max_iterations):
        Ax = np.dot(A, x)
        eigenvalue = Ax[0] / x[0]
        x = Ax / np.linalg.norm(Ax)

        if abs(eigenvalue - eigenvalue_prev) <= eps:
            break

        eigenvalue_prev = eigenvalue

    return eigenvalue, x



A = np.array([[4, -2],
              [1, 1]])

first_val = np.array([1, 1])
epsilon = 1e-6  # Критерий остановки
eigenvalue, eigenvector = power_iteration(A, first_val, epsilon)
print(f"Собственное число: {eigenvalue}")
print(f"Собственный вектор: {eigenvector}")
