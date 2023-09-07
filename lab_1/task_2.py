def f(x):
    return x**2 - 2

def g(x):
    return 1/2*(2/x + x)

x_0 = 1
eps = 0.01

x_prev = x_0
x_next = g(x_prev)

while abs(x_next - x_prev) > eps:
    x_prev = x_next
    x_next = g(x_prev)

print("Корень уравнения:", x_next)
