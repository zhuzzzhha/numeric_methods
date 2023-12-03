import numpy as np

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def newton_interpolation(x_values, y_values, x):
    n = len(x_values) - 1
    result = 0
    for i in range(n+1):
        if(i >0):
            term = pow((y_values[i] - y_values[i-1]), i+1)
        else:
            term = 1
        for j in range(i):
            term *= (x - x_values[j])
        term /= factorial(i)
        result += term

    return result


x_values = [0,1,2, 3]
y_values = [1, 2, 4, 1]
x_point = 1.5

result = newton_interpolation(x_values, y_values, x_point)
print(f"Interpolated value at {x_point}:", result)
