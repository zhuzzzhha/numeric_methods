import sympy as sp
def secant_method(f, x_0, x_1, eps=0.001):
    print('Начальные приближения: x_0 = {} x_1 = {}\n'
          'Точность: eps = {}'.format(x_0, x_1, eps))
    x = sp.Symbol('x')
    b = x_1
    x_1 = x_0 + 2*eps
    while abs((x_1 - x_0)) >= eps:
        x_0 = x_1
        x_1 = x_0 - f.subs(x, x_0) / (f.subs(x, b) - f.subs(x, x_0)) * (b - x_0)
    return float(x_1)

# Пример использования:
x = sp.Symbol('x')
f = -((5 * x)/(1 + x * x)) + 2 * sp.cos(2 * x) - 1
x_0 = -2.5
x_1 = -1.5
root = secant_method(f, x_0, x_1)
print(f"Приближенный корень: {root}")
