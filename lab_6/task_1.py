def derived_f(x_values, y_values):
    if len(x_values) == 1:
        return y_values[0]
    elif len(x_values) == 2:
        return (y_values[-1] - y_values[0])/(x_values[-1] - x_values[0])
    elif len(x_values) >2:
        return (derived_f(x_values[-1:], y_values[-1:]) - derived_f(x_values[-2:], y_values[-2:]))/(x_values[-1] - x_values[-2])


def newton_interpolation(n, x_values, y_values, x_point):
    result = 0
    diff = 1
    for i in range (n+1):
        print(f"{derived_f(x_values[:i+1], y_values[:i+1])} - f")
        print(f"{diff} diff")
        diff *= (x_point - x_values[i])
        result+=derived_f(x_values[:i+1], y_values[:i+1])*diff
        print(f"{result} result")
    return result


x_values = [0, 1, 2, 3]
y_values = [1, 3, 1, 0]
n = 3
x_point = 1.5

result = newton_interpolation(n, x_values, y_values, x_point)
print(f"N3({n}) =", result)
