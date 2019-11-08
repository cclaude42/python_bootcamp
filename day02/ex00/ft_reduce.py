from functools import reduce


def add(a, b):
    return (a+b)


def ft_reduce(func, list):
    if len(list) == 1:
        return (list[0])
    result = func(list[0], list[1])
    new_list = list[2:]
    for item in new_list:
        result = func(result, item)
    return (result)


sequence = [1, 2, 3, 4, 5, 6]

result = ft_reduce(add, sequence)
print(result)
