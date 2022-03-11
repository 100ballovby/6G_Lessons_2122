def factorial(n):
    """Функция считает факториал числа n.
    Факториалом называется произведение всех натуральных
    чисел от 1 до n включительно."""
    res = 1
    for i in range(n, 0, -1):  # n, n-1, n-2, ..., 1
        res *= i
    return res


def recursion_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursion_factorial(n - 1)


def recursion_summary(n):
    if n <= 1:
        return 1
    else:
        return n + recursion_factorial(n - 1)

print(factorial(7))
print(recursion_factorial(7))
print(recursion_summary(5))
