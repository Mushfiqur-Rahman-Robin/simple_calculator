def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 0


def multiply(x, y):
    return x * y
