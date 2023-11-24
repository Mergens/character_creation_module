import math

# import itertools.

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')

print(message)


def сalculate_square_root(Number: float):
    """Вычисляет квадратный корень."""
    return math.sqrt(Number)


def calc(your_number: float):
    """Начало расчета корня."""
    if your_number <= 0:
        return
    root = сalculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')


calc(25.5)
