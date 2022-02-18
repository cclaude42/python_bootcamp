#!/usr/bin/env python3
"""A file to test the logger package
"""
import time
from random import randint
from my_minipack.logger import logger

class CoffeeMachine(): # pylint: disable=missing-class-docstring

    water_level = 100

    @logger
    def start_machine(self): # pylint: disable=missing-function-docstring
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @logger
    def boil_water(self): # pylint: disable=missing-function-docstring
        return "boiling..."

    @logger
    def make_coffee(self): # pylint: disable=missing-function-docstring
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @logger
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
