import sys


class GotCharacter:

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = True


class Baelish(GotCharacter):
    """A class to represent the Baelish House - or how one man can stand by himself"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Baelish"
        self.house_words = "Knowledge is Power"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
