#!/usr/bin/env python3
""" ft_filter, ft_map and ft_reduce tests

"""
from functools import reduce
from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce

def test_function(message, tested_function, applied_function, iterable):
    """A function to test a version of the function"""
    print(message)
    try:
        print(tested_function(applied_function, iterable))
    except Exception as exc: # pylint: disable=broad-except
        print(exc)
    try:
        print(list(tested_function(applied_function, iterable)))
    except Exception as exc: # pylint: disable=broad-except
        print(exc)
    print()

def compare_behavior(real_function, my_function, applied_function, iterable):
    """A function to compare my function's behavior to the real one"""
    test_function("Real function :", real_function, applied_function, iterable)
    test_function("My function :", my_function, applied_function, iterable)
    print("------------------------")

def main():
    """Main"""
    lst = [1, 2, 3, 4, 5]
    stt = {10, 20, 30, 40, 50}
    empty = []
    hlo = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

    lsum = lambda dum: dum + 1
    lodd = lambda dum: not dum % 2
    lconcat = lambda u, v: u + v

    compare_behavior(map, ft_map, lsum, lst)
    compare_behavior(map, ft_map, lsum, stt)
    compare_behavior(map, ft_map, lsum, empty)
    compare_behavior(map, ft_map, lsum, range(10, 20))
    test_function("Real function :", map, lsum, iter(lst))
    test_function("My function :", ft_map, lsum, iter(lst))
    print("------------------------")
    compare_behavior(map, ft_map, lsum, 56) # Not iterable
    compare_behavior(map, ft_map, lsum, hlo) # Wrong iterable
    compare_behavior(map, ft_map, 56, lst) # Not function
    compare_behavior(map, ft_map, lconcat, lst) # Wrong function

    compare_behavior(filter, ft_filter, lodd, lst)
    compare_behavior(filter, ft_filter, lodd, stt)
    compare_behavior(filter, ft_filter, lodd, empty)
    compare_behavior(filter, ft_filter, lodd, range(10, 20))
    test_function("Real function :", filter, lodd, iter(lst))
    test_function("My function :", ft_filter, lodd, iter(lst))
    print("------------------------")
    compare_behavior(filter, ft_filter, lodd, 56) # Not iterable
    compare_behavior(filter, ft_filter, lodd, hlo) # Wrong iterable
    compare_behavior(filter, ft_filter, 56, lst) # Not function
    compare_behavior(filter, ft_filter, lconcat, lst) # Wrong function

    compare_behavior(reduce, ft_reduce, lconcat, hlo)
    compare_behavior(reduce, ft_reduce, lconcat, stt)
    compare_behavior(reduce, ft_reduce, lconcat, [1])
    compare_behavior(reduce, ft_reduce, lconcat, None) # Not iterable
    compare_behavior(reduce, ft_reduce, lconcat, empty) # Wrong iterable
    compare_behavior(reduce, ft_reduce, 56, hlo) # Not function
    compare_behavior(reduce, ft_reduce, lsum, lst) # Wrong function

if __name__ == '__main__':
    main()
