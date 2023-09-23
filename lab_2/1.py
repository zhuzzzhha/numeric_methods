def newton_method(f, f_prime, x0, eps=1e-10):
    """

    :param f: функция, корни которой мы ищем
    :param f_prime: производная функции f
    :param x0: начальное приближение к корню
    :param eps: допустимая погрешность
    """
    x = x0
    fx = f(x)
    while abs(fx) >= eps:
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("Производная равна нулю. Метод Ньютона не сходится.")
        x = x - fx / fpx
    return x


 # Пример: f(x) = x^2 - 4, тогда f'(x) = 2x
f = lambda x: x**2 - 4
f_prime = lambda x: 2 * x
x0 = 3
root = newton_method(f, f_prime, x0)
print(f"Приближенный корень: {root}")
