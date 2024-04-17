def add_numbers(*args):
    total = sum(args)
    return total

def subtract_numbers(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide_numbers(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

def digit_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + digit_sum(n // 10)