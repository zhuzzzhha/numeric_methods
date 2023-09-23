import sympy as sp

def newton_method(f, x_0, eps=1e-10):
    print('Начальные приближения: x_0 = {}\n'
          'Точность: eps = {}'.format(x_0, eps))
    x = sp.symbols('x')
    f_prime = sp.diff(f, x)
    f_prime_func = sp.lambdify(x, f_prime, 'numpy')
    fx = f.subs(x, x_0)
    while abs(fx) >= eps:
        fx = f.subs(x, x_0)
        fpx = f_prime_func(x_0)
        if fpx == 0:
            raise ValueError('Производная равна нулю. Метод Ньютона не сходится.')
        x_0 = x_0 - fx / fpx
    return float(x_0)


# Пример использования:

x = sp.symbols('x')
f = x ** 2 - 4
x_0 = 5
root = newton_method(f, x_0)
print('Приближенный корень: {}'.format(root))
