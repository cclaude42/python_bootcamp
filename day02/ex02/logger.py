#!/usr/bin/env python3
""" Logger file

"""
import os
import time
from random import randint


def log(func):
    """A logger, wrapping the function call"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        xtime = time.perf_counter() - start
        with open("machine.log", mode="a+", encoding="utf-8") as file:
            user = os.getenv('USER', "unknown")
            name = func.__name__.replace('_', ' ').title()
            if xtime > 0.001:
                file.write(f"({user}) Running: {name:18} [ exec-time = {xtime:.3f} s  ]\n")
            else:
                file.write(f"({user}) Running: {name:18} [ exec-time = {xtime * 1000:.3f} ms ]\n")
        return result
    return wrapper


class CoffeeMachine(): # pylint: disable=missing-class-docstring

    water_level = 100

    @log
    def start_machine(self): # pylint: disable=missing-function-docstring
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self): # pylint: disable=missing-function-docstring
        return "boiling..."

    @log
    def make_coffee(self): # pylint: disable=missing-function-docstring
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level): # pylint: disable=missing-function-docstring
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
