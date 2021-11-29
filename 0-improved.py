def sum(*args):
    total_sum = 0
    for number in args:
        total_sum += number
    return total_sum


print(sum(1, 5, 7, 10))
