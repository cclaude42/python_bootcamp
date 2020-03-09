

def func(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


def ft_filter(func, list):
    filtered = []
    for item in list:
        if func(item):
            filtered.append(item)
    return (filtered)


sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = ft_filter(func, 'hello')

print('The filtered letters are:')
for s in filtered:
    print(s)
