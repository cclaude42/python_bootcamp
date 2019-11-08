

def to_upper_case(s):
    return str(s).upper()


def print_iterator(it):
    for x in it:
        print(x, end=' ')


def ft_map(func, *args):
    max = len(args[0])
    for item in args:
        if max > len(item):
            max = len(item)
    mapped = []
    for index in range(max):
        listy = []
        for elem in args:
            listy.append(elem[index])
        mapped.append(func(*listy))
    return (mapped)


map_iterator = ft_map(to_upper_case, 'abcdede')
print(type(map_iterator))
print_iterator(map_iterator)

print("\n")
map_iterator = map(to_upper_case, 'abcdede')
print(type(map_iterator))
print_iterator(map_iterator)
