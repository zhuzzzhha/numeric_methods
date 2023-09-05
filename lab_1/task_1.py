def func(x):
    return (x-2)*(x-3)**2*(x-7)

def dih(function):
    x_0 = 0
    x_1 = 2.5
    eps = 0.01

    while abs(x_1 - x_0) >= eps:
        x_2 = (x_0 + x_1)/2
        if function(x_0) * function(x_2) == 0 or function(x_1)*function(x_2) == 0:
            return x_2
        if function(x_0)*function(x_2) < 0:
            x_1 = x_2
        if function(x_1)*function(x_2) < 0:
            x_0 = x_1
            x_1 = x_2
    return x_2
print(dih(func))
