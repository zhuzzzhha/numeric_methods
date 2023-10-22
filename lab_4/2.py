import numpy as np


import numpy as np

def jacobi_rotation(A, eps=0.001):
    n = A.shape[0]
    V = np.eye(n)
    max_val = 1
    while max_val >= eps:
        max_val = -np.inf
        p, q = 0, 0

        for i in range(n):
            for j in range(i+1, n):
                if abs(A[i, j]) > max_val:
                    max_val = abs(A[i, j])
                    p, q = i, j

        d = np.sqrt((A[p, p] - A[q, q])**2 + 4 * A[p, q]**2)
        c = np.sqrt(0.5 * (1 + abs(A[p, p] - A[q, q]) / d))
        s = np.sign(A[p, q] * (A[p, p] - A[q, q])) * np.sqrt(0.5 * (1 - abs(A[p, p] - A[q, q]) / d))

        R = np.eye(n)
        R[p, p] = c
        R[q, q] = c
        R[p, q] = s
        R[q, p] = -s

        A = R.T @ A @ R
        V = V @ R

    eigvals = np.diag(A)
    eigvecs = V

    return eigvals, eigvecs
# Пример использования
A = np.array([[4, -2], [-2, 5]])  # Пример симметричной матрицы
eigenvalues, eigenvectors = jacobi_rotation(A)

print("Собственные числа:", eigenvalues)
print("Собственные векторы:")
for i in range(len(eigenvalues)):
    print(f"lambda = {eigenvalues[i]}, x = {eigenvectors[:, i]}")
