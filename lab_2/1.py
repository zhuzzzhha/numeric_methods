import sympy as sp

def newton_method(f, x0, eps=1e-10):
    """
    :param f: символьное выражение функции, корни которой мы ищем
    :param x0: начальное приближение к корню
    :param eps: допустимая погрешность
    """
    x = sp.symbols('x')
    f_prime = sp.diff(f, x)
    f_prime_func = sp.lambdify(x, f_prime, 'numpy')
    fx = f.subs(x, x0)
    while abs(fx) >= eps:
        fx = f.subs(x, x0)
        fpx = f_prime_func(x0)
        if fpx == 0:
            raise ValueError("Производная равна нулю. Метод Ньютона не сходится.")
        x0 = x0 - fx / fpx
    return float(x0)


# Пример использования:

x = sp.symbols('x')
f = x ** 2 - 4
x0 = 5
root = newton_method(f, x0)
print(f"Приближенный корень: {root}")
